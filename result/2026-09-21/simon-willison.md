# Simon Willison's Web（2026-09-21）

- 生成时间：2026-09-21 06:35
- 数据来源：RSS 订阅（https://simonwillison.net/atom/everything/，最新 N 条）
- 查询条件：`RSS：https://simonwillison.net/atom/everything/`
- 处理方式：摘要级联提取（ADR-0011）→ LLM 翻译（≤5000B，ADR-0010，GLM）；仅存档，未发布

### 1. [引用 voxium 的话](https://simonwillison.net/2026/Sep/20/voxium/)（发布 2026-09-20 21:06）

- 中文简介：我在一家大公司开始新岗位已经半个月了。这里没有人真正了解任何事情。规格说明、代码、测试、PRD、工单、工单的解决记录、报告等等，一切都是由 Claude Code 生成的。我团队里没有人喜欢这种做法。他们被迫尽可能多地交付。我已多次听高层管理层说，推送代码并不是瓶颈，那为什么我们还是这么慢？人们每天工作 12 到 13 个小时，只是为了按一下回车键。没有人阅读任何内容。这里的每个人，真的是每一个人，从 L1 到 L7 工程师，都在做同样的事情：跟 Claude 谈。— voxium 标签：ai-misuse 、 llms 、 ai 、 generative-ai
- 原文简介：It has been half a month since I started a new role at a big company. Nobody knows anything here. The specs, code, tests, PRDs, tickets, resolution of those tickets, reports, etc., everything is made by Claude Code. Nobody on my team likes this. They are being forced to ship as much as they can. I have heard multiple times from higher management that pushing code is not a bottleneck, so why are we slow? People are working 12 to 13 hours a day just to press enter. Nobody is reading anything. Everyone, literally everyone, from an L1 to an L7 engineer here is doing the same thing. Talk to Claude. &mdash; voxium Tags: ai-misuse , llms , ai , generative-ai
- 摘要：feed · 翻译：llm

### 2. [llm-keys-ui 0.1](https://simonwillison.net/2026/Sep/20/llm-keys-ui/)（发布 2026-09-20 19:22）

- 中文简介：发布：llm-keys-ui 0.1 这个插件解决一个非常具体的问题。我开始使用 Codex Remote 在各种机器上运行编码代理，同时通过手机来控制它们。有时我会用这些机器来折腾 LLM 项目，偶尔这就意味着我需要配置 API 密钥。我不喜欢把 API 密钥粘贴到代理会话中，所以我想要一种方法，能把密钥放到机器上，而不必直接粘贴到 ChatGPT 应用里。有了这个插件，我可以让 Codex 运行：uvx --with llm-keys-ui llm keys-ui --all 然后让它告诉我一个 URL——包括局域网或 Tailscale 设备 IP——用于打开保存更多 API 密钥的界面。之后当它需要使用某个密钥时，可以在 shell 命令中使用类似 llm keys get anthropic 的命令。标签：llm , coding-agents , codex
- 原文简介：Release: llm-keys-ui 0.1 This plugin solves a very specific problem. I've started using Codex Remote to run coding agents on various machines while controlling them from my phone. Sometimes I use those machines to hack on LLM projects, and occasionally that means I need to configure an API key. I don't like pasting API keys into agent sessions, so I wanted a way to get those keys onto a machine without pasting them into the ChatGPT app directly. With this plugin, I can tell Codex to run: uvx --with llm-keys-ui llm keys-ui --all Then have it tell me the URL - including local network or Tailscale device IPs - for an interface to save additional API keys. Then later it can use a command like llm keys get anthropic as part of a shell command when it needs to use a key. Tags: llm , coding-agents , codex
- 摘要：feed · 翻译：llm

### 3. [datasette-auth-github 1.0](https://simonwillison.net/2026/Sep/19/datasette-auth-github/)（发布 2026-09-19 19:52）

