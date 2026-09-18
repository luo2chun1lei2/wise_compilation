# 验证

## V1 GitHub AI Top10 端到端试跑（2026-09-16）

- **目的**：验证 T3（GitHub 接口选型）与数据流（获取材料 → 获取摘要 → 翻译判定 → 存库 → 成文，ADR-0011）端到端可行。
- **命令**：`python3 tools/gh_ai_top10.py --query 'topic:artificial-intelligence stars:>500 pushed:>2026-09-09' --per-page 10`
- **结果**：✅ 全部成功。
  - 采集：Search API 命中 10 个项目（AutoGPT 187k★ ~ h4cker 29k★，全部本周活跃）。
  - 摘要级联：`feed`（description）6 条 / `readme_head`（README 文首提取）4 条，无空摘要。
  - 翻译路由：LLM 翻译 9 条；中文项目 minimind 正确 `zh-skip`（零 LLM）。
  - 存库：SQLite `data/wise.db` 新增 10 条（重跑验证过幂等：第二次运行新增 0）。
  - 成文：`result/github-ai-top10-2026-09-16.md`（排名表 + 详情，未发布，符合"先不发送"要求）。
- **LLM 用量**：9 次翻译调用（每次输入 ≤1500B，全部低于 5000B 上限，未触发超限分支）。
- **发现的问题与改进项**：
  1. `readme_head` 提取的摘要偏长，个别混入安装说明噪音（如 LLMs-from-scratch 的 Download ZIP 段）→ 后续加强噪音行过滤与长度收紧。
  2. 摘要含 markdown 链接原样保留，阅读可接受，暂不处理。
  3. 未认证限额（core 60/时）对每日 1 轮足够；多源扩展后建议在 `ai/secret.md` 配 `GITHUB_TOKEN`。
- **结论**：GitHub 源 + 数据流设计可行；`tools/gh_ai_top10.py` 可作为正式 `github` 采集适配器的实现基础。
- **补充（2026-09-16，用户要求）**：结果文档新增**成本统计项**——文档头一行摘要 + 文末「成本与运行统计」表。token 数取自 GLM 响应 `usage` 字段（精确值，误差 0），边际费用按包月订阅记 ¥0（ADR-0008），另统计 GitHub API 次数与总耗时；`runs` 表同步落库（stats JSON）。本轮实测：9 次调用 / 输入 1,674 / 输出 4,436 tokens。

## V2 四 topic 多源试跑（2026-09-16）

- **目的**：验证 sources.yaml 多源配置（用户指定 topic：codex / artificial-intelligence / agent-harness / ai-agents）与 `--source` 按配置运行。
- **命令**：`python3 tools/gh_ai_top10.py --source <name>`（四个源各一次，源定义见 `config/sources.yaml`）。
- **结果**：✅
  - 四源全部跑通，各产出一份排名文档（`result/github-<topic>-2026-09-16.md`）。
  - 查询参数支持 `now-Nd` 相对日期占位符（运行时解析）。
  - **跨源去重生效**：ai-agents 源命中 10 项仅新增 7 条（hermes-agent 等已由 codex 源入库）；artificial-intelligence 源与 V1 试跑重叠，新增 0 条。库内 37 条、重复 URL 组数为 0。
  - 每个 topic 的文档仍展示该 topic 完整 Top10（去重只作用于库与后续汇编，避免同一条目在周报中重复计数）。
- **发现的问题与改进项**：topic 热度差异大（codex 命中 1313 vs agent-harness 268），star 阈值与时间窗已按源分别配置；后续若某 topic 结果变稀，调该源的 query 即可。
- **结论**：多源配置驱动（ADR-0007）在 github 类型上验证可行。

## V3 GitHub Trending 页面解析源（2026-09-16）

- **目的**：验证 `mode: trending`（ADR-0013，用户指定取代自记录基线）：解析 github.com/trending 获取**本期 star 增量**。
- **命令**：`python3 tools/gh_ai_top10.py --source github-trending-monthly`
- **结果**：✅
  - 页面无需登录；21 行全部解析成功（仓库/描述/语言/总star/本期增量，如 archify +50,700★/月）。
  - 产出 `result/2026-09-16/github-trending-monthly.md`，表格带「本期新增」列。
  - 全流程复用数据流管道（摘要级联→翻译→存库→成文）。
