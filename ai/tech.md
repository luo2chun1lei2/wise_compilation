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
| T2 | 权威 AI 信息源清单 | ✅ 清单产出（2026-09-18，见 T2 小节；RSS 端点存活待接入时逐个验证） |
| T3 | GitHub API 能力与限额 | ✅ 完成（2026-09-16，官方 Search API + 实测三策略对比，ADR-0012） |
| T4 | LLM API 选型与成本 | ✅ 完成（2026-09-16 选定 GLM 包月订阅并**实测通过**，ADR-0008） |
| T5 | 调度与部署方式 | ✅ 决策完成（2026-09-16，ADR-0006：本机 + cron 一次性命令 + 并发可配置） |
| T6 | 微信推送通道 | 🔶 调查完成；通道全部暂缓（2026-09-17：企业微信无组织；WxPusher 因**内部信息不得经公众号外发**而搁置试验，ADR-0016/0017） |
| T13 | 邮件通知通道 | ✅ 方案确定（2026-09-17，ADR-0018：公司 SMTP + 同事邮箱清单；工具已预置，待用户提供 SMTP 参数实测） |
| T14 | 微信公众号文章/视频号采集 | ⏸ 搁置（2026-09-17 用户决定：自动汇集不可行、依赖人工选文；"手动投喂/邮件投喂"变体留档 T14 小节，需要时再启用） |
| T15 | InfoQ / CSDN 文章接口 | ✅ 调查完成（2026-09-17，见 T15 小节：InfoQ 匿名无接口；CSDN 搜索接口可用并已实装，ADR-0019） |
| T7 | 飞书群机器人通道 | ✅ 调查完成 / ⏸ 实施延后（ADR-0004，见下文） |
| T8 | 通用 wiki 源分析器可行性 | ⏸ 待用户提供样例 URL 后实测（ADR-0005） |
| T11 | GitHub star 增速查询 | ✅ 调查完成（2026-09-16，见 T11 小节：官方 API 无此能力，采用自记录基线） |
| T12 | 知乎信息源 | ✅ 调查完成（2026-09-16：热榜 API + **专栏文章 API 均无需登录**；专栏订阅为主，ADR-0014/0015，实测 V4/V5） |
| T9 | 非 LLM 翻译工具选型 | ✅ 关闭（2026-09-16 决策改为 **LLM + 字节上限路由**，ADR-0010；Argos 调查留档备用） |
| T10 | 非 AI 分析手段（归类/摘要/过滤） | ✅ 设计内解决（摘要级联提取：feed 自带/文首 TL;DR/文末总结/截断 + 规则归类 + 启发式过滤，ADR-0011） |

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
- **2026-09-16 端到端实测修订（V6）**：会话探测改用非 AJAX 的 `/book`（部署版 `/setting` 匿名也 200；过滤器对 AJAX 返回 200+errcode JSON）；create 响应字段为 `doc_id`；文档树按 `doc_identify` 幂等匹配；delete 需带 `identify` 参数；建项目需 `itemId`（`/book/itemsets/search`）。详见 verify.md V6 与 `tools/mindoc_publish.py`。

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

## T2 权威 AI 信息源清单（2026-09-18，用户要求的调查）

> 范围声明：调查权威性与覆盖面（实验室/媒体/newsletter/研究/社区榜单五类），标注可采集路径；RSS 端点存活不在本轮逐个实测（接入时验证）。

### 国外

| 类别 | 来源 | 特点 | 获取路径 |
|---|---|---|---|
| 实验室官方 | OpenAI News / Anthropic News / Google DeepMind Blog / Microsoft Research / NVIDIA Blog / Mistral News | 一手信源，权威性最高 | 均有或大概率有 RSS（接入时验证） |
| 实验室官方 | Meta AI Blog / Hugging Face Blog / Allen AI | 同上；HF Blog 有 feed.xml | RSS |
| 专业媒体 | MIT Technology Review AI、Ars Technica AI、The Verge AI、VentureBeat AI、TechCrunch AI、Wired AI | 深度报道与产业新闻 | 均有 RSS |
| Newsletter | Import AI（Jack Clark/Anthropic 联创，研究+政策）、The Batch（DeepLearning.AI）、Latent Space（工程师向）、Interconnects（Nathan Lambert，开源/RLHF）、Simon Willison Weblog（LLM 实践第一手）、Ahead of AI（Raschka）、TLDR AI（每日聚合） | 权威性来自作者专业度；多源交叉认可（2026 年多个榜单） | Substack/自有站多有 RSS |
| 研究/论文 | arXiv cs.AI/cs.CL/cs.LG、Hugging Face Daily Papers | 论文一手流 | arXiv 官方 RSS；HF papers 页 |
| 社区/榜单 | Hacker News（Algolia API）、Reddit r/MachineLearning & r/LocalLLaMA（JSON API）、LMArena（Chatbot Arena）、Artificial Analysis（能力/价格横评）、Epoch AI（算力与趋势数据）、OpenRouter Rankings（真实用量份额） | 热点风向与客观基准 | API/网页 |
| 已停运 | Papers with Code（2025 归档） | — | 不推荐 |

### 国内

| 类别 | 来源 | 特点 | 获取路径 |
|---|---|---|---|
| 技术媒体 | 机器之心 | 学术/技术深度，论文解读 | 知乎专栏已接入 ✓；官网 RSS 待验证 |
| 产业媒体 | 量子位 | 产业+大众，更新快 | 知乎专栏已接入 ✓；官网 qbitai.com |
| 快讯媒体 | 新智元 | 快讯密集、编译为主，量大需甄别 | 公众号为主 |
| 学术机构 | 智源社区 BAAI（hub.baai.ac.cn） | 研究院背景，学术权威 | 网页 |
| 产业智库 | 甲子光年、36氪 AI 频道 | 产业/创投视角 | RSS/接口待验证 |
| 技术社区 | CSDN AI 频道、知乎专栏 | — | 已接入 ✓（ADR-0019/0015）；InfoQ 接口不通（T15） |
| 国内实验室 | 智谱、DeepSeek、Qwen（qwen.ai+GitHub）、文心、豆包/火山 | 官方一手（中文） | 官网新闻页/公众号/GitHub，接入时核验 |
| 模型社区 | 魔搭 ModelScope | 模型动态 | 网页 |

