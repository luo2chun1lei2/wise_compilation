# 系统设计

> 依据：`ai/proposal.md`（需求）+ `ai/tech.md` T1/T7（已完成的调查）+ 用户 2026-09-16 指定的架构方向：
> **收集信息 → 内部 wiki 文件 → 外部 wiki / 飞书 / 微信等**。

## 1. 总体架构（三段式）

```
┌─────────────────┐   ┌──────────────────────────┐   ┌──────────────────────┐
│ Stage A 采集层    │   │ Stage B 内部 wiki 层       │   │ Stage C 分发层         │
│                 │   │ （枢纽/事实源）             │   │                      │
│ RSS / Atom      │   │  去重 → LLM翻译+摘要+分类    │   │  飞书群机器人（已核实）  │
│ GitHub API      │ → │  → 专题汇编 → 趋势统计      │ → │  微信（延后 ADR-0002） │
│ 定向网页抓取      │   │  → result/*.md（事实源）    │   │  外部 wiki（目标待定）  │
│                 │   │  → MinDoc 页面（阅读入口）   │   │  ...可扩展通道         │
└─────────────────┘   └──────────────────────────┘   └──────────────────────┘
     material/                result/ + 内网 MinDoc          channels.yaml
   （原料索引：链接+简介）        （git 版本化）                 （通道配置驱动）
```

### 中间层的职责划分（关键设计）

「内部 wiki 文件」由**两个表示**构成，职责不同、内容一致：

| 表示 | 角色 | 说明 |
|---|---|---|
| 本地 `result/*.md` | **事实源** | 汇编产出先落此目录并入 git（满足项目「提交推送」要求）；分发通道从这里读取，不依赖内网 wiki 的可用性 |
| MinDoc 页面 | **内部阅读入口** | 发布器把 `result/` 成品同步到内网 wiki（API 已在 tech.md T1 核实）；MinDoc 故障不阻塞 Stage C |

> 该设计同时覆盖两种理解（先落本地 wiki 文件再外发 / 以内网 wiki 为中枢再外发），数据流一致。若与你的本意不符，指出后调整。

### 数据流

1. **采集**（每日）：按 `sources.yaml` 逐源拉取 → 规范化条目（标题/链接/日期/原文摘要）→ 去重后入 SQLite，原料索引追加至 `material/`（只存链接+简介，符合需求约束）。
2. **汇编**（每周/手动）：取周期内新条目 → LLM 一次调用完成「翻译为中文 + 生成简介 + 归入专题」→ 按专题模板渲染 markdown（新闻周报 / 技术汇总）→ 追加「趋势观察」小节（规则统计 + LLM 一段解读）→ 写 `result/`。
3. **发布 wiki**：登录 MinDoc（30 天 remember cookie，失效自动重登）→ 按期次创建/更新文档（`cover=yes` 覆盖）→ 记录 `publish_log`。
4. **分发**：各通道从 `result/` 读取本期成品 → 按「卡片模式（摘要+wiki 链接）」或「全文模式（分片）」推送 → 记录 `publish_log`。

## 2. 模块与目录设计

```
tools/
  wise/                    # 主 Python 包
    config.py              # 配置加载（yaml + .env 密钥）
    store.py               # SQLite 访问（表见 §3）
    collect/
      rss.py               # RSS/Atom 采集（feedparser，支持 etag/last-modified 增量）
      github.py            # GitHub API（releases / commits / activity；T3 细化）
      web.py               # 定向抓取兜底（trafilatura 抽正文，仅无 RSS 源）
    pipeline/
      dedupe.py            # URL 规范化 + 内容 hash + 已见判重
      llm.py               # LLM 客户端：翻译+摘要+分类（一次调用，schema 校验输出）
      digest.py            # 专题模板渲染（新闻周报 / 技术汇总）
      trend.py             # 趋势统计（本期 vs 上期频次、条目数、star 增速）
    wiki/
      mindoc.py            # MinDoc 客户端：登录/会话续期/建文档/写内容/读内容
    deliver/
      base.py              # Channel 抽象接口
      feishu.py            # 飞书群机器人（T7 已核实）
      # wechat.py / ext_wiki.py —— 后续按 ADR-0002 与目标确定后扩展
    scheduler.py           # 调度入口（兼容 cron 单次调用与常驻两种方式，T5 定）
    cli.py                 # 子命令：collect / compile / publish / deliver / run / verify
  config/
    sources.yaml           # 信息源清单（T2 产出初始清单后由用户确认）
    topics.yaml            # 专题定义与模板变量
    channels.yaml          # 分发通道开关与模式（card/full）
  requirements.txt
data/                      # 运行数据（不入 git）：wise.db、cookies.json、日志
material/                  # 原料索引（AGENTS.md 布局）
result/                    # 汇编成品 = 事实源（入 git）
```

