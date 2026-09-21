# GitHub 热门项目（github-qwen · 2026-09-19）

- 生成时间：2026-09-19 06:38
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`user:QwenLM pushed:>2026-08-20`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 27,966 | TypeScript | 一款常驻终端的开源 AI 编程智能体。 |
| 2 | [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) | 2,906 | Python | 让任意 agent harness 原生支持多模态。 |
| 3 | [QwenLM/FlashQLA](https://github.com/QwenLM/FlashQLA) | 704 | Python | 基于 TileLang 构建的高性能线性注意力算子库 |
| 4 | [QwenLM/Qwen-Drive-1.0](https://github.com/QwenLM/Qwen-Drive-1.0) | 448 | Python | 迈向自动驾驶视觉-语言基础模型的初步探索 |
| 5 | [QwenLM/Qwen3.8-Flash-Next](https://github.com/QwenLM/Qwen3.8-Flash-Next) | 377 | - | Qwen3.8-Flash-Next 是阿里巴巴集团 Qwen 团队开发的基础模型。 |
| 6 | [QwenLM/E-CommerceBench](https://github.com/QwenLM/E-CommerceBench) | 96 | Python | 一项长周期基准测试：18 个 LLM 智能体各获得 10 万元人民币，基于真实市场数据运营模拟网店 365 天——与供应商谈判、定价、管理库存，并维持现金流不断。 |
| 7 | [QwenLM/qwen-code-docs](https://github.com/QwenLM/qwen-code-docs) | 51 | MDX | 专为 Qwen Code 设计的文档翻译工具 |
| 8 | [QwenLM/qwen-mm-plugins-hub](https://github.com/QwenLM/qwen-mm-plugins-hub) | 3 | HTML | # Qwen-MM-Plugins 文档 |
| 9 | [QwenLM/Omnilingua-Bench](https://github.com/QwenLM/Omnilingua-Bench) | 0 | Python | **English** \| [中文](#chinese) |

## 详情

### 1. QwenLM/qwen-code（27,966★）

- 链接：https://github.com/QwenLM/qwen-code
- 主题：agentic, ai, ai-agent, ai-coding, cli, coding-agent, developer-tools, llm
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：一款常驻终端的开源 AI 编程智能体。 **为你的终端、编辑器、桌面、浏览器和聊天打造的开源 AI 编程智能体。** 中文  | Deutsch  | français  | 日本語  | Русский  | Português (Brasil)  | 한국어 - **开箱即用的智能体能力** — Auto-Memory、Auto-Skills、SubAgents、Agent Teams 和 MCP。动态工作流，零配置。 - **彻底开源** — 框架与 Qwen 模型均为开源，共同演进，无供应商锁定。 - **多协议支持** — 支持 OpenAI、Anthropic、Gemini 和 Qwen API，以及任何第三方服务商或本地模型（Ollama / vLLM），可在运行时切换。 - **不止于终端** — 提供 IDE 插件、桌面应用、Web UI、SDK 以及聊天集成（Telegram / 钉钉 / 微信 / 飞书）。 > [!TIP] > Qwen Code 正在持续自我迭代 —— 利用自身的智能体与模型来提交 issue、提交 PR、审查代码和运行测试。社区共建，AI 驱动。 **Linux / macOS：** curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash **Windows：** irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex > 安装完成后请重启终端，以确保环境变量生效。 NPM / Homebrew **NPM**（需要 [Node.js 22+](https://nodejs.org/)）： npm install -g @qwen-code/qwen-code@latest **Homebrew**（macOS / Linux）： brew install qwen-code 在项目目录打开终端并启动 Qwen Code： cd /path/to/your-project qwen 在会话中运行 `/auth` 配置你的服务商和 API 密钥。然后试试：
- 原文简介：An open-source AI coding agent that lives in your terminal. **The open-source AI coding agent for your terminal, editor, desktop, browser, and chat.** 中文  | Deutsch  | français  | 日本語  | Русский  | Português (Brasil)  | 한국어 - **Agentic out of the box** — Auto-Memory, Auto-Skills, SubAgents, Agent Teams, and MCP. Dynamic workflows, zero setup. - **Open-source, inside and out** — The framework and the Qwen models are open-source. They evolve together. No vendor lock-in. - **Multi-protocol** — Supports OpenAI, Anthropic, Gemini, and Qwen APIs. Any third-party provider or local model (Ollama / vLLM). Switch at runtime. - **Beyond the terminal** — IDE plugins, Desktop app, Web UI, SDKs, and chat integrations (Telegram / DingTalk / WeChat / Feishu). > [!TIP] > Qwen Code is actively iterating on itself — using its own agent and models to file issues, submit PRs, review code, and run tests. Powered by the community, driven by AI. **Linux / macOS:** curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash **Windows:** irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex > Restart your terminal after installation to ensure environment variables take effect. NPM / Homebrew **NPM** (requires [Node.js 22+](https://nodejs.org/)): npm install -g @qwen-code/qwen-code@latest **Homebrew** (macOS / Linux): brew install qwen-code Open a terminal in your project and start Qwen Code: cd /path/to/your-project qwen Inside the session, run `/auth` to configure your provider and API key. Then try:

### 2. QwenLM/Qwen-MM-Plugins（2,906★）

- 链接：https://github.com/QwenLM/Qwen-MM-Plugins
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：让任意 agent harness 原生支持多模态。 **English** · [中文](README.zh.md) 为 Qwen 模型打造的原生多模态插件。让任意 agent harness 原生支持多模态。 按能力浏览插件，预览其 Skills 与工具定义，并通过内嵌视频和交互式案例试用 cookbook 示例。该 Hub 还托管英文文档。 引导式安装器支持 Claude Code、CodeBuddy、Codex、Qoder、OpenClaw、Qwen Code 和 Gemini CLI。共享配置位于 `~/.qwen-mm-plugins/config`。 WorkBuddy、QoderWork 和 QwenWork 的应用内设置，以及 DeepSeek Harness、Hermes Agent、opencode、pi 和 QwenPaw 的手动设置，记录在 ``` curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash ``` 更新已安装在某个 harness 中的能力： ``` curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash -s -- update ``` 已发布的能力使用独立且不可变的标签（tag）。关于本地 checkout 安装、回滚、手动 Skill + MCP 设置、依赖项以及 Windows/WSL2，请参阅 每个能力都作为一个 **Skill** 加上一个可选的 **MCP server** 独立安装，命名为 `qwen-mm-plugins- `。请根据你的 agent 主模型进行选择。对于多模态模型，我们强烈推荐使用 `core` 插件：它让主模型能够原生读取图像、视频和文件，而不是将它们经由单独的 API 或临时 shell 命令来处理。 **通用**： **Qwen VL 系列模型**（例如 **Qwen3.8-Max**、**Qwen3.7-Plus**）： **Qwen Omni 系列模型**（例如 **qwen3.8-omni-flash**）：
- 原文简介：Make any agent harness multimodal-native. **English** · [中文](README.zh.md) Native multimodal plugins for Qwen models. Make any agent harness multimodal-native. Browse plugins by capability, preview their Skills and tool definitions, and try the cookbook examples with embedded videos and interactive cases. The Hub also hosts the English documentation. The guided installer supports Claude Code, CodeBuddy, Codex, Qoder, OpenClaw, Qwen Code, and Gemini CLI. Shared configuration lives in `~/.qwen-mm-plugins/config`. In-app setup for WorkBuddy, QoderWork, and QwenWork, plus manual setup for DeepSeek Harness, Hermes Agent, opencode, pi, and QwenPaw, is documented in the curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash Update the capabilities already installed in one harness: curl -fsSL https://raw.githubusercontent.com/QwenLM/Qwen-MM-Plugins/main/install.sh | bash -s -- update Released capabilities use independent, immutable tags. For local checkout installs, rollback, manual skill + MCP setup, dependencies, and Windows/WSL2, see the Each capability is installed independently as a **Skill** plus an optional **MCP server**, named `qwen-mm-plugins- `. Pick by your agent's main model. We strongly recommend the `core` plugin for multimodal models: it lets the main model read images, video and files natively, rather than routing them through a separate API or ad-hoc shell commands. **General**: **Qwen VL series model** (e.g. **Qwen3.8-Max**, **Qwen3.7-Plus**): **Qwen Omni series model** (e.g. **qwen3.8-omni-flash**):

### 3. QwenLM/FlashQLA（704★）

- 链接：https://github.com/QwenLM/FlashQLA
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：基于 TileLang 构建的高性能线性注意力算子库 - [2026-07] 🚀 发布 FlashQLA v0.1.2 — 新增对 SM120（Blackwell）前向计算的支持（感谢 @minatoyukinaa），并可作为 [flash-linear-attention](https://github.com/fla-org/flash-linear-attention) GDN 的后端，通过标准 FLA API 提供即插即用的加速。 - [2026-06] ⚡ 发布 FlashQLA v0.1.1 — 为反向传播新增卡内序列并行支持，并加入对 SM100 的支持。同时将 tilelang 升级至 v0.1.9，并将入口函数签名对齐至最新的 `flash-linear-attention` 接口。  FlashQLA 是一个基于 [TileLang](https://github.com/tile-ai/tilelang) 构建的高性能线性注意力算子库。FlashQLA 对 GDN Chunked Prefill 的前向与反向计算进行了**合理的算子融合与性能优化**，在 NVIDIA Hopper 与 Blackwell 上的多种场景中，相比 FLA Triton kernel 实现了 **2-3 倍的前向加速**和 **2 倍的反向加速**。在预训练场景和边缘侧智能体推理中，效率提升尤为显著。  核心特性： 1. **门控驱动的自动卡内上下文并行**。通过利用 GDN 门控的指数衰减特性，FlashQLA 可在 TP、长序列以及小头数（small-head-count）设置下自动启用卡内 CP（Context Parallelism），从而提升 GPU SM 利用率。 2. **面向硬件的代数重构**。我们对 GDN Chunked Prefill 的前向与反向计算流程进行了一定程度的重构，在不牺牲数值精度的前提下，有效降低了 Tensor Core、CUDA Core 以及 SFU 的开销。
- 原文简介：high-performance linear attention kernel library built on TileLang - [2026-07] 🚀 Release FlashQLA v0.1.2 — adds forward pass for SM120 (Blackwell, thanks @minatoyukinaa) and now serves as a backend for [flash-linear-attention](https://github.com/fla-org/flash-linear-attention)'s GDN, providing plug-and-play acceleration through the standard FLA API. - [2026-06] ⚡ Release FlashQLA v0.1.1 — adds intra-card sequence parallelism for the backward pass and SM100 support. Also upgrades tilelang to v0.1.9 and aligned entry function signatures to the latest `flash-linear-attention` interface. FlashQLA is a high-performance linear attention kernel library built on [TileLang](https://github.com/tile-ai/tilelang). FlashQLA applies **reasonable operator fusion and performance optimization** to the forward and backward passes of GDN Chunked Prefill, achieving **2-3× forward speedup** and **2× backward speedup** over the FLA Triton kernel across multiple scenarios on NVIDIA Hopper and Blackwell. The efficiency gains are particularly pronounced in pretraining scenarios and edge-side agentic inference. Key features: 1.**Gate-driven automatic intra-card context parallelism**. By exploiting the exponential decay property of the GDN gate, FlashQLA automatically enables intra-card CP under TP, long-sequence, and small-head-count settings, improving GPU SM utilization. 2.**Hardware-friendly algebraic reformulation**. We reformulate the forward and backward flows of GDN Chunked Prefill to a certain extent, effectively reducing Tensor Core, CUDA Core, and SFU overhead without sacrificing numerical precision.

### 4. QwenLM/Qwen-Drive-1.0（448★）

- 链接：https://github.com/QwenLM/Qwen-Drive-1.0
- 主题：
- 最近推送：2026-09-03
- 摘要来源：feed | 翻译：llm
- 中文简介：迈向自动驾驶视觉-语言基础模型的初步探索
- 原文简介：An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving

### 5. QwenLM/Qwen3.8-Flash-Next（377★）

- 链接：https://github.com/QwenLM/Qwen3.8-Flash-Next
- 主题：
- 最近推送：2026-08-27
- 摘要来源：feed | 翻译：llm
- 中文简介：Qwen3.8-Flash-Next 是阿里巴巴集团 Qwen 团队开发的基础模型。
- 原文简介：Qwen3.8-Flash-Next is the foundation model developed by Qwen Team, Alibaba Group.

### 6. QwenLM/E-CommerceBench（96★）

- 链接：https://github.com/QwenLM/E-CommerceBench
- 主题：
- 最近推送：2026-09-13
- 摘要来源：feed | 翻译：llm
- 中文简介：一项长周期基准测试：18 个 LLM 智能体各获得 10 万元人民币，基于真实市场数据运营模拟网店 365 天——与供应商谈判、定价、管理库存，并维持现金流不断。
- 原文简介：Long-horizon benchmark where 18 LLM agents got ¥100,000 each and ran simulated online stores for 365 days on real market data: negotiating with suppliers, pricing, managing inventory, keeping cash flow alive.

### 7. QwenLM/qwen-code-docs（51★）

- 链接：https://github.com/QwenLM/qwen-code-docs
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：专为 Qwen Code 设计的文档翻译工具 一款专为 GitHub 项目打造的文档翻译工具。自动从 GitHub 仓库同步文档，使用 Qwen AI 进行翻译，并构建多语言的 Nextra 文档站点。 - 🌍 **多语言支持**：将文档翻译为中文（zh）、德语（de）、法语（fr）、俄语（ru）、日语（ja）、葡萄牙语（pt-BR）、西班牙语（es）和韩语（ko） - 🤖 **Qwen AI 翻译**：由 Qwen API 驱动，提供高质量的技术文档翻译 - 📚 **Nextra 集成**：使用 Nextra 自动生成现代化的文档站点 - 🔄 **Git 同步**：自动与源仓库同步，保持翻译内容的最新状态 - ⚡ **CLI 界面**：提供易于使用的命令行界面，覆盖所有操作 - 📝 **智能翻译**：在翻译内容的同时保留代码块、链接和技术术语 - 🚀 **并行处理**：并发翻译多种语言，加快处理速度 npm install -g @qwen-code/translator 1. **初始化一个新的翻译项目**： qwen-translator init 2. **配置环境变量**： cp .env.example .env 3. **同步源仓库文档**： qwen-translator sync 4. **翻译文档**： qwen-translator markdown 5. **启动文档站点**： npm install npm run dev 通过交互式配置初始化一个新的翻译项目。它会设置项目结构、复制 Nextra 模板并创建配置文件。 同步源仓库文档，并自动将发生变更的文件翻译为目标语言。
- 原文简介：A documentation translation tool specifically designed for Qwen Code A documentation translation tool specifically designed for the github project. Automatically sync documentation from GitHub repositories, translate with Qwen AI, and build a multilingual Nextra documentation site. - 🌍 **Multi-language Support**: Translate documentation to Chinese (zh), German (de), French (fr), Russian (ru), Japanese (ja), Portuguese (pt-BR), Spanish (es), and Korean (ko) - 🤖 **Qwen AI Translation**: Powered by Qwen API for high-quality technical document translation - 📚 **Nextra Integration**: Automatically generates a modern documentation site using Nextra - 🔄 **Git Synchronization**: Automatically syncs with source repositories to keep translations up-to-date - ⚡ **CLI Interface**: Easy-to-use command-line interface for all operations - 📝 **Smart Translation**: Preserves code blocks, links, and technical terms while translating content - 🚀 **Parallel Processing**: Translates multiple languages concurrently for faster processing npm install -g @qwen-code/translator 1. **Initialize a new translation project**: qwen-translator init 2. **Configure environment variables**: cp .env.example .env 3. **Sync source repository documents**: qwen-translator sync 4. **Translate documents**: qwen-translator markdown 5. **Start the documentation site**: npm install npm run dev Initialize a new translation project with interactive configuration. Sets up project structure, copies Nextra template, and creates configuration files. Sync source repository documents and automatically translate changed files into the target languages.

### 8. QwenLM/qwen-mm-plugins-hub（3★）

- 链接：https://github.com/QwenLM/qwen-mm-plugins-hub
- 主题：
- 最近推送：2026-09-11
- 摘要来源：readme_head | 翻译：llm
- 中文简介：# Qwen-MM-Plugins 文档  Qwen MM Plugins 的文档、工具参考和 cookbook。  打开 [Hub](https://qwenlm.github.io/qwen-mm-plugins-hub/)，选择一个插件，并按照其 **Install** 标签页操作。其 **Cookbook** 中包含工作流和示例。你无需运行本仓库。  1. **在 [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins) 中：** 实现插件，编写其 Skill 和工具 docstring，并按照 [Add a new plugin](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/how-to-add-new-capability/) 的说明完成注册。更新现有插件也在同一位置进行。 2. **在本仓库中：** 添加或编辑 `content/cookbooks/<capability>/usage.md`。将示例文件放在 `public/cases/<capability>/<plugin>/assert/` 中，并从 cookbook 中链接它们。将 `<capability>` 替换为插件的能力 ID，例如 `core`。  Hub 会自动读取插件描述、Skill、工具以及英文指南。生成的 `data/*.json` 不会纳入 Git；只有源仓库才拥有这些内容。  请使用 **Node 24**、Git 和 [uv](https://docs.astral.sh/uv/getting-started/installation/)：  ``` git clone https://github.com/QwenLM/qwen-mm-plugins-hub.git cd qwen-mm-plugins-hub npm ci npm run dev ```  打开服务器打印出的 URL。开发构建和生产构建都会自动生成内容；首次运行时会下载所配置的插件源码和 exporter 依赖。运行 `npm run content:sync` 可刷新缓存的源码。参见 [local validation](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/hub/#validate-locally)，以使用你自己的插件检出或 Python 环境。
- 原文简介：A documentation for Qwen-MM-Plugins Documentation, tool references, and cookbooks for Qwen MM Plugins. Open the [Hub](https://qwenlm.github.io/qwen-mm-plugins-hub/), choose a plugin, and follow its **Install** tab. Its **Cookbook** has workflows and examples. You do not need to run this repository. 1. **In [Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins):** implement the plugin, write its Skill and tool docstrings, and register it using [Add a new plugin](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/how-to-add-new-capability/). Update existing plugins in the same place. 2. **In this repository:** add or edit `content/cookbooks/ /usage.md`. Put example files in `public/cases/ / /assert/` and link them from the cookbook. Replace ` ` with the plugin's capability ID, such as `core`. The Hub reads plugin descriptions, Skills, tools, and English guides automatically. Generated `data/*.json` stays out of Git; only the source repository owns that content. Use **Node 24**, Git, and [uv](https://docs.astral.sh/uv/getting-started/installation/): git clone https://github.com/QwenLM/qwen-mm-plugins-hub.git cd qwen-mm-plugins-hub npm ci npm run dev Open the URL printed by the server. Development and production builds generate content automatically; the first run downloads the configured plugin source and exporter dependencies. Run `npm run content:sync` to refresh the cached source. See [local validation](https://qwenlm.github.io/qwen-mm-plugins-hub/docs/hub/#validate-locally) to use your own plugin checkout or Python environment.

### 9. QwenLM/Omnilingua-Bench（0★）

- 链接：https://github.com/QwenLM/Omnilingua-Bench
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：**English** | [中文](#chinese) **多语言、全模态评测，覆盖长音频识别、多说话人理解与指令遵循。** - **长音频能力**：已发布的 Omnilingua-LongASR 中单条音频时长约 **30.56–200.04 分钟**，重点考察长上下文下转写的完整性与稳定性。 - **长音频理解**：Omnilingua-LongQA（MuLA-Bench）考察事实完整性、长程信息整合、推理与时间定位能力。已发布的数据集涵盖 16 种语言，共 **5,029 条 QA 对**，涉及 **1,768 条以上**不同音频，每条 **20.10–180.00 分钟**，总计约 **1,370.95 小时**。 - **多说话人、真实场景**：Omnilingua-MSpeaker 音频轨取自公开社交媒体视频；已发布的数据集包含来自 105 个视频的 **297 条样本**，总计约 26.27 小时（`Omnilingua-MSpeaker/`）。数据通过 `source_url` 提供视频 URL 及起止时间范围，不附带任何媒体文件，需用户自行下载。参考标注保留文本、时间戳及匿名化的说话人 ID。 - **复杂指令组合**：Omnilingua-MaXIFE 完整源清单包含 **11 大类、47 种约束类型**，覆盖格式、长度、关键词、语言切换、风格、语气、引用等；当前发布版本支持 7 种中/高资源语言，范围内约束类型的分布正在重新统计。该基准不仅评估回答内容，还评估指令是否被遵循。
- 原文简介：**English** | [中文](#chinese) **Multilingual, omni-modal evaluation of long-audio recognition, multi-speaker understanding, and instruction following.** - **Long-audio capability**: single clips in the released Omnilingua-LongASR range about **30.56–200.04 minutes**, focusing on transcription completeness and stability in long context. - **Long-audio understanding**: Omnilingua-LongQA (MuLA-Bench) probes factual completeness, long-range information integration, reasoning and temporal grounding. The released dataset has **5,029 QA pairs** across 16 languages, over **1,768 distinct audios**, each **20.10–180.00 minutes**, totaling about **1,370.95 hours**. - **Multi-speaker, real-world scenes**: the Omnilingua-MSpeaker audio track is drawn from public social-media videos; the released dataset has **297 items from 105 videos**, about 26.27 hours in total (`Omnilingua-MSpeaker/`). It provides video URLs and start/end ranges via `source_url`, ships no media files, and users must download them themselves. Reference annotations keep text, timestamps and anonymized speaker IDs. - **Complex instruction composition**: the full Omnilingua-MaXIFE source list contains **11 categories, 47 constraint types** covering format, length, keywords, language switching, style, tone, citation and more; the current release supports 7 mid-/high-resource languages, and the in-scope constraint-type distribution is being re-counted. It evaluates not only the answer content but also whether the instruction is followed.

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 9 | 计数 |
| 输入 tokens | 2,679 | GLM usage（精确） |
| 输出 tokens | 8,775 | GLM usage（精确） |
| 合计 tokens | 11,454 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 7 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 177 秒 | 计时，统计系统占用时间 |
