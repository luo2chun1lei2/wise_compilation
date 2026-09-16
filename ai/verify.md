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
