# 演示视频脚本与分镜

## 调研结论

已安装并使用 HyperFrames skill 制作可复现演示视频工程。当前流程不再依赖纯手录：用 Browser/截图验证界面，用 HyperFrames 组织分镜、字幕、旁白和动画，再渲染 MP4。

参考社区最佳实践：

- Devpost 建议提前规划视频，写脚本，并在有限时间内讲清 what / why / how；多数 hackathon 视频少于 3 分钟。
- Devpost 的演示建议强调：先快速设定问题，再展示可工作的项目，最后讲潜力和影响。
- Devpost 模板提交建议 demo around 3 minutes，包含挑战、解决方式、技术、遇到的问题、最自豪的点，并展示项目功能。
- YC Demo Day 指南强调早讲清“做什么、为谁做”，少用行话，反复练习并删掉不必要内容。
- 产品发布社区常用 45-75 秒结构：开头 3-5 秒直接展示问题或结果，中段展示 2-3 个核心工作流，结尾给 CTA；视频要在静音时也能看懂。

本项目采用两版脚本：

- `75 秒主视频`：用于 Proof of Usefulness / 产品主页 / 社区传播。
- `3 分钟扩展版`：用于评审需要更多技术和证据时。

## 75 秒主视频

### 目标

让评审在 75 秒内看懂：这个工具帮开发者和小团队在投入开发前判断 AI 机会是否值得做，并且每个判断都有证据。

### 旁白稿

**0-5 秒：Hook**

> Before building an AI project, the expensive mistake is choosing the wrong opportunity.

屏幕：展示一句字幕“Stop building the wrong AI project.”，随后切到 UI。

**5-15 秒：问题**

> Hackathons, bounties, and internal AI ideas all hide important constraints: eligibility, deadlines, platform lock-in, hardware needs, and unclear deliverables.

屏幕：文本框中出现 Proof of Usefulness 规则片段。

**15-35 秒：核心工作流 1，正向机会**

> I paste a real opportunity brief. The harness turns it into a structured card: recommendation, eligibility, 8GB feasibility, risks, and a 48-hour plan.

屏幕：选择 `proof-of-usefulness.md`，展示 `主线推进`、`开放参赛`、`B API/云端`、时间窗口和风险。

**35-50 秒：核心工作流 2，反例识别**

> It also prevents bad starts. A Microsoft Agent Academy sample is open to join, but the tool flags Copilot Studio and M365 lock-in, so we keep it as reference instead of making it the main project.

屏幕：切换到 `microsoft-agent-academy.md`，展示 `reference` 和生态绑定风险。

**50-62 秒：核心工作流 3，扩展到非比赛场景**

> The same workflow works beyond competitions. An internal RAG support bot idea becomes a candidate with missing evidence and next steps.

屏幕：切换到 `internal-rag-support-bot.md`，展示 candidate、API/云端和证据行。

**62-70 秒：Proof of Usefulness**

> Every output keeps evidence lines and can be saved as JSON plus a run log. That makes decisions auditable, not just persuasive.

屏幕：点击“保存 JSON 和运行日志”，展示保存成功提示。

**70-75 秒：CTA**

> AI Opportunity Execution Harness: define the evidence before you build.

屏幕：展示项目名、GitHub URL、demo URL。当前 URL 待部署后替换。

### 屏幕字幕

- Stop building the wrong AI project.
- Paste an opportunity brief.
- Get feasibility, risks, evidence, and a 48-hour plan.
- Detect platform lock-in before it costs you days.
- Save auditable run logs.
- Define the evidence before you build.

## 3 分钟扩展版

### 结构

