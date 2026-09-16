# 技术调查

## 调查范围声明（调查开始前界定）

- **会调查**：
  1. 公司 wiki（http://gr_wiki.grt.sy ）的架构识别与程序化写入方式（重点）
  2. 主流 AI 信息源的 RSS/API 可用性清单（重点）
  3. GitHub API 能力与限额
  4. LLM API 选型与成本估算（翻译 + 摘要）
  5. 调度与部署方式
- **不会调查**：爬虫框架深度选型（RSS/API 优先，仅轻量抓取兜底）、需付费或登录的墙外源、任何 UI 界面方案。
- **重点与深度**：分发与采集两项确认到「有明确 API 和调用示例、可直接实现」的程度；LLM 与调度确认到「选定方案」即可。

## 调查状态

| 编号 | 项目 | 状态 |
|---|---|---|
| T1 | 公司 wiki（MinDoc）架构与写入 API | ✅ 完成（2026-09-16，见下文） |
| T2 | 信息源采集通道（RSS/API 清单） | ⬜ 未开始 |
| T3 | GitHub API 能力与限额 | ⬜ 未开始 |
| T4 | LLM API 选型与成本 | ✅ 完成（2026-09-16 选定 GLM 包月订阅并**实测通过**，ADR-0008） |
| T5 | 调度与部署方式 | ✅ 决策完成（2026-09-16，ADR-0006：本机 + cron 一次性命令 + 并发可配置） |
| T6 | 微信推送通道 | ⏸ 延后（用户决定，见 ADR-0002） |
| T7 | 飞书群机器人通道 | ✅ 调查完成 / ⏸ 实施延后（ADR-0004，见下文） |
| T8 | 通用 wiki 源分析器可行性 | ⏸ 待用户提供样例 URL 后实测（ADR-0005） |
| T9 | 非 LLM 翻译工具选型 | ✅ 关闭（2026-09-16 决策改为 **LLM + 字节上限路由**，ADR-0010；Argos 调查留档备用） |
| T10 | 非 AI 分析手段（归类/摘要/过滤） | ✅ 设计内解决（RSS 自带摘要 + 规则归类 + 启发式过滤，见 ADR-0009 与 design.md） |

## T1 公司 wiki 架构调查

### 结论

公司 wiki（http://gr_wiki.grt.sy ，「谦川科技知识库服务」）**确认为 MinDoc**（开源项目 https://github.com/mindoc-org/mindoc ，Go + beego2 + nginx/1.13.8 反代）。程序化写入走其 Web API：**表单登录获取会话 cookie → POST 建文档 → POST 写 markdown 内容**。无静态 API token，写接口必须携带登录会话。

### 证据（2026-09-16 实测）

- 响应头：`Mindoc-Site: https://www.iminho.me`、Cookie `mindoc_id`、`Mindoc-Version`（值为空，版本隐藏）。
- 首页标题：`谦川科技知识库服务 - Powered by MinDoc`；静态资源版本参数 `v=20240731111406`，推断部署构建于 2024-07（约 v2.2 时期）。
- 源码核实自 mindoc-org/mindoc master（2026-07），关键行为已在内网实测一致（见下）。
- `/mcp/*`（新版 MCP 接口）在内网为 404，未部署，不可用。

### 写入相关 API（源码核实）

| 端点 | 方法 | 关键参数 | 说明 |
|---|---|---|---|
| `/login` | POST | `account`、`password`、`is_remember=yes`、`_xsrf` | 登录；返回会话 cookie；`is_remember=yes` 额外下发 30 天加密免登 cookie |
| `/api/{key}/create` | POST | `identify`（项目 key）、`doc_name`、`doc_identify`（可选）、`parent_id`、`is_open` | 创建文档节点，返回含 `doc_id`；不写内容 |
| `/api/{key}/content/{doc_id}` | POST | `markdown`（或 `html`）、`version`、`cover=yes` | 保存文档内容；版本冲突时需 `cover=yes` 强制覆盖；支持历史版本与自动发布选项 |
| `/api/{key}/content/{doc_id}` | GET | — | 读取文档内容（可用于发布前校验） |
| `/api/{key}/delete` | POST | `doc_id` | 删除文档 |

- `{key}` 为项目（book）的 identify，需先在 wiki 上建好目标项目并获得账号的编辑权限。
- 响应为 JSON：成功 `{"errcode":0, ...}`；未登录 `{"errcode":403,"message":"请登录后再操作"}`。

### 鉴权链路

