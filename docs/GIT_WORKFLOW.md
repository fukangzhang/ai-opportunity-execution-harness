# GitHub 工作流

本项目计划提交到 GitHub，因此从一开始就按可协作、可审查、可回滚的方式管理。

## 分支

除紧急文档修正外，不直接在 `main` 上工作。

分支命名：

| 前缀 | 用途 |
|---|---|
| `feat/<short-name>` | 新功能、新比赛工作区、新自动化 |
| `fix/<short-name>` | 修正数据、脚本、文档或流程问题 |
| `docs/<short-name>` | 纯文档修改 |
| `research/<competition-or-platform>` | 来源调研或比赛分流 |
| `chore/<short-name>` | 维护、格式、配置 |

示例：

```plain
feat/agent-academy-workspace
research/iflytek-2026-tracks
fix/eligibility-labels
docs/harness-rules
```

## 多比赛并行

多个比赛同时推进时，默认使用 `git worktree` 给每个比赛分配独立工作目录，避免两个 Codex 对话框在同一个目录里切换分支。

推荐对应关系：

| 比赛 | 分支 | 工作目录 | 主要修改范围 |
|---|---|---|---|
| Agent Academy Hackathon | `competition/agent-academy-hackathon` | `D:\project\ai-competition-research-agent-academy` | `competitions/20-active/microsoft-agent-academy-hackathon/` |
| Predicting F1 Pit Stops | `competition/kaggle-f1-pit-stops` | `D:\project\ai-competition-research-f1-pit-stops` | `competitions/20-active/kaggle-f1-pit-stops/` |

边界规则：

- 每个 Codex 对话框只打开自己的 worktree。
- 比赛专属代码、笔记、提交物只改本比赛目录。
- `competition_matrix.csv`、`docs/registry/competition-index.md`、脚本和模板属于共享区，只有确实需要更新全局状态时才改。
- 两个分支都需要更新共享区时，先在主仓库做协调提交，再让各 worktree rebase 或 merge。
- PR 尽量一赛一 PR；不要把两个比赛的实验代码混在同一个 PR。

## 提交信息

使用 Conventional Commits 风格：

```plain
feat: add agent academy competition workspace
fix: correct student-only eligibility label
docs: add PowerShell 7 environment rules
chore: regenerate competition markdown index
```

每个提交尽量只表达一个清晰目的，方便审查和回滚。

## PR 规则

每个 PR 应包含：

- 本次改动目的；
- 新增或修改比赛事实对应的来源链接；
- 已运行的校验命令；
- 如果涉及 UI / demo，附截图、录屏或渲染结果；
- 风险说明和后续任务。

PR 检查清单：

```markdown
- [ ] 新增/修改的比赛事实都有来源链接。
- [ ] 如果修改了 `competition_matrix.csv`，已更新 `docs/registry/competition-index.md`。
- [ ] 已运行 `pwsh scripts/check-env.ps1`。
- [ ] 已运行 `pwsh scripts/check-registry.ps1`。
- [ ] 已更新 `claude-progress.txt`。
```

## 合并规则

- 小型功能/调研分支优先使用 squash merge。
- 分支合并后删除远端分支。
- 开新分支前先同步最新 `main`。
- 尽量一个活跃比赛对应一个分支。
- 比赛进入实际开发后，创建独立分支，并在 `competitions/20-active/` 下建工作区。

## 首次 Git 初始化建议

只有确定 GitHub 仓库名和远程地址后再执行：

```powershell
git init
git add .
git commit -m "docs: initialize ai competition research harness"
git branch -M main
git remote add origin <github-repo-url>
git push -u origin main
```
