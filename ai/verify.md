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
- **命令**：`python3 tools/gh_ai_top10.py --source <name>`（四个源各一次，源定义见 `tools/config/sources.yaml`）。
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