- **发现的问题与改进项**：
  1. 首次运行 render 有格式串 bug（列数不匹配），已修复并用合成数据回归测试；
  2. github.com 网页域名出现间歇性不可达（api.github.com 正常）——已加 3 次退避重试；生产运行需容忍偶发跳过；
  3. Trending 无 topic 过滤（全站榜），AI 过滤留待汇编层做。
- **结论**：trending 模式可行，已入 sources.yaml（github-trending-monthly，enabled）。

## V4 知乎热榜源（2026-09-16）

- **目的**：验证 `type: zhihu, mode: hot-list`（ADR-0014）。
- **命令**：`python3 tools/gh_ai_top10.py --source zhihu-hot`
- **结果**：✅
  - 热榜 API 无需登录，30 条全取；AI 关键词过滤后命中 2 条（华为大模型战略、努比亚豆包 AI 手机），产出 `result/2026-09-16/zhihu-hot.md`（话题/热度/回答数/中文简介表）。
  - 中文源全部 `zh-skip`：**零 LLM 调用**；摘要用接口自带 `excerpt`（feed 级）。
  - 修复两处渲染适配：知乎文档标题、详情标题以热度替代 star 数。
- **发现的问题与改进项**：
  1. 全站热榜以时事为主，AI 条目占比低（2/30）——按日采集累积进周报，属预期；
  2. 话题级接口（人工智能等）需登录态，未实现；若需要可后续由用户提供 cookie 扩展。
- **结论**：知乎源可行，已入 sources.yaml（zhihu-hot，enabled）。

## V5 知乎专栏文章源（2026-09-16）

- **目的**：验证 `mode: column`（ADR-0015，用户要求获取 AI 文章/专栏内容而非全站热榜）。
- **命令**：`python3 tools/gh_ai_top10.py --source zhihu-ai-columns`
- **结果**：✅
  - 专栏文章 API 无需登录；配置 jiqizhixin/QbitAI/paperweekly 三个专栏 ×10 篇，活跃专栏贡献 30 篇（paperweekly 2023 后停更、0 篇，自然失效）。
  - 产出 `result/2026-09-16/zhihu-ai-columns.md`：排名/文章/专栏/赞/评论/中文简介，含当日内容（如"GPT-6 Sol要来了？"38 赞等）。
  - `rank_by` 支持按时间或点赞热度排序；中文源零 LLM。
- **发现的问题与改进项**：
  1. 专栏 meta 的 `updated` 字段过期（机器之心显示 2020 实为当日仍在更），判断活跃度以文章列表实际日期为准——已写入 T12 记录；
  2. excerpt 含"[图片]"等占位符噪音，后续可在简介清洗时过滤。
- **结论**：专栏订阅即用户所需"AI 文章流 + 热点（点赞）排序"，已设为主源（zhihu-hot 停用）。

## V6 ai-digest 发布链路（MinDoc 写入，2026-09-16）

- **目的**：跑通 ADR-0001 的完整发布链路：登录 → 建项目（book）→ 建文档 → 写内容 → 读回校验 → 删除。
- **工具**：`tools/mindoc_publish.py`（自测子命令 + 幂等发布子命令）。
- **结果**：✅
  - **发现账号下并无 `ai-digest` 项目**（用户此前以为已建）→ 由工具创建：book_id=2，identify=`ai-digest`，公开，editor=markdown，归属「谦川内部知识库空间」。
  - 自测通过：临时文档 建立identify匹配→覆盖写入→读回校验→删除，2 秒。
  - 发布 2 份真实成果并通过读回校验：`GitHub Trending 月榜（2026-09-16）`（doc_id=274）、`知乎 AI 专栏精选（2026-09-16）`（doc_id=275）；匿名访问 `/docs/ai-digest` 可见目录。
