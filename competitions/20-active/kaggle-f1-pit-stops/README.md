# 比赛卡片：Predicting F1 Pit Stops

## 快照

| 字段 | 内容 |
|---|---|
| 平台 | Kaggle Playground |
| 官方链接 | https://www.kaggle.com/competitions/playground-series-s6e5 |
| 来源核验时间 | 2026-05-14 |
| 优先级 | P1 |
| 状态 | active |
| 截止时间 | 调研日显示 18 days to go；保守按 2026-06-01 规划，开工第一步需登录 Kaggle 规则页复核 |
| 参赛资格 | 开放参赛 |
| 队伍规则 | Kaggle 账号参赛；调研记录显示队伍上限 3 人；提交前复核地区和队伍规则 |
| 8GB 可行性 | A 本地可做 |
| 方向 | 表格 / 预测 / 轻量算法 |

## 为什么值得关注

- 作为第二并行线，用来快速建立算法赛 baseline、实验记录和提交节奏。
- 表格预测类任务适合 8GB Windows 本地开发，也可迁移到 Kaggle Notebook。
- 截止较近，适合作为“快跑一轮”的纪律训练。

## 交付物

- 可复现的 EDA 和 baseline notebook/script。
- 至少 1 个本地验证方案。
- 至少 1 个可提交文件。
- 实验记录：特征、模型、验证分数、提交分数、结论。

## 前 48 小时目标

- 登录 Kaggle，确认截止时间、评价指标、提交格式和规则。
- 下载数据并做 schema 记录。
- 建立 baseline：缺失值处理、简单特征、LightGBM/CatBoost/sklearn 模型。
- 生成第一次有效 submission。

## 风险

- 当前公开页面不易直接抓取完整规则，进入正式建模前必须登录复核。
- 近截止比赛不应消耗主线 Agent 应用赛的设计和提交时间。
- 需要严格防止数据泄露，尤其是时间或赛事顺序相关特征。

## 当前决策

作为第二 active 比赛推进，但限定范围为轻量 baseline 和一次有效提交，不与 Agent 主线争抢大量工程时间。
