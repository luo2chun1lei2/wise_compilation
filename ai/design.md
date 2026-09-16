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

> 2026-09-16 更新：Stage C 各外部通道（飞书、微信、外部发布类 wiki）**全部延后**——首期只实现 Stage A/B 与 MinDoc 发布，分发层保留 Channel 抽象（ADR-0004）。
> Stage A 同时纳入「通用 wiki 源分析器」：配置表中放入外部 wiki 的 URL，程序自动分析其内容/子页作为资料来源（ADR-0005，采集方向，待样例 URL 实测）。
> 流水线遵循「**工具优先，LLM 仅兜底**」（ADR-0009）：图中"LLM翻译+摘要+分类"更新为关键词规则归类 + 模板成文；翻译用 LLM + 字节上限路由（默认 5000 bytes，超限保原文/仅链接，ADR-0010）。

### 中间层的职责划分（关键设计）

「内部 wiki 文件」由**两个表示**构成，职责不同、内容一致：

| 表示 | 角色 | 说明 |
|---|---|---|
| 本地 `result/*.md` | **事实源** | 汇编产出先落此目录并入 git（满足项目「提交推送」要求）；分发通道从这里读取，不依赖内网 wiki 的可用性 |
| MinDoc 页面 | **内部阅读入口** | 发布器把 `result/` 成品同步到内网 wiki（API 已在 tech.md T1 核实）；MinDoc 故障不阻塞 Stage C |

> 该设计同时覆盖两种理解（先落本地 wiki 文件再外发 / 以内网 wiki 为中枢再外发），数据流一致。若与你的本意不符，指出后调整。

### 数据流

1. **采集**（每日；逐条处理管道：**获取材料 → 获取摘要 → 翻译判定 → 存库**，ADR-0011）：按 `sources.yaml` 逐源拉取 → 规范化 + 去重（已见条目跳过）→ **摘要级联提取**（纯工具：feed 自带摘要 → 文首 TL;DR/Abstract 段 → 文末 Summary/Conclusion 节 → 正文前 N 字节截断；中间正文不送 LLM）→ 归类（`topics.yaml` 关键词规则 + 重要性启发式）→ 翻译判定（中文源跳过；外文按 ADR-0010：简介 ≤ `translate.max_bytes` 走 LLM、超限 `keep_original/link_only`、标题始终译）→ 存 SQLite（含 `summary_from` 标记来源），原料索引追加至 `material/`（只存链接+摘要，符合需求约束）。
2. **汇编**（每周/手动；纯工具，零 LLM）：按专题/周期查询已入库条目 → 按专题模板渲染 markdown（新闻周报 / 技术汇总）→ 追加「趋势观察」（规则统计表格；LLM 解读仅当 `llm_polish: true` 时生成，默认关闭）→ 写 `result/`。
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
      wiki_src.py          # 通用 wiki 源分析器（URL 配置驱动：RSS→wiki API→sitemap→有界爬取，ADR-0005）
    pipeline/
      dedupe.py            # URL 规范化 + 内容 hash + 已见判重
      summarize.py         # 摘要级联提取：feed自带→文首TL;DR/Abstract→文末Summary/Conclusion→正文截断（纯工具，ADR-0011）
      classify.py          # 专题归类 + 重要性过滤（关键词规则/启发式，无 LLM）
      translate.py         # 英译中（采集期逐条执行）：LLM + 字节上限路由（max_bytes 默认 5000B；超限 keep_original/link_only，ADR-0010）
      digest.py            # 专题模板渲染（新闻周报 / 技术汇总，纯模板成文）
      trend.py             # 趋势统计（本期 vs 上期频次、条目数、star 增速，规则计算）
      llm.py               # LLM 客户端：仅兜底（翻译路由 / llm_polish 润色），默认低频使用
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
    settings.yaml          # 运行参数：concurrency.fetch/llm_rpm、translate.max_bytes/oversize、llm_polish 等
  requirements.txt
