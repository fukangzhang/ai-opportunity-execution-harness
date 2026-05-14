# Predicting F1 Pit Stops 证据与验收

## 官方规则证据

- 官方页面： https://www.kaggle.com/competitions/playground-series-s6e5
- 核验日期：2026-05-14
- 当前事实：Kaggle Playground 赛，调研日显示进行中且约 18 天后截止；详细截止时间、评价指标和提交格式需要登录 Kaggle 后复核。

## 最小可提交定义

- 能从原始数据生成一次 Kaggle submission。
- 有可复现 baseline 代码。
- 有验证方案和实验记录。
- 明确记录评价指标、泄露风险和提交分数。

## 验收检查

| 项目 | 状态 | 备注 |
|---|---|---|
| 资格确认 | 基本完成 | 提交前复核 Kaggle 通用地区规则 |
| 截止时间确认 | 待做 | 登录规则页确认精确时间 |
| 数据下载 | 待做 | 不提交原始大数据 |
| Baseline 可运行 | 待做 | 优先 LightGBM/CatBoost/sklearn |
| 第一次 submission | 待做 | 保存到 submissions/ |
| 实验记录 | 待做 | 后续补 `experiments.md` |
