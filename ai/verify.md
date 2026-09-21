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

- **补充（2026-09-18 晚）**：新增 5 个国内大模型厂商 GitHub 源（deepseek-ai/zai-org/MoonshotAI/bytedance/Tencent-Hunyuan，`user:<org> pushed:>now-30d`）全部试跑通过（8/4/6/10/7 条）；DeepSeek/智谱/Kimi/腾讯产出干净，bytedance 混有非 AI 仓库（sonic、xgplayer 等）——已列入 task.md 后续计划的有用性评价项。启用源增至 14 个。

## V13 国外首批源接入（2026-09-18）

- **目的**：接入 T2 国外实测通过的"首批 7+1"。
- **结果**：✅ 8 源全部试跑通过（各 10 条）：openai-news / deepmind-blog / techcrunch-ai / latent-space / simon-willison / tldr-ai / interconnects（RSS）+ hackernews-top（新 `type: hn` 适配器，Algolia front_page 按 points 排名=ADR-0020 排名语义）。
- **英文合并翻译**：RSS/HN 条目标题+摘要合并一次 LLM 调用（不增调用量，落实 ADR-0010"标题始终翻译"）；实测 OpenAI 榜中文标题+摘要俱佳；修复"标题：/摘要："前缀回显与（无）占位。
- **启用源达 22 个**；明早邮件目录 22 节。LLM 用量预估：英文源 +80 条/天 ≈ 10~15 万 token/天（包月内）。

## V14 OpenAI Research 源（2026-09-18，用户指定）

- **需求**：收集 openai.com 的 news 中文版与 research 板块（工程实践/技术研究博客），近一周，已收集过的去重。
- **调查**：中文 RSS 不存在（403）；research 无 RSS（404）且**不在 news RSS 中**（实测 0 条 research 链接，此前一直漏采）；research HTML 页面有 JS 反爬（完整浏览器头仍 403）。
- **方案**：新 `type: sitemap` 适配器——官方 `sitemap.xml/research/`（合规，ADR-0005 阶梯③）拿 URL+lastmod，近 7 天过滤（用户指定），slug 首字母大写后 LLM 翻译为标题（无摘要）。research 与 news 共用 `/index/` URL 空间 → url_norm 去重天然跨源生效。
- **结果**：✅ 10 篇近 7 天文章（模型对齐偏差报告框架、GPT 6 Astra、Sora 2 等），标题全部中文；修复仅标题条目的分行格式解析失败（改走简单翻译）与标题清洗。启用源 23 个。

> 运行记录自 2026-09-18 起移至 `result/<日期>/summary.md`（按天归档，每次运行追加一条，要求 #54）。

## V16 Anthropic 源（2026-09-18，用户指定三个入口）

- **调查**：三个入口页均服务端渲染（200，页面直接含文章链接，与 OpenAI 的 403 反爬不同）；无 RSS（T2 已证）但**官方 sitemap 完整**（534 URL，含 187 条 engineering/research，最新到昨日）。
- **方案**：复用 `type: sitemap` 适配器，按 url_include 分两个源——`anthropic-research`（/research/，近 7 天）与 `anthropic-engineering`（/engineering/，**近 45 天**：工程博客约月更，7 天窗口恒为 0；去重保证宽窗不重复）。
- **结果**：✅ research 10 条（Claude 助力生物分子建模、多样本越狱等，标题中文）；engineering 1 条（构建高效智能体，2026-08-10）。启用源 25 个。

## V17 外网代理支持与 Import AI（2026-09-18，用户提供 VPN 机制）

- **机制**：SquirrelVPN（进程 `sqd`，本地代理 `http://127.0.0.1:10077`，启动脚本 `~/bin/cnt_outer.sh`，启动后约 20s 可用）。
- **实现**：`settings.yaml` 新增 proxy 配置；源级 `proxy: true` 开关；采集前 `ensure_vpn()`（pgrep sqd → 未运行则调脚本并等待）；仅 rss/sitemap 请求走代理（LLM/国内源直连）；run_pipeline 开跑前对启用源统一兜底检查。
- **结果**：✅ `importai`（Import AI newsletter，substack 域名，评价最高的研究/政策源）接入成功——10 条，标题中文。启用源 26 个。
- **复测不可达源（via 代理）**：Mistral 无 RSS（404）；Meta AI RSS 400；VentureBeat 仍 429；**x.ai 仍被 Cloudflare 403**（HTML 页 JS 质询，合规通道到头，维持不接入）。

