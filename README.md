# 汇集资料和信息

定时采集 AI 情报（GitHub / 知乎等）→ 汇编成榜单文档 → 发布到公司 wiki 并邮件通知同事。全流程配置驱动、工具优先（LLM 仅用于翻译），在本机低负载运行。

## 整体流程

```
┌─ 采集 ──────────────┐   ┌─ 汇编/存档 ────────────┐   ┌─ 发布与通知 ───────────────┐
│ config/sources.yaml │   │ result/YYYY-MM-DD/*.md  │   │ 公司 wiki（MinDoc）         │
│  ├ GitHub（5 源）    │ → │  排名+中文简介+成本统计   │ → │  ai-digest 项目，按日期分组  │
│  └ 知乎专栏（1 源）  │   │ （事实源，入 git）        │   │ 邮件通知（阿里云企业邮箱）    │
└─────────────────────┘   └─────────────────────────┘   └────────────────────────────┘
```

每份成果文档包含：排名表、中文简介、原文简介、以及文末「成本与运行统计」（LLM token 用量/边际费用 ¥0/API 次数/耗时）。

## 快速开始

### 1. 准备凭据（一次性）

```bash
cp ai/secret.example.md ai/secret.md   # 然后编辑填写
```

必填：`WIKI_*`（公司 wiki 账号）、`LLM_*`（GLM 包月 Key）、`EMAIL_*`（发件邮箱，参数可从 Thunderbird 配置提取）。
可选：`GITHUB_TOKEN`（提升 API 限额）、`EMAIL_TO`（同事邮箱，逗号分隔）。

### 2. 采集（按源运行）

```bash
python3 tools/gh_ai_top10.py --source github-trending-monthly   # GitHub 热榜（月增速）
python3 tools/gh_ai_top10.py --source github-codex              # 或其他任一源
python3 tools/gh_ai_top10.py --source zhihu-ai-columns          # 知乎 AI 专栏
```

产出自动落 `result/当天日期/<源名>.md`，并入库 `data/wise.db`（重复运行幂等去重）。

### 3. 发布到 wiki

```bash
python3 tools/mindoc_publish.py --file result/2026-09-16/github-trending-monthly.md \
    --name 'GitHub 热门项目榜（2026-09-16）' --identify digest-20260916-github-trending
```

自动：登录 → 按日期分组建目录 → 建/更新文档（markdown+html 双写）→ 匿名读回校验。
其他子命令：`--selftest`（链路自测）、`--delete <identify>`（删文档）。

### 4. 邮件通知

```bash
python3 tools/email_notify.py --digest-day 2026-09-16    # 当日全文汇总邮件（含目录导航）
python3 tools/email_notify.py --test                     # 通道自测
```

汇总邮件为**全文内嵌**（wiki 是内网地址，公司外直接读邮件即可）：顶部「📋 目录」可点击跳转到各源章节，每节末尾有「↑ 返回目录」。

### 5. 一键全链路 与 定时运行（推荐）

```bash
python3 tools/run_pipeline.py                 # 采集全部启用源 → 发布 wiki → 邮件通知
python3 tools/schedule.py --check             # 检查 crontab/cron 服务可用性
python3 tools/schedule.py --install           # 安装定时（默认每天 08:30）
python3 tools/schedule.py --install --cron '0 9 * * 1'   # 例：每周一 09:00
python3 tools/schedule.py --remove            # 移除定时
```

流水线日志：`data/logs/pipeline-<日期>.log`；cron 运行日志：`data/logs/cron.log`。各源/环节失败相互隔离，汇总行显示成败计数。

## 配置说明（config/）

| 文件 | 作用 | 常用操作 |
|---|---|---|
| `sources.yaml` | 信息源清单 | 加源：新增一项 `name/type/url|query/topic/enabled`；不支持的类型会跳过并告警，走「调查→适配」流程 |
| `channels.yaml` | 分发通道 | 目前启用 `internal-wiki` 与 `email-colleagues`；微信类通道因内部信息保密暂缓（ADR-0017） |
| `topics.yaml` | 专题定义与归类关键词 | 加专题/关键词 |
| `settings.yaml` | 运行参数 | 并发、LLM 限速、翻译字节上限（默认 5000B）、润色开关 |

**当前启用的源（46 个）**：含 `juejin-ai-hot`（掘金 AI 热榜）、`arxiv-cs-ai`；国际 RSS 批（MIT TR/IEEE Spectrum AI/BAIR/MSR/GitHub Blog/Alignment Forum 等）；国内 RSS 批（雷锋网/开源中国/IT之家/爱范儿/极客公园/钛媒体/Solidot/少数派——泛科技源带 `ai_filter` 标题过滤）；github-trending 走代理。其余同前——：国外 15 个（OpenAI News、Mistral、DeepMind/Google Research 博客/blog.google AI/TechCrunch AI/Latent Space/Simon Willison/TLDR AI/Interconnects/Import AI 的 RSS，OpenAI Research 与 Anthropic Research/Engineering 的 sitemap，Hacker News 热点榜；Google/Mistral/substack 走 VPN 代理，源配置 `proxy: true`）；国内新增 InfoQ 中国 RSS；量子位 RSS；厂商 GitHub×6（Qwen/DeepSeek/智谱/Kimi/字节/腾讯混元）；GitHub Trending 与 4 个 topic 榜；知乎专栏（机器之心等）；CSDN 近 3 天。英文源标题+摘要自动合并翻译（一次调用）。

## 目录结构

```
ai/        需求(proposal)、调查与决策(tech/ADR)、设计(design)、验证(verify)、凭据(secret，不入库)
tools/     采集(gh_ai_top10.py)、发布(mindoc_publish.py)、通知(email_notify.py 等)
config/    四份配置（见上）
result/    汇编成果，按日期归档（入 git）；每天一个 summary.md 运行记录（耗时/LLM 用量）
material/  原材料（预留）
data/      SQLite 与运行数据（不入 git）
```

## 已知边界与注意

- `github.com` 网页域名偶发不可达（api.github.com 不受影响）：已内置 3 次退避重试，偶发失败会在下次运行补齐（幂等）。
- 知乎仅支持**专栏订阅**（`zhuanlan.zhihu.com/{slug}` 填入 columns 即可）；话题热点接口需签名，未采用（tech.md T12）。
- 微信通知暂缓：企业微信无组织；WxPusher 因内部信息不得经公众号外发而搁置（ADR-0017，代码保留）。
- wiki 链接为内网地址（`http://gr_wiki.grt.sy/docs/ai-digest`），需公司网络/VPN。
- 翻译走 GLM 包月（限 5000B/条，超限保留原文）；中文源全程零 LLM。

## 更多文档

- 需求与过程记录：`ai/proposal.md`（含「要求列表」）
- 技术调查与全部决策：`ai/tech.md`（ADR-0001~0018）
- 系统设计：`ai/design.md`；验证记录：`ai/verify.md`（V1~V8）
