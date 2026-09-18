# cs.AI updates on arX（2026-09-18）

- 生成时间：2026-09-18 17:59
- 数据来源：RSS 订阅（https://export.arxiv.org/rss/cs.AI，最新 N 条）
- 查询条件：`RSS：https://export.arxiv.org/rss/cs.AI`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 文章 | 发布时间 | 简介 |
|---|---|---|---|
| 1 | [正则化强调式时序差分学习：恒定步长下的稳定性](https://arxiv.org/abs/2609.19170) | 2026-09-18 00:00 | 强调式时序差分学习（ETD）稳定了期望意义下的离策略 TD 更新，并改变了其投影几何，但这两个性质都不能决定恒定步长下的采样动力学。我们构造了一个遍历的两状态反例，其中 ETD 的均值映射是收缩的，而采样乘积却具有正的最 |
| 2 | [BioPhys-Bridge：面向物理支撑型生物学研究中跨学科科学推理…](https://arxiv.org/abs/2609.19180) | 2026-09-18 00:00 | 语言模型在分析跨学科科学研究文献时面临独特的挑战。在生物物理学研究中，忠实的回答需要将观测数据锚定于源证据，通过定量物理模型对其进行解释，并将其与生物学机制联系起来。为应对这一挑战，我们推出了BioPhys-Bridge |
| 3 | [我们对LLM有何期待？LLM基准测试设计图谱](https://arxiv.org/abs/2609.19182) | 2026-09-18 00:00 | 基准测试是评估和传达大语言模型（LLM）进展的核心方式。然而，仅凭模型排名几乎无法揭示评估需求本身是如何变化的。不断扩大的基准测试种类提供了另一个视角：研究人员期待LLM做什么，以及他们将什么视为成功的表现。我们系统性地 |
| 4 | [立场：是时候用自进化操作系统层将基础模型虚拟化了](https://arxiv.org/abs/2609.19203) | 2026-09-18 00:00 | AI应用已从单一、整体式的基础模型（FM）转向复合型智能体系统。然而当今的技术栈仍然碎片化：尽管各类协议（如 MCP、A2A）简化了工具与智能体之间的连接，但每个框架都内嵌了一个隐式的运行时，用于管理状态、记忆、预算和防 |
| 5 | [当前的系统性泛化任务遗漏了什么？一种以推理为中心的分析](https://arxiv.org/abs/2609.19212) | 2026-09-18 00:00 | 系统性泛化，即通过重新组合已知的基本元素来解决新问题的能力，是人类智能的核心，但在受控环境下难以进行严格研究。因此，现有研究依赖于一些简化手段，例如近似线性的动作组合、基于生成性（productivity）的测试以及动作 |
| 6 | [刻画对话式LLM智能体的Web搜索：从搜索决策与策略到搜索结果与回复](https://arxiv.org/abs/2609.19244) | 2026-09-18 00:00 | 对话式LLM智能体日益依赖Web搜索，然而智能体搜索的端到端生命周期仍然鲜为人知。我们首次对四大主流对话平台（ChatGPT、Claude、Grok和DeepSeek）上的Web搜索开展了研究，将真实世界的用户交互（in |
| 7 | [AI 智能体理解计算机体系结构吗？](https://arxiv.org/abs/2609.19387) | 2026-09-18 00:00 | 智能体越来越多地被要求设计硬件，也越来越多地被报道取得成功。这类报告只能证明某项设计得到了改进，却无法证明改进的原因。一个改进了加速器的智能体，可能是在真正对机器进行推理，也可能只是在它从未理解其含义的众多旋钮之间进行熟 |
| 8 | [MAGS：多智能体自动形式化保障智能体输出的安全性](https://arxiv.org/abs/2609.19391) | 2026-09-18 00:00 | LLM 编程智能体如今生成的复杂程序规模庞大，使人工全面审查愈发困难，从而增加了安全与安保故障的风险。常见方法，包括模糊测试、静态分析和 LLM-as-a-Verifier，能够检测出许多故障，但难以覆盖所有可能的边界情 |
| 9 | [针对 LLM 智能体中工具幻觉的封闭世界消解方法](https://arxiv.org/abs/2609.19425) | 2026-09-18 00:00 | 工具增强的大型语言模型（LLM）智能体会以现有工具选择或工具安全方法都无法应对的方式失效：它们调用不存在的工具，并传递任何 schema 都未声明的参数。现有防御机制要么选出正确的工具（选择），要么约束智能体可对真实工具 |
| 10 | [目标的句法与语义](https://arxiv.org/abs/2609.19448) | 2026-09-18 00:00 | 在认知科学和计算机科学中，目标被概念化为一种认知状态，它与世界知识灵活结合，以组织和明确有目的的行为。就此而言，目标是组合性的表征，其内容与理性行为相关。我们在此提请注意作为表征的目标及其内容，因为这凸显了它与认知科学其 |

## 详情

### 1. 正则化强调式时序差分学习：恒定步长下的稳定性（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19170
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：强调式时序差分学习（ETD）稳定了期望意义下的离策略 TD 更新，并改变了其投影几何，但这两个性质都不能决定恒定步长下的采样动力学。我们构造了一个遍历的两状态反例，其中 ETD 的均值映射是收缩的，而采样乘积却具有正的最大李雅普诺夫指数。再生周期分析将这一符号与后续迹（follow-on trace）的无穷方差分离开来。我们提出了正则化强调 TD（RETD），这是一种归一化的一阶冲击后修复机制：它保持迹和重要性比率不变，将强调 TD 信号存储在一个泄漏标量状态中，并释放延迟校正。RETD 的原始平衡点是 ETD 平衡点的仿射平移；单正则化和双正则化读出可精确恢复 ETD 的不动点。我们证明了在调和递减步长下的几乎必然收敛性，并基于马尔可夫随机乘积界给出了一个条件性的恒定步长矩收缩结果。RETD 在两状态构造和某个 Baird 点上具有经认证的负指数，而 Baird 例子上 ETD 的正指数符号仍停留在数值层面。成对的 10,000 次运行实验验证了上述两个分离、不动点恢复、非单调稳定区域以及任务依赖性。RETD 改变的是冲击后动力学；它并不能降低共享的后续迹方差。
- 原文简介：Emphatic temporal-difference learning (ETD) stabilizes the expected off-policy TD update and changes its projection geometry, but neither property determines constant-stepsize sampled dynamics. We construct an ergodic two-state counterexample in which the ETD mean map contracts while the sampled product has a positive top Lyapunov exponent. Regenerative-cycle analysis separates this sign from the infinite variance of the follow-on trace. We introduce regularized emphatic TD (RETD), a normalized first-order post-shock repair that leaves the trace and importance ratios unchanged, stores the emphatic TD signal in a leaky scalar state, and releases a delayed correction. RETD's raw equilibrium is an affine shift of the ETD equilibrium; single- and two-regularization readouts recover the ETD fixed point exactly. We prove almost-sure convergence for harmonic diminishing stepsizes and a conditional constant-stepsize moment-contraction result from a Markovian random-product bound. RETD has certified negative exponents on the two-state construction and one Baird point, whereas the positive Baird ETD sign remains numerical. Paired 10,000-run experiments validate both separations, fixed-point recovery, a nonmonotone stability region, and task dependence. RETD changes post-shock dynamics; it does not reduce the shared follow-on-trace variance.

### 2. BioPhys-Bridge：面向物理支撑型生物学研究中跨学科科学推理的基准（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19180
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：语言模型在分析跨学科科学研究文献时面临独特的挑战。在生物物理学研究中，忠实的回答需要将观测数据锚定于源证据，通过定量物理模型对其进行解释，并将其与生物学机制联系起来。为应对这一挑战，我们推出了BioPhys-Bridge，这是一个新颖的基准数据集，用于对生物物理文献进行基于证据的科学推理。每个案例包含证据块、稳定的证据ID、定量数值、单位、方程、假设、机制和下一步决策，作为问答（QA）和检索增强生成（RAG）的锚定目标。初始版本包含500个案例和1,517个面向智能体的任务，涵盖六个生物学领域和九个物理模型家族，其中包括三个为未来扩展预留的稀疏家族。我们对所有案例在模式、证据完整性、定量锚定、源许可证、查重、单位归一化等方面执行严格的质量关卡，并对81个案例进行了领域专家审查和标注。初步评估显示，DeepSeek-V4-Flash获得了最高的证据ID $F_1$ 分数（0.360），其次是Qwen3.7-Max（0.316）和GPT-4o-mini（0.294）。BioPhys-Bridge是一个跨学科基准，用于评估归因能力、忠实性、幻觉减少以及涉及复杂多步科学推理的生物学实验设计。未来工作将扩大数据集的规模和复杂度，并进行全面评估。代码和数据可在GitHub仓库和Hugging Face上获取。
- 原文简介：Language models face unique challenges in analyzing interdisciplinary scientific research literature. In biophysics research, faithful answers require grounding observed data in source evidence, interpreting it through a quantitative physics model, and linking it to a biological mechanism. To address this challenge, we introduce BioPhys-Bridge, a novel benchmark dataset for evidence-grounded scientific reasoning over biophysical literature. Each case contains evidence blocks, stable evidence IDs, quantitative values, units, equations, assumptions, mechanisms, and next decisions as grounding targets for question answering (QA) and retrieval-augmented generation (RAG). The initial release contains 500 cases, 1,517 agent-facing tasks, and covers six biological domains and nine physical model families, including three sparse families reserved for future expansion. We enforce strict quality gates for all cases in schema, evidence-integrity, quantitative-grounding, source-license, duplicate, unit-normalization, with domain expert review and annotation for 81 cases. Preliminary evaluations show that DeepSeek-V4-Flash obtain the highest evidence-ID $F_1$ score (0.360), followed by Qwen3.7-Max (0.316) and GPT-4o-mini (0.294). BioPhys-Bridge is an interdisciplinary benchmark for evaluating attribution, faithfulness, hallucination reduction, and biological experiment design with complex, multi-step scientific reasoning. Future works will increase the size and complexity of the dataset and perform comprehensive evaluations. Code and data are available in the GitHub repository and on Hugging Face.

### 3. 我们对LLM有何期待？LLM基准测试设计图谱（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19182
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：基准测试是评估和传达大语言模型（LLM）进展的核心方式。然而，仅凭模型排名几乎无法揭示评估需求本身是如何变化的。不断扩大的基准测试种类提供了另一个视角：研究人员期待LLM做什么，以及他们将什么视为成功的表现。我们系统性地梳理了2022年1月至2026年8月间arXiv提交的14,767篇介绍或更新评估资源的论文。通过分阶段筛选和自动化全文编码，我们考察了目标系统与领域、评估材料与条件以及评分机制的变化。该论文集显示出对行动、交互和专业应用日益重视，同时成熟的设计元素与较新的设计元素经常并存。模型的参与发展也不均衡：基于LLM的评分在智能体（agent）组和非智能体组中均有增长，而模型生成的材料在近期批次中未见类似的持续增长。这些发现阐明了公共研究如何将能力期望转化为具体的测试和成功标准。随着AI参与构建测试、执行任务和评判响应，这些发现也提出了一个问题：不断扩大的评估是提供了更多独立的证据，还是有可能复制参与模型自身的偏好和盲点？
- 原文简介：Benchmarks are central to how progress in large language models (LLMs) is assessed and communicated. Yet model rankings alone reveal little about how evaluation requirements themselves are changing. The expanding variety of benchmarks offers another perspective: what researchers expect LLMs to do, and what they count as successful performance. We systematically map 14,767 papers introducing or updating evaluation resources from arXiv submissions between January 2022 and August 2026. Using staged screening and automated full-text coding, we examine changes in target systems and domains, evaluation materials and conditions, and scoring mechanisms. The collection shows growing emphasis on action, interaction, and professional applications, while established and newer design elements frequently coexist. Model participation also develops unevenly: LLM-based scoring grows within both agent and non-agent groups, whereas model-generated materials show no comparable sustained increase in recent cohorts. These findings illuminate how public research translates capability expectations into concrete tests and criteria for success. As AI participates in constructing tests, performing tasks, and judging responses, they also raise a question: does expanding evaluation provide more independent evidence, or risk reproducing the preferences and blind spots of its participating models?

### 4. 立场：是时候用自进化操作系统层将基础模型虚拟化了（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19203
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：AI应用已从单一、整体式的基础模型（FM）转向复合型智能体系统。然而当今的技术栈仍然碎片化：尽管各类协议（如 MCP、A2A）简化了工具与智能体之间的连接，但每个框架都内嵌了一个隐式的运行时，用于管理状态、记忆、预算和防护栏，导致行为不可移植、治理脆弱。这如同操作系统出现之前的计算时代，当时每个程序都需要重新实现基础服务。本立场论文认为，该领域现在需要一个基础模型操作系统（FMOS）——一个将FM交互虚拟化的系统层，其原理类似于虚拟机对物理硬件的抽象，为应用营造出拥有专用、可信且能力实际上无上限的FM实例的假象。在内部，FMOS负责跨记忆层级编排知识、进行模型选择与资源分配，并执行验证与策略管控。如同人脑在快速直觉与慢速深思之间切换，FMOS学习何时介入、何时让推理直接进行，并基于运行经验持续调整其策略。
- 原文简介：AI applications have shifted from single, monolithic foundation models (FM) to compound agentic systems. Yet today's stacks remain fragmented: even as protocols (e.g., MCP, A2A) ease tool/agent connectivity, each framework embeds an implicit runtime for state, memory, budgets, and guardrails, making behavior non-portable and governance brittle. It mirrors computing before operating systems, when every program re-implemented basic services. This position paper argues that the field now needs a Foundation Model Operating System (FMOS) -- a system layer that virtualizes FM interactions analogous to how virtual machines abstract physical hardware, giving applications the illusion of dedicated, trustworthy FM instances with effectively unbounded capabilities. Internally, the FMOS orchestrates knowledge across memory tiers, model selection and resource allocation, and verification and policy enforcement. Like the human brain switching between fast intuition and slow deliberation, the FMOS learns when to intervene and when to let inference proceed directly and continuously adapting its policies based on operational experience.

### 5. 当前的系统性泛化任务遗漏了什么？一种以推理为中心的分析（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19212
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：系统性泛化，即通过重新组合已知的基本元素来解决新问题的能力，是人类智能的核心，但在受控环境下难以进行严格研究。因此，现有研究依赖于一些简化手段，例如近似线性的动作组合、基于生成性（productivity）的测试以及动作显式的目标，这些简化使系统性泛化更易于研究，却遗漏了这一能力的某些本质方面。为了刻画这些简化所遗漏的内容，我们采用以推理为中心的视角，并提出了 TranSGrid——一个在统一任务中融合演绎、归纳和溯因推理的测试平台。在 4,800 个 TranSGrid 实例上对七个 Transformer 进行的实验表明，所有模型在 TranSGrid 上的表现都远差于在留出测试集上的表现：最大的模型解决了测试集中 79.6% 的问题，但在 TranSGrid 上仅解决 55.3%，在最难子集上仅解决 15.8%。该差距在训练长度范围内依然存在，这表明仅凭生成性不足以评估系统性泛化。此外，我们将另外两种简化重新引入 TranSGrid：一种变体使动作近乎线性地组合（降低了归纳需求），另一种使目标动作显式化（降低了溯因需求）。在这两种情况下，解决率都回升至大致相当于测试集的水平，表明任一简化单独就足以将 TranSGrid 降格为普通的留出测试集。综合来看，我们的结果表明，现有任务降低了对归纳、溯因或两者的需求，而要全面衡量系统性泛化，需要一个涉及全部三种推理形式的任务。
- 原文简介：Systematic generalization, the ability to solve novel problems by recombining known atomic elements, is central to human intelligence but difficult to study rigorously under controlled settings. Existing studies therefore rely on simplifications such as approximately linear action composition, productivity-based tests, and action-explicit goals, which make systematic generalization easier to study but omit some essential aspects of this capability. To characterize what these simplifications miss, we adopt a reasoning-centered lens and introduce TranSGrid, a testbed that brings deductive, inductive, and abductive reasoning together within a unified task. Experiments with seven Transformers on 4,800 TranSGrid instances show that all models perform much worse on TranSGrid than on a held-out test set: the largest model solves 79.6% of the test set, but only 55.3% of TranSGrid and 15.8% of the hardest subset. The gap remains within the training length range, showing that productivity alone is not sufficient to evaluate systematic generalization. Additionally, we reintroduce the other two simplifications into TranSGrid: one variant makes actions compose almost linearly (reducing the inductive demand), the other makes goals action-explicit (reducing the abductive one). In both, solve rates return to roughly the test set level, showing that either simplification alone is enough to reduce TranSGrid to an ordinary held-out test set. Together, our results show that existing tasks reduce either or both of the inductive and abductive demands, and that comprehensively measuring systematic generalization requires a task that involves all three forms of reasoning.

### 6. 刻画对话式LLM智能体的Web搜索：从搜索决策与策略到搜索结果与回复（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19244
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：对话式LLM智能体日益依赖Web搜索，然而智能体搜索的端到端生命周期仍然鲜为人知。我们首次对四大主流对话平台（ChatGPT、Claude、Grok和DeepSeek）上的Web搜索开展了研究，将真实世界的用户交互（invivo）与通过API调用同一平台模型进行的受控实验（invitro）相结合。我们研究了智能体调用Web搜索的决策质量、其构建查询的策略、其收到的搜索结果中潜在的域名偏好，以及它们在将搜索结果转化为有据可依的回复时所做的选择。我们发现，Web搜索决策在不同平台和模型之间差异显著，而更频繁地调用Web搜索并不一定能带来更好的回复质量。我们进一步表明，对话式智能体采用各不相同的复杂查询策略，且平台特定的搜索引擎会返回来自其偏好域名的搜索结果。最后，尽管回复在很大程度上以搜索结果为依据，但某些断言却依赖于未被引用的搜索结果，这引发了对归因与可靠性的担忧。我们的发现对未来AI智能体的设计以及针对对话式检索优化的Web搜索工具具有重要意义。
- 原文简介：Conversational LLM agents increasingly rely on Web search, yet the end-to-end lifecycle of agentic search remains poorly understood. We present the first study of Web search across four major conversational platforms (ChatGPT, Claude, Grok, and DeepSeek), combining real-world user interactions (invivo) with controlled experiments using the same platform's models by their APIs (invitro). We investigate the quality of agentic decisions to invoke Web search, their strategies to formulate queries, the potential domain preferences in the search results they receive, and the choices they make when transforming search results into grounded responses. We find that Web-search decisions vary substantially across platforms and models, while more frequent Web-search invocation does not necessarily yield better response quality. We further show that conversational agents employ different complex querying strategies and that platform specific search engines return search results from their preferred domains. Finally, although responses are largely grounded in search results, some claims rely on uncited search results, raising concerns about attribution and reliability. Our findings have important implications for the design of future AI agents and Web search tools optimized for conversational retrieval.

### 7. AI 智能体理解计算机体系结构吗？（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19387
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：智能体越来越多地被要求设计硬件，也越来越多地被报道取得成功。这类报告只能证明某项设计得到了改进，却无法证明改进的原因。一个改进了加速器的智能体，可能是在真正对机器进行推理，也可能只是在它从未理解其含义的众多旋钮之间进行熟练的搜索——而只有前者才能迁移到下一代体系结构上。现有评估无法区分这两种情况，因为它们在改变智能体的同时却固定了问题的表述框架。我们反其道而行之。AutoTuring 将同一个 15 维加速器搜索空间以两种方式交给同一个智能体：一次是以带有模拟器计数器的具名体系结构旋钮形式呈现，一次是以 [0,1] 区间上的匿名变量形式呈现，同时保持评估器、合法空间和可达最优值完全一致，从而使唯一发生变化的，就是这个问题本身是否有意义。两者之间的差距即为测量结果。在一个由九个 kernel 组成的 FP16 GEMM 基准组合上，意义带来了回报：“架构师”版本平均比建模的 H200 快 5.4%，比其“盲测”对应版本快 12.3%，且模拟器调用次数减少 70.1%。但这种回报并非其独有：一个 critic 循环能为盲测智能体挽回大部分差距，却对架构师毫无增益，因此体系结构知识与结构化评论表现为替代品而非互补品。我们将这些作为初步发现报告——在单一建模加速器上每种条件仅运行五到六次——并将这一对比本身（而非该加速器）视为本文的贡献。
- 原文简介：Agents are increasingly asked to design hardware, and increasingly reported to succeed. Such reports establish that a design improved; they cannot establish why. An agent that improves an accelerator may be reasoning about the machine, or may be searching competently over knobs whose meaning it never recovers -- and only the first transfers to the next architecture. Existing evaluations cannot tell the two apart, because they vary the agent while holding the framing of the problem fixed. We do the opposite. AutoTuring hands the same agent the same 15-dimensional accelerator space twice: once as named architectural knobs with simulator counters, once as anonymous variables on [0,1], with the evaluator, the legal space and the reachable optima held identical, so that the only thing that varies is whether the problem means anything. The gap between the two is the measurement. On a nine-kernel FP16 GEMM basket, meaning pays: the architect beats a modeled H200 by 5.4% and its blind counterpart by 12.3% on average, with 70.1% fewer simulator calls. It does not pay uniquely: a critic loop recovers most of that gap for the blind agent and buys the architect nothing, so architectural knowledge and structured critique behave as substitutes rather than as complements. We report these as preliminary findings -- five to six runs per condition on a single modeled accelerator -- and take the comparison itself, not the accelerator, to be the contribution.

### 8. MAGS：多智能体自动形式化保障智能体输出的安全性（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19391
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：LLM 编程智能体如今生成的复杂程序规模庞大，使人工全面审查愈发困难，从而增加了安全与安保故障的风险。常见方法，包括模糊测试、静态分析和 LLM-as-a-Verifier，能够检测出许多故障，但难以覆盖所有可能的边界情况。形式化验证通过为指定属性提供机器可验证的保证来解决这一问题，但传统上需要大量的人工规范编写和证明工程。我们提出了一个统一的多智能体框架 MAGS，它能生成带有形式化安全保证的可执行程序，并使用 Dafny 作为具备验证感知能力的中间表示，在其中安全属性可以被机械化检查。MAGS 对经人工审核的 API 和安全需求进行形式化并冻结，将生成的代码翻译为 Dafny，利用验证器反馈修复违规之处，并将通过验证的程序编译回可执行代码。我们在 100 个 CUDA 内核、100 个终端脚本和 20 个机械臂任务上评估了 MAGS。在全部 220 个示例中，它在针对冻结规范生成具有非平凡安全保证的程序方面均达到 100% 的成功率。独立的安全性和功能性评估进一步表明其在所有三个领域均有强劲表现，同时也揭示了当自动形式化的语义未能完整捕捉目标行为时会出现的失败。
- 原文简介：LLM coding agents now generate complex programs at a scale that makes thorough human review increasingly difficult, raising the risk of safety and security failures. Common approaches, including fuzz testing, static analysis, and LLM-as-a-Verifier, can detect many failures but struggle to cover all possible edge cases. Formal verification addresses this by providing machine-checkable guarantees over specified properties, but traditionally demands substantial manual specification and proof engineering. We introduce a unified multi-agent framework, MAGS, that generates executable programs with formal safety guarantees, using Dafny as a verification-aware intermediate representation where safety properties can be mechanically checked. MAGS formalizes and freezes human-audited APIs and safety requirements, translates generated code into Dafny, repairs violations using verifier feedback, and compiles verified programs back into executable code. We evaluate MAGS on 100 CUDA kernels, 100 terminal scripts, and 20 robotic-arm tasks. Across all 220 examples, it achieves a 100% success rate in producing programs with non-trivial safety guarantees against frozen specifications. Independent safety and functional evaluations further show strong performance across all three domains, while revealing failures when the auto-formalized semantics do not fully capture the target behavior.

### 9. 针对 LLM 智能体中工具幻觉的封闭世界消解方法（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19425
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：工具增强的大型语言模型（LLM）智能体会以现有工具选择或工具安全方法都无法应对的方式失效：它们调用不存在的工具，并传递任何 schema 都未声明的参数。现有防御机制要么选出正确的工具（选择），要么约束智能体可对真实工具执行的操作（门控），而两者都预设了所发出的调用至少指向一个真实存在的工具。我们证明这是一个结构性盲点：幻觉调用在构造上就不属于任何门控做出的决策，因此任何门控都无法将其拒绝。本文主要是一项测量与基准研究。我们给出了工具幻觉的五类分类法（H1-H5），并作为参照点提出了 Resolution Rung：一个免训练的封闭世界消解器（注册表成员检查加签名校验），其价值在于它必须所处的位置，而非它计算的内容。我们证明幻觉防御必须先于任何因果门控，并刻画了唯一不可消减的残余情况（借用参数在 schema 上与有效调用不可区分）。在两个调用表面上的十个托管模型中，我们测量到 322 次真实幻觉；虚构工具的调用集中在无约束的 raw-JSON 表面（34 比 3），且模型规模并无帮助（675B 模型与 7-8B 模型表现相当）。随后我们扩展到 Model Context Protocol，其中将多个服务器合并到一个命名空间会产生单个注册表无法表达的幻觉表面（第二套分类法 M1-M5）；在真实的 MCP 表面上我们测量到 154 次幻觉，其中包括在单一注册表表面上表现干净的前沿模型，因为冲突与遮蔽是合并所固有的结构性问题。我们发布了带版本管理的 Hallucinated-Tools Benchmark（HTB），使任何消解器在不同提交之间均可比较。
- 原文简介：Tool-augmented large language model (LLM) agents fail in a way no tool-selection or tool-security method addresses: they call tools that do not exist and pass arguments no schema declares. Existing defenses either pick the right tool (selection) or constrain what an agent may do with real tools (gating), both of which presuppose the emitted call refers to a real tool at all. We show this is a structural blind spot: a hallucinated call is by construction not a decision any gate made, so no gate can reject it. This paper is primarily a measurement and benchmark study. We give a five-class taxonomy of tool hallucination (H1-H5) and, as a reference point, the Resolution Rung: a training-free, closed-world resolver (registry membership plus a signature check) whose interest is where it must sit, not what it computes. We prove hallucination defense must precede any causal gate, and characterize the one irreducible residue (borrowed arguments schema-indistinguishable from a valid call). Across ten hosted models under two invocation surfaces we measure 322 genuine hallucinations; fabricated-tool calls concentrate on the unconstrained raw-JSON surface (34 vs. 3), and model scale does not help (a 675B model matches a 7-8B one). We then extend to the Model Context Protocol, where merging several servers into one namespace creates hallucination surfaces a single registry cannot express (a second taxonomy, M1-M5); on the live MCP surface we measure 154 hallucinations, including from frontier models that were clean on the single-registry surface, because collisions and shadowing are structural to the merge. We release the versioned Hallucinated-Tools Benchmark (HTB) so any resolver is comparable across submissions.

### 10. 目标的句法与语义（2026-09-18 00:00）

- 链接：https://arxiv.org/abs/2609.19448
- 主题：
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：在认知科学和计算机科学中，目标被概念化为一种认知状态，它与世界知识灵活结合，以组织和明确有目的的行为。就此而言，目标是组合性的表征，其内容与理性行为相关。我们在此提请注意作为表征的目标及其内容，因为这凸显了它与认知科学其他领域的平行关系——尤其是语言学和逻辑学中的句法-语义界面——同时也突出了关于不同目标表征的表达力、设计与效率的基础性问题。例如，目标通常被视为固定的，并对理想行为施加约束，但我们也可以识别目标表征自身所受的约束，例如某一特定的目标语言是否具有足够的表达力来刻画感兴趣的行为，或者不同的目标表征是否刻画了相同的行为。在此，我们综合了旨在刻画不同目标表征属性的相关研究，并指出这些表征只是更广泛设计空间中的一些点。最后，我们讨论了区分目标的形式与意义如何能够阐明我们对目标所持的隐含假设，为高级认知与动机之间交互作用的研究提供启示，并为不同的目标概念分离出变化的维度。
- 原文简介：In both cognitive science and computer science, goals are conceptualized as cognitive states that flexibly combine with world knowledge to organize and specify purposeful behavior. In this way, goals are compositional representations whose content relates to rational behavior. We here draw attention to goals as representations and their content because it highlights a parallel with other areas in cognitive science - in particular, the syntax-semantics interface in linguistics and logic - while also foregrounding foundational questions about the expressivity, design, and efficiency of different goal representations. For example, goals are typically taken as fixed and imposing constraints on desirable behaviors, but we can also identify constraints on goal representations themselves, such as whether a particular goal language is sufficiently expressive to capture behaviors of interest, or whether different goal representations capture the same behavior. Here, we synthesize work that aims to characterize the properties of different goal representations and suggest these are points of a broader design space. We close by discussing how distinguishing the form and meaning of goals can elucidate the implicit assumptions we make about goals, inform the study of interactions between higher-level cognition and motivation, and isolate axes of variation for different conceptions of goals.

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 10 | 计数 |
| 输入 tokens | 3,420 | GLM usage（精确） |
| 输出 tokens | 11,568 | GLM usage（精确） |
| 合计 tokens | 14,988 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 0 次（限额 60/时，未认证） | 计数 |
| RSS 抓取 | 1 次 | 计数 |
| 总耗时（获取→生成） | 388 秒 | 计时，统计系统占用时间 |