> 注：知乎社区对"机器之心/量子位/新智元"存在标题党/编译夸大的批评——建议以实验室一手信源为主、媒体为扩散层交叉阅读。

### 国内源实测（2026-09-18，按 ADR-0020 三原则）

| 来源 | 正规渠道 | 2026 活跃 | 清单语义 | 结论 |
|---|---|---|---|---|
| 量子位 | ✅ 官网 RSS `qbitai.com/feed`（WordPress，10 条/次） | ✅ 实测当日（2026-09-18）仍在更 | 最新 10 条 | **可接入**（type: rss，待实现适配器） |
| 机器之心 | 官网 RSS 已停用（302→数据服务营销页）；知乎专栏 = 合规通道 | ✅ | 最新 N 篇 | **已覆盖**（zhihu-ai-columns） |
| 新智元 | 知乎专栏 xinzhiyuan | ❌ 最新一篇 2025-07-09 停更；公众号无合规接口 | — | **排除** |
| 智源社区 BAAI | hub.baai.ac.cn 为 SPA、无 RSS；站内有「风云榜」（排名语义）但数据在接口后 | 未确认 | 风云榜=排名 | 待深查（可选） |
| 甲子光年 | `/feed` 连接失败，无公开 RSS | 未确认 | — | 排除（暂） |
| 36氪 | 官网 feed 与 AI 频道页均为 SPA 壳，无公开 RSS/API | — | — | 排除（正规渠道无） |
| CSDN AI | ✅ 搜索接口 + nav/ai 频道页 | ✅ | 热点（编辑流）/时间窗搜索 | **已覆盖**（ADR-0019） |
| 智谱 | 官网新闻页（898KB，含 2026-08 日期数据，标题提取待深查） | ✅（页面日期 2026-08） | 最新 | 候选，待深查提取 |
| DeepSeek | 官网 SPA；api-docs 的 news 为文档站、列表客户端渲染 | 未确认 | changelog | 候选弱 |
| Qwen | qwen.ai/blog 为 SPA；合规通道 = GitHub（QwenLM org releases） | ✅ | release 流 | **可经现有 github 类型接入**（加源即可） |

**接入优先级建议**：① 量子位 RSS（需实现 rss 适配器，feed 自带 10 条=最新规则）；② Qwen 的 GitHub 源（零新代码）；③ 智谱/智源风云榜深查（可选）。

### x.ai 调查（2026-09-18，用户指定）

| 项 | 结果 |
|---|---|
| 直连 | ❌ **DNS 污染**（x.ai 解析到 Facebook IP 段），无法建立连接 |
| 走本机 VPN 代理（127.0.0.1:10077） | ⚠️ 可连通但 **Cloudflare 403 JS 质询**（完整浏览器头仍被拦）——过质询需无头浏览器，属规避反爬，不采用 |
| 专门 research/engineering 板块 | 无法核实（页面被拦）；据公开信息 x.ai 研究内容主要混在 /news 与 arXiv 论文，无独立工程博客 |
| 过滤成本（若可达） | 规则过滤=0 token（标题关键词分类）；LLLM 过滤≈10 条标题 1 次调用 ≈ 0.1~0.15 万 token/天（当前日用量的 1%） |
| 结论 | **本机不可达，暂不接入**。替代：Grok/xAI 动态由 TechCrunch AI、Hacker News 等源间接覆盖；必要时走手动投喂链接 |

### 国内大模型厂商渠道实测（2026-09-18，用户指定的六家）

| 厂商 | GitHub 组织（近 30 天活跃仓库，实测） | 官网新闻/博客 | 结论 |
|---|---|---|---|
| DeepSeek | ✅ `deepseek-ai`（8 个：deepseek-harness 228k★、FlashMLA、DeepEP…） | 官网 SPA，无合规列表 | **GitHub 接入** |
| 智谱 | ✅ `zai-org`（GLM-5 7.2k★、GLM-V、SCAIL-2…） | news 页有 2026-08 数据但在 JS 后（标题提取待深查） | **GitHub 接入**；官网待深查 |
| Kimi（月之暗面） | ✅ `MoonshotAI`（kimi-cli 11.4k★、kimi-code、FlashKDA…） | moonshot.ai 为产品页，无新闻流 | **GitHub 接入** |
| 豆包（字节） | ✅ `bytedance`（31 个活跃，头部为 deer-flow 82.6k★/UI-TARS 等 AI 仓库，混杂部分非 AI 基础设施） | 火山引擎为产品页，无新闻列表 | **GitHub 接入**（star 排序下头部均为 AI；噪声可接受） |
| 腾讯混元 | ✅ `Tencent-Hunyuan`（7 个：HunyuanOCR、AuK、UniRL…） | hunyuan.tencent.com 为 6.9KB SPA 壳 | **GitHub 接入** |
| 华为盘古 | ❌ 无公开模型组织（MindSpore 为框架非盘古）；盘古不开源 | 华为云产品页，无资讯流 | **暂无合规通道**（公众号/华为云资讯为主） |

> 六家的模型发布动态在 GitHub releases 上都足够及时；官网侧全部 SPA/产品页，本轮不深查（智谱 news 页留作后续候选）。

### 国外源实测（2026-09-18，原则同国内：ADR-0020）