- **踩坑记录（部署版与 master 源码差异，均已处理）**：
  1. 会话探测：部署版 `/setting` 匿名也返回 200；且登录过滤器对 AJAX 请求返回 **HTTP 200 + errcode JSON**（状态码不带 403）→ 探测必须用非 AJAX 的 `/book`（匿名 302）；
  2. create 响应字段是 `doc_id`（非源码里的 `document_id`）；
  3. 文档树实际结构：`<li id="{doc_id}"><a href=".../docs/{book}/{doc_identify}" title="…">`（链接用 identify 而非数字 id）→ 幂等匹配按 identify；
  4. delete 需要表单参数 `identify`（非仅 doc_id）；
  5. 建项目 `POST /book/create` 必须带项目空间 `itemId`（从 `/book/itemsets/search` 获取）。
- **遗留**：~~项目内有一篇默认「空白文档」~~ 已删除（见 V7）。

## V7 发布链路修订（2026-09-16，用户反馈四项）

- **问题与修复**：
  1. **阅读页无内容**：只写 `markdown` 时阅读页（渲染 `content` HTML 字段）为空白；调用 `/book/{key}/release` 返回"已推送任务队列"但**部署站后台队列从不执行**（等待后 content 仍空）→ 修复：**客户端双写**——python-markdown 转 HTML，`markdown + html` 一起提交（MinDoc 网页编辑器即此行为）。修复后匿名阅读页正文可见（omarchy/梁文锋 等关键词命中）。
  2. **空白文档**：为建项目时 MinDoc 自动创建的默认文档（非用户手动）→ 已删除（doc_id=271）。
  3. **命名**：榜单不叫"月榜"，按具体日期命名（`GitHub 热门项目榜（2026-09-16）`）；采集脚本标题同步改为日期式。
  4. **日期分组**：publish 支持 `--day`（默认今天）——自动建日期父节点（identify=`day-YYYYMMDD`），文档挂其下，父节点维护当日索引（链接清单）；新增 `--delete <identify>` 子命令。
- **工具变更**：`mindoc_publish.py` write_content 双写 html；page_visible 匿名正文校验（带重试）；索引追加逻辑去重（标题只保留一个）。
- **验证**：`http://gr_wiki.grt.sy/docs/ai-digest` 目录 = 2026-09-16（索引页，含两链接）+ 两份榜单，正文匿名可见 ✓。

## V8 邮件通知通道（2026-09-17，ADR-0018）

- **目的**：验证公司邮箱 SMTP 通知链路（内部信息允许的通道）。
- **配置来源**：SMTP 参数从本机 Thunderbird `prefs.js` 提取（smtp.mxhichina.com:465 SSL，阿里云企业邮箱）；密码由用户填入 secret.md；SSL 连通性实测（220 AliMail 横幅）。
- **命令与结果**：✅
  - `email_notify.py --test` → 测试邮件送达（1 收件人）；
  - `email_notify.py --digest-day 2026-09-16` → 当日 2 篇文档汇总邮件送达（标题+gr_wiki 链接+当日目录）。
- **修复的两个问题**：
  1. secret 行内中文注释被解析进收件人地址（RCPT 报 Unicode 错）→ load_secret 剥离行内注释；
  2. `--digest-day` 原按 runs.finished_at 过滤（发布动作时间 ≠ 汇总日）→ 改为按文档 identify 前缀 `digest-YYYYMMDD-*` 筛选并按 identify 去重（同名重复发布取最新）；wxpusher_notify.py 同步修复。
- **通道状态**：channels.yaml `email-colleagues` 已启用；收件人暂为用户本人，待收集同事地址后追加。

## V9 CSDN 搜索源（2026-09-17）

- **目的**：验证 `type: csdn, mode: search`（ADR-0019）；同时记录 InfoQ 调查（匿名无接口，T15）。
- **命令**：`python3 tools/gh_ai_top10.py --source csdn-ai-search`
- **结果**：✅ 搜索接口（so.csdn.net/api/v3，无需登录）返回 30 篇近 3 天 AI 文章（tm=2 + 客户端 days 过滤），含标题/链接/日期/摘要/点赞/评论/作者；产出 `result/2026-09-17/csdn-ai-search.md`；中文源零 LLM。
- **发现的问题与改进项**：
  1. CSDN 的 digg/comment 字段是字符串 → render 的千分位格式化崩（已加 `_int` 兜底）；
  2. "AI" 泛关键词结果偏入门科普（多 0 赞）——调优：换关键词/点赞门槛/改用 nav/ai 频道页（T15 注记）。