1. `/api/*` 全部经过登录过滤器（`routers/filter.go`），仅认**会话**或「记住我」cookie，**不存在静态 API token**（`MemberToken` 模型是邮件找回密码用途）。
2. 登录验证码由站点选项 `ENABLED_CAPTCHA` 控制；**内网登录表单无验证码输入框（实测）**，即未开启。
3. 会话过期后，用 `is_remember=yes` 得到的 30 天免登 cookie 可自动恢复登录。

### 无头写入方案（已确定可实现）

```
GET  /login                     → 取 _xsrf 与初始 cookie
POST /login (account/password/is_remember=yes)
POST /api/{key}/create          → 得 doc_id
POST /api/{key}/content/{id}    (markdown=..., cover=yes)
```

- 持久化 cookie jar；每次发布前用轻量已登录探测（如 AJAX 访问受保护页）检测 403/302，失效则重走登录。

### 风险与错误处理

- **会话失效**：检测 403/302 → 自动重登（remember cookie 30 天内免密）；重登也失败则告警并在运行报告中标注「wiki 发布失败」，成品仍落 `result/` 不丢失。
- **版本落后**：内网部署（~2024-07）落后 master；仅使用已在内网实测存在的端点与行为（create/content/delete/登录），不依赖新版特性。
- **版本冲突**（6005 confirm_override_doc）：digest 场景直接传 `cover=yes` 覆盖。
- **凭据管理**：账号密码存本地配置（不入 git），泄漏影响面为该 wiki 账号。

## T7 飞书群机器人通道调查

### 结论

飞书「群自定义机器人 webhook」满足分发通道需求：无需管理员审核、纯 HTTP POST JSON、支持富文本（含链接）与交互卡片。作为首个外部分发通道技术上成立。

### 关键事实（来源：飞书开放平台官方文档，2026-09-16）

- Webhook：`POST https://open.feishu.cn/open-apis/bot/v2/hook/xxx`，`Content-Type: application/json`；群设置内添加，仅限本群使用。
- 消息类型：`text`、`post`（富文本，支持 `a` 链接/`at`）、`interactive` 卡片（仅跳转 URL，无回调交互）、`image`、`share_chat`。
- 签名校验（安全设置：关键词、IP 白名单、签名）：`sign = base64(HmacSHA256(key = timestamp + "\n" + secret, message = ""))`；`timestamp`（秒）与 `sign` 随请求体提交，时间戳有效期 1 小时。
- 限制：单租户单机器人 100 条/分钟、5 条/秒；请求体 ≤20KB；建议避开整点/半点发送（11232 限流）。
- 错误码：19021 签名失败、19022 IP 白名单失败、19024 关键词不匹配。

### 风险与错误处理

- 单条 20KB 上限 → 全文推送需按章节分片（设计见 design.md §5）。
- webhook 地址即凭据 → 存 `data/.env` 不入 git；签名 secret 同理。

## T4 LLM 选型（GLM 包月订阅）

### 结论

LLM 用用户已有的 **GLM Coding Plan 包月订阅**：在其控制台生成套餐专用 API Key，工具走 **OpenAI Chat Completions 兼容接口**调用；包月额度内无按量费用，"成本估算"转化为"额度是否够用"（以实测与用量监控为准）。

### 关键事实（来源：智谱官方文档 docs.bigmodel.cn，2026-09-16）

- Key 获取：登录后「个人编程套餐 → 套餐概览」新建 API Key；**套餐 Key 与平台普通 API Key 不通用**（团队版同理）。
- 接口地址（套餐）：
  - OpenAI Chat Completion：`https://open.bigmodel.cn/api/coding/paas/v4`（本工具采用）
  - Anthropic Message：`https://open.bigmodel.cn/api/anthropic`
- `model` 参数文档未列出全集（实现期用测试调用确认，如 `glm-4.7` 系列）。
- 每轮用量预估（估算，供额度核对）：按每日 ~50 条、每条「原文 800 token + 输出 300 token」计，日约 5.5 万 token、周约 40 万 token，远低于包月套餐典型额度；工具侧另有 `llm_rpm` 限速保护。

### 风险与错误处理

- **用途限制**：套餐文档注明"仅限官方支持的指定工具与产品环境使用"。本工具为自用脚本，若实测被拒或违反条款，回退方案：平台普通 Key 按量计费调用同系列 GLM 模型（费用很低），或用户改用资源包。
- **额度耗尽/限流**：按 design.md §7 的 LLM 错误处理（退避重试、条目降级 skipped）。
- **待完成验证**：~~拿到 Key 后做一次真实调用验证~~ ✅ 已完成（2026-09-16）：`https://open.bigmodel.cn/api/coding/paas/v4` + 套餐 Key + 模型 `GLM-5.3-flash` 实测通过。注意：该模型为思考型（响应含 `reasoning_content`），**max_tokens 需给足**（小值会把预算耗在思考上导致正文为空）。