| 来源 | 渠道（实测） | 2026 活跃 | 清单语义 | 结论 |
|---|---|---|---|---|
| OpenAI News | ✅ RSS `openai.com/news/rss.xml` | ✅ 当日 | 最新 | **可接** |
| Google DeepMind Blog | ✅ RSS `deepmind.google/blog/rss.xml` | ✅ 09-15（Gemini 3.8） | 最新 | **可接** |
| NVIDIA Blog | ✅ RSS `blogs.nvidia.com/feed/` | ✅ 当日 | 最新 | 可接（全站，非 AI 专属） |
| Microsoft Research | ✅ RSS `microsoft.com/en-us/research/feed/` | ✅ 08-31 | 最新 | 可接 |
| Anthropic News | ❌ 无 RSS（各路径 404，页面无 feed 声明） | — | — | 暂缓（后续可 web 定向抓取） |
| Mistral / Meta AI | ❌ 本机网络不可达（000） | — | — | 暂缓 |
| MIT Tech Review | ✅ RSS `technologyreview.com/feed/` | ✅ 当日 | 最新 | 可接（全站） |
| TechCrunch AI | ✅ RSS `techcrunch.com/category/artificial-intelligence/feed/` | ✅ 当日 | 最新 | **可接（AI 专属）** |
| The Verge | ✅ Atom `theverge.com/rss/index.xml` | ✅ 当日 | 最新 | 可接（全站） |
| Ars Technica | ✅ RSS `feeds.arstechnica.com/arstechnica/index` | ✅ 09-16 | 最新 | 可接（全站） |
| VentureBeat AI | ⚠️ 429 限流 | — | — | 暂缓 |
| Interconnects | ✅ RSS `interconnects.ai/feed` | ✅ 09-11 | 最新 | **可接** |
| Latent Space | ✅ RSS `latent.space/feed` | ✅ 当日 | 最新 | **可接** |
| Simon Willison | ✅ Atom `simonwillison.net/atom/everything/` | ✅ 当日 | 最新 | **可接** |
| Ahead of AI（Raschka） | ✅ RSS `magazine.sebastianraschka.com/feed` | ✅ 09-09 | 最新 | 可接 |
| TLDR AI | ✅ RSS `tldr.tech/api/rss/ai` | ✅ 当日 | 最新 | **可接** |
| Import AI | ❌ 本机网络不可达（substack 域名） | — | — | 暂缓 |
| arXiv cs.CL/cs.AI | ✅ RSS `export.arxiv.org/rss/cs.CL` | ✅ 当日 | 最新 | 可接（量大，论文向） |
| Hacker News | ✅ 官方 Algolia API（front_page，带 points） | ✅ | **排名/热点**（points 排序） | **可接（需小适配器）** |
| Reddit r/ML | ❌ 未登录 JSON 被拒 | — | — | 暂缓 |

**成本注记**：国外源为英文 → 每条摘要走 LLM 翻译（≤5000B）。全量接入约 +100 条/天 ≈ 15~20 万 token/天（包月内可承受，但值得分层）。建议首批：OpenAI、DeepMind、TechCrunch AI、Latent Space、Simon Willison、TLDR AI、Interconnects（7 个精选）+ HN；全站类（NVIDIA/MIT TR/Verge/Ars）与 arXiv 视阅读价值二期再加。

### 全通路复检（2026-09-18，要求 #60：SOP 8 步 × 28 站点，tools/full_channel_check.py）

**修正两处早期结论**：
1. **InfoQ 中国有 `/feed`**（20 条/当日/中文/AI 浓度高）——T15 当时只探了 `/rss`/`sitemap`/`/public`/GraphQL 而 `/feed` 是唯一活口，结论修正为"可用"，已接入（`infoq-cn`）。教训：SOP 第 1 步（rel=alternate 自动发现）应最先做，猜路径会漏。
2. **Mistral 有 RSS**：真实地址 `mistral.ai/news/rss`（无 .xml 后缀；自动发现标签给出，此前猜 `/news/rss.xml` 落空），走代理可用（87 条），已接入（`mistral-news`）。

**其他站点复检结论（无变化）**：知乎/CSDN/智源/Qwen/智谱（sitemap 302 无效）/DeepSeek（sitemap 仅 44 个静态产品页）维持原判；机器之心 robots 声明 gzip sitemap（可用但与知乎专栏重复，不接）；MetaAI/VentureBeat/TheVerge 的 robots 均声明 sitemap（备选通道留档）；x.ai 仍 Cloudflare。在用源全部健康（alternate/rss 复核 200）。

### T16 社区/论文类源调查（2026-09-18，用户指定五站）

| 站点 | 渠道实测 | 2026 活跃 | 清单语义 | 结论 |
|---|---|---|---|---|
| Hacker News | 官方 Algolia API（已接入 ADR-0013 前身/V13） | ✅ | **排名**（points） | 已接入（hackernews-top） |
| arXiv | `export.arxiv.org/rss/cs.AI`（官方 RSS，免登录） | ✅ 当日 48 篇 | 最新（无排名） | **已接入**（arxiv-cs-ai，rss 类型零新代码；描述元数据前缀已剥离） |
| 掘金 | `api.juejin.cn/recommend_api` 免登录 POST；AI 分类 cate_id=6809637771511070734 已验证；**sort_type=3 即热榜**（3=热门/200=最新，阅读量对比验证） | ✅ 当日 | **排名/热榜** | **已接入**（juejin-ai-hot，新 type: juejin；注：热榜混少量跨投非 AI 文，留待有用性评价） |
| Reddit | 匿名 JSON 直连/代理均被拒（403）；**官方路 = OAuth API**（需注册 reddit 应用拿 client_id/secret，免费） | — | top?t=week=排名 | 可接但需用户提供 Reddit 账号注册应用（待定） |
| 思否 | `/feeds` Atom 免登录（50 条/当日） | ✅ | 最新 | **不接**：内容为全站问答提问流（非技术文章），AI 占比低，价值有限 |

**同日运维**：github-trending-monthly 当日两轮直连超时（github.com 网络窗口），加 `proxy: true` 后恢复（数据验证成功）。

### T17 用户清单批次（2026-09-18，用户提供实测清单 → 按 ADR-0020 过筛接入）

| 处置 | 源 | 说明 |
|---|---|---|
| **接入·国际 6** | MIT TR、IEEE Spectrum AI、Berkeley BAIR、MS Research、GitHub Blog、Alignment Forum | 前 5 个 T2 已验证；Alignment Forum 新发现（AI 安全深度讨论，当日活跃）；MIT TR/GitHub Blog 为全站流 → `ai_filter: true` |
| **接入·国内 8** | 雷锋网、开源中国、爱范儿、极客公园、钛媒体、IT之家、Solidot、少数派 | 雷锋网 AI 专属；其余泛科技 → `ai_filter: true`（rss 适配器新增标题关键词过滤，纯规则零 LLM） |
| **排除** | SyncedReview | 最新一篇 2025-08-14——**不满足 2026 活跃**（ADR-0020 第 2 条） |
| **暂缓（留档）** | OpenAlex、Crossref | 文献元数据库，与 arXiv 定位重叠，日更场景价值有限 |
| **暂缓（留档）** | Semantic Scholar | 无 key 严格限流（429）；如需可申请免费 key 提额 |
| **可接未接（留档）** | Stack Exchange API | 匿名可用（sort=hot × tag=artificial-intelligence，排名语义）；问答形态，待用户确认需要再加 |
| 备注 | arXiv cs.LG | export.arxiv.org 直连当日抖动（cs.AI 正常），cs.LG 暂未接入，稳定后可加 |

