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
| `competition/<platform>-<slug>` | 已进入 active 的具体比赛推进 |
| `chore/<short-name>` | 维护、格式、配置 |

示例：

```plain
feat/proof-of-usefulness-workspace
research/iflytek-2026-tracks
competition/proof-of-usefulness-agent-harness
fix/eligibility-labels
docs/harness-rules
```

## 多比赛并行

多个比赛同时推进时，默认使用 `git worktree` 给每个比赛分配独立工作目录，避免两个 Codex 对话框在同一个目录里切换分支。

### 这是什么

`git worktree` 不是复制出多个独立仓库，而是让同一个 Git 仓库的不同分支同时出现在不同文件夹里。

当前关系：

```plain
D:\project\ai-competition-research
  main 分支，主线和稳定总账

D:\project\ai-competition-research-proof-of-usefulness-agent-harness
  competition/proof-of-usefulness-agent-harness 分支，开放 Agent/RAG 项目施工现场

D:\project\ai-competition-research-f1-pit-stops
  competition/kaggle-f1-pit-stops 分支，F1 比赛施工现场
```

这些目录看起来都有 `.git`，但不是三份互不相关的仓库。主目录保存真正的 Git 对象库；worktree 目录里的 `.git` 通常只是一个很小的指针文件，指向主仓库 `.git/worktrees/...` 中对应分支的管理信息。

### 为什么这样做

- 两个 Codex 对话框可以分别打开不同目录，各自在自己的分支工作。
- 不需要在同一个目录里反复 `git checkout`，避免一个对话框切分支影响另一个对话框。
- PR 仍然是普通 PR：比赛分支请求合并到 `main`。
- 合并完成后，额外 worktree 只是临时工作目录，可以安全移除。

推荐对应关系：

| 比赛 | 分支 | 工作目录 | 主要修改范围 |
|---|---|---|---|
| Proof of Usefulness Agent Harness | `competition/proof-of-usefulness-agent-harness` | `D:\project\ai-competition-research-proof-of-usefulness-agent-harness` | `competitions/20-active/proof-of-usefulness-agent-harness/` |
| Predicting F1 Pit Stops | `competition/kaggle-f1-pit-stops` | `D:\project\ai-competition-research-f1-pit-stops` | `competitions/20-active/kaggle-f1-pit-stops/` |

边界规则：

- 每个 Codex 对话框只打开自己的 worktree。
- 比赛专属代码、笔记、提交物只改本比赛目录。
- `competition_matrix.csv`、`docs/registry/competition-index.md`、脚本和模板属于共享区，只有确实需要更新全局状态时才改。
- 两个分支都需要更新共享区时，先在主仓库做协调提交，再让各 worktree rebase 或 merge。
- PR 尽量一赛一 PR；不要把两个比赛的实验代码混在同一个 PR。

### 自动创建新比赛工作区

进入 active 的新比赛，优先使用脚本创建分支和 worktree：

```powershell
pwsh scripts/new-competition-worktree.ps1 `
  -Slug <platform-competition-slug> `
  -CreateActiveDirectory
```

默认会创建：

- 分支：`competition/<platform-competition-slug>`
- 工作目录：`D:\project\ai-competition-research-<platform-competition-slug>`
- 比赛目录：`competitions/20-active/<platform-competition-slug>/`

也可以显式指定：

```powershell
pwsh scripts/new-competition-worktree.ps1 `
  -Slug proof-of-usefulness-agent-harness `
  -Branch competition/proof-of-usefulness-agent-harness `
  -WorktreePath D:\project\ai-competition-research-proof-of-usefulness-agent-harness `
  -CompetitionPath competitions/20-active/proof-of-usefulness-agent-harness `
  -CreateActiveDirectory
```

### 合回主线

比赛线开发完成后，在对应 worktree 中提交并推送：

```powershell
git add .
git commit -m "feat: add <competition> baseline"
git push -u origin competition/<platform-competition-slug>
gh pr create --base main --head competition/<platform-competition-slug>
```

PR 合并后，比赛成果进入 `main`。`main` 是最终稳定版本，worktree 只是临时施工现场。

### 清理工作区

确认 PR 已合并、没有未提交改动后，在主仓库运行：

```powershell
git worktree remove ..\ai-competition-research-<platform-competition-slug>
git branch -d competition/<platform-competition-slug>
```

如果远端分支也已合并且不再需要，可以删除远端分支：

```powershell
git push origin --delete competition/<platform-competition-slug>
```

## 提交信息

使用 Conventional Commits 风格：

```plain
feat: add proof of usefulness competition workspace
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
