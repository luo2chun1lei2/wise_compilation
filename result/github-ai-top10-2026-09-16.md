# GitHub AI 热门项目 Top 10

- 生成时间：2026-09-16 17:26
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`topic:artificial-intelligence stars:>500 pushed:>2026-09-09`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 187,376 | Python | AutoGPT 的愿景是让人人都能使用并加以构建的普惠 AI。我们的使命是提供工具，让你能够专注于真正重要的事情。 |
| 2 | [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) | 105,060 | Jupyter Notebook | 从零开始、一步一步地用 PyTorch 实现一个类 ChatGPT 的大语言模型（LLM） |
| 3 | [hacksider/Deep-Live-Cam](https://github.com/hacksider/Deep-Live-Cam) | 96,668 | Python | 实时换脸与一键视频深度伪造（deepfake），仅需一张图片 |
| 4 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 94,005 | TypeScript | 为每个智能体（Agent）提供跨会话的持久上下文——捕获智能体在会话期间执行的所有操作，利用 AI 进行压缩，并将相关上下文注入未来的会话中。兼容 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copil |
| 5 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 88,098 | TypeScript | 🙌 OpenHands：AI 驱动开发 |
| 6 | [usestrix/strix](https://github.com/usestrix/strix) | 62,882 | Python | 开源 AI 渗透测试工具，助您发现并修复应用中的漏洞。 |
| 7 | [jingyaogong/minimind](https://github.com/jingyaogong/minimind) | 61,269 | Python | 🧠 Train a 64M-parameter LLM from scratch in just 2h! |
| 8 | [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | 31,344 | Python | 在 1 块或 10,000+ 块 GPU 上预训练、微调任意规模的 AI 模型，零代码改动。 |
| 9 | [simstudioai/sim](https://github.com/simstudioai/sim) | 29,647 | TypeScript | Sim 是用于构建、部署和监控 AI 智能体与工作流的协作工作区。已有超过 100,000 名构建者在使用。 |
| 10 | [The-Art-of-Hacking/h4cker](https://github.com/The-Art-of-Hacking/h4cker) | 29,437 | Jupyter Notebook | 本仓库由 Omar Santos（@santosomar）维护，包含数千个与道德黑客、漏洞赏金、数字取证与事件响应（DFIR）、AI 安全、漏洞研究、exploit 开发、逆向工程等相关的资源。🔥 另请查看：https://hackertr |

## 详情

### 1. Significant-Gravitas/AutoGPT（187,376★）

- 链接：https://github.com/Significant-Gravitas/AutoGPT
- 主题：agentic-ai, agents, ai, artificial-intelligence, autonomous-agents, claude, gpt, llama-api
- 最近推送：2026-09-16
- 摘要来源：feed | 翻译：llm
- 中文简介：AutoGPT 的愿景是让人人都能使用并加以构建的普惠 AI。我们的使命是提供工具，让你能够专注于真正重要的事情。
- 原文简介：AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.

### 2. rasbt/LLMs-from-scratch（105,060★）

- 链接：https://github.com/rasbt/LLMs-from-scratch
- 主题：ai, artificial-intelligence, attention-mechanism, deep-learning, finetuning, from-scratch, generative-ai, gpt
- 最近推送：2026-09-10
- 摘要来源：readme_head | 翻译：llm
- 中文简介：从零开始、一步一步地用 PyTorch 实现一个类 ChatGPT 的大语言模型（LLM）  本仓库包含开发、预训练和微调一个类 GPT 大语言模型的代码，也是《Build a Large Language Model (From Scratch)》一书的官方代码仓库。  在 [*Build a Large Language Model (From Scratch)*](http://mng.bz/orYv) 一书中，你将通过从零开始、一步一步地编写代码，从内到外地学习并理解大语言模型（LLM）的工作原理。本书将引导你创建自己的 LLM，并以清晰的文字、图表和示例讲解每一个阶段。  本书所描述的、用于训练和开发一个面向教学用途的小而可用的模型的方法，与创建 ChatGPT 背后那类大规模基础模型所采用的方法如出一辙。此外，本书还包含用于加载更大规模预训练模型权重以进行微调的代码。  - 官方[源代码仓库](https://github.com/rasbt/LLMs-from-scratch)链接 - [Manning（出版商网站）上的图书链接](http://mng.bz/orYv) - [Amazon.com 上的图书页面链接](https://www.amazon.com/gp/product/1633437167) - ISBN 9781633437166  要下载本仓库的副本，请点击 [Download ZIP](https://github.com/rasbt/LLMs-from-scratch/archive/refs/heads/main.zip) 按钮，或在终端中执行以下命令：  git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git  （如果你是从 Manning 网站下载的代码包，请考虑访问 GitHub 上的官方代码仓库 [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) 以获取最新更新。）
- 原文简介：Implement a ChatGPT-like LLM in PyTorch from scratch, step by step This repository contains the code for developing, pretraining, and finetuning a GPT-like LLM and is the official code repository for the book [Build a Large Language Model (From Scratch)](https://amzn.to/4fqvn0D). In [*Build a Large Language Model (From Scratch)*](http://mng.bz/orYv), you'll learn and understand how large language models (LLMs) work from the inside out by coding them from the ground up, step by step. In this book, I'll guide you through creating your own LLM, explaining each stage with clear text, diagrams, and examples. The method described in this book for training and developing your own small-but-functional model for educational purposes mirrors the approach used in creating large-scale foundational models such as those behind ChatGPT. In addition, this book includes code for loading the weights of larger pretrained models for finetuning. - Link to the official [source code repository](https://github.com/rasbt/LLMs-from-scratch) - [Link to the book at Manning (the publisher's website)](http://mng.bz/orYv) - [Link to the book page on Amazon.com](https://www.amazon.com/gp/product/1633437167) - ISBN 9781633437166 To download a copy of this repository, click on the [Download ZIP](https://github.com/rasbt/LLMs-from-scratch/archive/refs/heads/main.zip) button or execute the following command in your terminal: git clone --depth 1 https://github.com/rasbt/LLMs-from-scratch.git (If you downloaded the code bundle from the Manning website, please consider visiting the official code repository on GitHub at [https://github.com/rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch) for the latest updates.)

### 3. hacksider/Deep-Live-Cam（96,668★）

- 链接：https://github.com/hacksider/Deep-Live-Cam
- 主题：ai, ai-deep-fake, ai-face, ai-webcam, artificial-intelligence, deep-fake, deepfake, deepfake-webcam
- 最近推送：2026-09-15
- 摘要来源：readme_head | 翻译：llm
- 中文简介：实时换脸与一键视频深度伪造（deepfake），仅需一张图片  Deep-Live-Cam 2.1.6  一键实现实时换脸与视频深度伪造，仅需一张图片。  这款深度伪造软件旨在成为 AI 生成媒体行业的高效生产力工具。它可以帮助艺术家为自定义角色制作动画、创作引人入胜的内容，甚至可以利用模型进行服装设计。  我们深知该软件存在被滥用于不道德用途的潜在风险，并致力于采取预防措施。内置检查机制可防止程序处理不当媒体内容（裸露、血腥内容、战争影像等敏感素材等）。我们将继续负责任地开发本项目，遵守法律与道德规范。如有法律要求，我们可能会关闭项目或为输出内容添加水印。  - 道德使用：用户应以负责任且合法的方式使用本软件。如使用真人面部，须征得当事人同意，并在网上分享时明确标注输出内容为深度伪造。 - 内容限制：软件内置检查机制，防止处理不当媒体内容，例如裸露、血腥内容或敏感素材。 - 法律合规：我们遵守所有相关法律和道德准则。如有法律要求，我们可能会关闭项目或在输出内容中添加水印。 - 用户责任：我们对最终用户的行为不承担责任。用户必须确保其对软件的使用符合道德标准和法律要求。  使用本软件即表示您同意上述条款，并承诺以尊重他人权利与尊严的方式使用它。
- 原文简介：real time face swap and one-click video deepfake with only a single image Deep-Live-Cam 2.1.6 Real-time face swap and video deepfake with a single click and only a single image. This deepfake software is designed to be a productive tool for the AI-generated media industry. It can assist artists in animating custom characters, creating engaging content, and even using models for clothing design. We are aware of the potential for unethical applications and are committed to preventative measures. A built-in check prevents the program from processing inappropriate media (nudity, graphic content, sensitive material like war footage, etc.). We will continue to develop this project responsibly, adhering to the law and ethics. We may shut down the project or add watermarks if legally required. - Ethical Use: Users are expected to use this software responsibly and legally. If using a real person's face, obtain their consent and clearly label any output as a deepfake when sharing online. - Content Restrictions: The software includes built-in checks to prevent processing inappropriate media, such as nudity, graphic content, or sensitive material. - Legal Compliance: We adhere to all relevant laws and ethical guidelines. If legally required, we may shut down the project or add watermarks to the output. - User Responsibility: We are not responsible for end-user actions. Users must ensure their use of the software aligns with ethical standards and legal requirements. By using this software, you agree to these terms and commit to using it in a manner that respects the rights and dignity of others.

### 4. thedotmack/claude-mem（94,005★）

- 链接：https://github.com/thedotmack/claude-mem
- 主题：ai, ai-agents, ai-memory, anthropic, artificial-intelligence, chromadb, claude, claude-agent-sdk
- 最近推送：2026-09-16
- 摘要来源：feed | 翻译：llm
- 中文简介：为每个智能体（Agent）提供跨会话的持久上下文——捕获智能体在会话期间执行的所有操作，利用 AI 进行压缩，并将相关上下文注入未来的会话中。兼容 Claude Code、OpenClaw、Codex、Gemini、Hermes、Copilot、OpenCode 等更多工具。
- 原文简介：Persistent Context Across Sessions for Every Agent –  Captures everything your agent does during sessions, compresses it with AI, and injects relevant context back into future sessions. Works with Claude Code, OpenClaw, Codex, Gemini, Hermes, Copilot, OpenCode + More

### 5. OpenHands/OpenHands（88,098★）

- 链接：https://github.com/OpenHands/OpenHands
- 主题：agent, artificial-intelligence, chatgpt, claude-ai, cli, developer-tools, gpt, llm
- 最近推送：2026-09-16
- 摘要来源：readme_head | 翻译：llm
- 中文简介：🙌 OpenHands：AI 驱动开发 Agent Canvas 面向编码智能体与自动化的自托管开发者控制中心。 在本地、远程和云端后端运行 OpenHands、Claude Code、Codex、Gemini 或任何兼容 ACP 的智能体。 快速入门  | 文档  | 自托管  | ACP 智能体  | 自动化  | Slack OpenHands Agent Canvas 将你的编码智能体转变为一支自托管、全天候在线的工程团队。它是一个开发者控制中心，可用于发起对话并自动化日常任务——例如生成发布到 Slack 的报告，或将 GitHub issue 自动分解为任务。  它默认在你的机器上本地运行，但可以连接到多个“智能体后端”，例如在 Docker 容器中、虚拟机上或公司基础设施内运行智能体。你也可以选择在 OpenHands Cloud 或 OpenHands Enterprise 基础设施上运行智能体。  Agent Canvas 开箱即支持运行开源的 OpenHands 智能体，同时也可以使用任何第三方智能体，如 Claude Code 和 Codex。  如果你有任何问题或反馈，请提交 GitHub issue，或加入 Slack 的 [#proj-agent-canvas 频道](https://openhands.dev/joinslack)。  你可以安装 OpenHands，在任何机器上运行智能体：笔记本电脑、Mac Mini 等专用计算机，或云端服务器。  运行 OpenHands 最强大的方式是在云端服务器上。这样即使合上笔记本电脑，你的智能体也能持续运行，并且更容易通过 Slack、GitHub 和 Datadog 等第三方服务触发你的智能体。详情请参阅 [SELF_HOSTING.md](docs/SELF_HOSTING.md)，尤其是有关安全加固方面的内容。
- 原文简介：🙌 OpenHands: AI-Driven Development Agent Canvas The self-hosted developer control center for coding agents and automations. Run OpenHands, Claude Code, Codex, Gemini, or any ACP-compatible agent across local, remote, and cloud backends. Quickstart  | Docs  | Self-Hosting  | ACP Agents  | Automations  | Slack OpenHands Agent Canvas turns your coding agents into a self-hosted, always-on engineering team. It's a developer control center for starting conversations and automating everyday tasks — like generating reports that publish to Slack or automatically decomposing GitHub issues into tasks. It runs locally on your machine by default, but can connect to multiple “agent backends”, e.g. running agents in Docker containers, on VMs, or within your company infrastructure. You can optionally choose to run agents on OpenHands Cloud or OpenHands Enterprise infrastructure. Agent Canvas runs the open source OpenHands agent out-of-the-box, but can use any third-party agent like Claude Code and Codex. If you have questions or feedback, please open a GitHub issue or join the [#proj-agent-canvas channel in Slack](https://openhands.dev/joinslack). You can install OpenHands to run agents on any machine: on your laptop, on a dedicated computer like a Mac Mini, or on a server in the cloud. The most powerful way to run OpenHands is on a server in the cloud. This allows your agents to continue running even when your laptop is shut, and makes it easier to trigger your agents through third-party services like Slack, GitHub, and Datadog. See [SELF_HOSTING.md](docs/SELF_HOSTING.md) for details, especially with respect to security hardening.

### 6. usestrix/strix（62,882★）

- 链接：https://github.com/usestrix/strix
- 主题：agents, ai-hacking, ai-penetration-testing, ai-pentesting, ai-security, artificial-intelligence, bug-bounty, code-quality
- 最近推送：2026-09-15
- 摘要来源：feed | 翻译：llm
- 中文简介：开源 AI 渗透测试工具，助您发现并修复应用中的漏洞。
- 原文简介：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.

### 7. jingyaogong/minimind（61,269★）

- 链接：https://github.com/jingyaogong/minimind
- 主题：artificial-intelligence, large-language-model
- 最近推送：2026-09-15
- 摘要来源：readme_head | 翻译：zh-skip
- 中文简介：🧠 Train a 64M-parameter LLM from scratch in just 2h! "大道至简" 中文 | [English](./README_en.md) * 此开源项目旨在完全从 0 开始，仅用 3 块钱成本与 2 小时训练时间，即可训练出规模约为 64M 的超小语言模型 MiniMind。 * MiniMind 系列极其轻量，主线最小版本体积约为 GPT-3 的 $\frac{1}{2700}$，力求让普通个人 GPU 也能快速完成训练与复现。 * 项目同时开源了大模型的极简结构与完整训练链路，覆盖 MoE、数据清洗、预训练（Pretrain）、监督微调（SFT）、LoRA、RLHF（DPO）、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏等全过程代码。 * MiniMind 同时拓展了视觉模态模型 [MiniMind-V](https://github.com/jingyaogong/minimind-v)、多模态 Omni 模型 [MiniMind-O](https://github.com/jingyaogong/minimind-o)、扩散语言模型（MiniMind-dLM）、线性模型（MiniMind-Linear），详见 [Discussion](https://github.com/jingyaogong/minimind/discussions)。 * 项目所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖第三方库提供的高层抽象接口。 * 这不仅是一个大语言模型全阶段开源复现项目，也是一套面向 LLM 入门与实践的教程。 * 希望此项目能为更多人提供一个可复现、可理解、可扩展的起点，一起感受创造的乐趣，并推动更广泛 AI 社区的进步。 > 注：本项目基于 Apache 2.0 协议开源，完全免费。“2 小时” 指 SFT 阶段在单张 NVIDIA 3090 上跑完 `1 epoch` 的实测耗时，“3 块钱” 指对应时段的 GPU 租用成本。

### 8. Lightning-AI/pytorch-lightning（31,344★）

- 链接：https://github.com/Lightning-AI/pytorch-lightning
- 主题：ai, artificial-intelligence, data-science, deep-learning, machine-learning, python, pytorch
- 最近推送：2026-09-14
- 摘要来源：feed | 翻译：llm
- 中文简介：在 1 块或 10,000+ 块 GPU 上预训练、微调任意规模的 AI 模型，零代码改动。
- 原文简介：Pretrain, finetune ANY AI model of ANY size on 1 or 10,000+ GPUs with zero code changes.

### 9. simstudioai/sim（29,647★）

- 链接：https://github.com/simstudioai/sim
- 主题：agent-workflow, agentic-workflow, agents, ai, aiagents, anthropic, artificial-intelligence, automation
- 最近推送：2026-09-16
- 摘要来源：feed | 翻译：llm
- 中文简介：Sim 是用于构建、部署和监控 AI 智能体与工作流的协作工作区。已有超过 100,000 名构建者在使用。
- 原文简介：Sim is the collaborative workspace to build, deploy, and monitor AI agents and workflows. Used by 100,000+ builders.

### 10. The-Art-of-Hacking/h4cker（29,437★）

- 链接：https://github.com/The-Art-of-Hacking/h4cker
- 主题：ai, ai-security, artificial-intelligence, awesome-list, awesome-lists, cybersecurity, ethical-hacking, exploit
- 最近推送：2026-09-12
- 摘要来源：feed | 翻译：llm
- 中文简介：本仓库由 Omar Santos（@santosomar）维护，包含数千个与道德黑客、漏洞赏金、数字取证与事件响应（DFIR）、AI 安全、漏洞研究、exploit 开发、逆向工程等相关的资源。🔥 另请查看：https://hackertraining.org
- 原文简介：This repository is maintained by Omar Santos (@santosomar) and includes thousands of resources related to ethical hacking, bug bounties, digital forensics and incident response (DFIR), AI security, vulnerability research, exploit development, reverse engineering, and more. 🔥 Also check: https://hackertraining.org