**新能力**：rss 适配器支持 `ai_filter`/`keywords`（标题关键词过滤）；过滤后 0 条时输出占位文档（不落错渲染分支）。启用源 **46 个**。

### 新源调查标准流程（SOP，2026-09-18 固化，源自 ADR-0005 阶梯）

按序探测，**首个可用通道即停**（经济原则）；阶梯失败或结论存疑时做全通道扫描：

1. **RSS 自动发现**：首页 `<link rel="alternate" type="application/rss|atom+xml">`（比猜路径可靠）；
2. **常见 RSS 路径**：`/rss`、`/rss.xml`、`/feed`、`/feed.xml`、`/atom.xml`；
3. **已知开放 API**（领域常识：GitHub/HN Algolia/知乎专栏/CSDN/arXiv…）；
4. **sitemap.xml**（注意 sitemapindex 子图需展开，如 OpenAI/Anthropic）；
5. **robots.txt**（既看许可，也常暴露 sitemap 与架构线索）；
6. **服务端渲染 HTML**（正文/列表是否直接在 HTML 中）；
7. **结构化数据**（JSON-LD / Schema.org / OG 标签——可取标题/时间/摘要元数据）；
8. **外网站点**：直连失败先走 VPN 代理复测，再下"不可达"结论；
9. WAF/JS 质询 = 该站对匿名机器关闭，不规避（原则见 ADR-0009 同源决策）。

> 补查记录（2026-09-18）：对早期查得较浅的三源做全通道扫描——机器之心（无 alternate/无 sitemap/robots 常规）、甲子光年（全无）、36氪（sitemap/robots 均 SPA 壳）——**无遗漏通道，维持原结论**。

### 下一步（T2 落地）

用户从清单勾选 → 逐个验证 RSS/接口存活 → 加入 `sources.yaml`（rss 类型已设计未实现，实现后启用）。

## T3 GitHub 信息源调查

### 结论

GitHub **没有官方 Trending API**（trending 页面仅为 HTML，只能爬取，脆弱不采用）。采用**官方 Search API**，用「topic + star 阈值 + 时间窗」组合查询表达"AI 最热"；README 走 raw 接口获取。已端到端试跑验证（见 verify.md V1）。

### 关键事实（2026-09-16 实测，未认证）

- 搜索：`GET /search/repositories?q=<query>&sort=stars&order=desc&per_page=10`
- 三种"AI 热门"查询策略对比：

| 策略 | 查询 | 结果评价 |
|---|---|---|
| A 新项目 | `topic:artificial-intelligence created:>两周前` | 真实新项目但 star 低（最高 44★），偏"新"不偏"热" |
| B 关键词 | `ai created:>一周前` | 噪音大（玩笑仓库也能 1000+★），不可用 |
| C 热门+活跃 | `topic:artificial-intelligence stars:>500 pushed:>一周前` | ✅ **采用**：头部项目且本周活跃（AutoGPT 187k、LLMs-from-scratch 105k 等） |

- README：`GET /repos/{owner}/{repo}/readme` + `Accept: application/vnd.github.raw` → 原文 markdown（404 = 无 README）。
- 限额：未认证 core 60 次/时、search 10 次/分；配 token 后 core 5000 次/时、search 30 次/分。限额头 `X-RateLimit-*` 可读取。请求间隔 ≥1s（ADR-0006）。
- 试跑脚本：`tools/gh_ai_top10.py`（数据流五步完整实现，可复用为 github 采集适配器的基础）。

## T11 GitHub star 增速查询（2026-09-16）

### 结论

官方 Search API **不能**按 star 增速/时间窗增量查询（仅支持当前 star 数、created/pushed 过滤）。可行途径与实测：

| 途径 | 实测/核实结果 | 评价 |
|---|---|---|
| Stargazers API（`star+json` 媒体类型带 `starred_at`） | **必须认证**（未带 token 实测 401）；分页上限 400 页×100=**4 万条**，且只能从最早的开始翻 | 可精确算增速，但仅适用 <40k★ 的仓库；二分页每仓库约 9–10 次请求；需配 `GITHUB_TOKEN` |
| 第三方 OSS Insight（api.ossinsight.io） | 趋势排行接口实测**已失效**（其数据质量自 2026-03-01 起不可用） | 不可依赖 |
| GitHub Trending 页面 | 本质是周/月 star 增速排名，但纯 HTML 无官方 API | 爬取脆弱，ADR-0012 已排除 |
| **自记录基线** | 每日采集时已把 `items.stars` 入库；新增每日快照表后，任意时间窗增速 = SQL 差值 | ✅ **采用**：零额外请求、零第三方依赖；缺点是从开始记录日起有效（30 天后才有完整月增速） |

### 决策

~~主方案：自记录基线~~（2026-09-16 用户否决）。**主方案改为：解析 GitHub Trending 页面**（`mode: trending`，ADR-0013）——页面每行自带"本期新增 N stars"，一次抓取即得增速榜单；自记录基线不采用。

## T12 知乎信息源调查（2026-09-16）

### 结论

知乎**全站热榜 API 无需登录**（`GET api.zhihu.com/topstory/hot-list?limit=N&domain=www.zhihu.com`），返回标题/excerpt 自带摘要/回答数/创建时间/热度（detail_text）。已实现为 `zhihu` 源类型 `mode: hot-list`，用 AI 关键词表过滤出 AI 相关条目（ADR-0014）。

### 实测情况

