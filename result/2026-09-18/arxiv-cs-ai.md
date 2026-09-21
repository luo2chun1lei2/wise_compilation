# cs.AI updates on arX（2026-09-18）

- 生成时间：2026-09-18 18:58
- 数据来源：RSS 订阅（https://export.arxiv.org/rss/cs.AI，最新 N 条）
- 查询条件：`RSS：https://export.arxiv.org/rss/cs.AI`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 文章 | 发布时间 | 简介 |
|---|---|---|---|
| 1 | [正则化强调时序差分学习：常数步长下的稳定性](https://arxiv.org/abs/2609.19170) | 2026-09-18 00:00 | 强调时序差分学习（ETD）稳定了期望离策略TD更新并改变了其投影几何，但这两种性质都不能决定常数步长下的采样动态。我们构造了一个遍历的两状态反例，其中ETD均值映射是压缩的，而采样乘积却具有正的最大Lyapunov指数。 |
| 2 | [BioPhys-Bridge：一个面向物理驱动生物学研究中跨学科科学推…](https://arxiv.org/abs/2609.19180) | 2026-09-18 00:00 | 语言模型在分析跨学科科学研究文献时面临独特挑战。在生物物理学研究中，忠实可靠的回答需要将观测数据建立在源证据之上，通过定量物理模型加以解释，并将其与生物学机制相关联。为应对这一挑战，我们提出了 BioPhys-Bridg |
| 3 | [我们对LLM有何期待？LLM基准测试设计的系统性梳理](https://arxiv.org/abs/2609.19182) | 2026-09-18 00:00 | 基准测试是评估和传达大语言模型（LLM）进展的核心方式。然而，仅凭模型排名几乎无法揭示评估需求本身是如何变化的。基准测试种类的不断扩展提供了另一个视角：研究人员期待LLM做什么，以及他们如何界定成功的表现。我们系统性地梳 |
| 4 | [立场：是时候用自进化操作系统层将基础模型虚拟化了](https://arxiv.org/abs/2609.19203) | 2026-09-18 00:00 | AI 应用已从单一、单体式的基础模型（FM）转变为复合式智能体系统。然而当今的技术栈依然碎片化：尽管各类协议（如 MCP、A2A）简化了工具/智能体之间的连接，但每个框架都内嵌了一套隐式的运行时，用于管理状态、记忆、预算 |
| 5 | [当前的系统性泛化任务遗漏了什么？一种以推理为中心的分析](https://arxiv.org/abs/2609.19212) | 2026-09-18 00:00 | 系统性泛化（systematic generalization），即通过重新组合已知的基本元素来解决新问题的能力，是人类智能的核心，但在受控环境下难以进行严格研究。因此，现有研究依赖于一些简化处理，例如近似线性的动作组合 |
| 6 | [以对话式大语言模型智能体刻画网络搜索：从搜索决策与策略到搜索结果与响应](https://arxiv.org/abs/2609.19244) | 2026-09-18 00:00 | 摘要：对话式大语言模型（LLM）智能体日益依赖网络搜索，然而智能体搜索的端到端生命周期仍然鲜为人知。我们首次对四大主流对话平台（ChatGPT、Claude、Grok 和 DeepSeek）的网络搜索进行了研究，将真实世 |
| 7 | [AI 智能体理解计算机体系结构吗？](https://arxiv.org/abs/2609.19387) | 2026-09-18 00:00 | 人们越来越多地要求智能体（Agent）设计硬件，也越来越多地看到其取得成功的报道。这类报道只能证明设计得到了改进，却无法证明原因。一个改进了加速器的智能体，可能是在对机器进行推理，也可能只是在一堆从未理解其含义的旋钮上进 |
| 8 | [MAGS：多智能体自动形式化保障智能体输出的安全性](https://arxiv.org/abs/2609.19391) | 2026-09-18 00:00 | LLM 编码智能体如今生成复杂程序的规模已使彻底的人工审查变得日益困难，从而增加了安全与安保故障的风险。常见的方法，包括模糊测试（fuzz testing）、静态分析以及 LLM-as-a-Verifier，能够检测出许 |
| 9 | [以封闭世界解析对抗 LLM 智能体中的工具幻觉](https://arxiv.org/abs/2609.19425) | 2026-09-18 00:00 | 工具增强的大语言模型（LLM）智能体会以一种现有工具选择或工具安全方法均未涉及的方式失效：它们调用不存在的工具，并传递任何 schema 均未声明的参数。现有防御要么挑选正确的工具（selection），要么约束智能体对 |
| 10 | [目标的语法与语义](https://arxiv.org/abs/2609.19448) | 2026-09-18 00:00 | 在认知科学与计算机科学中，目标被概念化为一种认知状态，它能够与世界知识灵活结合，从而组织和明确有目的的行为。就此而言，目标是组合性表征，其内容与理性行为相关。我们在此提请注意作为表征的目标及其内容，因为这凸显了与认知科学 |

## 详情

### 1. 正则化强调时序差分学习：常数步长下的稳定性（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19170
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：强调时序差分学习（ETD）稳定了期望离策略TD更新并改变了其投影几何，但这两种性质都不能决定常数步长下的采样动态。我们构造了一个遍历的两状态反例，其中ETD均值映射是压缩的，而采样乘积却具有正的最大Lyapunov指数。再生周期分析将该符号与后续迹（follow-on trace）的无穷方差分离开来。我们提出正则化强调TD（RETD），这是一种归一化的一阶冲击后修复方法，它保持迹和重要性比率不变，将强调TD信号存储在一个泄漏标量状态中，并释放延迟修正。RETD的原始平衡点是ETD平衡点的一个仿射平移；单正则化和双正则化读出可以精确恢复ETD不动点。我们证明了调和递减步长下的几乎必然收敛性，并基于马尔可夫随机乘积界得到了条件性的常数步长矩压缩结果。RETD在两状态构造和某个Baird点上具有经过认证的负指数，而Baird问题上ETD的正号仍仅为数值结果。配对的10,000次运行实验验证了这两种分离、不动点恢复、非单调稳定区域以及任务依赖性。RETD改变了冲击后动态；它并不能减少共享的后续迹方差。
- 原文简介：Emphatic temporal-difference learning (ETD) stabilizes the expected off-policy TD update and changes its projection geometry, but neither property determines constant-stepsize sampled dynamics. We construct an ergodic two-state counterexample in which the ETD mean map contracts while the sampled product has a positive top Lyapunov exponent. Regenerative-cycle analysis separates this sign from the infinite variance of the follow-on trace. We introduce regularized emphatic TD (RETD), a normalized first-order post-shock repair that leaves the trace and importance ratios unchanged, stores the emphatic TD signal in a leaky scalar state, and releases a delayed correction. RETD's raw equilibrium is an affine shift of the ETD equilibrium; single- and two-regularization readouts recover the ETD fixed point exactly. We prove almost-sure convergence for harmonic diminishing stepsizes and a conditional constant-stepsize moment-contraction result from a Markovian random-product bound. RETD has certified negative exponents on the two-state construction and one Baird point, whereas the positive Baird ETD sign remains numerical. Paired 10,000-run experiments validate both separations, fixed-point recovery, a nonmonotone stability region, and task dependence. RETD changes post-shock dynamics; it does not reduce the shared follow-on-trace variance.

### 2. BioPhys-Bridge：一个面向物理驱动生物学研究中跨学科科学推理的基准测试（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19180
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：语言模型在分析跨学科科学研究文献时面临独特挑战。在生物物理学研究中，忠实可靠的回答需要将观测数据建立在源证据之上，通过定量物理模型加以解释，并将其与生物学机制相关联。为应对这一挑战，我们提出了 BioPhys-Bridge，这是一个用于生物物理学文献中基于证据的科学推理的新型基准数据集。每个案例包含证据块、稳定的证据 ID、定量数值、单位、方程、假设、机制以及下一步决策，作为问答（QA）和检索增强生成（RAG）的锚定目标。首版发布包含 500 个案例和 1,517 个面向智能体的任务，涵盖六个生物学领域和九个物理模型家族，其中包括为未来扩展预留的三个稀疏家族。我们对所有案例在模式（schema）、证据完整性、定量锚定、源许可、重复性和单位归一化等方面执行严格的质量把关，并对其中 81 个案例进行了领域专家审校和标注。初步评估显示，DeepSeek-V4-Flash 获得了最高的证据 ID $F_1$ 分数（0.360），其次是 Qwen3.7-Max（0.316）和 GPT-4o-mini（0.294）。BioPhys-Bridge 是一个跨学科基准，用于评估归因能力、忠实度、幻觉减少以及涉及复杂多步科学推理的生物实验设计。未来工作将扩充数据集的规模与复杂度，并进行全面评估。代码和数据可在 GitHub 仓库及 Hugging Face 上获取。
- 原文简介：Language models face unique challenges in analyzing interdisciplinary scientific research literature. In biophysics research, faithful answers require grounding observed data in source evidence, interpreting it through a quantitative physics model, and linking it to a biological mechanism. To address this challenge, we introduce BioPhys-Bridge, a novel benchmark dataset for evidence-grounded scientific reasoning over biophysical literature. Each case contains evidence blocks, stable evidence IDs, quantitative values, units, equations, assumptions, mechanisms, and next decisions as grounding targets for question answering (QA) and retrieval-augmented generation (RAG). The initial release contains 500 cases, 1,517 agent-facing tasks, and covers six biological domains and nine physical model families, including three sparse families reserved for future expansion. We enforce strict quality gates for all cases in schema, evidence-integrity, quantitative-grounding, source-license, duplicate, unit-normalization, with domain expert review and annotation for 81 cases. Preliminary evaluations show that DeepSeek-V4-Flash obtain the highest evidence-ID $F_1$ score (0.360), followed by Qwen3.7-Max (0.316) and GPT-4o-mini (0.294). BioPhys-Bridge is an interdisciplinary benchmark for evaluating attribution, faithfulness, hallucination reduction, and biological experiment design with complex, multi-step scientific reasoning. Future works will increase the size and complexity of the dataset and perform comprehensive evaluations. Code and data are available in the GitHub repository and on Hugging Face.

### 3. 我们对LLM有何期待？LLM基准测试设计的系统性梳理（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19182
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：基准测试是评估和传达大语言模型（LLM）进展的核心方式。然而，仅凭模型排名几乎无法揭示评估需求本身是如何变化的。基准测试种类的不断扩展提供了另一个视角：研究人员期待LLM做什么，以及他们如何界定成功的表现。我们系统性地梳理了2022年1月至2026年8月间arXiv提交的14,767篇引入或更新评估资源的论文。通过分阶段筛选和自动化全文编码，我们考察了目标系统与领域、评估材料与条件以及评分机制的变化。这批文献显示，对行动、交互和专业应用的重视日益增强，同时成熟的设计元素与较新的设计元素常常并存。模型参与的发展也不均衡：基于LLM的评分在智能体（agent）组与非智能体组中均持续增长，而模型生成的材料在近期批次中并未出现可与之相比的持续增长。这些发现揭示了公共研究如何将能力预期转化为具体的测试与成功标准。当AI参与构建测试、执行任务和评判回答时，它们也提出了一个问题：不断扩展的评估是提供了更多独立的证据，还是有可能复制其参与模型的偏好与盲点？
- 原文简介：Benchmarks are central to how progress in large language models (LLMs) is assessed and communicated. Yet model rankings alone reveal little about how evaluation requirements themselves are changing. The expanding variety of benchmarks offers another perspective: what researchers expect LLMs to do, and what they count as successful performance. We systematically map 14,767 papers introducing or updating evaluation resources from arXiv submissions between January 2022 and August 2026. Using staged screening and automated full-text coding, we examine changes in target systems and domains, evaluation materials and conditions, and scoring mechanisms. The collection shows growing emphasis on action, interaction, and professional applications, while established and newer design elements frequently coexist. Model participation also develops unevenly: LLM-based scoring grows within both agent and non-agent groups, whereas model-generated materials show no comparable sustained increase in recent cohorts. These findings illuminate how public research translates capability expectations into concrete tests and criteria for success. As AI participates in constructing tests, performing tasks, and judging responses, they also raise a question: does expanding evaluation provide more independent evidence, or risk reproducing the preferences and blind spots of its participating models?

### 4. 立场：是时候用自进化操作系统层将基础模型虚拟化了（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19203
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：AI 应用已从单一、单体式的基础模型（FM）转变为复合式智能体系统。然而当今的技术栈依然碎片化：尽管各类协议（如 MCP、A2A）简化了工具/智能体之间的连接，但每个框架都内嵌了一套隐式的运行时，用于管理状态、记忆、预算和安全护栏，导致模型行为难以移植，治理也变得脆弱。这与操作系统诞生之前的计算时代如出一辙——当时每个程序都需要重新实现各类基础服务。本立场论文认为，该领域现在需要一种基础模型操作系统（FMOS）——一个将基础模型交互虚拟化的系统层，其原理类似于虚拟机对物理硬件的抽象，让应用仿佛拥有专用、可信且能力实际上不受限制的基础模型实例。在内部，FMOS 负责统筹跨记忆分层的知识管理、模型选择与资源分配，以及验证与策略执行。正如人脑会在快速直觉与慢速深思之间切换，FMOS 会学习何时介入、何时让推理直接进行，并基于运行经验持续调整其策略。
- 原文简介：AI applications have shifted from single, monolithic foundation models (FM) to compound agentic systems. Yet today's stacks remain fragmented: even as protocols (e.g., MCP, A2A) ease tool/agent connectivity, each framework embeds an implicit runtime for state, memory, budgets, and guardrails, making behavior non-portable and governance brittle. It mirrors computing before operating systems, when every program re-implemented basic services. This position paper argues that the field now needs a Foundation Model Operating System (FMOS) -- a system layer that virtualizes FM interactions analogous to how virtual machines abstract physical hardware, giving applications the illusion of dedicated, trustworthy FM instances with effectively unbounded capabilities. Internally, the FMOS orchestrates knowledge across memory tiers, model selection and resource allocation, and verification and policy enforcement. Like the human brain switching between fast intuition and slow deliberation, the FMOS learns when to intervene and when to let inference proceed directly and continuously adapting its policies based on operational experience.

### 5. 当前的系统性泛化任务遗漏了什么？一种以推理为中心的分析（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19212
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：系统性泛化（systematic generalization），即通过重新组合已知的基本元素来解决新问题的能力，是人类智能的核心，但在受控环境下难以进行严格研究。因此，现有研究依赖于一些简化处理，例如近似线性的动作组合、基于生成性（productivity）的测试以及动作显式的目标，这些简化使系统性泛化更易于研究，却忽略了该能力的某些关键方面。为了刻画这些简化所遗漏的内容，我们采用以推理为中心的视角，并提出了 TranSGrid——一个在统一任务中将演绎、归纳和溯因推理结合在一起的测试平台。在 4,800 个 TranSGrid 实例上对七个 Transformer 模型开展的实验表明，所有模型在 TranSGrid 上的表现都远差于留出测试集：最大的模型解决了测试集中 79.6% 的问题，但在 TranSGrid 上仅解决 55.3%，在最难的子集上仅解决 15.8%。这一差距在训练长度范围内依然存在，说明仅凭生成性不足以评估系统性泛化。此外，我们将另外两种简化重新引入 TranSGrid：一种变体使动作几乎以线性方式组合（降低归纳需求），另一种变体使目标变为动作显式（降低溯因需求）。在这两种情况下，解决率都回升到大致相当于测试集的水平，表明任何一种简化单独施加都足以将 TranSGrid 降格为一个普通的留出测试集。综合来看，我们的结果表明，现有任务降低了归纳需求或溯因需求中的一项或两项，而要全面衡量系统性泛化，需要一个同时涉及这三种推理形式的任务。
- 原文简介：Systematic generalization, the ability to solve novel problems by recombining known atomic elements, is central to human intelligence but difficult to study rigorously under controlled settings. Existing studies therefore rely on simplifications such as approximately linear action composition, productivity-based tests, and action-explicit goals, which make systematic generalization easier to study but omit some essential aspects of this capability. To characterize what these simplifications miss, we adopt a reasoning-centered lens and introduce TranSGrid, a testbed that brings deductive, inductive, and abductive reasoning together within a unified task. Experiments with seven Transformers on 4,800 TranSGrid instances show that all models perform much worse on TranSGrid than on a held-out test set: the largest model solves 79.6% of the test set, but only 55.3% of TranSGrid and 15.8% of the hardest subset. The gap remains within the training length range, showing that productivity alone is not sufficient to evaluate systematic generalization. Additionally, we reintroduce the other two simplifications into TranSGrid: one variant makes actions compose almost linearly (reducing the inductive demand), the other makes goals action-explicit (reducing the abductive one). In both, solve rates return to roughly the test set level, showing that either simplification alone is enough to reduce TranSGrid to an ordinary held-out test set. Together, our results show that existing tasks reduce either or both of the inductive and abductive demands, and that comprehensively measuring systematic generalization requires a task that involves all three forms of reasoning.

### 6. 以对话式大语言模型智能体刻画网络搜索：从搜索决策与策略到搜索结果与响应（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19244
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：摘要：对话式大语言模型（LLM）智能体日益依赖网络搜索，然而智能体搜索的端到端生命周期仍然鲜为人知。我们首次对四大主流对话平台（ChatGPT、Claude、Grok 和 DeepSeek）的网络搜索进行了研究，将真实世界的用户交互（invivo）与通过 API 使用同一平台模型的受控实验（invitro）相结合。我们考察了智能体调用网络搜索决策的质量、其构建查询的策略、所接收搜索结果中潜在的域名偏好，以及它们在将搜索结果转化为有据可依的响应时所做出的选择。我们发现，调用网络搜索的决策在不同平台和模型之间存在显著差异，而更频繁地调用网络搜索并不一定会带来更好的响应质量。我们进一步表明，对话式智能体采用了不同的复杂查询策略，且平台专属搜索引擎会返回来自其偏好域名的搜索结果。最后，尽管响应在很大程度上以搜索结果为依据，但部分论断依赖于未注明出处的搜索结果，这引发了对归属和可靠性的担忧。我们的研究结果对未来 AI 智能体的设计以及面向对话式检索优化的网络搜索工具具有重要意义。
- 原文简介：Conversational LLM agents increasingly rely on Web search, yet the end-to-end lifecycle of agentic search remains poorly understood. We present the first study of Web search across four major conversational platforms (ChatGPT, Claude, Grok, and DeepSeek), combining real-world user interactions (invivo) with controlled experiments using the same platform's models by their APIs (invitro). We investigate the quality of agentic decisions to invoke Web search, their strategies to formulate queries, the potential domain preferences in the search results they receive, and the choices they make when transforming search results into grounded responses. We find that Web-search decisions vary substantially across platforms and models, while more frequent Web-search invocation does not necessarily yield better response quality. We further show that conversational agents employ different complex querying strategies and that platform specific search engines return search results from their preferred domains. Finally, although responses are largely grounded in search results, some claims rely on uncited search results, raising concerns about attribution and reliability. Our findings have important implications for the design of future AI agents and Web search tools optimized for conversational retrieval.

### 7. AI 智能体理解计算机体系结构吗？（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19387
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：人们越来越多地要求智能体（Agent）设计硬件，也越来越多地看到其取得成功的报道。这类报道只能证明设计得到了改进，却无法证明原因。一个改进了加速器的智能体，可能是在对机器进行推理，也可能只是在一堆从未理解其含义的旋钮上进行熟练搜索——而只有前者才能迁移到下一代体系结构上。现有评估无法区分这两者，因为它们在改变智能体的同时，始终固定问题的呈现框架。我们反其道而行。AutoTuring 让同一个智能体两次面对同一个 15 维加速器空间：一次是以附带模拟器计数器的具名体系结构旋钮呈现，一次是以 [0,1] 区间上的匿名变量呈现，同时评估器、合法空间与可达最优值均保持一致，因此唯一变化的就是这个问题是否有意义。两者之间的差距即是测量结果。在一个包含九个内核的 FP16 GEMM 任务组合上，语义理解是有回报的：架构师智能体平均比建模的 H200 高出 5.4%，比其盲测对应版本高出 12.3%，且模拟器调用次数减少 70.1%。但这种回报并非其独有：一个 critic 循环能为盲测智能体挽回大部分差距，却对架构师智能体毫无助益，因此体系结构知识与结构化批评表现为替代品而非互补品。我们将这些结果作为初步发现报告——在单个建模加速器上每种条件仅运行五到六次——并且我们认为贡献在于这项对比本身，而非该加速器。
- 原文简介：Agents are increasingly asked to design hardware, and increasingly reported to succeed. Such reports establish that a design improved; they cannot establish why. An agent that improves an accelerator may be reasoning about the machine, or may be searching competently over knobs whose meaning it never recovers -- and only the first transfers to the next architecture. Existing evaluations cannot tell the two apart, because they vary the agent while holding the framing of the problem fixed. We do the opposite. AutoTuring hands the same agent the same 15-dimensional accelerator space twice: once as named architectural knobs with simulator counters, once as anonymous variables on [0,1], with the evaluator, the legal space and the reachable optima held identical, so that the only thing that varies is whether the problem means anything. The gap between the two is the measurement. On a nine-kernel FP16 GEMM basket, meaning pays: the architect beats a modeled H200 by 5.4% and its blind counterpart by 12.3% on average, with 70.1% fewer simulator calls. It does not pay uniquely: a critic loop recovers most of that gap for the blind agent and buys the architect nothing, so architectural knowledge and structured critique behave as substitutes rather than as complements. We report these as preliminary findings -- five to six runs per condition on a single modeled accelerator -- and take the comparison itself, not the accelerator, to be the contribution.

### 8. MAGS：多智能体自动形式化保障智能体输出的安全性（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19391
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：LLM 编码智能体如今生成复杂程序的规模已使彻底的人工审查变得日益困难，从而增加了安全与安保故障的风险。常见的方法，包括模糊测试（fuzz testing）、静态分析以及 LLM-as-a-Verifier，能够检测出许多故障，但难以覆盖所有可能的边缘情况。形式化验证通过为指定属性提供机器可检查的保证来解决这一问题，但传统上需要大量的手动规范编写和证明工程。我们提出了一个统一的多智能体框架 MAGS，它能生成具有形式化安全保证的可执行程序，并使用 Dafny 作为具备验证感知能力的中间表示，从而可以机械化地检查安全属性。MAGS 将经人工审核的 API 和安全需求形式化并冻结，将生成的代码翻译为 Dafny，利用验证器反馈修复违规之处，再将通过验证的程序编译回可执行代码。我们在 100 个 CUDA 内核、100 个终端脚本和 20 个机械臂任务上对 MAGS 进行了评估。在全部 220 个示例中，它在生成符合冻结规范并具有非平凡安全保证的程序方面达到了 100% 的成功率。独立的安全性和功能性评估进一步表明，该方法在所有三个领域均表现强劲，同时也揭示出当自动形式化的语义未能完全捕捉目标行为时会出现失败。
- 原文简介：LLM coding agents now generate complex programs at a scale that makes thorough human review increasingly difficult, raising the risk of safety and security failures. Common approaches, including fuzz testing, static analysis, and LLM-as-a-Verifier, can detect many failures but struggle to cover all possible edge cases. Formal verification addresses this by providing machine-checkable guarantees over specified properties, but traditionally demands substantial manual specification and proof engineering. We introduce a unified multi-agent framework, MAGS, that generates executable programs with formal safety guarantees, using Dafny as a verification-aware intermediate representation where safety properties can be mechanically checked. MAGS formalizes and freezes human-audited APIs and safety requirements, translates generated code into Dafny, repairs violations using verifier feedback, and compiles verified programs back into executable code. We evaluate MAGS on 100 CUDA kernels, 100 terminal scripts, and 20 robotic-arm tasks. Across all 220 examples, it achieves a 100% success rate in producing programs with non-trivial safety guarantees against frozen specifications. Independent safety and functional evaluations further show strong performance across all three domains, while revealing failures when the auto-formalized semantics do not fully capture the target behavior.

### 9. 以封闭世界解析对抗 LLM 智能体中的工具幻觉（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19425
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：工具增强的大语言模型（LLM）智能体会以一种现有工具选择或工具安全方法均未涉及的方式失效：它们调用不存在的工具，并传递任何 schema 均未声明的参数。现有防御要么挑选正确的工具（selection），要么约束智能体对真实工具可执行的操作（gating），而这两者都预设了所发出的调用指向的是一个真实存在的工具。我们证明这是一个结构性盲点：幻觉调用从构造上就不属于任何门控所作出的决策，因此没有任何门控能够拒绝它。本文主要是一项测量与基准研究。我们给出了工具幻觉的五类分类法（H1-H5），并作为参照点提出了 Resolution Rung（解析阶梯）：一个免训练的封闭世界解析器（注册表成员资格检查加上签名校验），其意义在于它必须所处的位置，而非它所计算的内容。我们证明幻觉防御必须先于任何因果门控，并刻画了唯一不可消除的残余（借用的参数，其在 schema 上与有效调用无法区分）。在两种调用表面下的十个托管模型上，我们测量到 322 次真实幻觉；伪造工具的调用集中在无约束的原始 JSON 表面上（34 对 3），且模型规模并无帮助（675B 模型与 7-8B 模型表现相当）。随后我们扩展到 Model Context Protocol，其中将多个服务器合并到同一命名空间会创造出单一注册表无法表达的幻觉表面（第二套分类法，M1-M5）；在实际运行的 MCP 表面上我们测量到 154 次幻觉，其中包括在单一注册表表面上表现干净的前沿模型，因为冲突与遮蔽是合并所固有的结构性问题。我们发布了带版本管理的 Hallucinated-Tools Benchmark（HTB），使任何解析器在不同提交之间均可比较。
- 原文简介：Tool-augmented large language model (LLM) agents fail in a way no tool-selection or tool-security method addresses: they call tools that do not exist and pass arguments no schema declares. Existing defenses either pick the right tool (selection) or constrain what an agent may do with real tools (gating), both of which presuppose the emitted call refers to a real tool at all. We show this is a structural blind spot: a hallucinated call is by construction not a decision any gate made, so no gate can reject it. This paper is primarily a measurement and benchmark study. We give a five-class taxonomy of tool hallucination (H1-H5) and, as a reference point, the Resolution Rung: a training-free, closed-world resolver (registry membership plus a signature check) whose interest is where it must sit, not what it computes. We prove hallucination defense must precede any causal gate, and characterize the one irreducible residue (borrowed arguments schema-indistinguishable from a valid call). Across ten hosted models under two invocation surfaces we measure 322 genuine hallucinations; fabricated-tool calls concentrate on the unconstrained raw-JSON surface (34 vs. 3), and model scale does not help (a 675B model matches a 7-8B one). We then extend to the Model Context Protocol, where merging several servers into one namespace creates hallucination surfaces a single registry cannot express (a second taxonomy, M1-M5); on the live MCP surface we measure 154 hallucinations, including from frontier models that were clean on the single-registry surface, because collisions and shadowing are structural to the merge. We release the versioned Hallucinated-Tools Benchmark (HTB) so any resolver is comparable across submissions.

### 10. 目标的语法与语义（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19448
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：在认知科学与计算机科学中，目标被概念化为一种认知状态，它能够与世界知识灵活结合，从而组织和明确有目的的行为。就此而言，目标是组合性表征，其内容与理性行为相关。我们在此提请注意作为表征的目标及其内容，因为这凸显了与认知科学其他领域的一个平行之处——尤其是语言学与逻辑学中的句法—语义接口——同时也突出了关于不同目标表征的表达能力、设计与效率的基础性问题。例如，目标通常被视为固定的，并对期望行为施加约束，但我们也可以识别出目标表征本身所受的约束，例如某个特定的目标语言是否具有足够的表现力来捕捉所关注的行为，或者不同的目标表征是否捕捉到相同的行为。在此，我们综合了旨在刻画不同目标表征特性的研究工作，并指出这些表征只是更广泛设计空间中的一些点。最后，我们讨论了如何通过区分目标的形式与意义来阐明我们对目标所作的隐含假设，为高级认知与动机之间交互作用的研究提供启示，并为不同的目标概念分离出变化的维度。
- 原文简介：In both cognitive science and computer science, goals are conceptualized as cognitive states that flexibly combine with world knowledge to organize and specify purposeful behavior. In this way, goals are compositional representations whose content relates to rational behavior. We here draw attention to goals as representations and their content because it highlights a parallel with other areas in cognitive science - in particular, the syntax-semantics interface in linguistics and logic - while also foregrounding foundational questions about the expressivity, design, and efficiency of different goal representations. For example, goals are typically taken as fixed and imposing constraints on desirable behaviors, but we can also identify constraints on goal representations themselves, such as whether a particular goal language is sufficiently expressive to capture behaviors of interest, or whether different goal representations capture the same behavior. Here, we synthesize work that aims to characterize the properties of different goal representations and suggest these are points of a broader design space. We close by discussing how distinguishing the form and meaning of goals can elucidate the implicit assumptions we make about goals, inform the study of interactions between higher-level cognition and motivation, and isolate axes of variation for different conceptions of goals.

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 10 | 计数 |
| 输入 tokens | 3,420 | GLM usage（精确） |
| 输出 tokens | 11,918 | GLM usage（精确） |
| 合计 tokens | 15,338 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 0 次（限额 60/时，未认证） | 计数 |
| RSS 抓取 | 1 次 | 计数 |
| 总耗时（获取→生成） | 332 秒 | 计时，统计系统占用时间 |
