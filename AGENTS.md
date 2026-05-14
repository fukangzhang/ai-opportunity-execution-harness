# AGENTS.md

## 项目

- 名称：AI 比赛调研与执行 Harness
- 目标：长期维护有真实来源支撑的比赛库，并把选中的比赛推进成可执行项目工作区。
- 当前优先级：AI 应用 / Agent / RAG 优先；轻量表格、时序、传统算法赛作为第二主线。

## 目录

- `docs/registry/competition-index.md`：人类可读的比赛总索引。
- `competition_matrix.csv`：保留为机器可读数据源，不作为主要阅读入口。
- `competitions/00-inbox/`：新发现、未分流的比赛。
- `competitions/10-candidates/`：认真考虑但尚未开做的候选比赛。
- `competitions/20-active/`：正在实际推进的比赛。
- `competitions/30-watchlist/`：未来跟踪、周期性平台、暂未开放的比赛。
- `competitions/80-rejected/`：已排除但保留原因的比赛。
- `competitions/90-archived/`：已完成、过期或中止的比赛。

## 命令

- `pwsh scripts/check-env.ps1`：检查 PowerShell 7 和项目根目录。
- `pwsh scripts/export-competition-index.ps1`：从 CSV 重新生成 Markdown 索引。
- `pwsh scripts/check-registry.ps1`：检查比赛库必要字段。

## 规则

- 每个比赛条目至少要有一个真实来源链接。
- 参赛资格必须记录为：`开放参赛`、`企业/组织限定`、`邀请制`、`未知` 之一；学生限定比赛不进入比赛库。
- 一旦确认比赛限制在读学生参赛，直接排除，不放入候选、观察或 active。
- 每个候选比赛必须标注 8GB Windows 可行性：`A 本地可做`、`B API/云端`、`C 平台 Notebook`、`D 不建议主攻`。
- 面向人阅读的资料优先使用 Markdown；CSV 只作为数据交换格式。
- Windows 环境使用 PowerShell 7（`pwsh`）。
- Markdown、CSV、脚本统一使用 UTF-8。
- 准备提交 GitHub 的改动使用功能分支，规则见 `docs/GIT_WORKFLOW.md`。
- 先定义证据，再开始构建；质量策略见 `docs/QUALITY.md`。

## 会话流程

1. 开始前阅读 `claude-progress.txt` 和 `docs/exec-plans/active/`。
2. 新发现比赛先放入 `competitions/00-inbox/`。
3. 只有记录了资格、截止时间、来源和 8GB 可行性后，才移动到 `10-candidates`。
4. 只有决定实际开做后，才移动到 `20-active`。
5. 修改 `competition_matrix.csv` 后，要更新 `docs/registry/competition-index.md`。
6. PR 或交接前运行 `pwsh scripts/check-env.ps1` 和 `pwsh scripts/check-registry.ps1`。
7. 结束前更新 `claude-progress.txt`。

## 已知坑

- 不要保留学生限定比赛的任何条目，避免污染从业人员可参赛决策。
- 不要优先冲需要多卡、大显存或专用硬件的大模型训练赛。
- 有官方比赛页时，不要只依赖聚合站信息。
