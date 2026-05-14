# Predicting F1 Pit Stops 执行计划

## 本轮目标

在 2 到 3 天内完成一次可复现 baseline 和有效 Kaggle 提交，沉淀算法赛通用流程。

## 工作边界

- 只做轻量表格建模，不引入重深度学习。
- 优先本地可跑；需要时再迁移 Kaggle Notebook。
- 只修改本比赛目录及后续明确创建的数据/实验目录。

## 里程碑

| 日期 | 目标 | 证据 |
|---|---|---|
| 2026-05-14 | 完成 active 工作区和规则复核清单 | README、plan、evidence |
| 2026-05-15 | 数据下载、EDA、baseline v0 | notebook/script、schema |
| 2026-05-16 | 第一次有效提交 | submission 文件、分数记录 |
| 2026-05-17 | 一轮特征改进 | 实验记录和结论 |

## Baseline 策略

1. 读入 train/test/sample submission。
2. 建立 schema、缺失值和目标分布报告。
3. 用简单数值/类别处理跑第一个模型。
4. 做 3 到 5 折交叉验证或按赛事时间顺序切分。
5. 保存每次实验配置、分数和提交文件。

## 当前下一步

1. 登录 Kaggle 复核规则。
2. 下载数据到本地未提交目录或 Kaggle Notebook。
3. 新建 `experiments.md` 记录第一轮 baseline。
