# 计划与任务

> 按 AGENTS.md 流程维护：已完成里程碑记录状态，后续计划按优先级排列。

## 已完成里程碑

| 日期 | 里程碑 | 记录 |
|---|---|---|
| 2026-09-16 | 三段式架构设计与技术调查（T1/T3/T4/T5/T7/T9/T10） | tech.md ADR-0001~0015 |
| 2026-09-16 | 首次端到端试跑（GitHub Top10，V1-V3） | verify.md |
| 2026-09-17 | MinDoc 发布链路 + 邮件通知 + 一键流水线 + cron（V6-V10） | verify.md |
| 2026-09-18 | 邮件全文/折叠/反垃圾修复（V11）；RSS 适配器 + 量子位 + Qwen（V12） | verify.md |
| 2026-09-18 | 国内大模型厂商源接入（DeepSeek/智谱/Kimi/字节/腾讯，共 14 源） | sources.yaml |
| 2026-09-18 | 国外首批源接入（7 RSS + Hacker News，共 22 源） | verify.md V13 |
| 2026-09-18 | OpenAI Research 源（sitemap 适配器，共 23 源） | verify.md V14 |
| 2026-09-18 | Anthropic 源×2（sitemap 复用，共 25 源） | verify.md V16 |
| 2026-09-18 | 外网代理支持（SquirrelVPN/ensure_vpn）+ Import AI（共 26 源） | verify.md V17 |
| 2026-09-18 | Google 系源×2（Research 博客 + blog.google AI，走代理，共 28 源） | verify.md V18 |
| 2026-09-18 | 全通路复检 28 站：修正 InfoQ/Mistral 误判并接入（共 30 源）；SOP 固化 | verify.md V19 |

## 后续计划

1. **数据源有用性评价**（2026-09-18 用户要求）：待数据积累后（建议 2~4 周，约 2026-10 上旬）评价各源价值——条目质量、跨源重复率、阅读价值，淘汰/降频低价值源。**重点评价本轮新增的 5 个厂商 GitHub 源**（尤其 github-bytedance 的混源噪声）与 CSDN 搜索源的关键词质量。
2. **T8 通用 wiki 源分析器**：等用户提供样例 wiki URL 后实测（ADR-0005）。
3. **国外源接入**：T2 清单中的 RSS 源（OpenAI/Anthropic/DeepMind/MIT TR/arXiv/HN 等）——rss 适配器已就绪，仅剩逐个验证端点+配置。
4. **周报汇编层**：design.md 中的 topics/digest/trend 模块（跨源按专题汇总的周报，目前是每源一份榜单）。
5. **智谱官网 news 深查**：页面有 2026-08 数据但标题在 JS 后（T2 遗留）。
6. **智源社区「风云榜」深查**：排名语义，数据在接口后（T2 遗留）。
7. **CSDN 源质量调优**：换关键词/点赞门槛/nav 频道模式（T15 注记）。