- 中文简介：发布：datasette-auth-github 1.0 我在 agent.datasette.io 演示站点上运行这个 GitHub 登录插件，并注意到我的已认证会话持续时间不长。原来该插件在设置 cookie 时没有带 Max-Age 参数，因此 cookie 会在浏览器会话结束时过期（在 Mobile Safari 上这种情况似乎发生得相当频繁，与你如何使用该应用无关）。我在 #80 中修复了这个问题，并且由于这个插件已经存在了相当长的时间，同时针对 Datasette 0.65.x 和 Datasette 1.0ax 都进行了测试，我决定将其版本提升到 1.0 发布。我正在努力更好地将稳定的插件提升到 1.0。 标签：github、plugins、datasette
- 原文简介：Release: datasette-auth-github 1.0 I run this GitHub login plugin on the agent.datasette.io demo site and I noticed that my authenticated sessions weren't lasting very long. It turned out that the plugin was setting cookies without a Max-Age parameter, so they were expiring at the end of a browser session (which in Mobile Safari seems to happen pretty often, independently of how you are using the app.) I fixed that in #80 and, since this plugin has been around for quite a while and is tested against both Datasette 0.65.x and Datasette 1.0ax, I decided to bump it up to a 1.0 release. I'm trying to get better at promoting stable plugins to 1.0. Tags: github , plugins , datasette
- 摘要：feed · 翻译：llm

### 4. [California Sea Lion, Brandt's Cormorant](https://simonwillison.net/2026/Sep/19/sighting-401567341/)（发布 2026-09-19 17:10）

- 中文简介：加州海狮、白脸鸬鹚，拍摄于美国加州Pillar Point Harbor。我是拍完照片后才发现的：北方塘鹅Morris正从标牌底座后面探出头来。标签：野生动物
- 原文简介：California Sea Lion, Brandt&#x27;s Cormorant, in Pillar Point Harbor, CA, US I only noticed this after I had taken the photo: Morris the Northern Gannet is peeking out from behind the base of the sign. Tags: wildlife
- 摘要：feed · 翻译：llm

### 5. [Gemini Hacked Three Companies in First Known Breakout by Google’s AI](https://simonwillison.net/2026/Sep/18/gemini-hacked-three-companies/)（发布 2026-09-18 23:57）

- 中文简介：Gemini 黑入三家公司，成为谷歌 AI 首次已知的“越狱”事件 Gemini 终于在 Felony Bench 上追平了！谷歌于周五确认了这些黑客攻击事件，它们发生在五月，是 Irregular 公司一项测试运行的一部分，该公司也参与了 OpenAI、Anthropic 和 Meta 此前披露的类似事件。在其中一起事件中，该模型不断猜测密码，直到成功访问了一个受保护的系统。在另外两起事件中，该模型在一个公开仓库中找到了凭据，从而得以访问受保护的系统。谷歌表示，在每起事件中，该模型在确定自己访问的是真实公司的系统后，便终止了入侵。显然，Gemini 的“决心”不如其他模型，决定不再继续下去。谷歌早在七月就已知晓这些事件，但选择不予披露，直到《华尔街日报》（WSJ）——推测是收到线报——联系询问。谷歌表示，它认为这些黑客攻击不值得公开披露——因为其模型没有对这些公司造成伤害，并且在确定自己黑入的是真实公司而非模拟环境后，立即终止了每次入侵。标签：security、ai、generative-ai、llms、gemini、accidental-cyberattacks
- 原文简介：Gemini Hacked Three Companies in First Known Breakout by Google’s AI Gemini finally caught up on Felony Bench ! The hacks, which the company confirmed on Friday, occurred in May as part of a test run by the company Irregular, which was also involved in similar incidents disclosed by OpenAI, Anthropic and Meta. In one of the cases, the model guessed passwords until it gained access to a protected system. In the other two cases, the model found credentials in a public repository that allowed it to then access protected systems. In each case, the model ended the intrusion after determining it had accessed a real company’s systems, Google said. Gemini is apparently less determined than other models, and decided not to keep going. Google knew about these in July, but chose not to disclose them until the WSJ reached out, presumably based on a tip. Google said it didn’t consider the hacks to warrant public disclosure—because its model didn’t cause harm to the companies and ended each intrusion immediately upon determining it had hacked a real company rather than a simulated one. Tags: security , ai , generative-ai , llms , gemini , accidental-cyberattacks
- 摘要：feed · 翻译：llm

### 6. [Note on 18th September 2026](https://simonwillison.net/2026/Sep/18/probably-gonna-eat-you/)（发布 2026-09-18 19:21）

