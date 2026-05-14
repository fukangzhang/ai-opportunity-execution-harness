# 下一步行动清单

调研日期：2026-05-14。

## 已确认的推进方式

- 主线 active：Microsoft Agent Academy Hackathon。
- 第二 active：Kaggle Predicting F1 Pit Stops，定位为轻量算法 baseline 和提交练习。
- 并行方式：每个比赛使用独立 Git 分支和独立 worktree，避免两个 Codex 对话框在同一个工作区反复切分支。

## 仍需确认的事

1. 是否愿意参加 2026-05 下旬前截止的短冲刺赛。  
   影响：Gemma 4 Good、DJI 机载 AI 应用挑战。

2. 方向来者不拒时，默认按“开放资格 + 可快速提交 + 8GB 友好”排序。  
   法律/政务、企业数据分析、教育、工业制造、交通、气象/时序、多模态都纳入候选。

## 建议主线

### 主线 A：AI 应用赛

目标：2 周内做出一个可演示的 AI 应用模板，后续换题即可复用。

最适合的候选：

- Microsoft Agent Academy Hackathon：2026-05-12 到 2026-06-02。
- Kaggle 5-Day AI Agents：2026-06-15 到 2026-06-19，适合练手。
- DJI 机载 AI 行业应用挑战：提交方案截止 2026-05-31，适合方案+demo。

通用作品模板：

- 前端：Streamlit 或 Next.js。
- 后端：FastAPI。
- 能力：RAG 检索、工具调用、任务分解、结果校验、日志与评测。
- 模型：API 优先；本地只跑小模型或 embedding。
- 8GB 显存策略：不做 7B+ 全量微调，不本地跑大 VLM；需要开源模型时用量化或平台 Notebook。

### 主线 B：轻量算法赛

目标：1 周内完成 baseline + 提交 + 实验记录。

最适合的候选：

- Kaggle Predicting F1 Pit Stops：调研日显示 18 天后截止。
- Kaggle Store Sales Time Series：长期开放。
- DrivenData Flu Shot / Pump it Up / DengAI：长期练习。
- Kaggle LLM Classification Finetuning：长期开放，适合小模型/特征工程/平台云端。

通用 baseline：

- EDA：缺失值、类别分布、时间泄露检查。
- 模型：LightGBM、XGBoost、CatBoost。
- 验证：时间序列用 time split；普通表格用 KFold/StratifiedKFold。
- 记录：每次实验保存配置、分数、提交文件和结论。

## 本周推荐排期

| 日期 | 动作 | 产出 |
|---|---|---|
| 2026-05-14 | 确认资格和主攻方向 | 已选择 Agent Academy + F1 Pit Stops |
| 2026-05-15 | 建应用赛模板仓库 | 可运行 RAG/Agent demo |
| 2026-05-16 | 选题调研和数据准备 | 需求文档 + 数据/知识库 |
| 2026-05-17 | 做第一版可演示产品 | demo v0.1 |
| 2026-05-18 | 完善评测、演示脚本、README | 可提交材料草稿 |
| 2026-05-19 | 如冲 Gemma，完成提交 | 提交包 |
| 2026-05-20 | 复盘并转向下一赛题 | 复盘记录和下一轮计划 |

## 暂不主攻清单

- ARC Prize 2026：研究价值高，但不是最适合第一阶段的应用方向。
- CAFA 6 Protein：领域门槛和数据处理复杂度较高。
- BirdCLEF+ 2026：可学习音频 pipeline，但不建议作为主线。
- 大模型推理优化/AI 芯片/具身抓取类：通常需要平台或专用硬件。