| 入口 | 结果 |
|---|---|
| `api.zhihu.com/topstory/hot-list` | ✅ 无需登录；limit=50 实际最多返回 **30 条**；字段齐全（AI 占比低，热榜源默认停用） |
| **`www.zhihu.com/api/v4/columns/{slug}/articles`** | ✅ **无需登录**（用户所需的"文章流"）；每篇自带 标题/excerpt/链接/**点赞数**/评论数/创建时间；`sort_by=created` 按最新 |
| `www.zhihu.com/api/v4/columns/{slug}` | ✅ 专栏元信息（名称/简介/文章数）；**meta 的 updated 字段过期不可信** |
| 话题 feeds API / 机构号动态接口 | ❌ 需登录态或 404。补充探测（2026-09-16 晚）：`/topics/{id}/feeds/essence` 返回 403"请求参数异常"（端点真实存在，需登录 cookie + 可能需 x-zse-96 签名）；`/feeds/top`、`/feeds/timeline`、api.zhihu.com 域名下各话题端点均 404。"我关注的专栏/话题"提取接口（followed_columns/followees）匿名同样 404/401 → **提取用户关注列表必须 cookie** |

#### 带 cookie 实测（2026-09-16 晚，用户提供）

- cookie 规范化注意：从 DevTools Cookies 表格复制的是 `key "value"` 带引号格式，需重建为标准 `key=value; ...` 串（脚本已内置解析）。
- `/api/v4/me`：✅ 通（登录态有效，可拿 url_token）。
- 「关注的话题」页 HTML：200 但是纯 SPA 壳，无服务端数据；followed_topics 接口 404。
- **话题精华流：cookie 仍 403（code 10003）→ 必须逆向 x-zse-96 签名**。判定：脆弱（知乎改版即失效）+ 主账号跑签名请求有风控/封号风险，**不采用，话题路线关闭**。
- 结论：知乎内容获取以**专栏订阅（ADR-0015）为主**；新专栏由用户提供 `zhuanlan.zhihu.com/{slug}` 链接加入，无需任何凭据。
| 网页版 `www.zhihu.com/hot`、`zhuanlan.zhihu.com` | ❌ 403 反爬 |

- AI 专栏 slug 探测（2026-09-16）：`jiqizhixin`（机器之心，活跃）、`QbitAI`（量子位，活跃）、`paperweekly`（PaperWeekly，2023-11 后停更）；专栏 slug 即 `zhuanlan.zhihu.com/{slug}`，用户可自行追加。
- 中文内容全部 `zh-skip` 零 LLM；摘要用接口 `excerpt`（feed 级）。

## T14 微信公众号文章 / 视频号采集调查（2026-09-17）

### 结论

- **视频号：无合规通道**。内容仅在微信 App 内呈现，无任何公开网页/API 入口；自动化只能靠 App 逆向（封号风险，不采用）。
- **公众号文章：自动发现不可稳定，单篇解析可行**。文章页 `mp.weixin.qq.com/s/xxx` 公开可读（含标题/发布时间/正文），"3 天内 + AI 关键词"过滤都可在拿到 URL 后完成；**卡点只在"发现"**——微信不开放任意公众号的文章列表接口。

### 实测：搜狗微信搜索（发现途径）

- 搜索列表页 `weixin.sogou.com/weixin?type=2&query=AI`：✅ 能返回 10 条结果（标题+`/link` 跳转）。
- **链接解析：❌ 立即触发 antispider 验证码**（302 到 `antispider` 页）——搜狗经典行为：列表短暂可用、点进真实文章即拦。
- 判定：不可作为稳定采集通道（每日运行必然撞验证码）。

### 商业方案价格调查（2026-09-17 晚）

| 服务 | 价格 | 说明 |
|---|---|---|
| 新榜「新媒体API」 | **无公开报价，企业定制**（按榜豆积分计费，业内量级通常为数万元/年，需商务询价） | 数据合规、覆盖最全（含分钟级监测/文章搜索/回采） |
| wcplusPro | 公开订阅制：Pro ¥49.8 起（1 小时版），另有 2 天/1 月/6 月/1 年档（1 年价在软件内，百元量级）；Max 版支持自动采集+API | 功能完全覆盖"指定公众号最新文章"；**无任何合规声明**——本质为微信客户端协议桥，与本项目"不逆向"原则冲突，存在账号/条款风险 |
| 极致了数据 | 价格不公开，联系销售 | 号称含视频号接口 |

结论：合规路线（新榜）为万元级企业采购；百元级工具走灰色通道不符合项目原则。维持 ⏸ 搁置，除非公司层面愿意采购新榜。

### 补充实测（2026-09-17 晚）：「指定公众号」路径

- 搜狗**账号搜索**（`type=1&query=公众号名` → 账号主页快照 `/gzh?openid=` 列最新文章）：❌ **索引已失效**——「机器之心」「人民日报」均返回"暂无相关官方认证订阅号"（连顶级认证号都查不到，该索引需登录或已停摆）。
- 结论：**指定公众号的自动收集与关键词路径同样不可行**，且无其他官方/合规列表接口（桥接与商业 API 评价见上表）。T14 维持 ⏸ 搁置。

### 其余候选路径评价

| 路径 | 评价 |
|---|---|
| wechat2rss 类自建桥 | 需微信号登录态 + 常驻服务 + 封号风险（用主号不可接受）→ 不采用 |
| 新榜/西瓜数据等商业 API | 收费 + 需企业账号 → 暂不采用 |
| RSSHub 公众号路由 | 依赖上述桥接服务，大多已失效 → 不可依赖 |
| **手动投喂链接** | ✅ 可行：用户把文章 URL 粘贴进清单 → 工具抓取公开文章页（标题/publish_time/正文）→ 时间窗（如 3 天）+ AI 关键词过滤 → 汇入管道 |
| 内容覆盖备注 | AI 头部公众号（机器之心/量子位等）的内容与其网站/知乎专栏高度同步，现有源已覆盖大半 |

## T15 InfoQ / CSDN 文章接口调查（2026-09-17）

### InfoQ（infoq.cn）：❌ 匿名无可用接口

| 入口 | 实测 |
|---|---|
| `infoq.cn/graphql` | 301 → www 后 **405**（openresty 边缘拦截 POST，加 Origin/Referer 无效） |
| `/rss`、`/sitemap.xml` | 200 但落到 SPA 壳页面（无内容） |
| `/public/v1/*`、`/api/*` | **451**（拒绝） |
| 首页内嵌数据 | 无（674KB 全是前端资源，内容靠被拦的 GraphQL 加载） |

结论：~~合规匿名路径不存在~~ **修正（2026-09-18 全通路复检）：`/feed` 可用**（当时漏探该路径），已接入 `infoq-cn`（rss，中文零 LLM）；GraphQL/451 等判断仍成立。

