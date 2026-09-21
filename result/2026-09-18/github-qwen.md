# GitHub 热门项目（github-qwen · 2026-09-18）

- 生成时间：2026-09-18 19:25
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`user:QwenLM pushed:>2026-08-19`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 27,952 | TypeScript | 一个运行在你终端中的开源 AI 编码代理。 |
| 2 | [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) | 2,892 | Python | 让任意 Agent Harness 原生支持多模态。 |
| 3 | [QwenLM/FlashQLA](https://github.com/QwenLM/FlashQLA) | 704 | Python | 基于 TileLang 构建的高性能线性注意力算子库 |
| 4 | [QwenLM/Qwen-Drive-1.0](https://github.com/QwenLM/Qwen-Drive-1.0) | 445 | Python | 迈向自动驾驶视觉-语言基础模型的初步探索 |
| 5 | [QwenLM/Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) | 374 | - | Qwen3.8-Flash-Next 是由阿里巴巴集团 Qwen 团队开发的基础模型。 |
| 6 | [QwenLM/E-CommerceBench](https://github.com/QwenLM/E-CommerceBench) | 95 | Python | 一项长周期基准测试：18 个 LLM 智能体各获得 ¥100,000，基于真实市场数据运营模拟网店 365 天——包括与供应商谈判、定价、管理库存、维持现金流等任务。 |
| 7 | [QwenLM/qwen-code-docs](https://github.com/QwenLM/qwen-code-docs) | 52 | MDX | 一个专门为 Qwen Code 设计的文档翻译工具 |
| 8 | [QwenLM/qwen-mm-plugins-hub](https://github.com/QwenLM/qwen-mm-plugins-hub) | 2 | HTML | # Qwen-MM-Plugins 文档 |

## 详情

### 1. QwenLM/qwen-code（27,952★）

- 链接：https://github.com/QwenLM/qwen-code
- 主题：agentic, ai, ai-agent, ai-coding, cli, coding-agent, developer-tools, llm
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：一个运行在你终端中的开源 AI 编码代理。 **面向终端、编辑器、桌面、浏览器和聊天工具的开源 AI 编码代理。** 中文  | Deutsch  | français  | 日本語  | Русский  | Português (Brasil)  | 한국어 - **开箱即用的代理能力** — Auto-Memory、Auto-Skills、SubAgents、Agent Teams 与 MCP。动态工作流，零配置。 - **彻底开源** — 框架与 Qwen 模型均为开源。二者共同演进，无厂商锁定。 - **多协议支持** — 支持 OpenAI、Anthropic、Gemini 和 Qwen API。兼容任何第三方服务商或本地模型（Ollama / vLLM），可在运行时切换。 - **超越终端** — IDE 插件、桌面应用、Web UI、SDK 以及聊天集成（Telegram / 钉钉 / 微信 / 飞书）。 > [!TIP] > Qwen Code 正在持续自我迭代——使用它自己的代理和模型来提交 issue、提交 PR、审查代码和运行测试。由社区赋能，由 AI 驱动。 **Linux / macOS：** curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash **Windows：** irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex > 安装完成后请重启终端，以确保环境变量生效。 NPM / Homebrew **NPM**（需要 [Node.js 22+](https://nodejs.org/)）： npm install -g @qwen-code/qwen-code@latest **Homebrew**（macOS / Linux）： brew install qwen-code 在你的项目目录下打开终端并启动 Qwen Code： cd /path/to/your-project qwen 在会话中运行 `/auth` 以配置你的服务商和 API 密钥。然后试试：
- 原文简介：An open-source AI coding agent that lives in your terminal. **The open-source AI coding agent for your terminal, editor, desktop, browser, and chat.** 中文  | Deutsch  | français  | 日本語  | Русский  | Português (Brasil)  | 한국어 - **Agentic out of the box** — Auto-Memory, Auto-Skills, SubAgents, Agent Teams, and MCP. Dynamic workflows, zero setup. - **Open-source, inside and out** — The framework and the Qwen models are open-source. They evolve together. No vendor lock-in. - **Multi-protocol** — Supports OpenAI, Anthropic, Gemini, and Qwen APIs. Any third-party provider or local model (Ollama / vLLM). Switch at runtime. - **Beyond the terminal** — IDE plugins, Desktop app, Web UI, SDKs, and chat integrations (Telegram / DingTalk / WeChat / Feishu). > [!TIP] > Qwen Code is actively iterating on itself — using its own agent and models to file issues, submit PRs, review code, and run tests. Powered by the community, driven by AI. **Linux / macOS:** curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash **Windows:** irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex > Restart your terminal after installation to ensure environment variables take effect. NPM / Homebrew **NPM** (requires [Node.js 22+](https://nodejs.org/)): npm install -g @qwen-code/qwen-code@latest **Homebrew** (macOS / Linux): brew install qwen-code Open a terminal in your project and start Qwen Code: cd /path/to/your-project qwen Inside the session, run `/auth` to configure your provider and API key. Then try:

### 2. QwenLM/Qwen-MM-Plugins（2,892★）

- 链接：https://github.com/QwenLM/Qwen-MM-Plugins
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：让任意 Agent Harness 原生支持多模态。  **English** · [中文](README.zh.md)  为 Qwen 模型提供原生多模态插件。让任意 Agent Harness 原生支持多模态。  按能力浏览插件，预览其 Skills 与工具定义，并通过内嵌视频和交互式案例体验 cookbook 示例。Hub 还托管了英文文档。  引导式安装程序支持 Claude Code、CodeBuddy、Codex、Qoder、OpenClaw、Qwen Code 和 Gemini CLI。共享配置位于 `~/.qwen-mm-plugins/config`。  WorkBuddy、QoderWork 和 QwenWork 的应用内设置，以及 DeepSeek Harness、Hermes Agent、opencode、pi 和 QwenPaw 的手动设置，记录在  ``` curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash ```  更新某个 harness 中已安装的能力：  ``` curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash -s -- update ```  已发布的能力使用独立且不可变的标签。关于本地 checkout 安装、回滚、手动 Skill + MCP 设置、依赖项以及 Windows/WSL2，请参阅  每项能力都作为 **Skill** 加上一个可选的 **MCP server** 独立安装，命名为 `qwen-mm-plugins- `。根据你 agent 的主模型进行选择。我们强烈建议多模态模型使用 `core` 插件：它让主模型能够原生读取图片、视频和文件，而不是通过单独的 API 或临时拼凑的 shell 命令来处理。  **通用**：  **Qwen VL 系列模型**（例如 **Qwen3.8-Max**、**Qwen3.7-Plus**）：  **Qwen Omni 系列模型**（例如 **qwen3.8-omni-flash**）：
- 原文简介：Make any agent harness multimodal-native. **English** · [中文](README.zh.md) Native multimodal plugins for Qwen models. Make any agent harness multimodal-native. Browse plugins by capability, preview their Skills and tool definitions, and try the cookbook examples with embedded videos and interactive cases. The Hub also hosts the English documentation. The guided installer supports Claude Code, CodeBuddy, Codex, Qoder, OpenClaw, Qwen Code, and Gemini CLI. Shared configuration lives in `~/.qwen-mm-plugins/config`. In-app setup for WorkBuddy, QoderWork, and QwenWork, plus manual setup for DeepSeek Harness, Hermes Agent, opencode, pi, and QwenPaw, is documented in the curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash Update the capabilities already installed in one harness: curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash -s -- update Released capabilities use independent, immutable tags. For local checkout installs, rollback, manual skill + MCP setup, dependencies, and Windows/WSL2, see the Each capability is installed independently as a **Skill** plus an optional **MCP server**, named `qwen-mm-plugins- `. Pick by your agent's main model. We strongly recommend the `core` plugin for multimodal models: it lets the main model read images, video and files natively, rather than routing them through a separate API or ad-hoc shell commands. **General**: **Qwen VL series model** (e.g. **Qwen3.8-Max**, **Qwen3.7-Plus**): **Qwen Omni series model** (e.g. **qwen3.8-omni-flash**):

### 3. QwenLM/FlashQLA（704★）

- 链接：https://github.com/QwenLM/FlashQLA
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：基于 TileLang 构建的高性能线性注意力算子库  - [2026-07] 🚀 发布 FlashQLA v0.1.2 —— 新增对 SM120（Blackwell，感谢 @minatoyukinaa）的前向计算支持，并正式作为 [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) 中 GDN 的后端，通过标准 FLA API 提供即插即用的加速。 - [2026-06] ⚡ 发布 FlashQLA v0.1.1 —— 新增反向传播的卡内序列并行（intra-card sequence parallelism）以及对 SM100 的支持。同时将 tilelang 升级至 v0.1.9，并使入口函数签名与最新的 `flash-linear-attention` 接口对齐。  FlashQLA 是一个基于 [TileLang](https://github.com/tile-ai/tilelang) 构建的高性能线性注意力算子库。FlashQLA 对 GDN Chunked Prefill 的前向与反向计算进行了**合理的算子融合与性能优化**，在 NVIDIA Hopper 和 Blackwell 的多种场景下，相较 FLA 的 Triton kernel 取得了 **2-3× 前向加速**和 **2× 反向加速**。这些效率提升在预训练场景和边缘侧智能体（agentic）推理中尤为显著。  核心特性： 1. **门控驱动的自动卡内上下文并行（intra-card context parallelism）**。FlashQLA 利用 GDN 门控的指数衰减特性，可在 TP、长序列以及头数较少的配置下自动启用卡内 CP，从而提升 GPU SM 利用率。 2. **面向硬件的代数重构**。我们对 GDN Chunked Prefill 的前向与反向流程进行了一定程度的代数重构，在不牺牲数值精度的前提下，有效降低了 Tensor Core、CUDA Core 和 SFU 的开销。
- 原文简介：high-performance linear attention kernel library built on TileLang - [2026-07] 🚀 Release FlashQLA v0.1.2 — adds forward pass for SM120 (Blackwell, thanks @minatoyukinaa) and now serves as a backend for [flash-linear-attention](https://github.com/fla-org/flash-linear-attention)'s GDN, providing plug-and-play acceleration through the standard FLA API. - [2026-06] ⚡ Release FlashQLA v0.1.1 — adds intra-card sequence parallelism for the backward pass and SM100 support. Also upgrades tilelang to v0.1.9 and aligned entry function signatures to the latest `flash-linear-attention` interface. FlashQLA is a high-performance linear attention kernel library built on [TileLang](https://github.com/tile-ai/tilelang). FlashQLA applies **reasonable operator fusion and performance optimization** to the forward and backward passes of GDN Chunked Prefill, achieving **2-3× forward speedup** and **2× backward speedup** over the FLA Triton kernel across multiple scenarios on NVIDIA Hopper and Blackwell. The efficiency gains are particularly pronounced in pretraining scenarios and edge-side agentic inference. Key features: 1.**Gate-driven automatic intra-card context parallelism**. By exploiting the exponential decay property of the GDN gate, FlashQLA automatically enables intra-card CP under TP, long-sequence, and small-head-count settings, improving GPU SM utilization. 2.**Hardware-friendly algebraic reformulation**. We reformulate the forward and backward flows of GDN Chunked Prefill to a certain extent, effectively reducing Tensor Core, CUDA Core, and SFU overhead without sacrificing numerical precision.

### 4. QwenLM/Qwen-Drive-1.0（445★）

- 链接：https://github.com/QwenLM/Qwen-Drive-1.0
- 主题：
- 最近推送：2026-09-03
- 摘要来源：feed | 翻译：llm
- 中文简介：迈向自动驾驶视觉-语言基础模型的初步探索
- 原文简介：An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving

### 5. QwenLM/Qwen3.8-Flash-Next（374★）

- 链接：https://github.com/QwenLM/Qwen3.8-Flash-Next
- 主题：
- 最近推送：2026-08-27
- 摘要来源：feed | 翻译：llm
- 中文简介：Qwen3.8-Flash-Next 是由阿里巴巴集团 Qwen 团队开发的基础模型。
- 原文简介：Qwen3.8-Flash-Next is the foundation model developed by Qwen Team, Alibaba Group.

### 6. QwenLM/E-CommerceBench（95★）

- 链接：https://github.com/QwenLM/E-CommerceBench
- 主题：
- 最近推送：2026-09-13
- 摘要来源：feed | 翻译：llm
- 中文简介：一项长周期基准测试：18 个 LLM 智能体各获得 ¥100,000，基于真实市场数据运营模拟网店 365 天——包括与供应商谈判、定价、管理库存、维持现金流等任务。
- 原文简介：Long-horizon benchmark where 18 LLM agents got ¥100,000 each and ran simulated online stores for 365 days on real market data: negotiating with suppliers, pricing, managing inventory, keeping cash flow alive.

### 7. QwenLM/qwen-code-docs（52★）

- 链接：https://github.com/QwenLM/qwen-code-docs
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：一个专门为 Qwen Code 设计的文档翻译工具  一个专门为 GitHub 项目设计的文档翻译工具。自动从 GitHub 仓库同步文档，使用 Qwen AI 进行翻译，并构建多语言 Nextra 文档站点。  - 🌍 **多语言支持**：将文档翻译为中文（zh）、德语（de）、法语（fr）、俄语（ru）、日语（ja）、葡萄牙语（pt-BR）、西班牙语（es）和韩语（ko） - 🤖 **Qwen AI 翻译**：由 Qwen API 驱动，实现高质量的技术文档翻译 - 📚 **Nextra 集成**：使用 Nextra 自动生成现代化文档站点 - 🔄 **Git 同步**：自动与源仓库同步，保持翻译内容的最新状态 - ⚡ **CLI 界面**：提供易于使用的命令行界面，覆盖所有操作 - 📝 **智能翻译**：在翻译内容的同时保留代码块、链接和技术术语 - 🚀 **并行处理**：并发翻译多种语言，加快处理速度  ```bash npm install -g @qwen-code/translator ```  1. **初始化新的翻译项目**：  ```bash qwen-translator init ```  2. **配置环境变量**：  ```bash cp .env.example .env ```  3. **同步源仓库文档**：  ```bash qwen-translator sync ```  4. **翻译文档**：  ```bash qwen-translator markdown ```  5. **启动文档站点**：  ```bash npm install npm run dev ```  初始化一个新的翻译项目并进行交互式配置。该命令会设置项目结构、复制 Nextra 模板并创建配置文件。  同步源仓库文档，并自动将发生变更的文件翻译为目标语言。
- 原文简介：A documentation translation tool specifically designed for Qwen Code A documentation translation tool specifically designed for the github project. Automatically sync documentation from GitHub repositories, translate with Qwen AI, and build a multilingual Nextra documentation site. - 🌍 **Multi-language Support**: Translate documentation to Chinese (zh), German (de), French (fr), Russian (ru), Japanese (ja), Portuguese (pt-BR), Spanish (es), and Korean (ko) - 🤖 **Qwen AI Translation**: Powered by Qwen API for high-quality technical document translation - 📚 **Nextra Integration**: Automatically generates a modern documentation site using Nextra - 🔄 **Git Synchronization**: Automatically syncs with source repositories to keep translations up-to-date - ⚡ **CLI Interface**: Easy-to-use command-line interface for all operations - 📝 **Smart Translation**: Preserves code blocks, links, and technical terms while translating content - 🚀 **Parallel Processing**: Translates multiple languages concurrently for faster processing npm install -g @qwen-code/translator 1. **Initialize a new translation project**: qwen-translator init 2. **Configure environment variables**: cp .env.example .env 3. **Sync source repository documents**: qwen-translator sync 4. **Translate documents**: qwen-translator markdown 5. **Start the documentation site**: npm install npm run dev Initialize a new translation project with interactive configuration. Sets up project structure, copies Nextra template, and creates configuration files. Sync source repository documents and automatically translate changed files into the target languages.

### 8. QwenLM/qwen-mm-plugins-hub（2★）

- 链接：https://github.com/QwenLM/qwen-mm-plugins-hub
- 主题：
- 最近推送：2026-09-11
- 摘要来源：readme_head | 翻译：llm
- 中文简介：# Qwen-MM-Plugins 文档  Qwen MM Plugins 的文档、工具参考与 cookbook。  打开 [Hub](https://qwenlm.github.io/qwen-mm-plugins-hub/)，选择一个插件，并按照其 **Install** 标签页操作。其 **Cookbook** 标签页包含工作流和示例。你无需运行本仓库。  1. **在 [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) 中：** 实现插件，编写其 Skill 和工具的 docstring，并按照 [Add a new plugin](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/how-to-add-new-capability/) 的说明进行注册。对现有插件的更新也在同一处进行。  2. **在本仓库中：** 添加或编辑 `content/cookbooks/ /usage.md`。将示例文件放入 `public/cases/ / /assert/`，并在 cookbook 中链接这些文件。将 ` ` 替换为插件的能力 ID，例如 `core`。  Hub 会自动读取插件描述、Skill、工具和英文指南。生成的 `data/*.json` 不会纳入 Git；这些内容仅由源仓库管理。  使用 **Node 24**、Git 和 [uv](https://docs.astral.sh/uv/getting-started/installation/)：  git clone https://github.com/QwenLM/qwen-mm-plugins-hub.git cd qwen-mm-plugins-hub npm ci npm run dev  打开服务器打印出的 URL。开发与生产构建会自动生成内容；首次运行会下载已配置的插件源码以及导出器依赖。运行 `npm run content:sync` 可刷新缓存的源码。参见 [本地验证](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/hub/#validate-locally)，以使用你自己的插件检出或 Python 环境。
- 原文简介：A documentation for Qwen-MM-Plugins Documentation, tool references, and cookbooks for Qwen MM Plugins. Open the [Hub](https://qwenlm.github.io/qwen-mm-plugins-hub/), choose a plugin, and follow its **Install** tab. Its **Cookbook** has workflows and examples. You do not need to run this repository. 1. **In [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins):** implement the plugin, write its Skill and tool docstrings, and register it using [Add a new plugin](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/how-to-add-new-capability/). Update existing plugins in the same place. 2. **In this repository:** add or edit `content/cookbooks/ /usage.md`. Put example files in `public/cases/ / /assert/` and link them from the cookbook. Replace ` ` with the plugin's capability ID, such as `core`. The Hub reads plugin descriptions, Skills, tools, and English guides automatically. Generated `data/*.json` stays out of Git; only the source repository owns that content. Use **Node 24**, Git, and [uv](https://docs.astral.sh/uv/getting-started/installation/): git clone https://github.com/QwenLM/qwen-mm-plugins-hub.git cd qwen-mm-plugins-hub npm ci npm run dev Open the URL printed by the server. Development and production builds generate content automatically; the first run downloads the configured plugin source and exporter dependencies. Run `npm run content:sync` to refresh the cached source. See [local validation](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/hub/#validate-locally) to use your own plugin checkout or Python environment.

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 8 | 计数 |
| 输入 tokens | 2,300 | GLM usage（精确） |
| 输出 tokens | 7,932 | GLM usage（精确） |
| 合计 tokens | 10,232 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 6 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 173 秒 | 计时，统计系统占用时间 |