## 3. 数据模型（SQLite `data/wise.db`）

| 表 | 关键字段 | 用途 |
|---|---|---|
| `sources` | id, name, type(rss/github/web), url, topic, enabled, last_fetch_at, fail_count | 源注册表与健康状况 |
| `items` | id, source_id, url_norm(唯一), title, title_zh, summary_zh, lang, published_at, content_hash, status(new/used/skipped) | 采集条目；去重键 = url_norm |
| `digests` | id, topic, period_start, period_end, file_path, wiki_doc_id, version | 每期汇编的登记与 wiki 映射 |
| `publish_log` | id, digest_id, channel(wiki/feishu/…), status, detail, at | 各通道发布结果，可重放 |
| `runs` | id, kind(collect/compile/publish/deliver), started_at, finished_at, status, stats(JSON), error | 每次运行的汇总报告与告警依据 |

## 4. 内部 wiki（MinDoc）发布设计

- 目标项目（book）：identify 计划为 `ai-digest`（名称「AI 资讯汇编」；**需用户在 wiki 创建并授予工具账号编辑权限**）。
- 文档树与命名（`doc_identify` 稳定可重入）：

```
AI 资讯汇编
 ├─ 说明
 ├─ 新闻周报/  news-2026-w38, news-2026-w39, …
 └─ 技术汇总/  tech-2026-09, tech-2026-10, …
```

- 发布算法（幂等）：
  1. 探测会话（AJAX 访问受保护页）→ 403/302 则重登（流程见 tech.md T1）。
  2. `GET /api/{key}/content/{doc_id}`：不存在则 `POST /api/{key}/create`（带 `doc_identify`）建文档；存在则直接更新。
  3. `POST /api/{key}/content/{doc_id}`（`markdown=成品`、`cover=yes`）。
  4. 写 `publish_log`；失败重试 ≤2 次后告警并跳过（成品仍在 `result/`，不丢）。

## 5. 分发层设计

### 通道抽象

```python
class Channel(ABC):
    name: str                       # 与 channels.yaml 的 key 对应
    def health_check(self) -> bool  # 凭据/连通性自检
    def send(self, digest) -> SendResult   # 消费 DigestDoc（含 md 全文与 wiki 链接）
```

- `channels.yaml` 每通道：`enabled`、`mode: card | full`、凭据引用（指向 .env 键名）。
- **card 模式（默认）**：推送标题 + 本期要点（3–5 条）+ 跳转 MinDoc 的链接。内网 wiki 链接对外部读者不可达时，该通道改用 full 模式。
- **full 模式**：全文分片推送（飞书单条 ≤20KB，按一级标题切分）。

### 飞书通道（T7 已核实）

- 自定义机器人 webhook：`POST https://open.feishu.cn/open-apis/bot/v2/hook/xxx`，`msg_type: post`（富文本，支持链接）或 `interactive` 卡片。
- 签名：`sign = base64(HmacSHA256(key=timestamp+"\n"+secret, message=""))`，随 `timestamp` 一起提交；时间戳有效期 1 小时。
- 限制：100 条/分钟、5 条/秒、单条 ≤20KB —— 每期一条卡片远低于限制。
- 错误码处理：19021（签名）→ 告警停用；19022（IP 白名单）/19024（关键词）→ 配置错误告警；11232（限流）→ 退避重试。

### 其余通道

