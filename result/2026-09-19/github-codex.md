# GitHub 热门项目（github-codex · 2026-09-19）

- 生成时间：2026-09-19 07:00
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`topic:codex stars:>50 pushed:>2026-08-20`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 246,894 | Python | 与你共同成长的智能体 |
| 2 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 133,567 | Rust | 一款跨平台桌面端一站式助手，支持 Claude Code、Codex、OpenCode、OpenClaw、Grok Build 与 Hermes Agent。唯一官方网站：ccswitch.io |
| 3 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 128,819 | Python | 一款 AI 技能，为跨多个平台构建专业 UI/UX 提供设计智能。 |
| 4 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 119,376 | Python | 将任何代码库——连同其文档、SQL schema、配置文件和 PDF——转换为可查询的知识图谱。一个适用于 Claude Code、Cursor、Codex 和 Gemini CLI 的 /graphify 技能：本地确定性 AST 解析， |
| 5 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 96,374 | JavaScript | 面向 AI 编程智能体的生产级工程 Skills。 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 88,242 | JavaScript | Taste-Skill —— 赋予你的 AI 良好品味。防止 AI 生成无聊、千篇一律的垃圾内容。 |
| 7 | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | 83,245 | TypeScript | 传授知识的图谱 > 令人惊艳的图谱。将任何代码转化为可探索、可搜索、可提问的交互式知识图谱。支持 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等多种工具。 |
| 8 | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 75,292 | Python | 一份精选的 Awesome Claude Skills、资源与工具列表，用于自定义 Claude AI 工作流 |
| 9 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 72,799 | TypeScript | 🌊 最早的 agent harness。部署智能多玩家蜂群（swarms），协调自主工作流，构建对话式 AI 系统。特性包括自适应记忆、自学习智能、联邦（federation）、向量 RAG 集成，并原生集成 Claude Code / C |
| 10 | [stablyai/orca](https://github.com/stablyai/orca) | 71,903 | TypeScript | Orca 是用于操控并行 agent 舰队的 ADE。使用你自己的订阅即可运行任何 coding agent。支持桌面端、移动端和远程 runtime。 |

## 详情

### 1. NousResearch/hermes-agent（246,894★）

- 链接：https://github.com/NousResearch/hermes-agent
- 主题：ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：与你共同成长的智能体  Hermes Agent  |  Hermes Desktop  **由 [Nous Research](https://nousresearch.com) 打造的自我改进 AI 智能体。**它是唯一内置学习闭环的智能体——从经验中创建技能、在使用过程中持续改进技能、主动提醒自己持久化知识、搜索自己过往的对话记录，并在一次次会话中不断加深对你的认知模型。它可以运行在 5 美元的 VPS、GPU 集群，或闲置时几乎零成本的无服务器基础设施上。它不受限于你的笔记本电脑——当它在云虚拟机上工作时，你可以通过 Telegram 与它对话。  随心使用任何模型——[Nous Portal](https://portal.nousresearch.com)、OpenRouter、OpenAI、你自己的端点，以及[其他众多选择](https://hermes-agent.nousresearch.com/docs/integrations/providers)。一条 `hermes model` 命令即可切换——无需改动代码，也不会被锁定。  真正的终端界面   完整的 TUI，支持多行编辑、斜杠命令自动补全、对话历史、中断并重定向，以及流式工具输出。  生活在你的场景中   Telegram、Discord、Slack、WhatsApp、Signal 以及 CLI——全部由单一网关进程承载。支持语音备忘录转录与跨平台对话连续性。  闭环学习系统   由智能体自主管理并定期强化的记忆。完成复杂任务后自动创建技能，技能在使用中自我改进。基于 FTS5 的会话搜索，配合 LLM 摘要实现跨会话召回。Honcho 辩证式用户建模。兼容 agentskills.io 开放标准。  定时自动化任务   内置 cron 调度器，可将结果推送到任意平台。每日报告、夜间备份、每周审计——全部用自然语言描述，无人值守自动运行。
- 原文简介：The agent that grows with you Hermes Agent  |  Hermes Desktop **The self-improving AI agent built by [Nous Research](https://nousresearch.com).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM. Use any model you want — [Nous Portal](https://portal.nousresearch.com), OpenRouter, OpenAI, your own endpoint, and [many others](https://hermes-agent.nousresearch.com/docs/integrations/providers). Switch with `hermes model` — no code changes, no lock-in. A real terminal interface   Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output. Lives where you do   Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity. A closed learning loop   Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall.  Honcho  dialectic user modeling. Compatible with the  agentskills.io  open standard. Scheduled automations   Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.

### 2. farion1231/cc-switch（133,567★）

- 链接：https://github.com/farion1231/cc-switch
- 主题：ai-tools, claude-code, codex, desktop-app, grok, grokbuild, hermes, hermes-agent
- 最近推送：2026-09-17
- 摘要来源：feed | 翻译：llm
- 中文简介：一款跨平台桌面端一站式助手，支持 Claude Code、Codex、OpenCode、OpenClaw、Grok Build 与 Hermes Agent。唯一官方网站：ccswitch.io
- 原文简介：A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io

### 3. nextlevelbuilder/ui-ux-pro-max-skill（128,819★）

- 链接：https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- 主题：ai-skills, antigravity, claude, claude-code, codex, command-line, copilot, cursor-ai
- 最近推送：2026-09-15
- 摘要来源：feed | 翻译：llm
- 中文简介：一款 AI 技能，为跨多个平台构建专业 UI/UX 提供设计智能。
- 原文简介：An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.

### 4. Graphify-Labs/graphify（119,376★）

- 链接：https://github.com/Graphify-Labs/graphify
- 主题：ai-agents, antigravity, ast, claude-code, code-analysis, code-search, codex, cursor
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：将任何代码库——连同其文档、SQL schema、配置文件和 PDF——转换为可查询的知识图谱。一个适用于 Claude Code、Cursor、Codex 和 Gemini CLI 的 /graphify 技能：本地确定性 AST 解析，每条边皆有解释，无需向量存储。
- 原文简介：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.

### 5. addyosmani/agent-skills（96,374★）

- 链接：https://github.com/addyosmani/agent-skills
- 主题：agent-skills, antigravity, claude-code, codex, cursor, skills
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：面向 AI 编程智能体的生产级工程 Skills。 **面向 AI 编程智能体的生产级工程 Skills。** Skills 将资深工程师在构建软件时所采用的工作流、质量关卡与最佳实践固化下来。这套 Skills 经过打包，可让 AI 智能体在开发的每个阶段都始终如一地遵循它们。  ```   定义          规划          构建          验证          评审          发布 ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐ │ 想法 │ ───▶ │ 规格 │ ───▶ │ 编码 │ ───▶ │ 测试 │ ───▶ │  QA  │ ───▶ │ 放行 │ │ 细化 │      │  PRD │      │ 实现 │      │ 调试 │      │ 关卡 │      │ 上线 │ └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘ /spec          /plan          /build        /test         /review       /ship ```  9 个对应开发生命周期的斜杠命令。每个命令都会自动激活相应的 Skills。  希望规格确定之后能少一些手动步骤？**`/build auto`** 会在一次获批的流程中生成计划并实现每一项任务——你只需批准计划一次，之后它便自主运行。它省去的是任务*之间*的人工介入，而非验证环节：每项任务依然采用测试驱动方式开发并逐项提交，遇到失败或有风险的步骤时会自动暂停。  Skills 还会根据你当前在做的事情自动激活——设计 API 会触发 `api-and-interface-design`，构建 UI 会触发 `frontend-ui-engineering`，诸如此类。
- 原文简介：Production-grade engineering skills for AI coding agents. **Production-grade engineering skills for AI coding agents.** Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. These ones are packaged so AI agents follow them consistently across every phase of development. DEFINE          PLAN           BUILD          VERIFY         REVIEW          SHIP ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐ │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │  QA  │ ───▶ │  Go  │ │Refine│      │  PRD │      │ Impl │      │Debug │      │ Gate │      │ Live │ └──────┘      └──────┘      └──────┘      └──────┘      └──────┘      └──────┘ /spec          /plan          /build        /test         /review       /ship 9 slash commands that map to the development lifecycle. Each one activates the right skills automatically. Want fewer manual steps once the spec exists? **`/build auto`** generates the plan and implements every task in a single approved pass — you approve the plan once, then it runs autonomously. It removes the human stepping *between* tasks, not the verification: every task is still test-driven and committed individually, and it pauses on failures or risky steps. Skills also activate automatically based on what you're doing — designing an API triggers `api-and-interface-design`, building UI triggers `frontend-ui-engineering`, and so on.

### 6. Leonxlnx/taste-skill（88,242★）

- 链接：https://github.com/Leonxlnx/taste-skill
- 主题：agent, ai, claude, claude-code, codex, coding, design, frontend
- 最近推送：2026-09-16
- 摘要来源：feed | 翻译：llm
- 中文简介：Taste-Skill —— 赋予你的 AI 良好品味。防止 AI 生成无聊、千篇一律的垃圾内容。
- 原文简介：Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop

### 7. Egonex-AI/Understand-Anything（83,245★）

- 链接：https://github.com/Egonex-AI/Understand-Anything
- 主题：antigravity-skills, business-knowledge, claude-code, claude-skills, codebase-analysis, codex, codex-skills, developer-tools-ai-agent
- 最近推送：2026-09-12
- 摘要来源：feed | 翻译：llm
- 中文简介：传授知识的图谱 > 令人惊艳的图谱。将任何代码转化为可探索、可搜索、可提问的交互式知识图谱。支持 Claude Code、Codex、Cursor、Copilot、Gemini CLI 等多种工具。
- 原文简介：Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.

### 8. ComposioHQ/awesome-claude-skills（75,292★）

- 链接：https://github.com/ComposioHQ/awesome-claude-skills
- 主题：agent-skills, ai-agents, antigravity, automation, claude, claude-code, codex, composio
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：一份精选的 Awesome Claude Skills、资源与工具列表，用于自定义 Claude AI 工作流
- 原文简介：A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows

### 9. ruvnet/ruflo（72,799★）

- 链接：https://github.com/ruvnet/ruflo
- 主题：agentic-ai, agentic-framework, agentic-workflow, agents, ai-agents, ai-assistant, ai-skills, autonomous-agents
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：🌊 最早的 agent harness。部署智能多玩家蜂群（swarms），协调自主工作流，构建对话式 AI 系统。特性包括自适应记忆、自学习智能、联邦（federation）、向量 RAG 集成，并原生集成 Claude Code / Codex / Hermes 等众多工具。
- 原文简介：🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federation, vector RAG integration, and native Claude Code / Codex / Hermes and many more Integrated

### 10. stablyai/orca（71,903★）

- 链接：https://github.com/stablyai/orca
- 主题：ade, agent-ide, ai-agents, claude-code, cli, codex, cursor-agent, devtools
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：Orca 是用于操控并行 agent 舰队的 ADE。使用你自己的订阅即可运行任何 coding agent。支持桌面端、移动端和远程 runtime。
- 原文简介：Orca is the ADE for working with a fleet of parallel agents. Run any coding agent with your own subscription. Available on desktop, mobile and remote runtime.

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 10 | 计数 |
| 输入 tokens | 1,400 | GLM usage（精确） |
| 输出 tokens | 8,636 | GLM usage（精确） |
| 合计 tokens | 10,036 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 3 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 204 秒 | 计时，统计系统占用时间 |
