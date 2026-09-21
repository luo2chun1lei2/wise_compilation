# Google Developers Blog（2026-09-21）

- 生成时间：2026-09-21 15:07
- 数据来源：RSS 订阅（https://developers.googleblog.com/feeds/posts/default/，最新 N 条）
- 查询条件：`RSS：https://developers.googleblog.com/feeds/posts/default/`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）

### 1. [Agent Anomaly Detection 现已在 Gemini Enterprise Agent Platform 上推出 Private Preview](https://developers.googleblog.com/agent-anomaly-detection-now-in-private-preview-on-the-gemini-enterprise-agent-platform/)（发布 2026-09-16）

- 中文简介：Agent Anomaly Detection 是 Gemini Enterprise Agent Platform 上一项全新的带外（out-of-band）监督层，它通过分析 OpenTelemetry 追踪数据和工具调用来捕捉行为风险，且不会给实时请求增加任何运行时延迟。该功能采用多层级检测流水线——将轻量级统计扫描与基于 LLM 的深度推理相结合——以识别基于 OWASP Agentic Top 10 的逻辑异常和策略违规行为。开发者可以在 Security Command Center 中对这些自动生成的发现结果进行分类排查，也可以在智能体超出预设风险阈值时，利用其提供的 API 以编程方式阻止后续的工具调用。
- 原文简介：Agent Anomaly Detection is a new, out-of-band oversight layer for the Gemini Enterprise Agent Platform that analyzes OpenTelemetry traces and tool calls to catch behavioral risks without adding runtime latency to live requests. It utilizes a multi-tiered detection pipeline—combining lightweight statistical scanning with deep LLM-based reasoning—to identify logical anomalies and policy violations grounded in the OWASP Agentic Top 10. Developers can triage these automated findings within Security Command Center or leverage the exposed API to programmatically block subsequent tool calls when an agent breaches defined risk thresholds.
- 摘要：feed · 翻译：llm

### 2. [构建零信任 AI 代理：判断意图，而不仅仅是语法](https://developers.googleblog.com/build-zero-trust-ai-agents-that-judge-intent-not-just-syntax/)（发布 2026-09-15）

- 中文简介：本文探讨了如何借助 Gemini Enterprise Agent Platform 将 AI 代理从静态的构建时安全控制转变为动态的运行时治理。文章重点介绍了三大主要的托管防御机制：用于筛选边缘提示词的 Model Armor、用于根据业务规则评估工具意图的 Semantic Governance Policies，以及用于捕捉多轮攻击的 Agent Anomaly Detection。通过将这些能力提升至平台层面，安全管理员可以动态执行策略并化解复杂攻击，而无需修改或重新部署代理的底层代码。
- 原文简介：This blog post explores how to transition AI agents from static, build-time security controls to dynamic runtime governance using the Gemini Enterprise Agent Platform. It highlights three primary managed defenses: Model Armor for screening edge prompts, Semantic Governance Policies for evaluating tool intent against business rules, and Agent Anomaly Detection for catching multi-turn exploits. By shifting these capabilities to the platform level, security administrators can dynamically enforce policies and neutralize complex attacks without needing to modify or redeploy the agent's underlying code.
- 摘要：feed · 翻译：llm

### 3. [使用 Tunix 在 TPU 上实现 LLM 自主后训练](https://developers.googleblog.com/autonomous-llm-post-training-with-tunix-on-tpus/)（发布 2026-09-17）

- 中文简介："autofinetune" 项目引入了一个自主研究循环，可完全自动化 LLM 后训练工作流，包括监督微调（SFT）以及通过 GRPO 进行的强化学习。开发者只需在单个 Markdown 规范中定义边界条件和评估指标，即可部署 AI 智能体来迭代编辑训练脚本、启动实验，并将经过验证的超参数优化自动提交到 Git。该框架构建于 Google 的 AI 技术栈之上——包括 Tunix、Gemma 和 Cloud TPU——消除了手动调优的周期，成功在函数调用和数学推理模型上实现了无需人工干预的性能提升。
- 原文简介：The "autofinetune" project introduces an autonomous research loop that fully automates LLM post-training workflows, including Supervised Fine-Tuning (SFT) and Reinforcement Learning via GRPO. By defining boundary conditions and evaluation metrics in a single Markdown specification, developers can deploy an AI agent to iteratively edit training scripts, launch experiments, and automatically commit verified hyperparameter optimizations to Git. Built on Google’s AI stack—including Tunix, Gemma, and Cloud TPUs—this framework eliminates manual tuning cycles, successfully demonstrating hands-off performance gains in both function calling and math reasoning models.
- 摘要：feed · 翻译：llm

