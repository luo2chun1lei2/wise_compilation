# GitHub 热门项目（github-artificial-intelligence · 2026-09-19）

- 生成时间：2026-09-19 07:02
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`topic:artificial-intelligence stars:>500 pushed:>2026-09-12`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 187,438 | Python | AutoGPT 的愿景是让人人都能使用并在此基础上构建触手可及的 AI。我们的使命是提供所需的工具，让您专注于真正重要的事情。 |
| 2 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 105,199 | Jupyter Notebook | 从零开始，一步步用 PyTorch 实现类 ChatGPT 的大语言模型（LLM） |
| 3 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | 96,716 | Python | 实时换脸与一键视频深度伪造，仅需一张图像 |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 94,208 | TypeScript | 为每个智能体（Agent）提供跨会话的持久上下文 – 捕获智能体在会话期间执行的所有操作，通过 AI 进行压缩，并将相关上下文注入到未来的会话中。支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Cop |
| 5 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 88,442 | TypeScript | 🙌 OpenHands：AI 驱动的开发 |
| 6 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 68,696 | Jupyter Notebook | # 12 周，24 节课，AI 属于所有人！ |
| 7 | [usestrix/strix](https://github.com/usestrix/strix) | 63,547 | Python | 开源 AI 渗透测试工具，帮助您发现并修复应用程序中的漏洞。 |
| 8 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 61,599 | Python | 🧠 Train a 64M-parameter LLM from scratch in just 2h! |
| 9 | [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | 31,349 | Python | 预训练、微调任意规模的任意 AI 模型，可在 1 块或 10,000+ 块 GPU 上运行，且无需改动任何代码。 |
| 10 | [simstudioai/sim](https://github.com/simstudioai/sim) | 29,664 | TypeScript | Sim 是一个协作工作区，用于构建、部署和监控 AI 智能体与工作流。已有超过 100,000 名开发者在使用。 |

## 详情

### 1. Significant-Gravitas/AutoGPT（187,438★）

- 链接：https://github.com/Significant-Gravitas/AutoGPT
- 主题：agentic-ai, agents, ai, artificial-intelligence, autonomous-agents, claude, gpt, llama-api
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：AutoGPT 的愿景是让人人都能使用并在此基础上构建触手可及的 AI。我们的使命是提供所需的工具，让您专注于真正重要的事情。
- 原文简介：AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.

### 2. rasbt/LLMs-from-scratch（105,199★）

- 链接：https://github.com/rasbt/LLMs-from-scratch
- 主题：ai, artificial-intelligence, attention-mechanism, deep-learning, finetuning, from-scratch, generative-ai, gpt
- 最近推送：2026-09-17
- 摘要来源：readme_head | 翻译：llm
- 中文简介：从零开始，一步步用 PyTorch 实现类 ChatGPT 的大语言模型（LLM）  本仓库包含开发、预训练和微调类 GPT 大语言模型的代码，是《[Build a Large Language Model (From Scratch)](https://amzn.to/4fqvn0D)》一书的官方代码仓库。  在 [*Build a Large Language Model (From Scratch)*](http://mng.bz/orYv) 一书中，你将通过从零开始、一步一步地编写代码，由内而外地学习并理解大语言模型（LLM）的工作原理。在本书中，我将引导你创建属于自己的 LLM，并以清晰的文字、图表和示例讲解每一个阶段。  本书所介绍的训练和开发小型但功能完整的模型（用于教学目的）的方法，与创建大规模基础模型（如 ChatGPT 背后的模型）所采用的方法是一致的。此外，本书还包含加载更大规模预训练模型权重以进行微调的代码。  - 官方[源代码仓库](https://github.com/rasbt/LLMs-from-scratch)链接 - [Manning（出版社网站）上的图书链接](http://mng.bz/orYv) - [Amazon.com 上的图书页面链接](https://www.amazon.com/gp/product/1633437167) - ISBN 9781633437166  要下载本仓库的副本，请点击 [Download ZIP](https://github.com/rasbt/LLMs-from-scratch/archive/refs/heads/main.zip) 按钮，或在终端中执行以下命令：  git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git  （如果你是从 Manning 网站下载的代码包，建议访问 GitHub 上的官方代码仓库 [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) 以获取最新更新。）
- 原文简介：Implement a ChatGPT-like LLM in PyTorch from scratch, step by step This repository contains the code for developing, pretraining, and finetuning a GPT-like LLM and is the official code repository for the book [Build a Large Language Model (From Scratch)](https://amzn.to/4fqvn0D). In [*Build a Large Language Model (From Scratch)*](http://mng.bz/orYv), you'll learn and understand how large language models (LLMs) work from the inside out by coding them from the ground up, step by step. In this book, I'll guide you through creating your own LLM, explaining each stage with clear text, diagrams, and examples. The method described in this book for training and developing your own small-but-functional model for educational purposes mirrors the approach used in creating large-scale foundational models such as those behind ChatGPT. In addition, this book includes code for loading the weights of larger pretrained models for finetuning. - Link to the official [source code repository](https://github.com/rasbt/LLMs-from-scratch) - [Link to the book at Manning (the publisher's website)](http://mng.bz/orYv) - [Link to the book page on Amazon.com](https://www.amazon.com/gp/product/1633437167) - ISBN 9781633437166 To download a copy of this repository, click on the [Download ZIP](https://github.com/rasbt/LLMs-from-scratch/archive/refs/heads/main.zip) button or execute the following command in your terminal: git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git (If you downloaded the code bundle from the Manning website, please consider visiting the official code repository on GitHub at [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) for the latest updates.)

### 3. hacksider/Deep-Live-Cam（96,716★）

- 链接：https://github.com/hacksider/Deep-Live-Cam
- 主题：ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam
- 最近推送：2026-09-15
- 摘要来源：readme_head | 翻译：llm
- 中文简介：实时换脸与一键视频深度伪造，仅需一张图像  Deep-Live-Cam 2.1.6  一键实现实时换脸与视频深度伪造，仅需一张图像。  这款深度伪造软件旨在成为 AI 生成媒体行业的生产力工具。它可以帮助艺术家为自定义角色制作动画、创作引人入胜的内容，甚至使用模型进行服装设计。  我们深知该软件可能被用于不道德用途，并已采取预防措施。内置检查机制可防止程序处理不当媒体内容（如裸露、血腥内容、战争影像等敏感素材）。我们将在遵守法律与道德的前提下，继续负责任地开发此项目。如有法律要求，我们可能会关闭项目或为输出内容添加水印。  - 道德使用：用户应以负责任且合法的方式使用本软件。如使用真人的面部，须征得本人同意，并在网上分享时明确标注输出内容为深度伪造。 - 内容限制：软件内置检查机制，防止处理不当媒体内容，例如裸露、血腥内容或敏感素材。 - 法律合规：我们遵守所有相关法律与道德准则。如有法律要求，我们可能会关闭项目或为输出内容添加水印。 - 用户责任：我们对最终用户的行为不承担责任。用户必须确保其对本软件的使用符合道德标准与法律要求。  使用本软件即表示您同意以上条款，并承诺以尊重他人权利与尊严的方式使用它。
- 原文简介：real time face swap and one-click video deepfake with only a single image Deep-Live-Cam 2.1.6 Real-time face swap and video deepfake with a single click and only a single image. This deepfake software is designed to be a productive tool for the AI-generated media industry. It can assist artists in animating custom characters, creating engaging content, and even using models for clothing design. We are aware of the potential for unethical applications and are committed to preventative measures. A built-in check prevents the program from processing inappropriate media (nudity, graphic content, sensitive material like war footage, etc.). We will continue to develop this project responsibly, adhering to the law and ethics. We may shut down the project or add watermarks if legally required. - Ethical Use: Users are expected to use this software responsibly and legally. If using a real person's face, obtain their consent and clearly label any output as a deepfake when sharing online. - Content Restrictions: The software includes built-in checks to prevent processing inappropriate media, such as nudity, graphic content, or sensitive material. - Legal Compliance: We adhere to all relevant laws and ethical guidelines. If legally required, we may shut down the project or add watermarks to the output. - User Responsibility: We are not responsible for end-user actions. Users must ensure their use of the software aligns with ethical standards and legal requirements. By using this software, you agree to these terms and commit to using it in a manner that respects the rights and dignity of others.

### 4. thedotmack/claude-mem（94,208★）

- 链接：https://github.com/thedotmack/claude-mem
- 主题：ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：为每个智能体（Agent）提供跨会话的持久上下文 – 捕获智能体在会话期间执行的所有操作，通过 AI 进行压缩，并将相关上下文注入到未来的会话中。支持 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等更多工具
- 原文简介：Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

### 5. OpenHands/OpenHands（88,442★）

- 链接：https://github.com/OpenHands/OpenHands
- 主题：agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：🙌 OpenHands：AI 驱动的开发 Agent Canvas 面向编码智能体与自动化的自托管开发者控制中心。 在本地、远程和云端后端上运行 OpenHands、Claude Code、Codex、Gemini 或任何兼容 ACP 的智能体。  快速入门  | 文档  | 自托管  | ACP 智能体  | 自动化  | Slack  OpenHands Agent Canvas 将你的编码智能体变成一支自托管的、全天候在线的工程团队。它是一个开发者控制中心，可用于发起对话并自动化日常工作任务——例如生成报告并发布到 Slack，或自动将 GitHub issue 分解为任务。  它默认在本地机器上运行，但可以连接到多个“智能体后端”，例如在 Docker 容器、虚拟机或公司内部基础设施中运行智能体。你也可以选择在 OpenHands Cloud 或 OpenHands Enterprise 基础设施上运行智能体。  Agent Canvas 开箱即用即可运行开源的 OpenHands 智能体，但也可以使用任何第三方智能体，例如 Claude Code 和 Codex。  如果你有任何问题或反馈，请提交 GitHub issue，或加入 Slack 中的 [#proj-agent-canvas 频道](https://openhands.dev/joinslack)。  你可以安装 OpenHands，在任何机器上运行智能体：笔记本电脑、Mac Mini 等专用计算机，或云端服务器。  运行 OpenHands 最强大的方式是在云端服务器上运行。这样，即使笔记本电脑合上了，智能体仍能继续运行，同时也更便于通过 Slack、GitHub 和 Datadog 等第三方服务触发你的智能体。详情请参阅 [SELF_HOSTING.md](docs/SELF_HOSTING.md)，尤其是在安全加固方面。
- 原文简介：🙌 OpenHands: AI-Driven Development Agent Canvas The self-hosted developer control center for coding agents and automations. Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. Quickstart  | Docs  | Self-Hosting  | ACP Agents  | Automations  | Slack OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — like generating reports that publish to Slack or automatically decomposing GitHub issues into tasks. It runs locally on your machine by default, but can connect to multiple “agent backends”, e.g. running agents in Docker containers, on VMs, or within your company infrastructure. You can optionally choose to run agents on OpenHands Cloud or OpenHands Enterprise infrastructure. Agent Canvas runs the open source OpenHands agent out-of-the-box, but can use any third-party agent like Claude Code and Codex. If you have questions or feedback, please open a GitHub issue or join the [#proj-agent-canvas channel in Slack](https://openhands.dev/joinslack). You can install OpenHands to run agents on any machine: on your laptop, on a dedicated computer like a Mac Mini, or on a server in the cloud. The most powerful way to run OpenHands is on a server in the cloud. This allows your agents to continue running even when your laptop is shut, and makes it easier to trigger your agents through third-party services like Slack, GitHub, and Datadog. See [SELF_HOSTING.md](docs/SELF_HOSTING.md) for details, especially with respect to security hardening.

### 6. microsoft/AI-For-Beginners（68,696★）

- 链接：https://github.com/microsoft/AI-For-Beginners
- 主题：ai, artificial-intelligence, cnn, computer-vision, deep-learning, gan, machine-learning, microsoft-for-beginners
- 最近推送：2026-09-16
- 摘要来源：readme_head | 翻译：llm
- 中文简介：# 12 周，24 节课，AI 属于所有人！  通过我们为期 12 周、共 24 节课的课程体系，探索**人工智能**（AI）的世界！课程包含实践课程、测验和实验。该课程对初学者十分友好，涵盖 TensorFlow 和 PyTorch 等工具，以及 AI 伦理相关内容。  > **更愿意在本地克隆？** > > 本仓库包含 50 多种语言的翻译，这会显著增加下载体积。若要在克隆时不包含翻译内容，请使用稀疏检出（sparse checkout）： > > **Bash / macOS / Linux：** > ```bash > git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git > cd AI-For-Beginners > git sparse-checkout set --no-cone '/*' '!translations' '!translated_images' > ``` > > **CMD (Windows)：** > ```cmd > git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git > cd AI-For-Beginners > git sparse-checkout set --no-cone "/*" "!translations" "!translated_images" > ``` > > 这样你就能获得完成课程所需的一切内容，且下载速度更快。  **如果你希望有更多翻译语言，支持的语言列表见[此处](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**  我们欢迎来自社区的贡献！无论是修正错别字、改进文档，还是添加新的示例，你的帮助都会让这套课程对所有人更好。请查阅我们的 [CONTRIBUTING.md](CONTRIBUTING.md) 指南开始参与贡献。  **[课程思维导图](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**
- 原文简介：12 Weeks, 24 Lessons, AI for All! Explore the world of **Artificial Intelligence** (AI) with our 12-week, 24-lesson curriculum!  It includes practical lessons, quizzes, and labs. The curriculum is beginner-friendly and covers tools like TensorFlow and PyTorch, as well as ethics in AI > **Prefer to Clone Locally?** > > This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout: > > **Bash / macOS / Linux:** > ```bash > git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git > cd AI-For-Beginners > git sparse-checkout set --no-cone '/*' '!translations' '!translated_images' > ``` > > **CMD (Windows):** > ```cmd > git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git > cd AI-For-Beginners > git sparse-checkout set --no-cone "/*" "!translations" "!translated_images" > ``` > > This gives you everything you need to complete the course with a much faster download. **If you wish to have additional translations languages supported are listed [here](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)** We welcome contributions from the community! Whether you're fixing typos, improving documentation, or adding new examples, your help makes this curriculum better for everyone. Check out our [CONTRIBUTING.md](CONTRIBUTING.md) guide to get started. **[Mindmap of the Course](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

### 7. usestrix/strix（63,547★）

- 链接：https://github.com/usestrix/strix
- 主题：agents, ai-hacking, ai-penetration-testing, ai-pentesting, ai-security, artificial-intelligence, bug-bounty, code-quality
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：开源 AI 渗透测试工具，帮助您发现并修复应用程序中的漏洞。
- 原文简介：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.

### 8. jingyaogong/minimind（61,599★）

- 链接：https://github.com/jingyaogong/minimind
- 主题：artificial-intelligence, large-language-model
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：zh-skip
- 中文简介：🧠 Train a 64M-parameter LLM from scratch in just 2h! "大道至简" 中文 | [English](./README_en.md) * 此开源项目旨在完全从 0 开始，仅用 3 块钱成本与 2 小时训练时间，即可训练出规模约为 64M 的超小语言模型 MiniMind。 * MiniMind 系列极其轻量，主线最小版本体积约为 GPT-3 的 $\frac{1}{2700}$，力求让普通个人 GPU 也能快速完成训练与复现。 * 项目同时开源了大模型的极简结构与完整训练链路，覆盖 MoE、数据清洗、预训练（Pretrain）、监督微调（SFT）、LoRA、RLHF（DPO）、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏等全过程代码。 * MiniMind 同时拓展了视觉模态模型 [MiniMind-V](https://github.com/jingyaogong/minimind-v)、多模态 Omni 模型 [MiniMind-O](https://github.com/jingyaogong/minimind-o)、扩散语言模型（MiniMind-dLM）、线性模型（MiniMind-Linear），详见 [Discussion](https://github.com/jingyaogong/minimind/discussions)。 * 项目所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖第三方库提供的高层抽象接口。 * 这不仅是一个大语言模型全阶段开源复现项目，也是一套面向 LLM 入门与实践的教程。 * 希望此项目能为更多人提供一个可复现、可理解、可扩展的起点，一起感受创造的乐趣，并推动更广泛 AI 社区的进步。 > 注：本项目基于 Apache 2.0 协议开源，完全免费。“2 小时” 指 SFT 阶段在单张 NVIDIA 3090 上跑完 `1 epoch` 的实测耗时，“3 块钱” 指对应时段的 GPU 租用成本。

### 9. Lightning-AI/pytorch-lightning（31,349★）

- 链接：https://github.com/Lightning-AI/pytorch-lightning
- 主题：ai, artificial-intelligence, data-science, deep-learning, machine-learning, python, pytorch
- 最近推送：2026-09-17
- 摘要来源：feed | 翻译：llm
- 中文简介：预训练、微调任意规模的任意 AI 模型，可在 1 块或 10,000+ 块 GPU 上运行，且无需改动任何代码。
- 原文简介：Pretrain, finetune ANY AI model of ANY size on 1 or 10,000+ GPUs with zero code changes.

### 10. simstudioai/sim（29,664★）

- 链接：https://github.com/simstudioai/sim
- 主题：agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：Sim 是一个协作工作区，用于构建、部署和监控 AI 智能体与工作流。已有超过 100,000 名开发者在使用。
- 原文简介：Sim is the collaborative workspace to build, deploy, and monitor AI agents and workflows. Used by 100,000+ builders.

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 9 | 计数 |
| 输入 tokens | 1,985 | GLM usage（精确） |
| 输出 tokens | 4,424 | GLM usage（精确） |
| 合计 tokens | 6,409 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 6 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 112 秒 | 计时，统计系统占用时间 |