| 时间 | 内容 | 画面 |
|---|---|---|
| 0:00-0:15 | 问题：AI 机会太多，约束隐藏在规则里 | 首页 UI + 文本输入 |
| 0:15-0:35 | 用户：独立开发者、小团队、内部创新团队 | 简短字幕，不做幻灯片堆叠 |
| 0:35-1:05 | 正向机会：Proof of Usefulness | 选择样例，展示 active / 8GB / deadline |
| 1:05-1:35 | 反例：Microsoft Agent Academy | 展示 reference 和生态绑定风险 |
| 1:35-2:00 | 非比赛：Internal RAG Support Bot | 展示 candidate 和缺失证据 |
| 2:00-2:25 | 原理：Markdown -> schema -> card -> run log | 展示 JSON、证据行号、运行日志 |
| 2:25-2:45 | 有用性证据：真实决策、截图、日志 | 展示 `run-logs/` 和 `screenshots/` |
| 2:45-3:00 | 下一步：LLM 抽取、部署、更多样例 | 项目名 + GitHub / demo URL |

### 3 分钟旁白稿

> AI builders often lose time before they write any serious code. The problem is not just implementation. It is choosing the wrong opportunity: a hackathon that quietly depends on a closed platform, an idea that needs data nobody can provide, or a project that cannot run in the available hardware.
>
> AI Opportunity Execution Harness helps independent builders and small teams decide whether an AI opportunity is worth pursuing before they spend days building in the wrong direction.
>
> Here is the core workflow. I paste a real opportunity brief, starting with Proof of Usefulness itself. The app extracts the source, timeline, eligibility, 8GB Windows feasibility, risks, evidence lines, and a 48-hour plan. The recommendation is active, but it still warns that sponsor technologies may influence prizes and that we need a live URL, GitHub repo, and verifiable usage evidence.
>
> Now a counterexample. Microsoft Agent Academy is open to join, but the rules and ecosystem are centered on Microsoft products, especially Copilot Studio and M365 workflows. The harness marks it as reference, not active. That single decision saves us from building a platform-config demo that would not become reusable code.
>
> The same workflow is not limited to competitions. Here is an internal RAG support bot idea. The harness marks it as candidate, because it needs real documents and a reviewer for answer quality before it deserves an implementation sprint.
>
> Under the hood, the first version is intentionally simple: Markdown in, a structured schema out. The schema keeps fields stable. Evidence lines make the output auditable. Run logs preserve the exact input and output, so this is not just an opinion generator.
>
> The usefulness is already visible in this repository. It helped choose Proof of Usefulness as the main target, reject a Copilot Studio-locked path, generate a first execution plan, and save screenshots and logs for review.
>
> The next version will add LLM extraction while keeping schema validation and human review. The principle stays the same: define the evidence before you build.

## 拍摄顺序

1. 打开本地 demo。
2. 展示 `proof-of-usefulness.md` 输出。
3. 切换到 `microsoft-agent-academy.md`，展示 reference 和风险。
4. 切换到 `internal-rag-support-bot.md`，展示非比赛 candidate。
5. 点击保存日志。
6. 展示 `app/out/`、`app/run-logs/`、`app/docs/screenshots/`。
7. 结尾展示提交页需要的项目名、简介、demo URL、GitHub URL。

## 待替换占位

- Demo URL：部署完成后替换。
- GitHub URL：推送公开仓库后替换。
- 最终视频链接：当前已生成本地 MP4，上传后替换为公开视频 URL。

## HyperFrames 产物

- 视频工程：`competitions/20-active/proof-of-usefulness-agent-harness/video/pou-demo-video/`
- 标准质量 MP4：`competitions/20-active/proof-of-usefulness-agent-harness/video/pou-demo-video/renders/pou-demo-video.mp4`
- 流程说明：`app/docs/HYPERFRAMES_DEMO_VIDEO_WORKFLOW.md`

## 来源

- Devpost: https://info.devpost.com/blog/6-tips-for-making-a-hackathon-demo-video
- Devpost: https://info.devpost.com/blog/how-to-present-a-successful-hackathon-demo
- Devpost template: https://devpost.com/software/example-template-submission
- Y Combinator: https://www.ycombinator.com/blog/guide-to-demo-day-pitches
- DemoPolish: https://demopolish.com/blog/product-demo-product-hunt-launch/