### CSDN：✅ 搜索接口可用（已实装，ADR-0019）

- **搜索接口** `GET so.csdn.net/api/v3/search?q=AI&t=blog&tm=N&size=M`（无需登录）：
  - `tm` 时间窗参数实测：1=当天（全部今日）、2/3=更宽窗口；条目自带 `created_at` → 客户端可精确过滤"近 3 天"；
  - 字段：标题/链接/created_at/description 摘要/点赞(digg)/评论/作者——中文源零 LLM。
- **AI 频道页** `blog.csdn.net/nav/ai`：服务端渲染（21+ 篇当日 AI 文章+链接，无需登录），作为备选采集面。
- 已实现 `type: csdn, mode: search`（config：`csdn-ai-search`，query/tm/size/days 可调），产出 `result/2026-09-17/csdn-ai-search.md`（30 篇，V9）。
- **质量注记**：按 "AI" 关键词搜索偏入门科普文（赞多为 0）；调优手段：换关键词（如"大模型/AI Agent"）、加点赞门槛（digg>0）、或改用 nav/ai 频道页（编辑精选，质量高）。

## T6 微信通知调查（2026-09-17，用户要求重启）

### 结论

「发到微信群通知群成员+文档链接」的官方可行路径是**企业微信群机器人 webhook**（内部群）；**纯个人微信群无任何官方发送接口**（iPad 协议/PC Hook 等逆向方案封号风险高，不采用——同 x-zse-96 结论）。

### 关键事实（来源：企业微信官方文档 + 社区核实）

- **群机器人 webhook**（官方文档 developer.work.weixin.qq.com/document/path/91770）：
  - 地址 `POST https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=<KEY>`，JSON 体；
  - 消息类型：text / markdown（**支持 `[链接](url)`**、加粗、引用、颜色）/ image / news 图文 / file / template_card 等；
  - 限制：markdown ≤4096 字节（UTF-8）、20 条/分钟——发"新文档通知"绰绰有余。
- **群类型限制（多源核实）**：群机器人**仅支持企业内部群**；含微信用户的外部群（客户群）**不支持**添加机器人（官方底层限制；外部群另有"关键词自动回复"等弱方案，不适合主动推送）。
- **微信侧接收**：企业微信成员可在 **微信内通过"微信插件"收发企业微信消息**（免装企业微信 App），同事在微信里即可收到群通知。
- 候选替代：Server酱/PushPlus 推送到**个人**微信（服务号消息，非群、免费额度有限），仅当群方案不可行时作为退路。

### 实现要点

- webhook URL 存 `ai/secret.md`（`WECOM_WEBHOOK`）；发送脚本 `tools/wecom_notify.py`（markdown 消息 = 标题 + 当日文档链接清单，复用发布产物）。
- gr_wiki 为内网地址：群成员需在内网或 VPN 环境才能打开链接（通知文案中注明）。
- 待用户提供：企业微信内部群 + 添加群机器人后的 webhook key。

### 修订（2026-09-17）：公司无企业微信 → 改用 WxPusher 主题群发（ADR-0017）

- 用户反馈公司没有企业微信组织、无法建内部群 → webhook 方案（ADR-0016）暂不可用，代码保留待未来启用。
- **合规替代调查结论**（不碰逆向协议的前提下，微信侧能主动推送的官方形态只有"公众号消息"）：

| 方案 | 一对多 | 费用/限额 | 门槛 | 评价 |
|---|---|---|---|---|
| **WxPusher** | ✅ 主题 Topic 群发 | 永久免费，无硬性频率限制（"合理范围"） | 微信登录建应用即可 | ✅ **采用** |
| PushPlus | ✅ 群组编码 | 免费实名 200 次/天；**未实名 0 次**（实名需开会员） | 实名认证门槛 | 备选 |
| Server酱 | ❌ 单人为主 | 免费 5 条/天 | 低 | 个人退路 |

- WxPusher 工作方式：同事**扫码关注 WxPusher 公众号 + 订阅应用主题**（一次），脚本 `POST https://wxpusher.zjiecode.com/api/send/message`（appToken + topicIds + content）→ 所有订阅者微信收到公众号消息。消息形态是公众号消息而非群聊气泡；内容经第三方服务器转发（内网 URL 对外无意义，不放敏感内容）。
- 代码预置：`tools/wxpusher_notify.py`；凭据 `WXPUSHER_APP_TOKEN` / `WXPUSHER_TOPIC_ID`（ai/secret.md）。

## ADR

### ADR-0016: 微信通知采用企业微信群机器人 webhook（内部群）

- **状态**：~~已接受~~ 暂缓（2026-09-17 用户反馈公司无企业微信组织；代码保留，未来开通即用）
- **决策**：微信侧通知通道采用企业微信群机器人 webhook（markdown 消息带 gr_wiki 文档链接）；个人微信群与外部群不做（无官方接口）。webhook 凭据存 `ai/secret.md`。
- **后果**：需要群成员加入企业微信组织（或通过微信插件在微信内接收）；实现零依赖（POST JSON）。

### ADR-0017: 无企业微信场景下，微信通知采用 WxPusher 主题群发

- **状态**：提案 · 暂缓试验（2026-09-17 用户决定：**后续汇集内容将包含公司内部信息，不能以公众号形式公开外发**，故不启用；方案与代码保留，待将来仅推送不含敏感信息的纯提醒时再试验）
- **决策（提案内容）**：用 WxPusher（公众号官方消息通道，合规）：微信扫码登录创建应用得 appToken，创建主题得 topicId；同事扫码关注 WxPusher 公众号并订阅主题（一次性）；脚本 `tools/wxpusher_notify.py` POST markdown 消息（含 gr_wiki 文档链接）到主题 → 全员微信收到。
- **搁置原因（重要约束）**：消息经第三方服务器（WxPusher）+ 公众号通道转发，任何含公司内部信息的内容（甚至标题）都不应经此通道外发。
- **后果**：微信侧通知当前无启用通道（企业微信无组织、WxPusher 保密搁置）；若未来需要通知能力，候选：① 公司开通企业微信（ADR-0016，数据不出内网）；② 内网自建通知（如邮件/内网 IM，数据完全自控）。

### ADR-0018: 通知通道采用公司内网邮件

