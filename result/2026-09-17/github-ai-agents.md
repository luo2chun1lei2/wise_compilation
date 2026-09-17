# GitHub 热门项目（github-ai-agents · 2026-09-17）

- 生成时间：2026-09-17 21:14
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`topic:ai-agents stars:>300 pushed:>2026-09-10`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 260,873 | JavaScript | Agent 运行框架性能优化系统。为 Claude Code、Codex、Opencode、Cursor 及更多工具提供 Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）与研究优先的开发方式。 |
| 2 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 246,406 | Python | 与你共同成长的智能体 |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 227,540 | TypeScript | # DeepSeek Harness：一切皆插件 |
| 4 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 181,514 | TypeScript | 用于大规模搜索、抓取和交互的网络数据 API。🔥 |
| 5 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 146,525 | Python | 智能体工程平台。 |
| 6 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 140,989 | JavaScript | 让你的 AI agent 像房间里最懒的资深开发工程师一样思考。最好的代码，就是你从未写过的代码。 |
| 7 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 118,842 | Python | 将任何代码库——连同其文档、SQL schema、配置文件和 PDF——转换为可查询的知识图谱。这是一个适用于 Claude Code、Cursor、Codex 和 Gemini CLI 的 /graphify 技能：本地确定性 AST 解 |
| 8 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 114,913 | Python | 使用浏览器的智能体。 |
| 9 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 107,030 | TypeScript | 一款开源 AI 智能体，将 Gemini 的强大功能直接带入你的终端。 |
| 10 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 94,103 | TypeScript | 为每个智能体（Agent）提供跨会话的持久化上下文 – 捕获您的智能体在会话期间执行的所有操作，利用 AI 进行压缩，并将相关上下文注入到未来的会话中。支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、 |

## 详情

### 1. affaan-m/ECC（260,873★）

- 链接：https://github.com/affaan-m/ECC
- 主题：ai-agents, anthropic, claude, claude-code, developer-tools, llm, mcp, productivity
- 最近推送：2026-09-17
- 摘要来源：feed | 翻译：llm
- 中文简介：Agent 运行框架性能优化系统。为 Claude Code、Codex、Opencode、Cursor 及更多工具提供 Skills（技能）、Instincts（直觉）、Memory（记忆）、Security（安全）与研究优先的开发方式。
- 原文简介：The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.

### 2. NousResearch/hermes-agent（246,406★）