## T9 非 LLM 翻译工具选型（初步）

### 结论

首选 **Argos Translate**（Python 库、开源、本地离线、OpenNMT 内核，`pip install argostranslate` 后装 en→zh 语言包）承担标题与短文本的英译中；LLM 作为质量兜底（长段/关键条目可配置走 LLM）。LibreTranslate 只是 Argos 的服务化封装（Docker 部署），对本项目是多余一层，不采用。

### 关键事实（2026-09-16 快查）

- Argos Translate：纯本地、无调用限制、无外部依赖；en→zh 语言包数百 MB，一次性下载。
- 质量：对标题/短句可用；长技术段落弱于 LLM/DeepL——所以按文本长度/重要性路由：短文本走 Argos，长文与周报导语可走 LLM（配置项）。
- 不采用 Google 免费接口（非官方、易失效）与 DeepL 免费层（需注册、有额度）。

### 尾项（实现期）

~~用真实采集到的标题/简介样本做 Argos vs LLM 质量对比~~ 已取消——2026-09-16 用户改定翻译方案：LLM 优先 + 字节上限（ADR-0010），本节调查留档备用。

## ADR

### ADR-0001: wiki 发布采用「表单登录 + cookie 会话 + MinDoc Web API」

- **状态**：已接受（2026-09-16）
- **背景**：需要定时把汇编结果发布到公司 wiki；内网 MinDoc 无静态 API token，MCP 未部署。
- **决策**：用脚本表单登录（`is_remember=yes`）维护 30 天 cookie 会话，通过 `/api/{key}/create` + `/api/{key}/content` 写入 markdown。
- **后果**：实现简单（纯 HTTP，无第三方依赖）；代价是需管理登录凭据与会话续期；服务端升级若改动这些端点需重新验证（已在 tech.md 固化验证方法）。

### ADR-0002: 微信推送通道延后

- **状态**：已接受（2026-09-16，用户决定）
- **决策**：发送方向先实现 wiki；微信作为后续任务，届时在企业微信群机器人 webhook 与 Server酱 等方案中选型调查。
- **后果**：分发模块需做成多通道抽象，wiki 通道先落地，微信通道后续按同一接口扩展。

### ADR-0003: 三段式架构——采集 → 内部 wiki 层 → 外部分发

- **状态**：已接受（2026-09-16，用户指定架构方向）
- **决策**：系统分为三段：采集层（RSS/GitHub/网页）→ 内部 wiki 层（本地 `result/` markdown 为事实源 + 内网 MinDoc 为阅读入口）→ 分发层（飞书等外部通道，从事实源读取，通道抽象可扩展）。
- **后果**：MinDoc 只是内部阅读入口而非数据源头，其故障不阻塞分发；`result/` 入 git 满足项目留痕要求；新增通道不改采集与汇编。
- **详细设计**：见 `ai/design.md`。

### ADR-0004: 飞书通道采用群自定义机器人 webhook

- **状态**：调查完成，实施延后（2026-09-16 用户更新：飞书与微信同为后续任务，暂不继续）
- **背景**：用户架构中引入飞书作为外部分发方向；T7 调查确认自定义机器人满足需求且零审批成本。
- **决策**：届时飞书通道用群自定义机器人 webhook（`post` 富文本/`interactive` 卡片 + HMAC 签名），不建飞书应用、不申请租户权限。
- **后果**：调查结论保留备用，后续实施时直接按本 ADR 执行；首期分发只做内部 wiki（MinDoc）。

### ADR-0005: 外部 wiki 采用「URL 配置驱动的通用源分析器」（采集侧）

- **状态**：提议（2026-09-16，待用户提供样例 URL 实测后转正，T8）
- **背景**：用户设想不绑定具体 wiki 系统——在配置表中放入 wiki URL，程序自动分析该 URL 的内容或子网页内容。经确认这是**采集方向**（把外部 wiki 当作资料来源），而非发布目标。
- **决策**：在采集层实现通用 wiki 源分析器，按自动探测阶梯处理：① 优先 RSS/Atom → ② 识别 MediaWiki/DokuWiki 等带 API 的系统走其 API → ③ sitemap.xml → ④ 同域有界爬取（深度与页数上限内）。遵循 robots.txt、每域限速。
- **边界**：JS 重渲染（SPA）站点需要无头浏览器，与低负载要求冲突，默认不支持——检测到时在运行报告中标记「该源需人工处理」。
- **后果**：新增源只需填 URL 即可接入，无需为每种 wiki 写适配；可行性最终以用户提供样例 URL 的实测为准。

### ADR-0006: 部署于本机，低负载优先

