# GitHub 热门项目（github-bytedance · 2026-09-18）

- 生成时间：2026-09-18 19:35
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`user:bytedance pushed:>2026-08-19`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 82,638 | Python | 一个开源的长时程 SuperAgent 框架，能够进行研究、编程和创作。借助沙箱、记忆、工具、技能、子代理和消息网关，它可以处理不同层级的任务，耗时从几分钟到数小时不等。 |
| 2 | [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 39,040 | TypeScript | 开源多模态 AI Agent 技术栈：连接前沿 AI 模型与 Agent 基础设施 |
| 3 | [bytedance/sonic](https://github.com/bytedance/sonic) | 9,597 | Go | 一个极致快速的 JSON 序列化与反序列化库 |
| 4 | [bytedance/xgplayer](https://github.com/bytedance/xgplayer) | 9,298 | JavaScript | 一款带解析器的 HTML5 视频播放器，可节省流量 |
| 5 | [bytedance/flowgram.ai](https://github.com/bytedance/flowgram.ai) | 8,457 | TypeScript | FlowGram 是一个可扩展的工作流开发框架，内置画布、表单、变量和物料，帮助开发者更快、更简单地构建 AI 工作流平台。 |
| 6 | [bytedance/android-inline-hook](https://github.com/bytedance/android-inline-hook) | 2,393 | C | 通用的Android inline hook库，支持thumb，arm32，arm64 |
| 7 | [bytedance/gopkg](https://github.com/bytedance/gopkg) | 2,048 | Go | # Go 通用工具库 |
| 8 | [bytedance/appshark](https://github.com/bytedance/appshark) | 1,750 | Kotlin | Appshark 是一个静态污点分析平台，用于扫描 Android 应用中的漏洞。 |
| 9 | [bytedance/Sa2VA](https://github.com/bytedance/Sa2VA) | 1,672 | Python | Pixel-LLM 代码库官方仓库：Sa2VA（T-PAMI-26）、SAMTok（CVPR-26）、VRT（Arxiv-25）、SaSaSa2VA（LSVOS 第一名解决方案） |
| 10 | [bytedance/SALMONN](https://github.com/bytedance/SALMONN) | 1,532 | - | SALMONN 系列：一套先进的多模态大语言模型 |

## 详情

### 1. bytedance/deer-flow（82,638★）

- 链接：https://github.com/bytedance/deer-flow
- 主题：agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, harness
- 最近推送：2026-09-18
- 摘要来源：feed | 翻译：llm
- 中文简介：一个开源的长时程 SuperAgent 框架，能够进行研究、编程和创作。借助沙箱、记忆、工具、技能、子代理和消息网关，它可以处理不同层级的任务，耗时从几分钟到数小时不等。
- 原文简介：An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

### 2. bytedance/UI-TARS-desktop（39,040★）

- 链接：https://github.com/bytedance/UI-TARS-desktop
- 主题：agent, agent-tars, browser-use, computer-use, cowork, gui-agent, gui-operator, mcp
- 最近推送：2026-09-11
- 摘要来源：feed | 翻译：llm
- 中文简介：开源多模态 AI Agent 技术栈：连接前沿 AI 模型与 Agent 基础设施
- 原文简介：The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

### 3. bytedance/sonic（9,597★）

- 链接：https://github.com/bytedance/sonic
- 主题：high-performance, jit, json, simd
- 最近推送：2026-09-11
- 摘要来源：readme_head | 翻译：llm
- 中文简介：一个极致快速的 JSON 序列化与反序列化库  English | [中文](README_ZH_CN.md)  一个极致快速的 JSON 序列化与反序列化库，借助 JIT（即时编译）与 SIMD（单指令多数据）技术加速。  - Go：1.18~1.27 - 注意：由于该 [issue](https://github.com/golang/go/issues/71672)，暂不支持 Go1.24.0；请使用更高的 Go 版本，或在构建时传入参数 `-ldflags="-checklinkname=0"`。 - 操作系统：Linux / MacOS / Windows - CPU：AMD64 /（ARM64，需 go1.20 及以上版本）  - 无需代码生成，即可实现运行时对象绑定 - 提供完整的 JSON 值操作 API - 快，快，快！  详见 [go.dev](https://pkg.go.dev/github.com/bytedance/sonic)  对于**任意大小**的 json 和**任何使用场景**，**Sonic 都能提供最佳性能**。  - [Medium](https://github.com/bytedance/sonic/blob/main/decoder/testdata_test.go#L19)（13KB，300+ 键，6 层嵌套）  goversion: 1.17.1 goos: darwin goarch: amd64 cpu: Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz  BenchmarkEncoder_Generic_Sonic-16                      32393 ns/op         402.40 MB/s       11965 B/op          4 allocs/op BenchmarkEncoder_Generic_Sonic_Fast-16                 21668 ns/op         601.57 MB/s       10940 B/op          4 allocs/op BenchmarkEncoder_Generic_JsonIter-16                   42168 ns/op         309.12 MB/s       14345 B/op        115 allocs/op BenchmarkEncoder_Generic_GoJson-16                     65189 ns/op         199.96 MB/s       23261 B/op         16 allocs/op BenchmarkEncoder_Generic_StdLib-16                    106322 ns/op         122.60 MB/s       49136 B/op        789 allocs/op
- 原文简介：A blazingly fast JSON serializing & deserializing library English | [中文](README_ZH_CN.md) A blazingly fast JSON serializing &amp; deserializing library, accelerated by JIT (just-in-time compiling) and SIMD (single-instruction-multiple-data). - Go: 1.18~1.27 - Notice: Go1.24.0 is not supported due to the [issue](https://github.com/golang/go/issues/71672); please use a higher Go version or pass the build flag `-ldflags="-checklinkname=0"`. - OS: Linux / MacOS / Windows - CPU: AMD64 / (ARM64, need go1.20 above) - Runtime object binding without code generation - Complete APIs for JSON value manipulation - Fast, fast, fast! see [go.dev](https://pkg.go.dev/github.com/bytedance/sonic) For **all sizes** of json and **all scenarios** of usage, **Sonic performs best**. - [Medium](https://github.com/bytedance/sonic/blob/main/decoder/testdata_test.go#L19) (13KB, 300+ key, 6 layers) goversion: 1.17.1 goos: darwin goarch: amd64 cpu: Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz BenchmarkEncoder_Generic_Sonic-16                      32393 ns/op         402.40 MB/s       11965 B/op          4 allocs/op BenchmarkEncoder_Generic_Sonic_Fast-16                 21668 ns/op         601.57 MB/s       10940 B/op          4 allocs/op BenchmarkEncoder_Generic_JsonIter-16                   42168 ns/op         309.12 MB/s       14345 B/op        115 allocs/op BenchmarkEncoder_Generic_GoJson-16                     65189 ns/op         199.96 MB/s       23261 B/op         16 allocs/op BenchmarkEncoder_Generic_StdLib-16                    106322 ns/op         122.60 MB/s       49136 B/op        789 allocs/op

### 4. bytedance/xgplayer（9,298★）

- 链接：https://github.com/bytedance/xgplayer
- 主题：dash, flv, flv-parser, fmp4, hls, hls-player, html5-video, html5-video-player
- 最近推送：2026-09-17
- 摘要来源：readme_head | 翻译：llm
- 中文简介：一款带解析器的 HTML5 视频播放器，可节省流量  xgplayer 是一个 Web 视频播放器库。基于一切皆组件化的原则，它设计了独立、可拆卸的 UI 组件。更重要的是，它不仅在 UI 层足够灵活，在功能上也十分大胆：摆脱了视频加载、缓冲和格式支持对视频播放的依赖。尤其是对于 mp4 格式，即使是不支持流式加载的 mp4，它也可以实现分阶段加载。这意味着清晰度的无缝切换、加载控制以及流量的节省。它还集成了对 FLV、HLS 和 dash 的点播与直播支持。[文档](https://h5player.bytedance.com/en/)  1. 安装 $ npm install xgplayer  2. 使用 第一步： 第二步： ```javascript import Player from 'xgplayer';  const player = new Player({     id: 'vs',     url: 'https://s2.pstatp.com/cdn/expire-1-M/byted-player-videos/1.0.0/xgplayer-demo.mp4' }) ``` 这是配置播放器最简单的方式，配置完成后即可播放视频。如需了解更高级的内容，请参阅插件部分或文档。[更多配置](https://h5player.bytedance.com/en/config/)  xgplayer 提供了更多插件，并支持自定义插件，查看更多内容请参见 [插件](https://h5player.bytedance.com/en/plugins/)。播放器中内置了许多插件，如果需要关闭特定插件，可以通过 [ignores](https://h5player.bytedance.com/config/#ignores) 配置将其禁用。  为了方便开发者调试，我们在仓库的 fixtures 目录中提供了示例代码。播放器使用 yarn 进行包管理，只需几个简单的步骤即可在仓库中开始调试。
- 原文简介：A HTML5 video player with a parser that saves traffic xgplayer is a web video player library. It has designed a separate, detachable UI component based on the principle that everything is componentized. More importantly, it is not only flexible in the UI layer, but also bold in its functionality: it gets rid of video loading, buffering, and format support for video dependence. Especially on mp4 it can be staged loading for that does not support streaming mp4. This means seamless switching with clarity, load control, and video savings. It also integrates on-demand and live support for FLV, HLS, and dash. [Document](https://h5player.bytedance.com/en/) 1. Install $ npm install xgplayer 2. Usage Step 1: Step 2: import Player from 'xgplayer'; const player = new Player({ id: 'vs', url: 'https://s2.pstatp.com/cdn/expire-1-M/byted-player-videos/1.0.0/xgplayer-demo.mp4' }) This is the easiest way to configure the player, then it runs with video. For more advanced content, see the plug-in section or documentation. [more config](https://h5player.bytedance.com/en/config/) xgplayer provides more plugins and supports custom plugins, for more content viewing [plugins](https://h5player.bytedance.com/en/plugins/). There are many built-in plugins in the player, if you need to close specific plugins, you can disable them by [ignores](https://h5player.bytedance.com/config/#ignores) configuration In order to debug by developers, we provide demos code in the fixtures directory of the repo. The player uses yarn for package management, and it only takes a few simple steps to start debugging in the repo

### 5. bytedance/flowgram.ai（8,457★）

- 链接：https://github.com/bytedance/flowgram.ai
- 主题：ai, automation, coze, data-flow, diagram, flow, flowchart, graph
- 最近推送：2026-09-01
- 摘要来源：feed | 翻译：llm
- 中文简介：FlowGram 是一个可扩展的工作流开发框架，内置画布、表单、变量和物料，帮助开发者更快、更简单地构建 AI 工作流平台。
- 原文简介：FlowGram is an extensible workflow development framework with built-in canvas, form, variable, and materials that helps developers build AI workflow platforms faster and simpler.

### 6. bytedance/android-inline-hook（2,393★）

- 链接：https://github.com/bytedance/android-inline-hook
- 主题：android, androidinlinehook, arm, arm64, hook, inline, inlinehook, jni
- 最近推送：2026-08-26
- 摘要来源：readme_head | 翻译：llm
- 中文简介：通用的Android inline hook库，支持thumb，arm32，arm64  **shadowhook 是一个 Android inline hook 库。** 其目标是：  - **稳定性** - 可在生产应用中稳定使用。 - **兼容性** - 在新版本中始终保持 API 和 ABI 的向后兼容。 - **性能** - 持续降低 API 调用开销以及 hook 引入的额外运行时开销。 - **功能性** - 除基本 hook 功能外，还针对“hook 相关”问题提供通用解决方案。  > 如果你需要 Android PLT hook 库，请尝试 [ByteHook](https://github.com/bytedance/bhook)。  **Android `4.1` - `17 QPR1 Beta 4`**  > 我们会尽快测试并支持最新的 Android OS Beta 版本，并在此处列出受支持的 Android OS 版本。  - 支持 armeabi-v7a 和 arm64-v8a。 - 支持 Android `4.1` - `17`（API level `16` - `37`）。 - 支持 hook 和 intercept。 - 支持通过“地址”或“库名 + 函数名”指定 hook 和 intercept 的目标位置。 - 自动完成对“新加载 ELF”的 hook 和 intercept，执行后可选回调。 - 自动防止代理函数之间的递归循环调用。 - 支持 hook 和 intercept 操作记录，可随时导出。 - 支持在 linker 调用新加载 ELF 的 `.init` + `.init_array` 和 `.fini` + `.fini_array` 前后注册回调。 - 支持绕过 linker namespace 限制，查询进程中所有 ELF 的 `.dynsym` 和 `.symtab` 中的符号地址。 - 在 hook 代理函数和 interceptor 函数中兼容 CFI unwind 和 FP unwind。
- 原文简介：通用的Android inline hook库，支持thumb，arm32，arm64 **shadowhook is an Android inline hook library.** Its goals are: - **Stability** - Can be stably used in production apps. - **Compatibility** - Always maintains backward compatibility of API and ABI in new versions. - **Performance** - Continuously reduces API call overhead and additional runtime overhead introduced by hooks. - **Functionality** - Besides basic hook functionality, provides general solutions for "hook-related" issues. > If you need an Android PLT hook library, try [ByteHook](https://github.com/bytedance/bhook). **Android `4.1` - `17 QPR1 Beta 4`** > We will test and support the latest Android OS Beta versions as promptly as possible, and list the supported Android OS versions here. - Supports armeabi-v7a and arm64-v8a. - Supports Android `4.1` - `17` (API level `16` - `37`). - Supports hook and intercept. - Supports specifying hook and intercept target locations via "address" or "library name + function name". - Automatically completes hook and intercept for "newly loaded ELFs", with optional callbacks after execution. - Automatically prevents recursive circular calls between proxy functions. - Supports hook and intercept operation recording, which can be exported at any time. - Supports registering callbacks before and after linker calls `.init` + `.init_array` and `.fini` + `.fini_array` of newly loaded ELFs. - Supports bypassing linker namespace restrictions to query symbol addresses in `.dynsym` and `.symtab` of all ELFs in the process. - Compatible with CFI unwind and FP unwind in hook proxy functions and interceptor functions.

### 7. bytedance/gopkg（2,048★）

- 链接：https://github.com/bytedance/gopkg
- 主题：
- 最近推送：2026-09-18
- 摘要来源：readme_head | 翻译：llm
- 中文简介：# Go 通用工具库  `gopkg` 是 Go 语言的通用工具集合，它对 Boost、Better std、Cloud tools 等同类项目形成了补充。  - [简介](#Introduction) - [目录](#Catalogs) - [版本发布](#Releases) - [如何使用](#How-To-Use) - [许可证](#License)  `gopkg` 是 Go 语言的通用工具集合，它对 Boost、Better std、Cloud tools 等同类项目形成了补充。它迁移自字节跳动（ByteDance）的内部代码库，并已在生产环境中得到广泛采用。  我们的生产环境依赖同一份代码（即本仓库）。  * [cache](https://github.com/bytedance/gopkg/tree/main/cache)：缓存机制 * [cloud](https://github.com/bytedance/gopkg/tree/main/cloud)：云计算设计模式 * [collection](https://github.com/bytedance/gopkg/tree/main/collection)：数据结构 * [lang](https://github.com/bytedance/gopkg/tree/main/lang)：增强标准库 * [util](https://github.com/bytedance/gopkg/tree/main/util)：跨领域通用工具  为保证稳定性，`gopkg` 推荐使用最新的带标签（tagged）版本。  我们在 `main` 分支上进行开发，并在版本稳定时创建带标签的发布版本。  你可以使用 `go get -u github.com/bytedance/gopkg@latest` 来获取或更新 `gopkg`。  `gopkg` 基于 Apache 2.0 许可证授权。更多信息请参见 [LICENSE](LICENSE)。
- 原文简介：Universal Utilities for Go `gopkg` is a universal utility collection for Go, it complements offerings such as Boost, Better std, Cloud tools. - [Introduction](#Introduction) - [Catalogs](#Catalogs) - [Releases](#Releases) - [How To Use](#How-To-Use) - [License](#License) `gopkg` is a universal utility collection for Go, it complements offerings such as Boost, Better std, Cloud tools. It is migrated from the internal code base at ByteDance and has been extensively adopted in production. We depend on the same code(this repo) in our production environment. * [cache](https://github.com/bytedance/gopkg/tree/main/cache): Caching Mechanism * [cloud](https://github.com/bytedance/gopkg/tree/main/cloud): Cloud Computing Design Patterns * [collection](https://github.com/bytedance/gopkg/tree/main/collection): Data Structures * [lang](https://github.com/bytedance/gopkg/tree/main/lang): Enhanced Standard Libraries * [util](https://github.com/bytedance/gopkg/tree/main/util): Utilities Useful across Domains `gopkg` recommends using the latest tagged version for stability. We develop on the `main` branch and create tagged releases when stable. You can use `go get -u github.com/bytedance/gopkg@latest` to get or update `gopkg`. `gopkg` is licensed under the terms of the Apache license 2.0. See [LICENSE](LICENSE) for more information.

### 8. bytedance/appshark（1,750★）

- 链接：https://github.com/bytedance/appshark
- 主题：android, compliance, static-analysis, vulnerability
- 最近推送：2026-09-16
- 摘要来源：feed | 翻译：llm
- 中文简介：Appshark 是一个静态污点分析平台，用于扫描 Android 应用中的漏洞。
- 原文简介：Appshark is a static taint analysis platform to scan vulnerabilities in an Android app.

### 9. bytedance/Sa2VA（1,672★）

- 链接：https://github.com/bytedance/Sa2VA
- 主题：computer-vision, large-language-models, mllm
- 最近推送：2026-09-08
- 摘要来源：feed | 翻译：llm
- 中文简介：Pixel-LLM 代码库官方仓库：Sa2VA（T-PAMI-26）、SAMTok（CVPR-26）、VRT（Arxiv-25）、SaSaSa2VA（LSVOS 第一名解决方案）
- 原文简介：Official Repo For Pixel-LLM Codebase: Sa2VA (T-PAMI-26), SAMTok (CVPR-26), VRT (Arxiv-25), SaSaSa2VA (1-st solution for LSVOS)

### 10. bytedance/SALMONN（1,532★）

- 链接：https://github.com/bytedance/SALMONN
- 主题：audio, audio-processing, audio-visual-understanding, bytedance, iclr2024, icml-2024, large-language-models, multi-modal
- 最近推送：2026-08-24
- 摘要来源：readme_head | 翻译：llm
- 中文简介：SALMONN 系列：一套先进的多模态大语言模型  🚀🚀 欢迎来到 **SALMONN** 的仓库！！  SALMONN 模型系列由一系列先进的多模态大语言模型组成。更多详情，请参阅对应的分支。 - [SALMONN 2](https://github.com/bytedance/SALMONN/tree/salmonn2) - [[ICLR 2026] ELLSA](https://github.com/bytedance/SALMONN/tree/ELLSA) - [video-SALMONN 2](https://github.com/bytedance/video-SALMONN-2) - [[ICML 2025] F-16](https://github.com/bytedance/F-16) - [[ICML 2025] video-SALMONN-o1](https://github.com/bytedance/SALMONN/tree/video-salmonn-o1) - [[ICASSP 2025 & ACL 2025] 用于语音质量评估的 SALMONN](https://github.com/bytedance/SALMONN/tree/speech_quality_assessment) - [[ICML 2024] video-SALMONN](https://github.com/bytedance/SALMONN/tree/videosalmonn) - [[ICLR 2024] SALMONN](https://github.com/bytedance/SALMONN/tree/salmonn) - [2026-04-20] 我们已发布 **ELLSA** 的模型和推理代码！详情见[这里](https://github.com/bytedance/SALMONN/tree/ELLSA)！ELLSA 是首个在流式全双工框架中统一视觉、语音、文本和动作的端到端模型，可实现联合多模态感知与并行生成。 - [2025-07-08] 我们已开源 **video-SALMONN 2**！video-SALMONN 2 是一个强大的视听大语言模型，能够生成高质量的视听视频描述，并在通用视频问答基准测试中取得了具有竞争力的表现。 - [2025-06-01] 我们已开源 **QualiSpeech** 数据集——一个带有自然语言推理的语音质量评估数据集。你可以使用 QualiSpeech 开发自己的语音质量评估音频大语言模型，或评估现有音频大语言模型的底层语音感知能力。欢迎点击[这里](https://huggingface.co/datasets/tsinghua-ee/QualiSpeech)下载！
- 原文简介：SALMONN family: A suite of advanced multi-modal LLMs 🚀🚀 Welcome to the repo of **SALMONN**!! The SALMONN model family consists of a series of advanced multi-modal large language models. For more details, please refer to the corresponding branches. - [SALMONN 2](https://github.com/bytedance/SALMONN/tree/salmonn2) - [[ICLR 2026] ELLSA](https://github.com/bytedance/SALMONN/tree/ELLSA) - [video-SALMONN 2](https://github.com/bytedance/video-SALMONN-2) - [[ICML 2025] F-16](https://github.com/bytedance/F-16) - [[ICML 2025] video-SALMONN-o1](https://github.com/bytedance/SALMONN/tree/video-salmonn-o1) - [[ICASSP 2025 & ACL 2025] SALMONN for speech quality assessment](https://github.com/bytedance/SALMONN/tree/speech_quality_assessment) - [[ICML 2024] video-SALMONN](https://github.com/bytedance/SALMONN/tree/videosalmonn) - [[ICLR 2024] SALMONN](https://github.com/bytedance/SALMONN/tree/salmonn) - [2026-04-20] We have released the model and inference code for **ELLSA**! See [here](https://github.com/bytedance/SALMONN/tree/ELLSA)! ELLSA is the first end-to-end model that unifies vision, speech, text and action in a streaming full-duplex framework, enabling joint multimodal perception and concurrent generation. - [2025-07-08] We have opensourced **video-SALMONN 2**! video-SALMONN 2 is a powerful audio-visual LLM that generates high-quality audio-visual video captions and achieves competitive performance on general video QA benchmarks. - [2025-06-01] We have opensourced **QualiSpeech** dataset - A speech quality assessment dataset with natural language reasoning. You can use QualiSpeech to develop your own audio LLM for speech quality assessment or to evaluate the low-level speech perception capabilities of existing audio LLMs. Feel free to download it [here](https://huggingface.co/datasets/tsinghua-ee/QualiSpeech)!

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 10 | 计数 |
| 输入 tokens | 2,659 | GLM usage（精确） |
| 输出 tokens | 8,367 | GLM usage（精确） |
| 合计 tokens | 11,026 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 6 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 180 秒 | 计时，统计系统占用时间 |