- **结论**：CSDN 源可行并已启用（sources.yaml）。

## V10 一键流水线与定时任务（2026-09-17）

- **目的**：验证 `tools/run_pipeline.py`（采集→发布→通知全链路）与 `tools/schedule.py`（crontab 管理）。
- **命令**：`python3 tools/run_pipeline.py`；`python3 tools/schedule.py --check/--install`
- **结果**：✅
  - 流水线：采集 7/7 源成功、发布 7/7 文档（wiki 出现 day-20260917 分组 + 7 篇）、邮件通知 OK；总耗时 1243s（github.com 当日网络慢，含 3 次退避重试），日志落 `data/logs/pipeline-2026-09-17.log`。
  - crontab：命令可用、cron 服务运行中；已安装默认定时 **每天 08:30**（托管块标记，`--remove` 可移除；日志 data/logs/cron.log）。
- **结论**：从收集到发送的完整闭环可手工执行也可定时执行；cron 环境使用绝对路径 python，无环境依赖。

## V11 定时调整与全文邮件（2026-09-18）

- **变更**：
  1. cron 定时改为**每天 06:00**（原 08:30；`schedule.py --install --cron '0 6 * * *'`）；
  2. `email_notify.py --digest-day` 重构为**全文邮件**（用户要求 #41：wiki 内网外不可达，邮件直接承载内容）：
     - 顶部「📋 目录」锚点导航（点击跳转到各源章节），每节末尾「↑ 返回目录」；
     - 各源按 sources.yaml 顺序排列，节标题含条数；markdown→HTML，表格内联边框样式；纯文本降级版同步存在；
     - 保留 wiki 当日目录链接（内网用户可点原文）。
- **实测**：发送 2026-09-17 汇总 → 7 个源全文、HTML 130KB、1 收件人，成功。
- **注意**：HTML 130KB 超过 Gmail 网页版的 102KB 截断线（Thunderbird/阿里云企业邮箱无此限制）；收件人若用 Gmail 网页版会看到"消息被截断"。

- **补充（2026-09-18，要求 #42）**：邮件中每个条目的「详情」块改为 `<details><summary>` 折叠（纯 HTML 无 JS）——排名总表保持可见，点击详情标题展开；不支持的客户端自动全展开（降级安全）。实测发送 7 源 138KB；离线校验 30 折叠块/表格保留。阿里云网页版交互效果待用户收信确认。

- **补充（2026-09-18，要求 #43）**：折叠层级上调——每个源整节折叠（如"CSDN AI 文章榜（2026-09-17）"为折叠条，点开才显示表格），条目详情保持二级折叠；邮件打开即纯目录视图。另：邮件缺 Date/Message-ID 头曾致反垃圾拦截（用户未收到），补标准头后恢复（实测两封均达）。

## V12 RSS 适配器与两个新源（2026-09-18）

- **目的**：实现 `type: rss`（feedparser，ADR-0007 类型扩展）；接入 T2 国内实测通过的两个源。
- **结果**：✅
  - `qbitai-rss`（量子位官网 RSS）：10 条当日文章，标题/链接/发布时间/摘要（feed 级，去 HTML 标签），中文零 LLM；产出 `result/2026-09-18/qbitai-rss.md`。
  - `github-qwen`（`user:QwenLM pushed:>now-30d`）：8 个活跃仓库（qwen-code 27.9k★ 等），零新代码（现有 github search 模式）。
  - 新渲染分支：feed 型表格（排名/文章/发布时间/简介）；成本表增加 RSS 抓取计数。
- **结论**：rss 类型就绪——T2 清单中所有"RSS 可用"的源（含未来的国外源）自此均可一条配置接入。