## V18 Google 系源（2026-09-18，用户指定 deepmind.google/research）

- **调查**：用户猜测的 `deepmind.google/research/` 存在（200/212KB）但正文 JS 渲染、无 sitemap（直连间歇 000）；研究亮点会同步进 DeepMind 博客 RSS（已接入）。另发现两大源：**Google Research 博客**（research.google/blog/rss/，100 条、当日更新、研究级内容）与 **blog.google AI 频道**（innovation-and-ai/technology/ai/rss/，20 条）——直连均不可达，走 VPN 代理全通。
- **接入**：`google-research-blog`、`blog-google-ai`（均 proxy: true）；`deepmind-blog` 补 proxy: true（google 域名直连间歇不稳）。
- **结果**：✅ 三源各 10 条；Research 博客摘要列即分类标签（算法与理论/机器智能…）。启用源 28 个。

## V19 全通路复检与新源（2026-09-18，要求 #60）

- **工具**：`tools/full_channel_check.py`（SOP 8 步 × 28 站点，alternate/常见 RSS 路径/sitemap/robots，外网走代理）。
- **发现并接入**：`infoq-cn`（/feed，当日中文 AI 资讯，修正 T15 误判）、`mistral-news`（/news/rss 走代理，修正"无 RSS"误判）——均实测 10 条通过。启用源 30 个。
- **复核无变化**：其余站点维持原判（智谱/DeepSeek sitemap 无新闻价值；机器之心 gzip sitemap 与知乎专栏重复；Meta/VB/Verge sitemap 留档备选）。
- **流程改进确认**：SOP 第 1 步（rel=alternate 自动发现）必须是第一步——两次误判都源于"猜路径"。

## V20 社区/论文源与全流程双收件人测试（2026-09-18）

- **新源（T16）**：`juejin-ai-hot`（掘金热榜 sort_type=3，AI 分类，作者/赞/评论列）与 `arxiv-cs-ai`（cs.AI RSS 当日 10 篇，摘要前缀清洗）——均实测 10 条通过。启用源 32 个。
- **全流程测试（用户加第二个收件人 icloud 后）**：采集 29/30（仅 github-trending 直连超时，后已加 proxy 修复并验证）、发布 29/29、**邮件双收件人 OK**、55 分钟 / 255 次调用 / ~20.3 万 tokens（summary.md 已记录）。
- **Reddit**：需用户注册 OAuth 应用后可接；**思否**：问答流价值低不接。

## V21 用户清单批次 14 源接入（2026-09-18）

- **依据**：用户提供实测清单（国际 17 项 + 国内 10 项），按 ADR-0020 过筛。
- **接入 14 源全部试跑通过**（109 条）：国际 6（MIT TR 9/过滤、IEEE Spectrum AI 10、BAIR 10、MSR 10、GitHub Blog 5/过滤、Alignment Forum 10）+ 国内 8（雷锋网 10、开源中国 10、爱范儿 6/过滤、极客公园 10、钛媒体 6/过滤、IT之家 9/过滤自 60、Solidot 2/过滤、少数派 2/过滤）。
- **排除/暂缓**：SyncedReview（2025-08 停更）；OpenAlex/Crossref（与 arXiv 重叠）；Semantic Scholar（无 key 限流）；Stack Exchange（可接未接，待确认）。
- **新能力**：rss `ai_filter` 标题关键词过滤（零 LLM）+ 空结果占位渲染。启用源 **46 个**；日用量预估升至 ~30 万 tokens、运行 ~75-90 分钟（包月内，留待有用性评价再裁剪）。

## V22 iCloud 拒收处置与邮件瘦身（2026-09-20）

- **现象**：用户手动转发汇总邮件至 icloud 被 Apple 服务器 SMTP 层拒收（`554 5.7.1 [CS01]`，内容策略）——大体积 HTML+海量链接是典型群发特征；另该日 06 时 VPN 抖动致 5 个代理源失败。
- **处置**：
  1. **邮件拆分**：--digest-day 按国内/国际拆两封（FOREIGN_SOURCES 名单），各自带目录+折叠；
  2. **邮件瘦身**：去掉详情"原文简介"行（英文原文是体积大头；中文简介保留，原文点链接看；result/wiki 不变）+ 中文简介截断 320 字；实测 09-20：国内 418→213KB、国际 990→**118KB**（低于 Gmail 102KB 截断线附近）；
  3. **失败源重试**：run_pipeline 新增阶段 1.5——采集失败的源等待 30s 后统一重试一轮（应对 06 时 VPN 抖动）；
  4. 已发小测试信验证通道（待用户确认 icloud 是否收到）。
