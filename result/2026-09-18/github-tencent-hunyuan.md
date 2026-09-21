# GitHub 热门项目（github-tencent-hunyuan · 2026-09-18）

- 生成时间：2026-09-18 19:38
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`user:Tencent-Hunyuan pushed:>2026-08-19`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [Tencent-Hunyuan/HunyuanOCR](https://github.com/Tencent-Hunyuan/HunyuanOCR) | 2,007 | Python | HunyuanOCR-1.5：让轻量级 OCR VLM 更快更好 |
| 2 | [Tencent-Hunyuan/AuK](https://github.com/Tencent-Hunyuan/AuK) | 1,099 | Python | AuK：开源语音生成与编辑基础模型 |
| 3 | [Tencent-Hunyuan/UniRL](https://github.com/Tencent-Hunyuan/UniRL) | 966 | Python | UniRL 是一个面向统一多模态模型强化学习的框架。 |
| 4 | [Tencent-Hunyuan/Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2) | 620 | Python | 中文&nbsp;｜&nbsp;中文 |
| 5 | [Tencent-Hunyuan/Hy4-preview](https://github.com/Tencent-Hunyuan/Hy4-preview) | 381 | Python | 中文 &nbsp;｜&nbsp;English |
| 6 | [Tencent-Hunyuan/Simple-Attention-Sp…](https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification) | 59 | Python | 我们研究论文《SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking》的代码 |
| 7 | [Tencent-Hunyuan/evolve-scaler](https://github.com/Tencent-Hunyuan/evolve-scaler) | 3 | HTML | 论文《EvolveScaler：通过可执行状态机与自然语言渲染合成信息演化语境》的 GitHub 页面 |

## 详情

### 1. Tencent-Hunyuan/HunyuanOCR（2,007★）

- 链接：https://github.com/Tencent-Hunyuan/HunyuanOCR
- 主题：
- 最近推送：2026-09-13
- 摘要来源：readme_head | 翻译：llm
- 中文简介：HunyuanOCR-1.5：让轻量级 OCR VLM 更快更好 🤗 HF 模型   | 📄 论文 > [!NOTE] > 👉 想找 **HunyuanOCR-1.0** 的原始发布版？请切换到 [`v1.0`](https://github.com/Tencent-Hunyuan/HunyuanOCR/tree/v1.0) 分支，或阅读 [`README_v1.0.md`](./HunyuanOCR_v1.0/README_v1.0.md) · [`README_zh_v1.0.md`](./HunyuanOCR_v1.0/README_zh_v1.0.md)。 - **[2026/07/24]** 🚀 我们进一步开源了 HunyuanOCR-1.5 的**统一推理环境**（见 [`docs/inference/inference.md`](docs/inference/inference.md)）以及**基于 verl 的强化学习训练栈**（见 [`train_verl/README_en.md`](train_verl/README_en.md)）。 - **[2026/07/13]** 📊 我们开源了 [**CHAOS-Bench**](./benchmarks/CHAOS-Bench)，这是一个字符级幻觉评测基准，通过向学术论文图像中注入字符级扰动，来考察 OCR VLM 的“眼见为实”能力。 - **[2026/07/07]** 🚀 我们发布了 **HunyuanOCR-1.5**，这是一次系统性升级，借助 DFlash 投机解码、PC 端 llama.cpp 部署、Agentic Data Flow 以及升级后的训练配方，使轻量级端到端 OCR 更快更好。欢迎查阅[论文](https://arxiv.org/pdf/2607.04884)。 - **[2026/06/18]** 🎉 我们的表格解析工作被 ECCV 2026 主会接收！欢迎查阅论文：[StrucTab: A Structured Optimization Framework for Table Parsing](https://arxiv.org/abs/2606.29905)。 - **[2026/06/02]** 🎉 我们发布了两个新评测基准。[Chronicles-OCR](https://github.com/VirtualLUOUCAS/Chronicles-OCR)（[arXiv](https://arxiv.org/abs/2605.11960)）是一个开源的古文字感知评测基准，涵盖“汉字七体”的演变轨迹，由 **SSV 数字文化实验室**与 **SSV 技术架构部**联合**故宫博物院**和**安阳师范学院**共同构建。我们还发布了 [ChartArena](https://github.com/pspdada/ChartArena)（[arXiv](https://arxiv.org/abs/2606.01348)），一个支持多种图表类型的新型图表解析评测基准。欢迎大家评测并提供宝贵反馈！
- 原文简介：HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better 🤗 HF Model   | 📄 Paper > [!NOTE] > 👉 Looking for the original **HunyuanOCR-1.0** release? Switch to the [`v1.0`](https://github.com/Tencent-Hunyuan/HunyuanOCR/tree/v1.0) branch, or read [`README_v1.0.md`](./HunyuanOCR_v1.0/README_v1.0.md) · [`README_zh_v1.0.md`](./HunyuanOCR_v1.0/README_zh_v1.0.md)。 - **[2026/07/24]** 🚀 We further open-sourced the **unified inference environment** (see [`docs/inference/inference.md`](docs/inference/inference.md)) and the **verl-based reinforcement learning stack** for HunyuanOCR-1.5 (see [`train_verl/README_en.md`](train_verl/README_en.md)). - **[2026/07/13]** 📊 We open-sourced [**CHAOS-Bench**](./benchmarks/CHAOS-Bench), a character-level hallucination benchmark that probes the "seeing-is-believing" ability of OCR VLMs by injecting character-level corruptions into academic-paper images. - **[2026/07/07]** 🚀 We released **HunyuanOCR-1.5**, a systematic upgrade that makes lightweight end-to-end OCR **faster and better** via DFlash speculative decoding, PC-side llama.cpp deployment, an Agentic Data Flow, and an upgraded training recipe. Check out the [paper](https://arxiv.org/pdf/2607.04884). - **[2026/06/18]** 🎉 Our work on table parsing has been accepted to the ECCV 2026 Main Conference! Check out the paper: [StrucTab: A Structured Optimization Framework for Table Parsing](https://arxiv.org/abs/2606.29905). - **[2026/06/02]** 🎉 We have released two new benchmarks. [Chronicles-OCR](https://github.com/VirtualLUOUCAS/Chronicles-OCR) ([arXiv](https://arxiv.org/abs/2605.11960)), an open-source ancient-text perception benchmark covering the evolutionary trajectory of the "Seven Chinese Scripts", is jointly built by the **SSV Digital Culture Lab** and the **SSV Technical Architecture Department**, together with the **Palace Museum** and **Anyang Normal University**. We have also released [ChartArena](https://github.com/pspdada/ChartArena) ([arXiv](https://arxiv.org/abs/2606.01348)), a new chart-parsing benchmark supporting diverse chart types. Welcome to evaluate and provide your valuable feedback!

### 2. Tencent-Hunyuan/AuK（1,099★）

- 链接：https://github.com/Tencent-Hunyuan/AuK
- 主题：deep-learning, foundation-models, python, pytorch, separation, speaker-extraction, speech, speech-editing
- 最近推送：2026-09-16
- 摘要来源：readme_head | 翻译：llm
- 中文简介：AuK：开源语音生成与编辑基础模型 💻 欢迎在 [HuggingFace Space](https://huggingface.co/spaces/tencent/AuK) · [ModelScope Space](https://modelscope.cn/studios/Tencent-Hunyuan/AuK) 上试用我们的模型！ - **[2026/09/16]** 💻 编码器内存占用降低约 **7.5 GiB**，让**消费级 GPU** 上的本地推理更加触手可及。详见 [PR #19](https://github.com/Tencent-Hunyuan/AuK/pull/19)。 - **[2026/09/13]** 🍎🖥️ **AuK** 现已正式支持 **Apple Silicon 上的 MLX 推理**（可在 [feat/mlx-apple-silicon](https://github.com/Tencent-Hunyuan/AuK/tree/feat/mlx-apple-silicon) 分支获取）以及 **CUDA 推理的 CPU offload**。 - **[2026/09/13]** 🏆 **AuK** 担任 [ICASSP 2027 音频编辑挑战赛](https://audio-editing-challenge.github.io/) **Single Model Track（单模型赛道）** 的端到端基线模型。 - **[2026/09/09]** 🙌 感谢 **SGLang-Omni** 在发布首日（Day 0）即支持 **AuK** 与 **AuK-Flash**！请查看 [SGLang-Omni cookbook](https://sgl-project.github.io/sglang-omni/cookbook/auk.html) 快速上手。 - **[2026/09/09]** 🎉 我们正式开源 **AuK**。代码与模型权重均已公开发布。欢迎在 [🤗 Demo Space](https://huggingface.co/spaces/tencent/AuK) 或 [🤖 ModelScope Space](https://modelscope.cn/studios/Tencent-Hunyuan/AuK) 上试用！ 英文 https://github.com/user-attachments/assets/d07332fc-5f69-4f16-9d00-a7443cc19e6a 中文 https://github.com/user-attachments/assets/c532bbdb-e6ce-4434-a9a5-16f29a8d4135 - [最新动态](#news) - [简介](#introduction) - [性能](#performance) - [模型架构](#model-architecture) - [支持的任务](#supported-tasks)
- 原文简介：AuK: An Open-Source Foundational Model for Speech Generation and Editing 💻 Try our model on the  HuggingFace Space  ·  ModelScope Space ! - **[2026/09/16]** 💻 Reduced encoder memory by **~7.5 GiB**, making local inference more accessible on **consumer GPUs**. See [PR #19](https://github.com/Tencent-Hunyuan/AuK/pull/19). - **[2026/09/13]** 🍎🖥️ **AuK** now officially supports **MLX inference on Apple Silicon** (available on the [feat/mlx-apple-silicon](https://github.com/Tencent-Hunyuan/AuK/tree/feat/mlx-apple-silicon) branch) and **CPU offload for CUDA inference**. - **[2026/09/13]** 🏆 **AuK** serves as the end-to-end baseline for the **Single Model Track** of the [ICASSP 2027 Audio Editing Challenge](https://audio-editing-challenge.github.io/). - **[2026/09/09]** 🙌 Thanks to **SGLang-Omni** for Day 0 support for **AuK** and **AuK-Flash**! Check out the [SGLang-Omni cookbook](https://sgl-project.github.io/sglang-omni/cookbook/auk.html) to get started. - **[2026/09/09]** 🎉 We open-source **AuK**. Code and model weights are publicly available. Try it on the [🤗 Demo Space](https://huggingface.co/spaces/tencent/AuK) or the [🤖 ModelScope Space](https://modelscope.cn/studios/Tencent-Hunyuan/AuK)! English https://github.com/user-attachments/assets/d07332fc-5f69-4f16-9d00-a7443cc19e6a 中文 https://github.com/user-attachments/assets/c532bbdb-e6ce-4434-a9a5-16f29a8d4135 - [News](#news) - [Introduction](#introduction) - [Performance](#performance) - [Model Architecture](#model-architecture) - [Supported Tasks](#supported-tasks)

### 3. Tencent-Hunyuan/UniRL（966★）

- 链接：https://github.com/Tencent-Hunyuan/UniRL
- 主题：ai-infrastructure, reinforcement-learning, sglang, vllm
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：UniRL 是一个面向统一多模态模型强化学习的框架。  UniRL 将同一套 RL 后训练循环——生成样本、对其打分、计算优势、更新策略，并将权重同步回 rollout worker——应用于多模态模型家族。  UniRL 是一个分层、可组合的系统。每个 **entrypoint**（`train_diffusion`、`train_ar`、`train_pe`、`train_unified_model`）加载一份覆盖模型、算法、rollout、奖励、placement 和同步的 **Hydra 示例配置**，然后创建对应的领域 **trainer**（`DiffusionTrainer`、`ARTrainer`、`PETrainer`、`UnifiedModelTrainer`）。trainer 在可插拔的 **rollout 引擎**、**算法**、**模型捆绑包**、**奖励服务**以及共享的**分布式运行时**之间协调 RL 循环：Ray `DevicePool`、FSDP、Transfer Queue（TQ）以及 LoRA/全权重同步。运行时循环、部署模式和模块映射请参见 [`unirl/README.md`](unirl/README.md)。  agentic entrypoint 在 AR 路径的基础上扩展了多轮工具交互。它将每一轮保留为 `Sample` 血缘（lineage），通过奖励服务对最终答案打分，并在共置（colocated）的 rollout 屏障处进行训练。
- 原文简介：UniRL is a Framework for Unified Multimodal Model Reinforcement Learning UniRL applies one RL post-training loop — generate samples, score them, compute advantages, update the policy, and sync weights back to rollout workers — across multimodal model families. UniRL is a layered, composable system. Each **entrypoint** (`train_diffusion`, `train_ar`, `train_pe`, `train_unified_model`) loads a **Hydra example config** covering model, algorithm, rollout, reward, placement, and sync, then creates the matching domain **trainer** (`DiffusionTrainer`, `ARTrainer`, `PETrainer`, `UnifiedModelTrainer`). The trainer coordinates the RL loop across pluggable **rollout engines**, **algorithms**, **model bundles**, **reward services**, and the shared **distributed runtime**: Ray `DevicePool`, FSDP, Transfer Queue (TQ), and LoRA/full-weight sync. See [`unirl/README.md`](unirl/README.md) for the runtime loop, deployment modes, and module map. The agentic entrypoint extends the AR path with multi-turn tool interaction. It preserves each turn as a `Sample` lineage, scores terminal answers through a reward service, and trains at a colocated rollout barrier.

### 4. Tencent-Hunyuan/Hy-MT2（620★）

- 链接：https://github.com/Tencent-Hunyuan/Hy-MT2
- 主题：
- 最近推送：2026-08-26
- 摘要来源：readme_head | 翻译：llm
- 中文简介：中文&nbsp;｜&nbsp;中文 &nbsp;&nbsp; 🖥️&nbsp;  官方网站  &nbsp;&nbsp;|&nbsp;&nbsp; 💬&nbsp;  GitHub  &nbsp;&nbsp;|&nbsp;&nbsp; 🪡&nbsp;  AngelSlim  &nbsp;&nbsp;|&nbsp;&nbsp; 📚&nbsp;  Hy-MT2 技术报告 Hy-MT2 是一系列专为复杂真实场景设计的“快思考”多语言翻译模型，包含 1.8B、7B 和 30B-A3B（MoE）三种模型规格，均支持 33 种语言之间的互译，并能有效遵循多种语言的翻译指令。 在端侧部署方面，AngelSlim 1.25-bit 极限量化将 1.8B 模型的存储需求降至仅 440 MB，并将推理速度提升 1.5 倍。 多维度评测显示，Hy-MT2 在通用、真实业务、领域专用及指令遵循等翻译任务上均有出色表现。7B 和 30B-A3B 模型在快思考模式下超越了 DeepSeek-V4-Pro、Kimi K2.6 等开源模型，轻量级的 1.8B 模型也在整体上超越了 Microsoft、豆包等厂商的主流商用 API。 在本次发布中，我们还开源了 [IFMTBench](./IFMTBench/README.md)，一个用于评估翻译指令遵循能力的基准测试。 我们也欢迎大家使用我们发布的 Hy-MT2-Translator Skill，它可以便捷地将 Hy-MT2 系列模型集成到翻译任务中。下载链接：[ClawHub](https://clawhub.ai/tencent-adm/hy-mt2-translator-skill) 和 [SkillHub](https://skillhub.cn/skills/hy-mt2-translator)。
- 原文简介：English&nbsp;｜&nbsp; 中文 &nbsp;&nbsp; 🖥️&nbsp;  Official Website  &nbsp;&nbsp;|&nbsp;&nbsp; 💬&nbsp;  GitHub  &nbsp;&nbsp;|&nbsp;&nbsp; 🪡&nbsp;  AngelSlim  &nbsp;&nbsp;|&nbsp;&nbsp; 📚&nbsp;  Hy-MT2 Report Hy-MT2 is a family of “fast-thinking” multilingual translation models designed for complex real-world scenarios. It includes three model sizes: 1.8B, 7B, and 30B-A3B (MoE), all of which support translation among 33 languages and effectively follow translation instructions in multiple languages. For on-device deployment, AngelSlim 1.25-bit extreme quantization reduces the storage requirement of the 1.8B model to only 440 MB and improves inference speed by 1.5x. Multi-dimensional evaluations show that Hy-MT2 delivers outstanding performance across general, real-world business, domain-specific, and instruction-following translation tasks. The 7B and 30B-A3B models outperform open-source models such as DeepSeek-V4-Pro and Kimi K2.6 in fast-thinking mode, while the lightweight 1.8B model also surpasses mainstream commercial APIs from providers such as Microsoft and Doubao overall. In this release, we also open-source [IFMTBench](./IFMTBench/README.md), a benchmark for evaluating translation instruction-following capabilities. We also welcome everyone to use our released Hy-MT2-Translator Skill, which makes it easy to integrate Hy-MT2 series models for translation tasks. Download links: [ClawHub](https://clawhub.ai/tencent-adm/hy-mt2-translator-skill) and [SkillHub](https://skillhub.cn/skills/hy-mt2-translator).

### 5. Tencent-Hunyuan/Hy4-preview（381★）

- 链接：https://github.com/Tencent-Hunyuan/Hy4-preview
- 主题：
- 最近推送：2026-08-28
- 摘要来源：readme_head | 翻译：llm
- 中文简介：中文 &nbsp;｜&nbsp;English &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; 🖥️&nbsp;  官方网站  &nbsp;&nbsp;|&nbsp;&nbsp; 💬&nbsp;  GitHub - [模型介绍](#model-introduction) - [全新一代旗舰](#a-new-flagship-generation) - [为生产力而生](#built-for-productivity) - [评测附录](#benchmark-appendix) - [已知局限性](#known-limitations) - [新闻动态](#news) - [模型链接](#model-links) - [快速开始](#quickstart) - [部署](#deployment) - [vLLM](#vllm) - [SGLang](#sglang) - [微调](#finetuning) - [量化](#quantization) - [许可证](#license) - [联系我们](#contact-us)  **Hy4 preview** 是腾讯 Hy 团队开发的新一代混合专家（MoE）旗舰模型。模型总参数量为 770B，每个 token 激活 49B。主干网络共 78 层，其中第一层采用标准稠密 FFN，其余 77 层以 MoE 替代，每层包含 256 个路由专家和 1 个共享专家；每个 token 激活 top-8 路由专家以及共享专家。除主干网络外，模型还内置了 1 个原生 MTP 层（总参数量 10B，激活 0.7B），用于投机解码（speculative decoding）。  在架构方面，受 DeepSeek 和 GLM 启发，注意力模块采用 Gated [DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556)（Gated DSA），并通过 [IndexCache](https://arxiv.org/abs/2603.12201) 实现跨层稀疏索引复用。残差通路采用 [iHC（identity Hyper-Connections）](https://zhuanlan.zhihu.com/p/2010852389670908320)来扩展层间信息流动。
- 原文简介：中文 &nbsp;｜&nbsp;English &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp; 🖥️&nbsp;  Official Website  &nbsp;&nbsp;|&nbsp;&nbsp; 💬&nbsp;  GitHub - [Model Introduction](#model-introduction) - [A New Flagship Generation](#a-new-flagship-generation) - [Built for Productivity](#built-for-productivity) - [Benchmark Appendix](#benchmark-appendix) - [Known Limitations](#known-limitations) - [News](#news) - [Model Links](#model-links) - [Quickstart](#quickstart) - [Deployment](#deployment) - [vLLM](#vllm) - [SGLang](#sglang) - [Finetuning](#finetuning) - [Quantization](#quantization) - [License](#license) - [Contact Us](#contact-us) **Hy4 preview** is a new-generation Mixture-of-Experts (MoE) flagship model developed by the Tencent Hy Team. The model comprises 770B total parameters, of which 49B are activated per token. The backbone consists of 78 layers, where the first layer uses a standard dense FFN and the remaining 77 layers replace it with MoE, each containing 256 routed experts and 1 shared expert; every token activates the top-8 routed experts along with the shared expert. In addition to the backbone, 1 native MTP layer (10B total parameters, 0.7B activated) is built in for speculative decoding. On the architecture side, inspired by DeepSeek and GLM, the attention module employs Gated [DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556) (Gated DSA) with [IndexCache](https://arxiv.org/abs/2603.12201) for cross-layer sparse index reuse. The residual pathway uses [iHC (identity Hyper-Connections)](https://zhuanlan.zhihu.com/p/2010852389670908320) to expand inter-layer information flow.

### 6. Tencent-Hunyuan/Simple-Attention-Sparsification（59★）

- 链接：https://github.com/Tencent-Hunyuan/Simple-Attention-Sparsification
- 主题：
- 最近推送：2026-09-14
- 摘要来源：feed | 翻译：llm
- 中文简介：我们研究论文《SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking》的代码
- 原文简介：Code for our resarch paper "SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking"

### 7. Tencent-Hunyuan/evolve-scaler（3★）

- 链接：https://github.com/Tencent-Hunyuan/evolve-scaler
- 主题：
- 最近推送：2026-09-09
- 摘要来源：feed | 翻译：llm
- 中文简介：论文《EvolveScaler：通过可执行状态机与自然语言渲染合成信息演化语境》的 GitHub 页面
- 原文简介：Github page for paper "EvolveScaler: Synthesizing Information-Evolution Contexts via Executable State Machines and Natural-Language Rendering"

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 7 | 计数 |
| 输入 tokens | 2,582 | GLM usage（精确） |
| 输出 tokens | 10,204 | GLM usage（精确） |
| 合计 tokens | 12,786 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 6 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 186 秒 | 计时，统计系统占用时间 |