- **状态**：已接受（2026-09-17，用户提出；待 SMTP 参数实测后启用）
- **背景**：汇集内容含公司内部信息，不能经公众号/第三方通道外发（ADR-0017 搁置原因）；用户可收集同事邮箱。
- **决策**：经**公司 SMTP 服务器**发邮件通知（`tools/email_notify.py`，Python 标准库 smtplib，零第三方依赖）：`--test` / `--notify 标题 URL` / `--digest-day 日期`（当日发布汇总 + 文档链接）。凭据与收件人清单存 `ai/secret.md`（`EMAIL_SMTP_HOST/PORT/SSL/USER/PASS/FROM/TO`），内网免认证 relay 时 USER/PASS 留空。
- **探测记录（2026-09-17）**：`smtp/mail/email/pop/imap.grt.sy` 常见端口（25/465/587/110/143）均无响应——SMTP 服务器地址需用户从邮件客户端设置或 IT 获取。
- **后果**：数据不出内网（保密合规）；依赖公司邮件服务器可用性；收件人清单维护在 secret.md（不入 git）。



### ADR-0023: 代理连通性预检 + 失败源多轮重试

- **状态**：已接受（2026-09-21，用户确认后实现）
- **背景**：09-21 晨 06:33–06:45 代理握手持续超时（进程在但通道死），3 个代理源（deepmind/google-research/mistral）在"30 秒后单轮重试"下仍失败；09-20 06:10 同模式。抖动自愈周期是分钟级，重试间隔必须覆盖。
- **决策**：
  1. **代理连通性预检**（run_pipeline 采集前）：`proxy_alive()` 过代理实测 google `generate_204`（区别于 ensure_vpn 只查进程）；不通则 30s 步进等待，最多 5 分钟，仍不通才放行（告警，其余源不受影响）；
  2. **阶段 1.5 多轮重试**：失败源最多 3 轮，间隔 2/4/6 分钟递增（原为 1 轮 30 秒）。
- **代价上界**：最坏情况（预检等满 5 分钟 + 3 轮重试全跑）流水线延长约 20 分钟，发信仍在 07:45 前；仅在网络不佳日发生。
- **兜底不变**：失败不消耗采集间隔，RSS 最新-N 窗口次日自动补齐（延迟而非丢失）；手工 `--source` 可即时补采（09-21 已实践补齐 28/28）。

### ADR-0022: 结果页卡片式布局（合并榜单与详情，移动端友好）

- **状态**：已接受（2026-09-21，用户提出两点建议后实现）
- **背景**：旧格式为「宽榜单表格 + ## 详情段」双段——①链接/中文简介两处重复；②5~6 列宽表格在手机上横向溢出难读（用户手机实测反馈）。
- **决策**：改为**卡片式条目块**，一个条目一个 `### N. [标题](链接)（关键指标）` 标题行，下挂堆叠行：
  - `- 中文简介：`（全文，邮件端仍 320 字截断）
  - `- 原文简介：`（全文；zh-skip/空时省略；邮件端剥离）
  - `- 属性行`：`来源（专栏/作者）· 主题 · 推送 · 摘要 · 翻译` 按类型取有值段合并为一行
  - 关键指标按类型：GitHub=`stars★ · +增量★/期 · 语言`；feed=`发布 时间`；专栏类=`N 赞 · N 评论`（HN=`N 分 · N 评`）；知乎热榜=`热度`。
- **为何不用「id | 内容」堆叠表格**（用户草图方案）：表格单元格内无法嵌 `<details>` 折叠（邮件条目级折叠是既有要求 #42/#44），且左列在窄屏仍占宽；卡片块是用户堆叠布局去掉表格框的等价形式，信息组织相同（标题行/简介行/属性行）。
- **配套**：`email_notify.fold_details` 改为折叠任意 `### N.` 块，统计表保留在折叠外；新增 `--dry-run` 渲染到 `data/preview/` 不投递；`tools/reformat_cards.py` 一次性迁移历史格式文件（回收旧表格列中的专栏/语言）。
- **修订（2026-09-21 晚，要求 #67）**：邮件折叠条标题**不带链接**——标题链接与"点标题展开"手势冲突，手机易误点跳转；链接移至展开内容首行「- 原文链接：[打开原文](url)」。wiki 页不受影响（标题在网页上本就是跳转语义，无展开动作可冲突）。
- **后果**：md/wiki/邮件三端同构；文档更短（表格与详情不再重复）；手机上纵向堆叠无横向滚动。当日已发布页面就地迁移重发布，次日起流水线直接产出新格式。

### ADR-0021: 翻译缓存 + 源级采集间隔（消重与降本）

- **状态**：已接受（2026-09-20，用户确认方案后实现）
- **背景**：日采集存在两类浪费——①中低频源（周更/月更）同一批条目每天重复进邮件；②重复条目每天被重新翻译（DB 去重在翻译之后）。
- **决策（三层）**：
  1. **翻译缓存**：采集时先查 `items` 表，`url_norm` 已有 `summary_zh/title_disp` 的条目直接复用（lang=cache），仅新条目调 LLM；`items` 增列 `title_disp`；
  2. **源级间隔 `interval`**（sources.yaml，默认 1）：run_pipeline 按 `sources.last_fetch_at` 判断到期，未到期跳过（成功才更新 last_fetch_at，失败不消耗间隔）；手工 `--source` 不受间隔限制；
  3. **邮件自动跟随**：未到期的源当日无产物 → 不进邮件；到期但无新条目 → 占位"无更新"。
- **间隔分档（判断标准：间隔 ≈ 该源内容更新一轮的周期）**：日更=高频媒体与热榜；3 日=周更型 newsletter/媒体 + GitHub topic 榜 + blog.google；7 日=BAIR/Anthropic Eng/OpenAI Research/GitHub Trending 月榜/Anthropic Research。
- **后果**：邮件从"全量日快照"变为"当日真正新增"；LLM 日调用量预计降一半以上；低频源内容不再天天重印。间隔可逐源在 config 调整。

### ADR-0020: T2 信息源接入方向与准入三原则（待调查对象清单）