- **建议用户侧**：在 icloud 把 `chunlei.luo@goldenrivertek.com` 加入通讯录（Apple 对联系人来件显著放宽过滤）。

- **结果确认（2026-09-20 10:00，用户反馈）**：添加联系人后，9:53–9:56 的全部 7 封（含 990KB 的大版本）**均成功送达 icloud**——联系人是决定性修复；拆分+瘦身保留作为纵深防御（兼顾 Gmail 截断线与其他收件人）。日常形态固定为**每天两封（国内/国际）**。

## V23 翻译缓存 + 源级间隔（2026-09-20，ADR-0021）

- **实现**：①翻译缓存——items 表增 title_disp 列（幂等迁移），采集先查库复用译文（lang=cache），仅新条目调 LLM；②源级 interval（18 个源分 3/7 日档，其余默认日更）——run_pipeline 按 sources.last_fetch_at 判到期，未到期跳过（失败不消耗间隔），成功才更新；③邮件自动跟随（未到期源无产物不进邮件）。
- **实测**：
  - bair-blog 单源：10 条全缓存命中，**LLM 0 调用 0 token**（原 10 次/天）；
  - 全流程集成：bair/importai 正确跳过（"间隔 7/3 天未到"），44/44 采集发布成功；
  - **耗时 19 分钟（原 72 分钟，提速 ~4 倍）；LLM 仅 28 次调用 / 1.2 万 tokens（原 ~20 万，降 94%）**——大部分条目当天已被晨间运行翻译过，缓存直接复用。
- **说明**：本次为同日复跑（缓存命中率极端高）；日常形态下日更源每天仍会产生新条目翻译，但中低频源的重复翻译彻底消失。明日 06:30 首个常规运行可观察真实稳态。

## V24 结果页卡片式布局（2026-09-21，ADR-0022）

- **实现**：①`render_md` 改为卡片式条目块（`### N. [标题](链接)（指标）` + 中文简介/原文简介/属性行），去掉宽榜单表格与 `## 详情` 段；②`email_notify.fold_details` 折叠任意 `### N.` 块（标题内链接转 `<a>`，统计表留折叠外），新增 `--dry-run` 渲染到 `data/preview/` 不投递；③`tools/reformat_cards.py` 一次性迁移旧格式（回收旧表格列中的专栏名/语言）。
- **验证**：
  - 合成渲染测试：feed/GitHub/专栏/热榜/zh-skip 五分支输出正确（指标行、属性行、特殊字符清洗）；
  - 迁移：当日 24 个旧格式文件全部转换（arxiv 占位文档跳过），专栏名（量子位/机器之心…）与语言（TypeScript/C++…）成功从旧表格回收；
  - 邮件 dry-run：国内 20 源/国际 6 源，212 个 `<details>`（20 节 + 192 条目级折叠）、目录计数正确、原文简介剥离、中文简介 320 字截断 34 处、无「排名」宽表残留；
  - wiki 重发布：25 个页面全部 OK，线上抽查 qbitai 页——宽表格消失（仅剩文末统计表 1 个 table）、10 个 h3 卡片标题带链接与「发布 时间」指标；
  - 次日 06:30 流水线直接产出新格式（渲染路径单一，无兼容分支）。
- **稳态观察（同日 06:47 常规运行，ADR-0021 首个稳态）**：28 源到期采集 25 成功、18 分钟、21 次调用/1.1 万 tokens——较改造前全量 44 源/72 分钟/20 万 tokens 显著回落，间隔+缓存按预期生效。

## V25 邮件折叠条防误点（2026-09-21，要求 #67，ADR-0022 修订）

- **问题（用户手机实测）**：折叠条标题带链接，点标题展开时易误触链接直接跳转网页。
- **实现**：`fold_details` 中把标题里的 md 链接摘出——折叠条留纯文本标题，展开内容首行注入「- 原文链接：[打开原文](url)」。wiki/md 文件不动（网页标题无展开语义，无冲突）。
- **验证**：dry-run 国内 20 源 192 个折叠条**全部无 `<a>`**、展开首行「原文链接」192 处；随后实发两封（国内 117KB/国际 27KB）供用户手机复验。
- **结果确认（2026-09-21，用户反馈）**：符合要求——卡片式布局（V24）+ 防误点折叠（V25）两轮迭代验收通过，布局工作关闭。