data/                      # 运行数据（不入 git）：wise.db、cookies.json、日志
material/                  # 原料索引（AGENTS.md 布局）
result/                    # 汇编成品 = 事实源（入 git）
```

### 配置文件设计（双配置驱动，ADR-0007）

**采集与分发均为多来源/多目标，全部由两个配置文件驱动**，每项 = `类型 + 地址（或 ID）`。

`config/sources.yaml`（采集源）：

```yaml
sources:
  - name: openai-news          # 唯一别名
    type: rss                  # 类型：rss | github | wiki | web
    url: https://openai.com/news/rss.xml
    topic: tech                # 归入的专题（topics.yaml 定义）
    enabled: true

  - name: pytorch
    type: github               # 地址为 repo；watch 指定关注项
    url: https://github.com/pytorch/pytorch
    watch: [releases]
    topic: tech

  - name: some-ai-wiki
    type: wiki                 # 通用 wiki 源分析器（ADR-0005）
    url: https://example-wiki/
    depth: 1                   # 子页爬取深度上限
    topic: tech
```

`config/channels.yaml`（分发目标）：

```yaml
channels:
  - name: internal-wiki
    type: mindoc               # 类型：mindoc | feishu | wecom | serverchan | …
    target: ai-digest          # 地址或 ID：MinDoc 项目 identify
    mode: full                 # full=全文写入 | card=摘要卡片+链接
    enabled: true
  # 延后的通道后续按同样格式追加，例如飞书：
  # - name: team-feishu
  #   type: feishu
  #   target: https://open.feishu.cn/open-apis/bot/v2/hook/xxx
  #   mode: card
```

**类型扩展规则**：每个 `type` 对应代码里一个适配器（采集适配器 / 通道适配器）。

1. 配置中出现的类型无适配器时，启动校验报错并列出已支持类型；运行时该项标记 `skipped(unsupported type)`，**不影响其他源/目标**。
2. 需要新类型时走项目流程：AI 先调查该类型的获取/发送方式（记入 tech.md），**优先用现成工具/库实现**，没有再自制；实现后在 task.md 排任务、verify.md 记验证。

## 3. 数据模型（SQLite `data/wise.db`）

| 表 | 关键字段 | 用途 |
|---|---|---|
| `sources` | id, name, type(rss/github/web), url, topic, enabled, last_fetch_at, fail_count | 源注册表与健康状况 |
| `items` | id, source_id, url_norm(唯一), title, title_zh, summary, summary_zh, **summary_from(feed/head/tail/truncate)**, lang, published_at, content_hash, status(new/used/skipped) | 采集条目；去重键 = url_norm |
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

> 2026-09-16 更新：飞书与微信同为后续任务（ADR-0002/0004），**首期不实现任何外部通道**，仅做 MinDoc 发布；本节内容作为后续通道实施依据保留。

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

- 所有子命令**幂等**（去重靠 url_norm + content_hash；重发布靠 doc_identify + cover=yes）。
- **部署决策（ADR-0006，2026-09-16）**：本机部署，cron（或 systemd timer）触发一次性命令，进程跑完即退出，无常驻服务。

### 负载与并发控制（ADR-0006）

| 项 | 默认值 | 说明 |
|---|---|---|
| `concurrency.fetch` | 2 | 并发抓取的源数量上限，可配置 |
| 每域策略 | 串行 + ≥1s 间隔 | 礼貌抓取，避免对目标站点压力 |
| `concurrency.llm_rpm` | 10 | LLM 每分钟调用上限，防突发用量 |
| 单轮时长预算 | 30 分钟 | 超时中止并在 runs 报告标注 |

- 存储 SQLite、无常驻进程、空闲期零负载；运行期为网络 IO 为主，内存占用预期 < 100MB。

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
2. 飞书：✅ 延后（2026-09-16）——与微信同为后续任务，调查结论保留（tech.md T7），届时按 ADR-0004 实施。
3. 外部 wiki：重新定义为「URL 配置驱动的通用源分析器」（ADR-0005，采集方向）——待用户提供样例 URL 后实测可行性（T8）。
4. LLM API：✅ 已定 GLM 包月订阅（2026-09-16，ADR-0008）——用户在智谱控制台「个人编程套餐 → 套餐概览」生成 Key 填入 `ai/secret.md`；实现期做一次真实调用验证。
5. 部署机器：✅ 本机（2026-09-16，ADR-0006）——低负载设计，并发量可配置（见 §6）。
6. 初始信息源清单：待 T2 产出建议清单，与用户后续给出的源示例合并勾选确认；分发目标初始仅 `internal-wiki`，其余等用户提供示例后追加。