- **状态**：已接受（2026-09-18，用户指示）
- **决策**：T2 清单（tech.md T2 小节）所列来源作为**待调查对象**，按以下准入原则逐个调查后接入：
  1. **正规渠道**：仅走官方/公开合规通道（RSS、开放 API、服务端渲染页面），不做逆向与灰色抓取；
  2. **2026 年活跃**：仍在更新（最近内容在 2026 年内），停更即弃；
  3. **取数规则**：有排名取**排名前十**；无排名有热点取**热点头十条**；都没有则取**最新十条**。
- **顺序**：先国内（本轮），后国外。
- **后果**：调查结论逐源记录于 T2 小节（渠道/活跃度/清单语义三列），通过者按类型写入 sources.yaml。

### ADR-0019: CSDN 源采用 so.csdn.net 搜索接口

- **状态**：已接受（2026-09-17）
- **决策**：`sources.yaml` 新增 `type: csdn, mode: search`（query/tm/size/days 可配，tm 时间窗 + days 客户端过滤表达"近 N 天"）；条目映射：文章=标题、专栏=作者、赞/评论=digg/comment、摘要=description。备选采集面：nav/ai 频道页（服务端渲染）。
- **后果**：新增中文 AI 文章流（零 LLM）；搜索质量依赖关键词，可按 T15 注记调优。

### ADR-0013: github 源新增 trending 模式——解析 github.com/trending 页面

- **状态**：已接受（2026-09-16，用户指定；修订 ADR-0012 中"不爬 Trending 页"的条款）
- **决策**：`sources.yaml` 的 github 类型支持 `mode: trending`（参数 `since: daily|weekly|monthly`）：抓取 `github.com/trending?since=X`，按行解析出 仓库/描述/语言/总star/**本期 star 增量**，全流程复用数据流管道，产出文档带「本期新增」列。
- **风险与错误处理**：
  1. HTML 改版风险——解析到 0 行即抛错、按源隔离不影响其他源（ADR-0006）；
  2. github.com 网页域名偶发不可达（2026-09-16 实测超时，api.github.com 不受影响）——3 次退避重试；
  3. Trending 无 topic 过滤（全站榜），如需 AI 过滤可在汇编层按关键词/项目清单筛选。
- **后果**：直接获得"月增 N★"级别的增速数据，零第三方依赖；代价是依赖页面结构（已固化解析与 0 行告警）。实测：21 行全部解析成功（V3）。

### ADR-0014: 知乎源采用全站热榜 API + AI 关键词过滤

- **状态**：已接受（2026-09-16，用户要求新增知乎源）
- **决策**：`sources.yaml` 新增 `type: zhihu, mode: hot-list`（limit≤30，`ai_filter: true` 按内置 AI 关键词表过滤标题，`keywords` 可追加）；条目映射：话题=标题、热度=detail_text、回答数=answer_count、摘要=excerpt（feed 级自带）；话题级接口需登录，未采用。
- **后果**：零登录、零 LLM（中文源自动 zh-skip）获取知乎热点；AI 条目数取决于热榜当日构成（实测 30 条中约 2 条），按天采集累积；如需 AI 话题流全量，后续可由用户提供知乎 cookie 扩展。
- **修订**：2026-09-16 用户反馈热榜非所需（要文章/专栏内容）——知乎信息源主方式改为专栏订阅（ADR-0015），热榜源默认停用（`zhihu-hot.enabled: false`）。

### ADR-0015: 知乎源主方式改为专栏文章订阅（mode: column）

- **状态**：已接受（2026-09-16，用户要求获取 AI 文章/专栏内容）
- **决策**：`type: zhihu, mode: column`，配置 `columns: [slug...]`（slug 即 `zhuanlan.zhihu.com/{slug}`，用户可自行追加）、`per_column`（每专栏取最新 N 篇）、`rank_by: updated|voteup`（按发布时间或点赞热度排序）。数据来自 `api/v4/columns/{slug}/articles`（无需登录），每篇自带 点赞/评论/excerpt。
- **后果**：直接获得 AI 机构号/作者的文章流，点赞数可作热点排序；新增专栏只需在配置加 slug；停更专栏不产生条目（自然失效）。实测：机器之心+量子位 30 篇（V5），当日内容。

### ADR-0012: GitHub 源采用官方 Search API（策略 C 组合查询），不爬 Trending 页

- **状态**：已接受（2026-09-16）
- **决策**：`sources.yaml` 的 `github` 类型用 Search API（topic + stars 阈值 + pushed 时间窗，参数可配）+ README raw 接口；不爬取 trending HTML。
- **后果**：稳定、官方支持、限额可预期；"热"的语义由查询参数表达，可按需调整（如仅看新项目用策略 A）。
- **修订**：2026-09-16 起"不爬 Trending 页"条款由 [ADR-0013](#adr-0013-github-源新增-trending-模式解析-githubcomtrending-页面) 的 trending 模式取代（用户指定）。

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

### ADR-0011: 摘要级联提取（文首/文末优先），处理管道「采集→摘要→翻译判定→存库」

- **状态**：已接受（2026-09-16，用户提出）
- **决策**：
  1. 单条摘要**不用 LLM 生成**，按级联提取（纯工具）：① feed 自带 summary/description → ② 文首摘要段（识别 "TL;DR"、"Abstract"、"摘要" 等标记或首段）→ ③ 文末总结节（识别 "Summary/Conclusion/总结/结论" 标题的节）→ ④ 都没有则正文前 N 字节截断。中间正文不送 LLM。
  2. 逐条处理管道固定为：**获取材料 → 获取摘要 → 翻译判定 → 存库**，在每日采集期完成（归类规则亦在此步）；周汇编退化为纯模板拼接 + 规则趋势统计，零 LLM（`llm_polish` 除外）。
  3. 存库记录摘要来源 `summary_from`（feed/head/tail/truncate）便于验证与调参。
- **后果**：LLM 仅剩"翻译判定通过的外文摘要"一处；摘要质量取决于原文写作习惯（有 TL;DR 的文章效果最好）；中文源全程零 LLM。

## 下一步调查

1. T2：信息源 RSS/API 可用性清单（厂商博客、arXiv、Hacker News、中文源等）→ 产出 `sources.yaml` 初始清单供用户勾选。
2. T8：拿到用户提供的样例 wiki URL 后，实测「通用 wiki 源分析器」可行性（静态/JS 渲染判定、API/RSS/sitemap 探测、子页发现与正文抽取，见 ADR-0005）。