- 中文简介：如今，作为一名拒绝觉得LLM有任何有趣之处的计算机科学家，就有点像一位拒绝觉得新开业的侏罗纪公园（Jurassic Park）有任何有趣之处的遗传学家。标签：llms、ai、generative-ai
- 原文简介：Being a computer scientist who refuses to find anything about LLMs interesting right now is a bit like being a geneticist who refuses to find anything interesting about the recently opened Jurassic Park. Skeptical geneticist: "pfft, it's just frog DNA. And they deliberately let them eat people for the marketing." Tags: llms , ai , generative-ai
- 摘要：feed · 翻译：llm

### 7. [Quoting Thariq Shihipar](https://simonwillison.net/2026/Sep/18/thariq-shihipar/)（发布 2026-09-18 19:09）

- 中文简介：我们正在为 Claude Code 添加对 AGENTS.md 的支持。从今天发布的 2.1.277 版本开始，如果某个文件夹中不存在 CLAUDE.md，Claude 将会查找并使用 AGENTS.md。AGENTS.md 支持基于 Claude Code mods 构建，这是我们即将推出的自定义 Claude Code harness 的方式。这是一个内置的 mod，但你也可以按自己的需求构建自定义版本的项目指令。你可以在这里查看该 mod 的源代码！—— Thariq Shihipar，这里有更多 mods  标签：thariq-shihipar、coding-agents、anthropic、claude-code、generative-ai、ai、llms
- 原文简介：We're adding support for AGENTS.md to Claude Code. Starting today in version 2.1.277, if there is no CLAUDE.md in a folder, Claude will check for and use AGENTS.md. AGENTS.md support is built off of Claude Code mods, our upcoming way to customize the Claude Code harness. This is a built-in mod, but you’ll be able to build custom versions of project instructions yourself as you’d like too. You can see the source for the mod here ! &mdash; Thariq Shihipar , there are more mods here Tags: thariq-shihipar , coding-agents , anthropic , claude-code , generative-ai , ai , llms
- 摘要：feed · 翻译：llm

### 8. [The Creative Spirit of Who Framed Roger Rabbit](https://simonwillison.net/2026/Sep/18/the-creative-spirit-of-who-framed-roger-rabbit/)（发布 2026-09-18 14:36）

- 中文简介：我爱《谁陷害了兔子罗杰》（Who Framed Roger Rabbit），这部 1988 年由 Robert Zemeckis 执导的电影。我已经好几年没看过它了，而 Cypress Frankenfeld 刚刚指出了电影开头不久的这一段：一只鹈鹕在骑自行车！仔细看你会发现，鹈鹕是动画绘制的，而自行车却是一辆真实的自行车。据说他们往车轮里灌了水以增加稳定性，然后让它行驶起来，并用缆绳加以引导。Cypress 收集了关于这个场景的更多细节。真是妙趣横生。来自 @cypressf.bsky.social  标签：animation、film、pelican-riding-a-bicycle
- 原文简介：The Creative Spirit of Who Framed Roger Rabbit I love Who Framed Roger Rabbit , the 1988 movie by Robert Zemeckis. I haven't watched it in quite a few years, and Cypress Frankenfeld just pointed out this sequence from early in the movie: It's a pelican riding a bicycle! Look closely and you'll note that the pelican is animated while the bicycle is a real bicycle. Apparently they filled the wheels with water to add stability, then set it running and guided it with a cable. Cypress gathered more details on the scene. What a delight. Via @cypressf.bsky.social Tags: animation , film , pelican-riding-a-bicycle
- 摘要：feed · 翻译：llm

### 9. [Be alert: targeted attacks on prominent Rustaceans](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/)（发布 2026-09-17 23:59）

