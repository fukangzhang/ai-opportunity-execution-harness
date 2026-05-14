# Proof of Usefulness Agent Harness 执行计划

## 本轮目标

在 2 到 3 周内完成一个可运行的 AI 机会可行性与执行 Agent：能读取 hackathon、bounty、比赛规则或内部 AI idea，抽取关键事实，判断资源可行性，拆解交付物，生成可执行 sprint plan，并维护证据链。

## 工作边界

- 本比赛对话框只修改 `competitions/20-active/proof-of-usefulness-agent-harness` 及明确约定的比赛专属代码目录。
- 共享文件变更需要单独协调。

## 推荐产品形态

- 前端：Streamlit 或 Next.js，先用 Streamlit 快速成型。
- 后端：FastAPI 或轻量 Python service。
- 数据：Markdown/CSV 作为初始知识源，SQLite 记录比赛、来源、决策和实验日志。
- Agent 能力：RAG 检索、结构化抽取、资格枚举校验、计划生成、人工确认点、失败样例记录。
- 模型：API 优先；本地只跑 embedding、小模型或规则校验。

## 里程碑

| 日期 | 目标 | 证据 |
|---|---|---|
| 2026-05-14 | 新建主线分支和 active 工作区 | README、plan、evidence |
| 2026-05-15 | 完成需求草图和数据 schema | product-spec、schema |
| 2026-05-16 | 完成 demo v0.1 | 可运行本地 demo、截图和操作文档 |
| 2026-05-18 | 加入评测样例、日志、失败处理 | eval cases、run logs |
| 2026-05-22 | 完成公开 README 和演示脚本 | README、demo script |
| 2026-05-29 | 准备提交材料 | video、screenshots、submission notes |

## 当前下一步

1. [x] 新建比赛专属产品目录。
2. [x] 定义最小输入输出 schema。
3. [x] 选 3 个真实比赛作为回归样例。
4. [x] 实现第一个从 Markdown 规则到结构化计划的闭环。
5. [x] 增加 Streamlit UI，支持粘贴规则 Markdown 并展示人工复核点。
6. [x] 准备演示视频脚本、分镜和录制清单。
7. [x] 准备 Proof of Usefulness 提交草稿。
8. [ ] 把关键词启发式升级为 LLM 抽取 + schema 校验。
9. [ ] 准备公开 README、demo URL 和 HackerNoon 文档草稿。
