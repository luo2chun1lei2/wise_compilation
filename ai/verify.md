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