- 中文简介：保持警惕：针对知名 Rustaceans 的定向攻击 来自 Adam Harvey 和 crates 安全团队的重要警告：我们相信，目前存在一场针对 rust-lang 成员和热门 crates 所有者的持续性攻击活动，其目的是入侵设备与账户，以便利用它们发布恶意软件。攻击者会以一些正当的名义安排视频通话——可能是求职、可能是项目合作、也可能是合同机会——然后将视频通话作为攻击载体，要么诱使目标在电脑上安装某些东西（比如据称缺失的音频编解码器），要么执行其他命令（例如，通过将命令放入剪贴板）。上个月，这个伎俩被用于一次成功的供应链攻击，受害者包括 array ref crate 在内的多个 crate。任何依赖开源的软件（几乎涵盖所有软件）背后都有一个由人组成的网络，他们都是潜在的攻击载体——即对该软件依赖网络中任何软件包拥有发布权限的所有人。我想，目前我们最好的防御手段是依赖冷却期（dependency cooldowns）——在升级到新发布的软件包之前先等待几天，希望这样的供应链攻击能被其他人先发现。 标签：开源、安全、rust、供应链、依赖冷却
- 原文简介：Be alert: targeted attacks on prominent Rustaceans Important warning from Adam Harvey and the crates security team: We believe that there is an ongoing campaign targeting rust-lang members and owners of popular crates that is attempting to compromise devices and accounts in order to use them to publish malware. A video call is set up for something positive — maybe for a job, maybe for a project, maybe for a contract opportunity — and then that's used as a vector to either get the target to install something on their computer (such as a purportedly missing audio codec) or execute another command (for example, via putting a command on the clipboard). Last month this trick was used in a successful supply chain attack against the array ref crate , among others. Any piece of software that depends on open source (which is almost every piece of software) has a network of human beings who are potential attack vectors - everyone with publishing rights to any of the packages in the dependency network for that software. I guess our best defense right now is dependency cooldowns - giving new package releases a few days before upgrading to them, in the hope that supply chain attacks like this will be spotted by someone else. Tags: open-source , security , rust , supply-chain , dependency-cooldowns
- 摘要：feed · 翻译：llm

### 10. [How To Write With An LLM](https://simonwillison.net/2026/Sep/17/how-to-write-with-an-llm/)（发布 2026-09-17 23:37）

- 中文简介：Thomas Ptacek 谈论将 LLM 用作文字编辑而非写作助手：第一守则：你不得使用 LLM 建议的任何一个词。[...] 我认为，作为一种智力上的个人防护装备，你应该采纳这样一条规则：LLM 建议的任何具体措辞都属禁区。要严格执行这条规则！我不会让 LLM 为我的博客撰写内容，但我用它们来做事实核查、拼写和语法检查，以及偶尔充当同义词词典（参见我的校对提示词）。绝不使用 LLM 建议的措辞这条规则让我感觉很合心意。这类文本带有那种怪异的味道，而且这也是一条有助于保持自律的好原则。在本文后面，Thomas 展示了他个人 LLM 文字编辑工具的截图（另见这条 Twitter 帖子），并提供了一个提示词，帮助你着手构建自己的工具。标签：thomas-ptacek、writing、ai、generative-ai、llms
- 原文简介：How To Write With An LLM Thomas Ptacek on using LLMs as copyeditors, not as writing assistants: Rule Number One: You may not use a single word an LLM suggests to you. [...] I think that as a form of intellectual personal protective equipment you should adopt the rule that any specific turn of phrase an LLM suggests is off limits. Be strict about the rule! I won't let LLMs write content for my blog, but I use them for fact-checking, spelling and grammar and as an occasional thesaurus (see my proofreading prompt ). The rule to never use a turn of phrase suggested by an LLM feels good to me. The text has that weird smell to it, and it's also a good principle to help stay disciplined. Later in this piece Thomas shows a screenshot of his personal LLM copyediting tool (see also this Twitter thread ), and provides a prompt to help kickstart building your own. Update : Thomas also shared his system prompt in a comment on Hacker News. Tags: thomas-ptacek , writing , ai , generative-ai , llms
- 摘要：feed · 翻译：llm

## 成本与运行统计

| 项目 | 数值 | 来源 |
|---|---|---|
| LLM 调用次数 | 2 | 计数 |
| 输入 tokens | 478 | GLM usage（精确） |
| 输出 tokens | 1,329 | GLM usage（精确） |
| 合计 tokens | 1,807 | GLM usage（精确） |
| 边际费用 | ¥0 | GLM 包月订阅（ADR-0008） |
| GitHub API 调用 | 0 次（限额 60/时，未认证） | 计数 |
| RSS 抓取 | 1 次 | 计数 |
| 总耗时（获取→生成） | 32 秒 | 计时，统计系统占用时间 |
