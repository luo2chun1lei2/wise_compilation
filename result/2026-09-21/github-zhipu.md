# GitHub 热门项目（github-zhipu · 2026-09-21）

- 生成时间：2026-09-21 06:39
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`user:zai-org pushed:>2026-08-22`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

### 1. [zai-org/GLM-5](https://github.com/zai-org/GLM-5)（7,207★）

- 中文简介：GLM-5：从 Vibe Coding 到智能体工程  👋 欢迎加入我们的 WeChat 或 Discord 社区。  📖 请查看 GLM-5.3-Flash 博客、GLM-5.3 博客以及 GLM-5 技术报告。  📍 在 Z.ai API 平台上使用 GLM-5.3 与 GLM-5.3-Flash 的 API 服务。  🔜 在 z.ai 上体验 GLM-5.3 与 GLM-5.3-Flash。  GLM-5.3 与 GLM-5.2 使用相同的基础模型——所有提升均来自后训练。与 GLM-5.2 相比，它在复杂编程和长时程任务方面的能力显著增强：  + 更强的编程能力：GLM-5.3 是编程能力最强的开源权重模型，在我们内部的 Z.ai Code Bench 上相比 GLM-5.2 提升了 50%。它还在 Terminal Bench 3.0 和 Agents' Last Exam 等公开基准测试中取得了开源 SOTA 成绩。  + 涌现的网络攻防能力：随着后训练规模的扩大，网络攻防能力的发展速度超出了我们的预期。GLM-5.3 在 CyberGym 漏洞发现任务上达到业界最先进（SOTA）水平，且在漏洞利用链条越靠上游的环节提升越显著——在漏洞利用基准上，其成绩达到 GLM-5.2 的两倍以上。  GLM-5.3-Flash 基于全新训练的基础模型打造，其架构与训练方案围绕能力与效率进行了重新设计。我们在 GLM 系列中首次引入了稀疏注意力与线性注意力相结合的混合架构，在保持精准长上下文能力的同时，大幅降低了长上下文的服务成本。该模型还采用了流形约束超连接（Manifold-Constrained Hyper-Connections，mHC）以进一步提升扩展效率。结合我们最新的 30T token 多模态预训练语料库，这些改进使 GLM-5.3-Flash 能够以更少的算力提供更强的智能。
- 原文简介：GLM-5: From Vibe Coding to Agentic Engineering 👋 Join our  Wechat  or  Discord  community. 📖 Check out the GLM-5.3-Flash  blog , GLM-5.3  blog  and GLM-5  Technical report . 📍 Use GLM-5.3 & GLM-5.3-Flash API services on  Z.ai API Platform. 🔜 Try GLM-5.3 & GLM-5.3-Flash at  z.ai . GLM-5.3 uses the same base model as GLM-5.2 — every gain comes from post-training. Compared with GLM-5.2, it is much better at complex coding and long-horizon tasks: + Stronger Coding: GLM-5.3 is the most capable open-weights model for coding, with a 50% improvement over GLM-5.2 on our in-house Z.ai Code Bench. It also achieve open-source SOTA on public benchmarks including Terminal Bench 3.0 and Agents' Last Exam. + Emergent Cyber Capability: As we scaled post-training, cyber capability developed faster than we expected. GLM-5.3 is state of the art on CyberGym for vulnerability discovery, and its gains are largest further up the exploitation chain, where it more than doubles GLM-5.2 on exploitation benchmarks. GLM-5.3-Flash starts from a newly trained base model, with its architecture and training recipe redesigned around capability and efficiency. For the first time in the GLM series, we introduce a hybrid architecture combining sparse and linear attention, sharply reducing long-context serving costs while preserving precise long-context capabilities. The model also adopts Manifold-Constrained Hyper-Connections (mHC) to further improve scaling efficiency. Together with our latest 30T-token multimodal pre-training corpus, these changes enable GLM-5.3-Flash to deliver more intelligence with less compute.
- 主题：agentic-ai, coding, llm, long-horizon · 推送：2026-09-01 · 摘要：readme_head · 翻译：llm

### 2. [zai-org/GLM-V](https://github.com/zai-org/GLM-V)（2,388★ · Python）

