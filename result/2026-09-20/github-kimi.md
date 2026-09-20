# GitHub 热门项目（github-kimi · 2026-09-20）

- 生成时间：2026-09-20 10:58
- 数据来源：GitHub Search API（官方接口，按 star 数降序）
- 查询条件：`user:MoonshotAI pushed:>2026-08-21`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

| 排名 | 项目 | Stars | 语言 | 中文简介 |
|---|---|---|---|---|
| 1 | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | 11,406 | Python | Kimi Code CLI 是你的下一代 CLI 智能体。 |
| 2 | [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) | 7,513 | TypeScript | Kimi Code CLI — 下一代智能体的起点 |
| 3 | [MoonshotAI/FlashKDA](https://github.com/MoonshotAI/FlashKDA) | 1,254 | Cuda | FlashKDA：高性能 Kimi Delta Attention 内核 |
| 4 | [MoonshotAI/checkpoint-engine](https://github.com/MoonshotAI/checkpoint-engine) | 1,004 | Python | Checkpoint-engine 是一个简单的中间件，用于更新 LLM 推理引擎中的模型权重。 |
| 5 | [MoonshotAI/Kimi-Vendor-Verifier](https://github.com/MoonshotAI/Kimi-Vendor-Verifier) | 154 | Python | Kimi-Vendor-Verifier |
| 6 | [MoonshotAI/walle](https://github.com/MoonshotAI/walle) | 30 | Go | 一个 Moonshot AI 风格的 JSON schema 校验器。 |

## 详情

### 1. MoonshotAI/kimi-cli（11,406★）

- 链接：https://github.com/MoonshotAI/kimi-cli
- 主题：
- 最近推送：2026-09-01
- 摘要来源：readme_head | 翻译：llm
- 中文简介：Kimi Code CLI 是你的下一代 CLI 智能体。 > [!IMPORTANT] > **Kimi CLI 正在演进为 [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code)**——由同一团队打造的下一代终端 AI 智能体。安装 Kimi Code CLI 会自动迁移你的配置和会话。本项目将逐步停止维护；文档和已有安装仍可继续使用。 Kimi CLI 是一个运行在终端中的 AI 智能体，帮助你完成软件开发任务和终端操作。它可以读取和编辑代码、执行 shell 命令、搜索并抓取网页，并在执行过程中自主规划与调整行动。 请参阅[快速上手](https://moonshotai.github.io/kimi-cli/en/guides/getting-started.html)，了解如何安装并开始使用 Kimi CLI。 Kimi CLI 不仅仅是一个编码智能体，同时也是一个 shell。你可以按 `Ctrl-X` 切换到 shell 命令模式。在该模式下，你可以直接运行 shell 命令，无需离开 Kimi CLI。 > [!NOTE] > 暂不支持 `cd` 等内置 shell 命令。 Kimi CLI 可以通过 [Kimi Code VS Code 扩展](https://marketplace.visualstudio.com/items?itemName=moonshot-ai.kimi-code)与 [Visual Studio Code](https://code.visualstudio.com/) 集成。 Kimi CLI 开箱即支持 [Agent Client Protocol]。你可以将它与任何兼容 ACP 的编辑器或 IDE 配合使用。 要在 ACP 客户端中使用 Kimi CLI，请先确保在终端中运行 Kimi CLI，并发送 `/login` 完成登录。然后，你可以在 ACP 客户端中配置，使用命令 `kimi acp` 将 Kimi CLI 作为 ACP 智能体服务器启动。
- 原文简介：Kimi Code CLI is your next CLI agent. > [!IMPORTANT] > **Kimi CLI is evolving into [Kimi Code CLI](https://github.com/MoonshotAI/kimi-code)** — the next-generation terminal AI agent from the same team. Installing Kimi Code CLI automatically migrates your configuration and sessions. This project will be gradually wound down; the docs and existing installations remain available. Kimi CLI is an AI agent that runs in the terminal, helping you complete software development tasks and terminal operations. It can read and edit code, execute shell commands, search and fetch web pages, and autonomously plan and adjust actions during execution. See [Getting Started](https://moonshotai.github.io/kimi-cli/en/guides/getting-started.html) for how to install and start using Kimi CLI. Kimi CLI is not only a coding agent, but also a shell. You can switch the shell command mode by pressing `Ctrl-X`. In this mode, you can directly run shell commands without leaving Kimi CLI. > [!NOTE] > Built-in shell commands like `cd` are not supported yet. Kimi CLI can be integrated with [Visual Studio Code](https://code.visualstudio.com/) via the [Kimi Code VS Code Extension](https://marketplace.visualstudio.com/items?itemName=moonshot-ai.kimi-code). Kimi CLI supports [Agent Client Protocol] out of the box. You can use it together with any ACP-compatible editor or IDE. To use Kimi CLI with ACP clients, make sure to run Kimi CLI in the terminal and send `/login` to complete the login first. Then, you can configure your ACP client to start Kimi CLI as an ACP agent server with command `kimi acp`.

### 2. MoonshotAI/kimi-code（7,513★）

- 链接：https://github.com/MoonshotAI/kimi-code
- 主题：
- 最近推送：2026-09-20
- 摘要来源：readme_head | 翻译：llm
- 中文简介：Kimi Code CLI — 下一代智能体的起点  Kimi Code CLI 是一款在终端中运行的 AI 编程智能体——它可以读取和编辑代码、运行 shell 命令、搜索文件、抓取网页，并根据收到的反馈决定下一步操作。开箱即用即可连接 Moonshot AI 的 Kimi 模型，也可以配置为使用其他兼容的服务提供商。  使用官方脚本安装。无需 Node.js。  - **macOS 或 Linux**： ```bash curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash ``` - **Windows (PowerShell)**： ```powershell irm https://code.kimi.com/kimi-code/install.ps1 | iex ``` > 在 Windows 上，首次启动前请先安装 [Git for Windows](https://gitforwindows.org/)，因为 Kimi Code CLI 使用自带的 Git Bash 作为其 shell 环境。如果 Git Bash 安装在自定义位置，请将 `KIMI_SHELL_PATH` 设置为 `bash.exe` 的绝对路径。  然后，在一个新的 shell 会话中运行： ```bash kimi --version ```  有关通过 npm 安装、升级、卸载的方法，请参阅[入门指南](https://moonshotai.github.io/kimi-code/en/guides/getting-started)。  打开一个项目并启动交互式界面： ```bash cd your-project kimi ```  首次启动时，在 Kimi Code CLI 中运行 `/login`，并选择 Kimi Code OAuth 或 Moonshot AI 开放平台 API 密钥。登录后，试试你的第一个任务：  ``` 看一下这个项目，解释一下它的主要目录结构。 ```  - **单二进制文件分发。** 一条命令即可安装：无需配置 Node.js、折腾 PATH，也不会出现全局模块冲突。 - **极速启动。** TUI 在毫秒内即可就绪，开启会话毫无负担。
- 原文简介：Kimi Code CLI  —  The Starting Point for Next-Gen Agents Kimi Code CLI is an AI coding agent that runs in your terminal — it can read and edit code, run shell commands, search files, fetch web pages, and choose the next step based on the feedback it receives. It works out of the box with Moonshot AI’s Kimi models and can also be configured to use other compatible providers. Install with the official script. No Node.js required. - **macOS or Linux**: curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash - **Windows (PowerShell)**: irm https://code.kimi.com/kimi-code/install.ps1 | iex > On Windows, install [Git for Windows](https://gitforwindows.org/) before first launch because Kimi Code CLI uses the bundled Git Bash as its shell environment. If Git Bash is installed in a custom location, set `KIMI_SHELL_PATH` to the absolute path of `bash.exe`. Then, run it with a new shell session: kimi --version For npm install, upgrade, uninstall, see [Getting Started](https://moonshotai.github.io/kimi-code/en/guides/getting-started). Open a project and start the interactive UI: cd your-project kimi On first launch, run `/login` inside Kimi Code CLI and choose either Kimi Code OAuth or a Moonshot AI Open Platform API key. After login, try your first task: Take a look at this project and explain its main directories. - **Single-binary distribution.** Install with one command: no Node.js setup, PATH gymnastics, or global module conflicts. - **Blazing-fast startup.** The TUI is ready in milliseconds, so starting a session never feels heavy.

### 3. MoonshotAI/FlashKDA（1,254★）

- 链接：https://github.com/MoonshotAI/FlashKDA
- 主题：
- 最近推送：2026-09-01
- 摘要来源：readme_head | 翻译：llm
- 中文简介：FlashKDA：高性能 Kimi Delta Attention 内核 FlashKDA：Flash Kimi Delta Attention — 基于 CUTLASS 构建的高性能 KDA 内核 - **2026-04-22** — 深度解析博客：FlashKDA v1 背后的设计决策，[点击此处](docs/20260420-flashkda-v1-deep-dive.md)阅读。 - SM90 及以上 - CUDA 12.9 及以上 - PyTorch 2.4 及以上  ```bash git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda cd flash-kda git submodule update --init --recursive pip install -v --no-build-isolation . ```  默认情况下，构建过程会检测当前 CUDA 设备并针对该架构进行编译。若用于 wheel 包或 CI 构建，请显式编译所有受支持的架构：  ```bash FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation . ```  支持的取值为 `auto`（默认）、`all`，或以逗号分隔的架构列表，例如 `90a,100a`。  安装完成后，`flash-linear-attention` 的 `chunk_kda` 会自动调度 FlashKDA。集成详情请参见 [fla-org/flash-linear-attention#852](https://github.com/fla-org/flash-linear-attention/pull/852)。  **环境要求**  1. 安装 `flash-linear-attention >= 0.5.0`：  ```bash pip install -U flash-linear-attention ```  2. 在 `torch.inference_mode()` 下调用 `chunk_kda`  ```python import torch from fla.ops.kda import chunk_kda  with torch.inference_mode():     out, final_state = chunk_kda(         q=q, k=k, v=v, g=g, beta=beta,         scale=scale,         initial_state=h0,         output_final_state=True,         use_gate_in_kernel=True,         use_qk_l2norm_in_kernel=True,         use_beta_sigmoid_in_kernel=True,         safe_gate=True,         A_log=A_log, dt_bias=dt_bias,         lower_bound=lower_bound,         transpose_state_layout=True, ```
- 原文简介：FlashKDA: high-performance Kimi Delta Attention kernels FlashKDA: Flash Kimi Delta Attention — high-performance KDA kernels built on CUTLASS - **2026-04-22** — Deep-Dive Blog: the design decisions behind FlashKDA v1, read it [here](docs/20260420-flashkda-v1-deep-dive.md). - SM90 and above - CUDA 12.9 and above - PyTorch 2.4 and above git clone https://github.com/MoonshotAI/FlashKDA.git flash-kda cd flash-kda git submodule update --init --recursive pip install -v --no-build-isolation . By default, the build detects the current CUDA device and compiles for that architecture. For wheel or CI builds, compile all supported architectures explicitly: FLASH_KDA_CUDA_ARCHS=all pip install -v --no-build-isolation . Supported values are `auto` (default), `all`, or a comma-separated arch list such as `90a,100a`. Once installed, FlashKDA is auto-dispatched from `flash-linear-attention`'s `chunk_kda`. See [fla-org/flash-linear-attention#852](https://github.com/fla-org/flash-linear-attention/pull/852) for integration details. **Requirements** 1. Install `flash-linear-attention >= 0.5.0`: pip install -U flash-linear-attention 2. Call `chunk_kda` under `torch.inference_mode()` import torch from fla.ops.kda import chunk_kda with torch.inference_mode(): out, final_state = chunk_kda( q=q, k=k, v=v, g=g, beta=beta, scale=scale, initial_state=h0, output_final_state=True, use_gate_in_kernel=True, use_qk_l2norm_in_kernel=True, use_beta_sigmoid_in_kernel=True, safe_gate=True, A_log=A_log, dt_bias=dt_bias, lower_bound=lower_bound, transpose_state_layout=True,

### 4. MoonshotAI/checkpoint-engine（1,004★）

- 链接：https://github.com/MoonshotAI/checkpoint-engine
- 主题：
- 最近推送：2026-09-15
- 摘要来源：feed | 翻译：llm
- 中文简介：Checkpoint-engine 是一个简单的中间件，用于更新 LLM 推理引擎中的模型权重。
- 原文简介：Checkpoint-engine is a simple middleware to update model weights in LLM inference engines

### 5. MoonshotAI/Kimi-Vendor-Verifier（154★）

- 链接：https://github.com/MoonshotAI/Kimi-Vendor-Verifier
- 主题：
- 最近推送：2026-09-17
- 摘要来源：readme_head | 翻译：llm
- 中文简介：Kimi-Vendor-Verifier English | [中文](README_zh.md) 按提交时间顺序列出。 model: kimi-k3 thinking effort: max uv sync && uv pip install -e . export KIMI_API_KEY="your-api-key" export KIMI_BASE_URL="your-base-url" 或者将 `.env.example` 复制为 `.env` 并填写配置。 在运行基准测试之前，请先完成 API 参数、tool-call schema、K3 特性以及 prompt-token 的预检（pre-flight checks）。 验证 API 是否正确约束了 `temperature`、`top_p`、`presence_penalty`、`frequency_penalty` 和 `n` 等不可变参数。 uv run pytest tests/params --smoke-model kimi/your-model-id --think-mode kimi -v uv run pytest tests/params --smoke-model your-model-id --think-mode opensource -v 只有在所有测试通过后，才能运行正式的基准测试。 验证供应商能否将 walle-valid 的 MFJS schema 用作 tool-call 的 `parameters`，并返回符合该 schema 的 `tool_calls[].function.arguments`。 uv run pytest -n 4 tests/tool_call_json_schema \ --base-url "${KIMI_BASE_URL}" \ --api-key "${KIMI_API_KEY}" \ --smoke-model "${MODEL_NAME}" \ --think-mode "$THINK_MODE" \ --thinking \ --reruns 3 \ --reruns-delay 2 \ --tool-json-report=tool-call-schema-report.json \ -ra -v 此检查会运行 walle 的 `valid.jsonl` 用例，将每个 schema 作为 `tools[].function.parameters` 发送，强制触发一次工具调用，并在本地使用 `jsonschema` 验证返回的 `function.arguments`。每个选定的用例分别以 `stream=false` 和 `stream=true` 各运行一次；流式返回的分块会在验证前重新组装。在 GitLab CI 中，此检查作为 `verify_tool_call_json_schema` 任务运行，并应用相同的重试选项。除 JUnit XML 报告外，还会生成一份 JSON 报告（`tool-call-schema-report.json`），其中包含选定的用例、每个用例的结果，以及与原始独立脚本在日志末尾打印的内容相同的 `summary` 块（total / by_status / by_selection_reason / by_mode）。
- 原文简介：Kimi-Vendor-Verifier English | [中文](README_zh.md) Listed in the order of submission time. model: kimi-k3 thinking effort: max uv sync && uv pip install -e . export KIMI_API_KEY="your-api-key" export KIMI_BASE_URL="your-base-url" Or copy `.env.example` to `.env` and fill in the configuration. Before running benchmarks, complete the API parameter, tool-call schema, K3 feature, and prompt-token pre-flight checks. Validate that the API correctly constrains immutable parameters such as `temperature`, `top_p`, `presence_penalty`, `frequency_penalty`, and `n`. uv run pytest tests/params --smoke-model kimi/your-model-id --think-mode kimi -v uv run pytest tests/params --smoke-model your-model-id --think-mode opensource -v Run formal benchmarks only after all tests pass. Validate that the vendor can use walle-valid MFJS schemas as tool-call `parameters` and return `tool_calls[].function.arguments` that conform to the schema. uv run pytest -n 4 tests/tool_call_json_schema \ --base-url "${KIMI_BASE_URL}" \ --api-key "${KIMI_API_KEY}" \ --smoke-model "${MODEL_NAME}" \ --think-mode "$THINK_MODE" \ --thinking \ --reruns 3 \ --reruns-delay 2 \ --tool-json-report=tool-call-schema-report.json \ -ra -v This check runs walle `valid.jsonl` cases, sends each schema as `tools[].function.parameters`, forces a tool call, and uses `jsonschema` to validate the returned `function.arguments` locally. Each selected case is run once with `stream=false` and once with `stream=true`; streaming chunks are reassembled before validation. In GitLab CI, this check runs as the `verify_tool_call_json_schema` job; the same retry options are applied. In addition to the JUnit XML report, a JSON report (`tool-call-schema-report.json`) is produced containing the selected cases, per-case outcomes, and the same `summary` block (total / by_status / by_selection_reason / by_mode) that the original standalone script printed at the end of its log.

### 6. MoonshotAI/walle（30★）

- 链接：https://github.com/MoonshotAI/walle
- 主题：
- 最近推送：2026-09-15
- 摘要来源：readme_head | 翻译：llm
- 中文简介：一个 Moonshot AI 风格的 JSON schema 校验器。 主要入口是 `walle.go`，它提供两个核心 API： - `ParseSchema`：解析输入的 JSON schema 字符串并创建 walle schema 实例 - `Schema.Validate`：使用可选配置校验 schema - 校验级别： - **ultra** / **default**：最全面的校验，包含一些可能“无害”的检查（例如不允许重复项）。 - **strict**：Moonshot AI 服务器为实现高效结构化生成所需的最宽松级别。 - **lite**：跳过 **strict** 强制执行的规则中的一部分。 - **loose**：跳过 `Schema.Validate` 中的 schema 校验，更多依赖模型自身的能力。 go install github.com/moonshotai/walle/cmd/walle@latest walle -schema '{"type": "object"}' -level strict walle -schema-file your_schema.json import "github.com/moonshotai/walle"  // 定义你的 JSON schema schemaStr := `{ "type": "object", "properties": { "name": {"type": "string"}, "age": {"type": "integer"} }, "required": ["name"] }`  // 创建 schema 实例 schema, err := walle.ParseSchema(schemaStr) ... // 使用默认选项校验 schema err = schema.Validate() ... // 规范化 JSON 字符串 canonicalJSON, warnErr := schema.Canonical() // 使用自定义选项校验 schema err = schema.Validate( 	walle.WithValidateLevel(walle.ValidateLevelStrict), ) ... Python 接口打包为 `walle`。发布的 wheel 包中包含 `libwalle.so`，因此用户安装 wheel 后即可直接导入。
- 原文简介：A Moonshot AI flavored Json schema validator. The main entry point is `walle.go`, which provides two core APIs: - `ParseSchema`: Parses input JSON schema string and creates a walle schema instance - `Schema.Validate`: Validates the schema with optional configurations - Validation levels: - **ultra** / **default**: Most comprehensive validation including potentially "harmless" checks (e.g., no duplicate items). - **strict**: The most permissive level required by Moonshot AI server for efficient structured generation. - **lite**: Skips a subset of rules that **strict** enforces. - **loose**: Skips schema validation in `Schema.Validate` and relies more on model capabilities. go install github.com/moonshotai/walle/cmd/walle@latest walle -schema '{"type": "object"}' -level strict walle -schema-file your_schema.json import "github.com/moonshotai/walle" // Define your JSON schema schemaStr := `{ "type": "object", "properties": { "name": {"type": "string"}, "age": {"type": "integer"} }, "required": ["name"] }` // Create a schema instance schema, err := walle.ParseSchema(schemaStr) ... // Validate the schema with default options err = schema.Validate() ... // Canonical JSON string canonicalJSON, warnErr := schema.Canonical() // Validate the schema with custom options err = schema.Validate( walle.WithValidateLevel(walle.ValidateLevelStrict), ) ... The Python interface is packaged as `walle`. Release wheels include `libwalle.so`, so users can import it directly after installing the wheel.

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 0 | 计数 |
| 输入 tokens | 0 | GLM usage（精确） |
| 输出 tokens | 0 | GLM usage（精确） |
| 合计 tokens | 0 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 6 次（限额 60/时，未认证） | 计数 |
| 总耗时（获取→生成） | 16 秒 | 计时，统计系统占用时间 |
