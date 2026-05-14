# 比赛调研 Harness 架构

本目录借鉴 Harness Engineering 的三层结构：

| Harness 层 | 本项目落地 | 作用 |
|---|---|---|
| GUIDES 指南 | `AGENTS.md`、`ARCHITECTURE.md`、`WORKFLOW.md`、模板 | 告诉后续 AI 会话和人类如何理解、维护、推进比赛库 |
| SENSORS 传感器 | `scripts/check-env.ps1`、`scripts/check-registry.ps1`、人工来源核验、各比赛评测 | 检查环境编码、来源缺失、资格缺失、方向跑偏 |
| MEMORY 记忆 | `claude-progress.txt`、`docs/exec-plans/`、单比赛工作区 | 跨会话保留状态、决策和下一步 |

## 目录模型

```plain
ai-competition-research/
├── AGENTS.md
├── ARCHITECTURE.md
├── WORKFLOW.md
├── README.md
├── claude-progress.txt
├── competition_matrix.csv
├── docs/
│   ├── registry/
│   │   ├── competition-index.md
│   │   └── eligibility-policy.md
│   ├── exec-plans/
│   │   ├── active/
│   │   └── completed/
│   ├── templates/
│   ├── references/
│   └── sources/
│       └── index.md
├── competitions/
│   ├── 00-inbox/
│   ├── 10-candidates/
│   ├── 20-active/
│   ├── 30-watchlist/
│   ├── 80-rejected/
│   └── 90-archived/
└── scripts/
```

## 单比赛工作区约定

每个具体比赛的工作区建议使用以下结构：

```plain
competitions/20-active/platform-slug-competition-slug/
├── README.md              # 一页比赛简报
├── eligibility.md         # 参赛资格和队伍规则
├── plan.md                # 冲刺计划和提交清单
├── sources.md             # 官方链接和来源摘记
├── product/               # 应用赛的产品或演示
├── experiments/           # 算法赛的实验、Notebook、报告
├── submissions/           # 提交包、视频、PPT、表单资料
└── notes/                 # 会议记录、评分标准、想法
```

除非确有必要，不要把大型原始数据直接复制进仓库。优先用 `data/README.md` 记录下载链接、校验值和准备步骤。