- 中文简介：GLM-4.6V/4.5V/4.1V-Thinking：迈向基于可扩展强化学习的通用多模态推理
- 原文简介：GLM-4.6V/4.5V/4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning
- 主题：image2text, reasoning, video-understanding, vlm · 推送：2026-09-02 · 摘要：feed · 翻译：llm

### 3. [zai-org/SCAIL-2](https://github.com/zai-org/SCAIL-2)（1,209★ · Python）

- 中文简介：SCAIL-2 官方实现：通过端到端上下文内条件化（In-Context Conditioning）统一可控角色动画
- 原文简介：Official Implementation of SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning
- 推送：2026-08-24 · 摘要：feed · 翻译：llm

### 4. [zai-org/zcode-plugins](https://github.com/zai-org/zcode-plugins)（40★ · Python）

- 中文简介：ZCode 插件市场 - ZCode 官方内置插件与社区插件  [ZCode](https://zcode.z.ai) 的官方插件市场，收录由 ZCode 维护的插件以及社区贡献的插件。  你可以使用此仓库浏览可用插件、在兼容客户端中安装该市场，或通过 GitHub pull request 提议新插件。  - [贡献指南](./CONTRIBUTING.md) ([中文](./CONTRIBUTING_CN.md)) - [分发格式](./docs/distribution.md) ([中文](./docs/distribution_CN.md)) - [插件开发教程](./docs/PLUGIN_DEVELOPMENT.md) ([中文](./docs/PLUGIN_DEVELOPMENT_CN.md))  十个 `finance` 插件，覆盖卖方、买方、公司银行业务以及企业财务职能。每个插件都将一个路由 agent 与领域技能配对，并且除 `accounting-and-reporting` 外，还包含通过 ZCode host 完成认证的远程行情数据 MCP 服务器——无需配置任何数据供应商账号。所有插件均需要付费套餐，唯独 `accounting-and-reporting` 除外——它基于你自己的账本运行。  [`marketplace.json`](./marketplace.json) 中的 `category` 字段保证了插件发现的一致性：  ZCode 内置了官方市场。打开插件管理器，选择插件，即可直接安装。  对某个插件有疑问，或者正在开发自己的插件？欢迎在 Discord 上加入 ZCode 插件开发者社区——我们在那里解答问题、分享进行中的工作，并发布市场更新公告。  中国大陆的开发者可以改为加入我们的飞书群——详见[中文文档](./README_CN.md#社区)。  欢迎社区贡献：
- 原文简介：ZCode Plugins Marketplace - official built-in and community plugins for ZCode The official plugins marketplace for [ZCode](https://zcode.z.ai), featuring plugins maintained by ZCode and contributions from the community. Use this repository to browse available plugins, install the marketplace in compatible clients, or propose a new plugin through a GitHub pull request. - [Contributing guide](./CONTRIBUTING.md) ([中文](./CONTRIBUTING_CN.md)) - [Distribution format](./docs/distribution.md) ([中文](./docs/distribution_CN.md)) - [Plugin development tutorial](./docs/PLUGIN_DEVELOPMENT.md) ([中文](./docs/PLUGIN_DEVELOPMENT_CN.md)) Ten `finance` plugins covering the sell side, the buy side, corporate banking, and the corporate finance function. Each pairs one routing agent with domain skills and, except `accounting-and-reporting`, remote market-data MCP servers that authenticate through the ZCode host — no data-vendor account to configure. All of them require a paid plan except `accounting-and-reporting`, which works off your own ledger. The `category` field in [`marketplace.json`](./marketplace.json) keeps discovery consistent: ZCode includes the official marketplace. Open the plugin manager, choose a plugin, and install it directly. Have a question about a plugin, or building one of your own? Join the ZCode plugin developers on Discord — that is where we answer questions, share work in progress, and announce marketplace releases. Developers in mainland China can join our Feishu group instead — see the [中文文档](./README_CN.md#社区). Community contributions are welcome:
- 推送：2026-09-17 · 摘要：readme_head · 翻译：llm

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 0 | 计数 |
| 输入 tokens | 0 | GLM usage（精确） |
| 输出 tokens | 0 | GLM usage（精确） |
| 合计 tokens | 0 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 3 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 8 秒 | 计时，统计系统占用时间 |