- 链接：https://github.com/NousResearch/hermes-agent
- 主题：ai, ai-agent, ai-agents, anthropic, chatgpt, claude, claude-code, codex
- 最近推送：2026-09-17
- 摘要来源：readme_head | 翻译：llm
- 中文简介：与你共同成长的智能体  Hermes Agent | Hermes Desktop  **由 [Nous Research](https://nousresearch.com) 打造的自我进化型 AI 智能体。** 它是唯一内置学习闭环的智能体——能从经验中创建技能，在使用中不断改进，主动提醒自己持久化知识，检索自己过往的对话，并在一次次会话中构建对你日益加深的认知模型。它可以运行在 5 美元的 VPS、GPU 集群，或闲置时几乎零成本的无服务器基础设施上。它不受限于你的笔记本电脑——当它在云虚拟机上工作时，你可以通过 Telegram 与它对话。  想用什么模型就用什么模型——[Nous Portal](https://portal.nousresearch.com)、OpenRouter、OpenAI、你自己的端点，以及[许多其他选择](https://hermes-agent.nousresearch.com/docs/integrations/providers)。用 `hermes model` 即可切换——无需改代码，没有平台锁定。  真正的终端界面——完整的 TUI，支持多行编辑、斜杠命令自动补全、会话历史记录、中断并重定向，以及流式工具输出。  生活在你的日常场景中——Telegram、Discord、Slack、WhatsApp、Signal 和 CLI，全部由单一网关进程承载。支持语音备忘录转写与跨平台会话延续。  闭环学习——由智能体自行整理的记忆，并定期自我提醒。完成复杂任务后自主创建技能。技能在使用过程中自我改进。基于 FTS5 的会话搜索配合 LLM 摘要，实现跨会话回忆。基于 Honcho 的辩证式用户建模。兼容 agentskills.io 开放标准。  定时自动化——内置 cron 调度器，可向任意平台推送。日报、夜间备份、每周审计——全部用自然语言描述，无人值守自动运行。
- 原文简介：The agent that grows with you Hermes Agent  |  Hermes Desktop **The self-improving AI agent built by [Nous Research](https://nousresearch.com).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM. Use any model you want — [Nous Portal](https://portal.nousresearch.com), OpenRouter, OpenAI, your own endpoint, and [many others](https://hermes-agent.nousresearch.com/docs/integrations/providers). Switch with `hermes model` — no code changes, no lock-in. A real terminal interface   Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output. Lives where you do   Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity. A closed learning loop   Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall.  Honcho  dialectic user modeling. Compatible with the  agentskills.io  open standard. Scheduled automations   Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.

### 3. deepseek-ai/deepseek-harness（227,540★）

- 链接：https://github.com/deepseek-ai/deepseek-harness
- 主题：ai-agents, cordis, dsh, dsh-plugin
- 最近推送：2026-09-15
- 摘要来源：readme_head | 翻译：llm
- 中文简介：# DeepSeek Harness：一切皆插件  英文 | [中文](README.zh.md)  DeepSeek Harness（`dsh`）是由 [DeepSeek AI](https://deepseek.com) 开发的开源 agent harness。它构建于**一切皆插件**的架构之上，由 [Cordis](https://github.com/cordiverse/cordis) 驱动，其设计思想在《_A Programming Paradigm for Spatiotemporal Composability_》一文中有所阐述。  文档：[https://deepseek-harness.github.io/deepseek-harness/](https://deepseek-harness.github.io/deepseek-harness/)  DeepSeek Harness 目前处于_开发者预览_阶段，迭代迅速。**未来会出现破坏兼容性的变更。**  在运行本项目之前，请先阅读[安全须知](SAFETY.md)。  安装 `Node.js`，然后运行：  ```bash npx @deepseek-ai/dsh web ```  该命令默认在 `http://127.0.0.1:3080` 启动 Web UI，并在本地启动时使用默认浏览器打开它。通过 SSH 启动时只会打印主机 URL，因为本地转发的地址由 SSH 客户端或编辑器管理。传入 `--no-open` 可在不打开浏览器的情况下运行服务器。参见 [Web UI 指南](docs/user/guide/index.md)。  若要从仓库检出运行：  ```bash git clone https://github.com/deepseek-ai/deepseek-harness.git cd deepseek-harness pnpm install pnpm run build pnpm dsh web ```  `pnpm run build` 用于准备仓库的构建产物。`pnpm dsh web` 会直接使用这些构建产物，无需重新构建。  - 通过 [GitHub Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions) 提交反馈或错误报告。 - 在你的插件仓库中添加 [`dsh-plugin`](https://github.com/topics/dsh-plugin) 话题，以便于被发现。
- 原文简介：DeepSeek Harness: Everything is a Plugin. English | [中文](README.zh.md) DeepSeek Harness (`dsh`) is an open-source agent harness developed by [DeepSeek AI](https://deepseek.com). It is built on an **everything-is-a-plugin** architecture and powered by [Cordis](https://github.com/cordiverse/cordis), whose design is described in [_A Programming Paradigm for Spatiotemporal Composability_](https://arxiv.org/abs/2608.25512). Documentation: [https://deepseek-harness.github.io/deepseek-harness/](https://deepseek-harness.github.io/deepseek-harness/) DeepSeek Harness is in _developer preview_ and iterating rapidly. **THERE WILL BE COMPATIBILITY-BREAKING CHANGES.** Review the [safety notice](SAFETY.md) before running the project. Install `Node.js`, then run: npx @deepseek-ai/dsh web The command starts the Web UI at `http://127.0.0.1:3080` by default and opens it in the default browser for a local launch. An SSH launch only prints the host URL because the SSH client or editor owns the local forwarded address. Pass `--no-open` to run the server without opening a browser. See [Web UI guide](docs/user/guide/index.md). To run from a repository checkout: git clone https://github.com/deepseek-ai/deepseek-harness.git cd deepseek-harness pnpm install pnpm run build pnpm dsh web `pnpm run build` prepares the repository artifacts. `pnpm dsh web` uses those built artifacts without rebuilding. - Submit feedback or bug reports through [GitHub Discussions](https://github.com/deepseek-ai/deepseek-harness/discussions). - Add the [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic to your plugin repository for discoverability.

### 4. firecrawl/firecrawl（181,514★）

- 链接：https://github.com/firecrawl/firecrawl
- 主题：ai, ai-agents, ai-crawler, ai-scraping, ai-search, crawler, data-extraction, html-to-markdown
- 最近推送：2026-09-17
- 摘要来源：readme_head | 翻译：llm
- 中文简介：用于大规模搜索、抓取和交互的网络数据 API。🔥 src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_logo.png" height="200" > **用于大规模搜索、抓取并与网络交互的 API。🔥** 这款网络数据 API 可帮你查找信息源、提取内容，并将其转换为干净的 Markdown 或结构化数据，供你的智能体直接使用。开源项目，同时提供[托管服务](https://firecrawl.dev/?ref=github)。  _嘘。嘿，就是你，来给我们点星吧 :)_  - **业界领先的可靠性**：覆盖 96% 的网络，包括重度依赖 JS 的页面——无需为代理服务器烦恼，直接获取干净的数据（[查看基准测试](https://www.firecrawl.dev/blog/the-worlds-best-web-data-api-v25)） - **极速响应**：数百万页面的 P95 延迟仅为 3.4 秒，专为实时智能体和动态应用打造 - **LLM 就绪的输出**：干净的 Markdown、结构化 JSON、截图等——消耗更少的 token，构建更好的 AI 应用 - **难题我们搞定**：轮换代理、编排调度、速率限制、JS 拦截内容等——零配置 - **智能体就绪**：一条命令即可将 Firecrawl 连接到任何 AI 智能体或 MCP 客户端 - **媒体解析**：解析并提取网络托管的 PDF、DOCX 等文件中的内容 - **操作（Actions）**：在提取内容之前执行点击、滚动、输入、等待和按键 - **开源**：以透明、协作的方式开发——[加入我们的社区](https://discord.gg/firecrawl)  **核心端点**  **更多**  前往 [firecrawl.dev](https://firecrawl.dev) 注册以获取你的 API 密钥。试试[演练场](https://firecrawl.dev/playground)来体验一下。
- 原文简介：The web data API to search, scrape, and interact at scale. 🔥 src="https://raw.githubusercontent.com/firecrawl/firecrawl/main/img/firecrawl_logo.png" height="200" > **The API to search, scrape, and interact with the web at scale. 🔥** The web data API to find sources, extract content, and turn it into clean Markdown or structured data your agents can ship with. Open source and available as a [hosted service](https://firecrawl.dev/?ref=github). _Pst. Hey, you, join our stargazers :)_ - **Industry-leading reliability**: Covers 96% of the web, including JS-heavy pages — no proxy headaches, just clean data ([see benchmarks](https://www.firecrawl.dev/blog/the-worlds-best-web-data-api-v25)) - **Blazingly fast**: P95 latency of 3.4s across millions of pages, built for real-time agents and dynamic apps - **LLM-ready output**: Clean markdown, structured JSON, screenshots, and more — spend fewer tokens, build better AI apps - **We handle the hard stuff**: Rotating proxies, orchestration, rate limits, JS-blocked content, and more — zero configuration - **Agent ready**: Connect Firecrawl to any AI agent or MCP client with a single command - **Media parsing**: Parse and extract content from web-hosted PDFs, DOCX, and more - **Actions**: Click, scroll, write, wait, and press before extracting content - **Open source**: Developed transparently and collaboratively — [join our community](https://discord.gg/firecrawl) **Core Endpoints** **More** Sign up at [firecrawl.dev](https://firecrawl.dev) to get your API key. Try the [playground](https://firecrawl.dev/playground) to test it out.

### 5. langchain-ai/langchain（146,525★）

- 链接：https://github.com/langchain-ai/langchain
- 主题：agents, ai, ai-agents, anthropic, chatgpt, deepagents, enterprise, framework
- 最近推送：2026-09-17
- 摘要来源：readme_head | 翻译：llm
- 中文简介：智能体工程平台。 智能体工程平台。 LangChain 是一个用于构建智能体和 LLM 应用的框架。它帮助你将可互操作的组件与第三方集成串联起来，简化 AI 应用开发——同时确保你的决策经得起底层技术演进，不会过时。 > [!TIP] > 刚刚开始？不妨了解一下 **[Deep Agents](http://docs.langchain.com/oss/python/deepagents/)** —— 这是一个基于 LangChain 构建的更高级的包，用于构建内置规划、子智能体、文件系统使用等常见使用模式能力的智能体。 uv add langchain from langchain.chat_models import init_chat_model model = init_chat_model("openai:gpt-5.5") result = model.invoke("Hello, world!") 如果你需要更高级的自定义或智能体编排能力，请查看 [LangGraph](https://github.com/langchain-ai/langgraph)，这是我们用于构建可控智能体工作流的框架。 如需等效的 JS/TS 库，请查看 [LangChain.js](https://github.com/langchain-ai/langchainjs)。 > [!TIP] > 有关开发、调试和部署 AI 智能体及 LLM 应用，请参阅 [LangSmith](https://docs.langchain.com/langsmith/home)。 虽然 LangChain 框架可以独立使用，但它也能与任何 LangChain 产品无缝集成，为开发者构建 LLM 应用提供一整套工具。 - **[Deep Agents](http://docs.langchain.com/oss/python/deepagents/)** —— 构建能够进行规划、使用子智能体并利用文件系统处理复杂任务的智能体
- 原文简介：The agent engineering platform. The agent engineering platform. LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves. > [!TIP] > Just getting started? Check out **[Deep Agents](http://docs.langchain.com/oss/python/deepagents/)** — a higher-level package built on LangChain for agents that have built-in capabilities for common usage patterns such as planning, subagents, file system usage, and more. uv add langchain from langchain.chat_models import init_chat_model model = init_chat_model("openai:gpt-5.5") result = model.invoke("Hello, world!") If you're looking for more advanced customization or agent orchestration, check out [LangGraph](https://github.com/langchain-ai/langgraph), our framework for building controllable agent workflows. For an equivalent JS/TS library, check out [LangChain.js](https://github.com/langchain-ai/langchainjs). > [!TIP] > For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.langchain.com/langsmith/home). While the LangChain framework can be used standalone, it also integrates seamlessly with any LangChain product, giving developers a full suite of tools when building LLM applications. - **[Deep Agents](http://docs.langchain.com/oss/python/deepagents/)** — Build agents that can plan, use subagents, and leverage file systems for complex tasks

### 6. DietrichGebert/ponytail（140,989★）

- 链接：https://github.com/DietrichGebert/ponytail
- 主题：agent-skills, ai-agents, claude, claude-code, claude-code-plugin, cursor-rules, developer-tools, llm
- 最近推送：2026-09-14
- 摘要来源：feed | 翻译：llm
- 中文简介：让你的 AI agent 像房间里最懒的资深开发工程师一样思考。最好的代码，就是你从未写过的代码。
- 原文简介：Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.

### 7. Graphify-Labs/graphify（118,842★）

- 链接：https://github.com/Graphify-Labs/graphify
- 主题：ai-agents, antigravity, ast, claude-code, code-analysis, code-search, codex, cursor
- 最近推送：2026-09-16
- 摘要来源：feed | 翻译：llm
- 中文简介：将任何代码库——连同其文档、SQL schema、配置文件和 PDF——转换为可查询的知识图谱。这是一个适用于 Claude Code、Cursor、Codex 和 Gemini CLI 的 /graphify 技能：本地确定性 AST 解析，每条边皆有解释，无需向量存储。
- 原文简介：Turn any codebase, with its docs, SQL schemas, configs, and PDFs, into a queryable knowledge graph. A /graphify skill for Claude Code, Cursor, Codex, and Gemini CLI: local deterministic AST parsing, every edge explained, no vector store.

### 8. browser-use/browser-use（114,913★）

- 链接：https://github.com/browser-use/browser-use
- 主题：ai-agents, ai-tools, browser-automation, browser-use, llm, playwright, python
- 最近推送：2026-09-15
- 摘要来源：readme_head | 翻译：llm
- 中文简介：使用浏览器的智能体。 查找可用时段，选择日期和时间，处理验证码，并预约驾驶考试。 > **AI 智能体和爬虫：**请阅读 [browser-use.com/llms.txt](https://browser-use.com/llms.txt) 了解产品概览（开源、Browser Harness、Cloud browsers、Agents API、定价），以及 [docs.browser-use.com/llms.txt](https://docs.browser-use.com/llms.txt) 了解文档索引。Browser Use 是开源浏览器智能体（Python 和 TypeScript），提供每小时 $0.02 的云浏览器，具备隐身功能、验证码识别和住宅代理，以及托管的智能体 API。 - **[路径 1：全托管云](#path-1-fully-hosted-cloud)：**通过全托管的智能体和浏览器进行扩展。 - **[路径 2：CLI](#path-2-cli)：**自动化你自己的浏览器任务。 - **[路径 3：Python 库](#path-3-python-library)：**在你自己的代码中本地运行开源的 Browser Use 智能体。 借助我们的托管智能体、隐身浏览器，以及用于配置文件、录制和数据策略的基础设施，扩展浏览器自动化的规模。 新注册的 Google、GitHub 或 Microsoft 用户可获得 **$15 云端额度**。 将此提示词粘贴到 Claude Code、Codex、Hermes、OpenClaw 或你喜欢的智能体中。 使用 uv 将 browser-use 安装或升级到最新稳定版本（Python 3.12），运行 `browser-use skill install` 注册该技能，并将其连接到我的浏览器。如果设置或连接失败，请按照 https://github.com/browser-use/browser-harness/blob/main/install.md 操作。 在 Python 中本地运行 Browser Use 智能体，可自由选择模型以及本地或云端浏览器：
- 原文简介：Agents that use the browser. Find an available slot, pick a date and time, handle the CAPTCHA, and book a driving test. > **AI agents and crawlers:** read [browser-use.com/llms.txt](https://browser-use.com/llms.txt) for the product map (open source, Browser Harness, Cloud browsers, Agents API, pricing) and [docs.browser-use.com/llms.txt](https://docs.browser-use.com/llms.txt) for the documentation index. Browser Use is the open-source browser agent (Python and TypeScript), a $0.02 per browser-hour cloud browser with stealth, CAPTCHA solving and residential proxies, and a hosted agent API. - **[Path 1: Fully Hosted Cloud](#path-1-fully-hosted-cloud):** Scale up with a fully hosted agent and browser. - **[Path 2: CLI](#path-2-cli):** Automate your own browser tasks. - **[Path 3: Python Library](#path-3-python-library):** Run the open source Browser Use agent locally from your own code. Scale browser automation with our hosted agent, stealth browsers, and infrastructure for profiles, recordings, and data policies. New Google, GitHub, or Microsoft signups get **$15 cloud credit**. Paste this prompt into Claude Code, Codex, Hermes, OpenClaw, or your favorite agent. Install or upgrade browser-use to the latest stable version with uv using Python 3.12, run `browser-use skill install` to register the skill, and connect it to my browser. If setup or connection fails, follow https://github.com/browser-use/browser-harness/blob/main/install.md. Run the Browser Use agent locally from Python, with your choice of model and a local or cloud browser:

### 9. google-gemini/gemini-cli（107,030★）

- 链接：https://github.com/google-gemini/gemini-cli
- 主题：ai, ai-agents, cli, gemini, gemini-api, mcp-client, mcp-server
- 最近推送：2026-09-17
- 摘要来源：feed | 翻译：llm
- 中文简介：一款开源 AI 智能体，将 Gemini 的强大功能直接带入你的终端。
- 原文简介：An open-source AI agent that brings the power of Gemini directly into your terminal.

### 10. thedotmack/claude-mem（94,103★）

- 链接：https://github.com/thedotmack/claude-mem
- 主题：ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk
- 最近推送：2026-09-17
- 摘要来源：feed | 翻译：llm
- 中文简介：为每个智能体（Agent）提供跨会话的持久化上下文 – 捕获您的智能体在会话期间执行的所有操作，利用 AI 进行压缩，并将相关上下文注入到未来的会话中。支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等更多工具。
- 原文简介：Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 10 | 计数 |
| 输入 tokens | 2,442 | GLM usage（精确） |
| 输出 tokens | 8,047 | GLM usage（精确） |
| 合计 tokens | 10,489 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 6 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 209 秒 | 计时，统计系统占用时间 |
