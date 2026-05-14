# 工作流

## 新比赛进入

1. 使用 `docs/templates/competition-card.md`，在 `competitions/00-inbox/<platform>-<slug>/README.md` 新建比赛卡片。
2. 立即记录来源链接。
3. 补齐截止时间、参赛资格、队伍规则、奖金/权益、交付物和 8GB 可行性。

## 分流

调研后把比赛移动到对应目录：

| 目录 | 含义 |
|---|---|
| `10-candidates` | 值得近期认真考虑 |
| `20-active` | 正在实际推进 |
| `30-watchlist` | 平台、周期性赛事、未来关注、暂未开放的比赛 |
| `80-rejected` | 不适合，保留排除原因 |
| `90-archived` | 已完成、已过期、已提交或已中止 |

比赛进入 `20-active` 时，应同步创建独立 Git 分支和 worktree。推荐使用：

```powershell
pwsh scripts/new-competition-worktree.ps1 -Slug <platform-competition-slug> -CreateActiveDirectory
```

每个 active 比赛对应一个 worktree。后续 Codex 对话框只打开自己的 worktree，避免并行比赛互相切换分支或修改同一批文件。

## 立项门槛

比赛进入 `20-active` 前，必须满足：

- 参赛资格与正式队伍身份兼容。
- 截止时间明确且仍可操作。
- 交付物明确。
- 8GB Windows 可行性为 `A`、`B` 或可控的 `C`。
- 能说清前 48 小时要交付什么。

## 学生限定排除规则

如果比赛明确限制在读学生参赛，直接排除。不要放入 `10-candidates`、`20-active` 或 `30-watchlist`，也不要在主仓库中保留该比赛条目。

## 冲刺循环

对正在推进的比赛：

1. 创建或更新 `plan.md`。
2. 开做前先定义证据：指标、演示脚本、冒烟测试或提交文件格式。
3. 先做最小可提交版本。
4. 尽早补评测证据或演示证据。
5. 最终提交材料统一放在 `submissions/`。
6. 提交、过期或中止后写简短复盘，并移动到 `90-archived` 或 `80-rejected`。