- **状态**：已接受（2026-09-16，用户决定）
- **决策**：程序部署在本机；用 cron（或 systemd timer）触发一次性命令，进程跑完即退出，**无常驻服务**；负载控制：抓取并发默认 2（可配置上限）、每域串行且间隔 ≥1 秒、LLM 调用按每分钟上限限速、单轮运行设时长预算；存储用 SQLite。
- **后果**：空闲期零负载，运行期网络与 CPU 占用可控；代价是时效性取决于 cron 周期（符合"每天/每周"需求）。

### ADR-0007: 采集与分发均为配置驱动（类型 + 地址/ID），新类型走「调查→适配」流程

- **状态**：已接受（2026-09-16，用户安排）
- **背景**：用户要求采集多来源、分发多目标，各自用一份配置文件设置，每项为类型+地址（或 ID）；程序暂不支持的类型由 AI 调查后用已有工具或自制工具补齐（用户后续提供示例）。
- **决策**：`config/sources.yaml` 与 `config/channels.yaml` 双配置驱动；每个 type 对应一个适配器；未支持类型在校验时报错、运行时跳过该单项不阻塞；新类型按项目流程（调查记 tech.md → 优先现成工具 → 自制 → task/verify 记录）。
- **后果**：新增来源/目标只需改配置；适配器集合可增量扩展；配置 schema 见 design.md §2。

### ADR-0008: LLM 采用 GLM 包月订阅（OpenAI 兼容接口）

- **状态**：已接受（2026-09-16，用户决定）
- **决策**：翻译/摘要/分类/趋势解读统一调用用户已有的 GLM Coding Plan：套餐 Key + `https://open.bigmodel.cn/api/coding/paas/v4`（OpenAI Chat Completions 兼容）；凭据填 `ai/secret.md` 的 `LLM_BASE_URL/LLM_API_KEY/LLM_MODEL`。
- **后果**：包月额度内零边际成本，成本关注点变为额度余量（工具限速 + 用量监控）；若套餐对非指定工具调用受限，回退平台按量 Key 调用同系列模型。细节见 tech.md T4。

### ADR-0009: 工具优先，AI（LLM）仅兜底

- **状态**：已接受（2026-09-16，用户原则）
- **决策**：实现工具本身尽量由 AI 编写；但工具**运行时**尽量少用 LLM——
  1. 采集与发送一律用现成工具（RSS 解析、HTTP API、webhook），无 LLM；
  2. 翻译：首选本地 Argos Translate（T9），LLM 仅用于长文/关键内容（可配置路由阈值）；
  3. 分析：用 RSS 自带摘要 + trafilatura 正文抽取 + 关键词规则归类 + 启发式过滤（T10），趋势统计本就是规则计算；
  4. LLM 仅保留两处：翻译兜底、周报成文的可选润色（`llm_polish`，默认关闭，纯模板成文）。
- **后果**：日常运行几乎不消耗 LLM 额度、更快更稳；代价是简介/导语的文字质量上限低于 LLM 全程生成，由 `llm_polish` 开关按需提升。
- **修订**：第 2 条"翻译首选 Argos"已被 [ADR-0010](#adr-0010-翻译采用-llm--字节上限路由成本折中) 取代——翻译改用 LLM + 字节上限，Argos 留档备用。

### ADR-0010: 翻译采用 LLM + 字节上限路由（成本折中）

- **状态**：已接受（2026-09-16，用户决定；取代 ADR-0009 第 2 条）
- **决策**：翻译引擎用 LLM（GLM 包月，ADR-0008），设字节上限 `translate.max_bytes`（默认 **5000 bytes**，UTF-8）：
  - 待译文本（简介/摘录）在上限内 → LLM 翻译；
  - 超上限 → **不翻译**，按 `translate.oversize` 处理：`keep_original`（默认，保留原文展示）或 `link_only`（只留标题与 URL，不展示原文）；
  - 标题始终翻译（很短，成本可忽略）。
- **背景**：超限内容多为长文，条目本就附 URL，翻译边际价值低；上限让单条 LLM 输入有界（≤ 约 2k token），包月额度消耗可控。
- **后果**：成本与合用的折中；Argos（T9）降为留档备用，不再实现。

## 下一步调查

1. T2：信息源 RSS/API 可用性清单（厂商博客、arXiv、Hacker News、中文源等）→ 产出 `sources.yaml` 初始清单供用户勾选。
2. T3：GitHub API（releases/activity、限额、是否配 token）。
3. T8：拿到用户提供的样例 wiki URL 后，实测「通用 wiki 源分析器」可行性（静态/JS 渲染判定、API/RSS/sitemap 探测、子页发现与正文抽取，见 ADR-0005）。