### 4. [ADK for Kotlin 1.0 正式发布：在 Kotlin、Android 及更多平台上构建生产级 AI 智能体](https://developers.googleblog.com/announcing-adk-for-kotlin-10-building-production-ready-ai-agents-in-kotlin-android-and-beyond/)（发布 2026-09-09）

- 中文简介：Google 正式发布面向 Kotlin 的智能体开发套件（Agent Development Kit，ADK）1.0 版本，实现了与 Python 和 Java ADK 核心的完全功能对等，从而支持符合 Kotlin 语言习惯的多智能体 AI 开发。该框架基于 Kotlin Multiplatform (KMP) 构建，利用 Kotlin Symbol Processing (KSP) 实现零反射、类型安全的函数调用，并具备诸如人工介入（human-in-the-loop）工作流和上下文压缩等高级编排能力。此外，本次发布还推出了一套强大的 Android 优先扩展套件，使移动开发者能够通过 LiteRT-LM 集成本地模型、通过 Firebase AI 进行云端推理、使用 Room 实现会话持久化，并借助 AppSearch 提供语义记忆功能。
- 原文简介：Google has officially released version 1.0 of the Agent Development Kit (ADK) for Kotlin, achieving full feature parity with the Python and Java ADK cores to enable idiomatic, multi-agent AI development. Built on Kotlin Multiplatform (KMP), the framework leverages Kotlin Symbol Processing (KSP) for zero-reflection, type-safe function calling, alongside advanced orchestration capabilities like human-in-the-loop workflows and context compaction. Additionally, the release introduces a robust suite of Android-first extensions, allowing mobile developers to integrate local models via LiteRT-LM, cloud reasoning through Firebase AI, session persistence using Room, and semantic memory powered by AppSearch.
- 摘要：feed · 翻译：llm

### 5. [Harness 工程剖析：如何评估、迭代并守护 AI 编码智能体](https://developers.googleblog.com/the-anatomy-of-harness-engineering-how-to-evaluate-iterate-and-guard-ai-coding-agents/)（发布 2026-09-09）

- 中文简介：尽管像 SWE-bench 这样的端到端基准测试能够为 AI 智能体提供整体性能评分，但它们往往成本高昂、速度缓慢，并且缺乏根因诊断能力，无法准确解释智能体的逻辑究竟在哪个环节出现了故障。为解决这一问题，开发者应当采用行为评估——即快速、本地化的单元式测试，针对离散的中间动作进行断言，例如验证特定的工具调用或文件修改，而不是比对最终输出字符串是否完全一致。通过在这些宏观基准测试之外同步构建此类低成本的微型检查，工程团队便能放心地迭代系统提示词（system prompt）并升级模型，而不必担心出现性能回退。
- 原文简介：While end-to-end benchmarks like SWE-bench provide broad performance scores for AI agents, they are often expensive, slow, and lack the root-cause diagnostics needed to explain exactly where an agent's logic broke down. To solve this, developers should adopt behavioral evaluations—fast, local, unit-style tests that assert on discrete intermediate actions, such as verifying specific tool calls or file modifications rather than final string equality. By building these inexpensive micro-checks alongside macro benchmarks, engineering teams can confidently iterate on system prompts and upgrade models without the risk of regressions.
- 摘要：feed · 翻译：llm

### 6. [最强 AI Agents Challenge 参赛作品背后的 4 种工程模式](https://developers.googleblog.com/4-engineering-patterns-behind-the-strongest-ai-agents-challenge-submissions/)（发布 2026-09-02）

- 中文简介：最近的 Google for Startups AI Agents Challenge 表明，最成功的多智能体（multi-agent）系统依赖的是基础性的软件工程模式，而不仅仅是原始的模型能力。获奖架构无一例外地实现了双向 MCP 以实现智能体之间的无缝通信、用于并行执行的异步事件总线（async event bus）、针对模型回退（model fallback）的严格统一校验，以及最大限度减少昂贵推理调用的分级路由。通过优先采用这些结构性实践，而非简单的线性提示词链（prompt chain），开发者可以构建更具弹性、低延迟且高性价比的智能体（agentic）工作流。
- 原文简介：The recent Google for Startups AI Agents Challenge revealed that the most successful multi-agent systems rely on foundational software engineering patterns rather than just raw model power. Winning architectures consistently implemented bidirectional MCP for seamless inter-agent communication, async event buses for parallel execution, strict unified validation for model fallbacks, and tiered routing to minimize expensive inference calls. By prioritizing these structural practices over simple linear prompt chains, developers can build more resilient, low-latency, and cost-effective agentic workflows.
- 摘要：feed · 翻译：llm

### 7. [用深度学习与 Keras 解码宇宙信号](https://developers.googleblog.com/decoding-cosmic-signals-with-deep-learning-and-keras/)（发布 2026-09-01）