- **微信**：延后（ADR-0002），届时在企业微信群机器人 / Server酱 中选型，按同一 Channel 接口接入。
- **外部 wiki**：目标系统未定（需用户提供地址/类型），实现为独立 Channel 插件。

## 6. 调度设计

| 任务 | 频率 | 命令 | 说明 |
|---|---|---|---|
| 采集 | 每日 06:00 | `wise collect` | 各源独立失败不互相影响 |
| 汇编+发布+分发 | 每周一 08:00 | `wise run weekly` | compile → publish(wiki) → deliver 顺序执行 |
| 手动特刊 | 按需 | `wise compile --topic news --since 2026-09-14` | 特殊时间点/重大事件手动触发 |

- 所有子命令**幂等**（去重靠 url_norm + content_hash；重发布靠 doc_identify + cover=yes），调度载体用 cron / systemd timer / 常驻 APScheduler 均可，待 T5 定（不影响本设计）。

## 7. 错误处理矩阵

| 阶段 | 故障 | 处理 |
|---|---|---|
| 采集 | 单源超时/403/RSS 格式变化 | 源隔离；退避重试 ×3；连续 5 次失败在 runs 报告标记「源失效」并告警 |
| 采集 | GitHub 限流 | 带 token；读 `X-RateLimit-Reset` 暂停等待 |
| LLM | API 超时/失败 | 退避重试 ×3；仍失败该条目置 `skipped`，汇编中标注「本期未译」保留英文标题与链接 |
| LLM | 输出不符合 schema | 校验失败重试 1 次；再失败降级为原文截断 |
| 汇编 | 周期内无素材 | 产出「本期无重要动态」占位文档，不推空卡片 |
| wiki | 会话失效 | 自动重登（remember cookie 30 天）；重登失败 → 告警、本轮跳过 wiki，其余通道照常 |
| wiki | 版本冲突 6005 | `cover=yes` 覆盖（机器生成内容，安全） |
| 分发 | webhook 失败/限流 | 按错误码分类处理（见 §5）；重试 ≤2 后记录 publish_log 并告警 |
| 整体 | 任一环节失败 | 各 stage 独立可重跑；`runs` 汇总统计供运行报告 |

## 8. 凭据与安全

- 密钥统一存放于 `ai/secret.md`（**已加入 .gitignore，不入 git**；格式为 `键: 值`，工具直接解析），键包括：`WIKI_URL`、`WIKI_ACCOUNT`、`WIKI_PASSWORD`、`WIKI_BOOK_IDENTIFY`、`FEISHU_WEBHOOK`、`FEISHU_SECRET`、`GITHUB_TOKEN`、`LLM_API_KEY` 等；仓库提交同结构的空模板 `ai/secret.example.md`。
- cookie jar 与 SQLite 均在 `data/`（gitignore）。
- 日志不打印密钥与完整 cookie。

## 9. 设计自检（对照 AGENTS.md 四条要求）

- **明确**：每个模块的输入/输出、每个外部 API 的端点与参数均已核实（tech.md T1/T7）。
- **无矛盾**：「只存链接和简介」与「趋势对比」的张力以 SQLite 结构化元数据 + `material/` 轻量索引化解；MinDoc 与 `result/` 双表示职责分工明确（§1）。
- **准确**：MinDoc API 行为来自源码并经内网实测；飞书限制来自官方文档。
- **错误处理**：§7 矩阵覆盖全部阶段与已知故障模式。

## 10. 未决问题（实现前需确认）

1. MinDoc 目标项目：✅ 已创建「AI 资讯汇编」（identify=`ai-digest`，2026-09-16 用户确认）。待定：工具登录账号方案——推荐建专用账号（如 `ai-digest-bot`）并在项目中以「编辑者」角色加入；或直接用创建者个人账号。凭据届时由用户写入 `data/.env`（不经对话传递）。
2. 飞书：目标群是否已可添加自定义机器人？提供 webhook + secret 的时间点。
3. 外部 wiki：具体是哪个系统/地址？
4. LLM API：可用厂商与 key（T4 调查时一并定）。
5. 部署机器与调度载体（T5）。
6. 初始信息源清单（T2 产出建议清单后由你勾选确认）。
