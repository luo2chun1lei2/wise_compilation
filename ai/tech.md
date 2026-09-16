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
| T4 | LLM API 选型与成本 | ⬜ 未开始 |
| T5 | 调度与部署方式 | ⬜ 未开始 |
| T6 | 微信推送通道 | ⏸ 延后（用户决定，见 ADR-0002） |
| T7 | 飞书群机器人通道 | ✅ 完成（2026-09-16，见下文） |

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

- **状态**：已接受（2026-09-16）
- **背景**：用户架构中引入飞书作为外部分发方向；T7 调查确认自定义机器人满足需求且零审批成本。
- **决策**：飞书通道用群自定义机器人 webhook（`post` 富文本/`interactive` 卡片 + HMAC 签名），不建飞书应用、不申请租户权限。
- **后果**：仅能向机器人所在群推送（满足"发汇总"场景）；单条 ≤20KB，默认走「卡片摘要 + wiki 链接」模式，全文模式按章节分片。

## 下一步调查

1. T2：信息源 RSS/API 可用性清单（厂商博客、arXiv、Hacker News、中文源等）→ 产出 `sources.yaml` 初始清单供用户勾选。
2. T3：GitHub API（releases/activity、限额、是否配 token）。
3. T4：LLM API 选型与 token 成本估算。
4. T5：调度与部署方式（本机 / 服务器 / cron）。
5. T8（新）：外部 wiki 通道——待用户提供目标系统后调查（ADR-0003 分发层插件）。