- 中文简介：天体粒子物理学处于天体物理学与粒子物理学这一激动人心的交叉领域，研究……
- 原文简介：Astroparticle physics sits at the exciting intersection of astrophysics and particle physics and stu...
- 摘要：feed · 翻译：llm

### 8. [Cloud TPU 上长上下文多模态 Embedding 推理的企业级精度](https://developers.googleblog.com/enterprise-grade-precision-for-long-context-multimodal-embedding-inference-on-cloud-tpu/)（发布 2026-08-26）

- 中文简介：Google Cloud 已将 TPU 支持原生集成到 vLLM 服务引擎中，使开发者能够借助 Google Kubernetes Engine (GKE) 弹性扩展高负载 Embedding 流水线。为处理 Qwen3-Embedding-8B 等模型高达 15K+ token 的超大上下文，工程团队实施了多项 TPU 专属优化，例如硬件安全的张量对齐、JAX/XLA 编译预热，以及用于分块预填充管理的混合 StepPool 架构。这些改进实现了与参考 GPU 基准近乎完美的数值一致性，开发者可以立即利用 AI-Hypercomputer GitHub 上开源的配置方案，构建自己的高吞吐语义检索应用。
- 原文简介：Google Cloud has natively integrated TPU support into the vLLM serving engine, allowing developers to elastically scale high-demand embedding pipelines using Google Kubernetes Engine (GKE). To handle massive 15K+ token contexts for models like Qwen3-Embedding-8B, the engineering team implemented TPU-specific optimizations such as hardware-safe tensor alignment, JAX/XLA compilation pre-warming, and a hybrid StepPool architecture for chunked prefill management. These enhancements achieve near-perfect numerical parity with reference GPU baselines, and developers can immediately leverage the open-sourced setup recipes on the AI-Hypercomputer GitHub to build their own high-throughput semantic retrieval applications.
- 摘要：feed · 翻译：llm

### 9. [如何在 ADK 中评估实时与语音 Agent](https://developers.googleblog.com/how-to-evaluate-live-voice-agents-in-adk/)（发布 2026-08-24）

- 中文简介：要将实时语音 Agent 从演示推向生产环境，需要严格、自动化的测试，以应对真实多轮对话的不可预测性。ADK 现已提供原生的实时评估功能，让开发者能够针对由 LLM 驱动的模拟用户来测试基于图的 Agent 工作流，这些模拟用户可通过 Gemini TTS 生成真实音频。通过定义评估场景和自然语言评分标准，你可以自动为音频响应和工具执行打分，在 ADK Web 中检查生成的对话记录，或直接在 CI/CD 流水线中运行 CLI。
- 原文简介：Moving live voice agents from demo to production requires rigorous, automated testing to handle the unpredictability of real multi-turn conversations. ADK now provides native live evaluation, allowing developers to test graph-based agent workflows against LLM-driven simulated users that generate actual audio via Gemini TTS. By defining evaluation scenarios and natural-language rubrics, you can automatically score audio responses and tool executions, inspect the resulting transcripts in ADK Web, or run the CLI directly in your CI/CD pipeline.
- 摘要：feed · 翻译：llm

### 10. [使用 Google 的 Agent Development Kit 构建零信任 AI 智能体](https://developers.googleblog.com/build-zero-trust-ai-agents-with-googles-agent-development-kit/)（发布 2026-08-17）

- 中文简介：构建会修改生产环境状态的自主 AI 智能体，需要超越软性的系统提示词，转向健壮的零信任架构。为了保护 Google Agent Development Kit (ADK) 工作流免受提示词注入和恶意执行的攻击，开发者必须为数据库写入实现基于硬件的加密签名，为动态代码实现基于 gVisor 的内核级沙箱，并为 I/O 校验实现确定性的语义网关。通过在基础设施层面强制执行这些硬性安全边界，你可以安全地部署多工具 AI 智能体，而不会面临未经授权的数据篡改或服务器被入侵的风险。
- 原文简介：Building autonomous AI agents that mutate production state requires moving beyond soft system prompts to a robust zero-trust architecture. To secure Google Agent Development Kit (ADK) workflows against prompt injections and malicious execution, developers must implement hardware-backed cryptographic signatures for database writes, kernel-level sandboxing with gVisor for dynamic code, and deterministic semantic gateways for I/O validation. By enforcing these hard security boundaries at the infrastructure level, you can safely deploy multi-tool AI agents without risking unauthorized data manipulation or server compromise.
- 摘要：feed · 翻译：llm

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 0 | 计数 |
| 输入 tokens | 0 | GLM usage（精确） |
| 输出 tokens | 0 | GLM usage（精确） |
| 合计 tokens | 0 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 0 次（限额 60/时，未认证） | 计数 |
| RSS 抓取 | 2 次 | 计数 |
| 总耗时（获取→生成） | 14 秒 | 计时，统计系统占用时间 |
