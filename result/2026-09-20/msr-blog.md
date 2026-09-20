# Microsoft Research（2026-09-20）

- 生成时间：2026-09-20 10:48
- 数据来源：RSS 订阅（https://www.microsoft.com/en-us/research/feed/，最新 N 条）
- 查询条件：`RSS：https://www.microsoft.com/en-us/research/feed/`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 文章 | 发布时间 | 简介 |
|---|---|---|---|
| 1 | [GigaPath-Flash and GigaTIME-Flash: …](https://www.microsoft.com/en-us/research/blog/gigapath-flash-and-gigatime-flash-toward-population-scale-discovery-with-efficient-pathology-foundation-models/) | 2026-08-31 16:00 | 如果病理学基础模型能以更少的资源做更多的事情，会怎样？GigaPath-Flash 和 GigaTIME-Flash 在保持强大性能的同时降低了计算需求，为更大规模的研究和更广泛的探索打开了大门。本文《GigaPath- |
| 2 | [Broadening access to Skala creates …](https://www.microsoft.com/en-us/research/blog/broadening-access-to-skala-creates-a-faster-path-to-predictive-dft/) | 2026-08-20 16:00 | Skala 1.1 是 Microsoft Research 推出的深度学习交换相关泛函的更新版本，它带来了更高的精度、在整个计算化学生态系统中更广泛的可及性，以及一个用于追踪计算性能的动态基准。本文《扩大 Skala  |
| 3 | [MindTopo reveals VLMs’ spatial reas…](https://www.microsoft.com/en-us/research/blog/mindtopo-reveals-vlms-spatial-reasoning-abilities/) | 2026-08-12 16:00 | 一条路径、一道栅栏、一个绳结。MindTopo 为测试 AI 如何理解拓扑关系设立了新基准，并凸显了加强空间推理与规划能力的新机遇。《MindTopo 揭示 VLM 的空间推理能力》一文首发于 Microsoft Res |
| 4 | [Introducing CARE-X: Towards Clinica…](https://www.microsoft.com/en-us/research/blog/introducing-care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement/) | 2026-08-11 16:00 | 放射学 AI 正在超越报告生成而不断演进。CARE-X 探索了一种统一的方法，将灵活推理、经校准的预测与基于测量的工具相结合，用于胸部 X 光片判读。本文《CARE-X 亮相：借助辅助监督、奖励对齐学习与工具增强测量，迈 |
| 5 | [Orchard: An open framework for scal…](https://www.microsoft.com/en-us/research/blog/orchard-an-open-framework-for-scalable-agentic-ai/) | 2026-08-03 16:00 | Orchard 是一个面向研究社区的开源框架，用于跨任务类型训练和评估 AI 智能体。它降低了复杂性，同时通过让研究人员复用相同的基础设施，使较小的模型也能实现强大性能。本文《Orchard：用于可扩展智能体 AI 的开 |
| 6 | [Echoverse: Deep, evolving environme…](https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents/) | 2026-07-30 17:00 | 计算机操作 AI 智能体在处理电子邮件、客户支持等多步骤工作流时表现不佳。Echoverse 通过在真实环境中训练智能体，而非仅仅提供更多训练任务，帮助它们随着任务、测试和环境的演进不断提升。本文《Echoverse：面 |
| 7 | [EvoLib: Turning experience into evo…](https://www.microsoft.com/en-us/research/blog/evolib-turning-experience-into-evolving-knowledge/) | 2026-07-30 16:00 | LLM 并不会仅仅因为记住更多内容就变得更聪明。EvoLib 将经验转化为不断演进的知识，从中提取可复用的技能与洞察，帮助模型在部署之后的很长时间里跨任务进行学习与适应。本文《EvoLib：将经验转化为不断演进的知识》最 |
| 8 | [Verifying Rust cryptography in SymC…](https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/) | 2026-07-13 16:00 | 密码学代码为现代计算系统提供了至关重要的保护。了解一种新方法如何帮助开发者在编写代码的同时对其进行验证，并在代码实现和演进的过程中保持速度与灵活性。本文《在 SymCrypt 中验证 Rust 密码学实现：从标准到代码》 |
| 9 | [Aurora 1.5: Extending open foundati…](https://www.microsoft.com/en-us/research/blog/aurora-1-5-extending-open-foundation-models-for-weather-and-earth-system-applications/) | 2026-07-09 16:46 | Aurora 1.5 在 Aurora 基础模型的基础上新增了 22 个变量、小时级时间分辨率以及概率集合预报，使其在真实的天气、气候和能源应用中更加实用。本文《Aurora 1.5：扩展面向天气和地球系统应用的开放基础 |
| 10 | [Flint: A visualization language for…](https://www.microsoft.com/en-us/research/blog/flint-a-visualization-language-for-the-ai-era/) | 2026-07-08 16:00 | 简短的图表规范易于编写，但往往产生平淡乏味的结果。Flint 是一款开源可视化语言，提供了一条折中之路，让 AI 智能体能够基于紧凑且易于人工编辑的规范创建富有表现力的图表。本文《Flint：AI 时代的可视化语言》最先 |

## 详情

### 1. GigaPath-Flash and GigaTIME-Flash: Toward population-scale discovery with efficient pathology foundation models（2026-08-31 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/gigapath-flash-and-gigatime-flash-toward-population-scale-discovery-with-efficient-pathology-foundation-models/
- 主题：
- 最近推送：2026-08-31
- 摘要来源：feed | 翻译：llm
- 中文简介：如果病理学基础模型能以更少的资源做更多的事情，会怎样？GigaPath-Flash 和 GigaTIME-Flash 在保持强大性能的同时降低了计算需求，为更大规模的研究和更广泛的探索打开了大门。本文《GigaPath-Flash 与 GigaTIME-Flash：借助高效病理学基础模型迈向人群规模的科学发现》最先发布于 Microsoft Research。
- 原文简介：What if pathology foundation models could do more with less? GigaPath-Flash and GigaTIME-Flash cut computational demands while maintaining strong performance, opening the door to larger studies and broader exploration. The post GigaPath-Flash and GigaTIME-Flash: Toward population-scale discovery with efficient pathology foundation models appeared first on Microsoft Research .

### 2. Broadening access to Skala creates a faster path to predictive DFT（2026-08-20 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/broadening-access-to-skala-creates-a-faster-path-to-predictive-dft/
- 主题：
- 最近推送：2026-08-20
- 摘要来源：feed | 翻译：llm
- 中文简介：Skala 1.1 是 Microsoft Research 推出的深度学习交换相关泛函的更新版本，它带来了更高的精度、在整个计算化学生态系统中更广泛的可及性，以及一个用于追踪计算性能的动态基准。本文《扩大 Skala 的开放范围，为预测性 DFT 开辟更快路径》最先发表于 Microsoft Research。
- 原文简介：Skala 1.1, the updated deep-learning exchange-correlation functional from Microsoft Research, provides greater accuracy, expanded accessibility across the computational chemistry ecosystem, and a living benchmark to track computational performance. The post Broadening access to Skala creates a faster path to predictive DFT appeared first on Microsoft Research .

### 3. MindTopo reveals VLMs’ spatial reasoning abilities（2026-08-12 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/mindtopo-reveals-vlms-spatial-reasoning-abilities/
- 主题：
- 最近推送：2026-08-12
- 摘要来源：feed | 翻译：llm
- 中文简介：一条路径、一道栅栏、一个绳结。MindTopo 为测试 AI 如何理解拓扑关系设立了新基准，并凸显了加强空间推理与规划能力的新机遇。《MindTopo 揭示 VLM 的空间推理能力》一文首发于 Microsoft Research。
- 原文简介：A path, a fence, a knot. MindTopo sets a new benchmark for testing how AI understands topological relationships and highlights new opportunities to strengthen spatial reasoning and planning. The post MindTopo reveals VLMs&#8217; spatial reasoning abilities appeared first on Microsoft Research .

### 4. Introducing CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement（2026-08-11 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/introducing-care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement/
- 主题：
- 最近推送：2026-08-11
- 摘要来源：feed | 翻译：llm
- 中文简介：放射学 AI 正在超越报告生成而不断演进。CARE-X 探索了一种统一的方法，将灵活推理、经校准的预测与基于测量的工具相结合，用于胸部 X 光片判读。本文《CARE-X 亮相：借助辅助监督、奖励对齐学习与工具增强测量，迈向临床实用的放射学 VLM》最先发布于 Microsoft Research（微软研究院）。
- 原文简介：Radiology AI is evolving beyond report generation. CARE-X explores a unified approach that combines flexible reasoning, calibrated predictions, and measurement-based tools for chest X-ray interpretation. The post Introducing CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement appeared first on Microsoft Research .

### 5. Orchard: An open framework for scalable agentic AI（2026-08-03 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/orchard-an-open-framework-for-scalable-agentic-ai/
- 主题：
- 最近推送：2026-08-03
- 摘要来源：feed | 翻译：llm
- 中文简介：Orchard 是一个面向研究社区的开源框架，用于跨任务类型训练和评估 AI 智能体。它降低了复杂性，同时通过让研究人员复用相同的基础设施，使较小的模型也能实现强大性能。本文《Orchard：用于可扩展智能体 AI 的开放框架》最先发布于 Microsoft Research。
- 原文简介：Orchard is an open-source framework for the research community to train and evaluate AI agents across task types. It reduces complexity while supporting strong performance from smaller models by enabling researchers to reuse the same infrastructure. The post Orchard: An open framework for scalable agentic AI appeared first on Microsoft Research .

### 6. Echoverse: Deep, evolving environments for computer-use agents（2026-07-30 17:00）

- 链接：https://www.microsoft.com/en-us/research/blog/echoverse-deep-evolving-environments-for-computer-use-agents/
- 主题：
- 最近推送：2026-07-30
- 摘要来源：feed | 翻译：llm
- 中文简介：计算机操作 AI 智能体在处理电子邮件、客户支持等多步骤工作流时表现不佳。Echoverse 通过在真实环境中训练智能体，而非仅仅提供更多训练任务，帮助它们随着任务、测试和环境的演进不断提升。本文《Echoverse：面向计算机操作智能体的深度、持续演进的环境》最先发布于 Microsoft Research。
- 原文简介：Computer-use AI agents struggle with multi-step workflows like email and customer support. Echoverse trains agents in realistic environments rather than simply providing more training tasks, helping them improve as the tasks, tests, and environments evolve. The post Echoverse: Deep, evolving environments for computer-use agents appeared first on Microsoft Research .

### 7. EvoLib: Turning experience into evolving knowledge（2026-07-30 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/evolib-turning-experience-into-evolving-knowledge/
- 主题：
- 最近推送：2026-07-30
- 摘要来源：feed | 翻译：llm
- 中文简介：LLM 并不会仅仅因为记住更多内容就变得更聪明。EvoLib 将经验转化为不断演进的知识，从中提取可复用的技能与洞察，帮助模型在部署之后的很长时间里跨任务进行学习与适应。本文《EvoLib：将经验转化为不断演进的知识》最先发布于 Microsoft Research。
- 原文简介：LLMs do not get smarter just by remembering more. EvoLib turns experience into evolving knowledge, taking reusable skills and insights that help models learn and adapt across tasks long after deployment. The post EvoLib: Turning experience into evolving knowledge appeared first on Microsoft Research .

### 8. Verifying Rust cryptography in SymCrypt, from standards to code（2026-07-13 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/verifying-rust-cryptography-in-symcrypt-from-standards-to-code/
- 主题：
- 最近推送：2026-07-13
- 摘要来源：feed | 翻译：llm
- 中文简介：密码学代码为现代计算系统提供了至关重要的保护。了解一种新方法如何帮助开发者在编写代码的同时对其进行验证，并在代码实现和演进的过程中保持速度与灵活性。本文《在 SymCrypt 中验证 Rust 密码学实现：从标准到代码》最初发布于 Microsoft Research。
- 原文简介：Cryptographic code supports vital protections in modern computing systems. Learn how a new method helps verify code as developers write it while preserving speed and adaptability as it gets implemented and evolves. The post Verifying Rust cryptography in SymCrypt, from standards to code appeared first on Microsoft Research .

### 9. Aurora 1.5: Extending open foundation models for weather and Earth-system applications（2026-07-09 16:46）

- 链接：https://www.microsoft.com/en-us/research/blog/aurora-1-5-extending-open-foundation-models-for-weather-and-earth-system-applications/
- 主题：
- 最近推送：2026-07-09
- 摘要来源：feed | 翻译：llm
- 中文简介：Aurora 1.5 在 Aurora 基础模型的基础上新增了 22 个变量、小时级时间分辨率以及概率集合预报，使其在真实的天气、气候和能源应用中更加实用。本文《Aurora 1.5：扩展面向天气和地球系统应用的开放基础模型》最先发布于 Microsoft Research。
- 原文简介：Aurora 1.5 adds 22 more variables, hourly temporal resolution, and probabilistic ensemble forecasting to the Aurora foundation model, making it more useful for real-world weather, climate, and energy applications. The post Aurora 1.5: Extending open foundation models for weather and Earth-system applications appeared first on Microsoft Research .

### 10. Flint: A visualization language for the AI era（2026-07-08 16:00）

- 链接：https://www.microsoft.com/en-us/research/blog/flint-a-visualization-language-for-the-ai-era/
- 主题：
- 最近推送：2026-07-08
- 摘要来源：feed | 翻译：llm
- 中文简介：简短的图表规范易于编写，但往往产生平淡乏味的结果。Flint 是一款开源可视化语言，提供了一条折中之路，让 AI 智能体能够基于紧凑且易于人工编辑的规范创建富有表现力的图表。本文《Flint：AI 时代的可视化语言》最先发布于 Microsoft Research。
- 原文简介：Short chart specifications are easy to write, but often produce uninspiring results. Flint is an open-source visualization language that offers a middle path, letting AI agents create expressive charts from compact, human-editable specifications. The post Flint: A visualization language for the AI era appeared first on Microsoft Research .

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 0 | 计数 |
| 输入 tokens | 0 | GLM usage（精确） |
| 输出 tokens | 0 | GLM usage（精确） |
| 合计 tokens | 0 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 0 次（限额 60/时，未认证） | 计数 |
| RSS 抓取 | 1 次 | 计数 |
| 总耗时（获取→生成） | 13 秒 | 计时，统计系统占用时间 |
