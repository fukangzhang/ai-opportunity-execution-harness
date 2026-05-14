# 完成度审计

审计日期：2026-05-14。

## 目标拆解

原目标：调研 AI 相关比赛生态，重点关注 AI 应用方向，同时覆盖时序、气象、多模态等方向；基于真实来源整理到 `D:\project` 下，形成后续选赛与排期可用的资料沉淀。

成功标准：

1. 文件位于 `D:\project` 下。
2. 有总览判断，能说明优先方向。
3. 重点覆盖 AI 应用方向。
4. 覆盖时序/表格算法赛。
5. 覆盖气象/气候/地理空间方向。
6. 覆盖多模态方向。
7. 纳入 8GB Windows 显存约束。
8. 来源来自真实网页/平台，并可追溯。
9. 能支持后续选赛和排期。

## 需求到产物检查表

| 要求 | 证据 | 状态 |
|---|---|---|
| 放在 `D:\project` 下 | `D:\project\ai-competition-research` 包含 README、矩阵、来源、行动清单、方向雷达 | 已完成 |
| AI 相关比赛生态 | `competition_matrix.csv` 覆盖 Kaggle、DrivenData、Zindi、AIcrowd、天池、DataFountain、讯飞、华为云、百度 CTI、CCF BDCI、ECMWF、ITU 等 | 已完成 |
| AI 应用方向优先 | `README.md` 和 `docs/registry/direction-radar.md` 均将 Agent/RAG/应用赛列为最高优先级 | 已完成 |
| 时序方向 | `competition_matrix.csv` 含 Store Sales、DengAI、F1 Pit Stops；`direction_radar.md` 有时序/表格策略 | 已完成 |
| 气象方向 | `competition_matrix.csv` 含 ECMWF Code for Earth、AI Weather Quest、CMA 示范计划、GeoAI、AI and Space Computing；`direction_radar.md` 有气象策略 | 已完成 |
| 多模态方向 | `competition_matrix.csv` 含 BirdCLEF+、数字中国多模态、AICAS VLM、DataFountain 具身多模态、讯飞多模交互；`direction_radar.md` 有多模态策略 | 已完成 |
| 8GB Windows 显存约束 | `README.md` 有 A/B/C/D 可做性规则；矩阵含 `8gb_fit` 列；`direction_radar.md` 有每方向显存风险 | 已完成 |
| 真实资料 | `docs/sources/index.md` 列出官方/平台/赛事页链接；矩阵每行含 source | 已完成 |
| 后续选赛与排期 | `docs/exec-plans/active/next-actions.md` 有确认事项、主线建议、本周排期；矩阵含优先级、截止窗口、建议 | 已完成 |

## 剩余不确定性

- 部分国内平台页面会动态变化，后续需要每周更新报名状态。
- 学生限定赛已从主矩阵和索引中移除，后续确认此类限制时直接排除。
- 一些镜像页来自赛事聚合站，最终报名仍应回到官方比赛页核验。
