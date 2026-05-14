# AI 比赛调研总览

调研日期：2026-05-14  
本地环境约束：Windows，8GB 显存。  
目标：优先寻找适合 AI 应用方向的比赛，同时保留满足算力条件的算法赛，后续按时间、队伍能力和报名条件做取舍。

## 结论先行

最优先方向是“AI 应用 / Agent / RAG / 行业工具 / 数据应用”类比赛。这类比赛更看重问题定义、可用产品、演示、场景落地和工程完整度，8GB 本地显存足够完成大部分前后端、RAG、API 调用、小模型推理和演示工作。

算法赛可以参加，但应优先选 Tabular、传统机器学习、时序预测、文本分类、Text-to-SQL、小型 NLP、轻量 CV。暂不建议把大规模视频、多模态大模型端到端训练、蛋白/基础科学、ARC-AGI 这类重研究赛作为主攻，除非明确允许外部 API、Kaggle Notebook/云端算力，或我们只做轻量 baseline 和学习复盘。

## 8GB 显存筛选规则

| 等级 | 判断 | 适合度 |
|---|---|---|
| A | 本地即可完成，CPU/8GB GPU 足够 | 主攻 |
| B | 本地做工程，模型调用 API 或平台云端 | 主攻 |
| C | 需要 Kaggle/Colab/平台 Notebook，训练受限但可做 baseline | 可参与 |
| D | 需要 16GB+ 显存、多卡、长时间训练或专用硬件 | 不主攻 |

推荐技术栈：

- 应用赛：Next.js / FastAPI / Streamlit / Gradio + RAG + API 模型 + SQLite/Postgres + 向量库。
- 算法赛：LightGBM / XGBoost / CatBoost / sklearn / Prophet 或 darts/nixtla 类时序工具；深度学习只做小模型、LoRA 或推理。
- 大模型赛：优先 API、量化小模型、平台 Notebook；避免本地全量微调 7B+。

方向细分见 [docs/registry/direction-radar.md](D:/project/ai-competition-research/docs/registry/direction-radar.md)。  
人类可读比赛索引见 [docs/registry/competition-index.md](D:/project/ai-competition-research/docs/registry/competition-index.md)。  
参赛资格核验见 [docs/registry/eligibility-review.md](D:/project/ai-competition-research/docs/registry/eligibility-review.md)。
开放资格优先短名单见 [docs/registry/open-target-shortlist.md](D:/project/ai-competition-research/docs/registry/open-target-shortlist.md)。
环境规范见 [docs/ENVIRONMENT.md](D:/project/ai-competition-research/docs/ENVIRONMENT.md)。  
GitHub 工作流见 [docs/GIT_WORKFLOW.md](D:/project/ai-competition-research/docs/GIT_WORKFLOW.md)。  
质量与测试策略见 [docs/QUALITY.md](D:/project/ai-competition-research/docs/QUALITY.md)。
来源索引见 [docs/sources/index.md](D:/project/ai-competition-research/docs/sources/index.md)。  
当前行动清单见 [docs/exec-plans/active/next-actions.md](D:/project/ai-competition-research/docs/exec-plans/active/next-actions.md)。

## 当前第一梯队候选

1. Proof of Usefulness: Tech & AI Hackathon：2026-01-05 到 2026-06-05 滚动提交，技术栈开放，适合做真实有用的 Agent/RAG 工程项目。
2. Google Cloud Rapid Agent Hackathon：2026-05-05 到 2026-06-11，偏 Gemini + Google Cloud + MCP，代码化程度较高但仍有生态绑定。
3. 大疆机载 AI 行业应用创新挑战大赛：方案提交截止 2026-05-31，偏行业应用和边缘智能，适合做“方案 + 可运行 demo”，但硬件和行业理解门槛较高。
4. Kaggle 5-Day AI Agents: Intensive Vibe Coding Course With Google：2026-06-15 到 2026-06-19，偏学习和作品提交，适合作为快速练手。

新增重点跟踪：

- 科大讯飞 AI 开发者大赛：国内 AI 应用和算法赛源，覆盖语音、多模交互、办公娱乐、大模型能力。
- 华为云杯人工智能 OPC 应用创新大赛：偏业务应用与智能开发工具，适合应用方向跟踪。
- CCF BDCI：每年秋季重点关注，真实产业场景强，兼有算法、应用、系统赛题。
- 交通运输大模型智能体创新应用大赛：行业 Agent 应用方向匹配度高。
- ECMWF Code for Earth、GeoAI Challenge、AI Weather Quest：作为气象/地理空间 AI 方向赛源和参考。

## 当前 active 工作区

- [Proof of Usefulness Agent Harness](D:/project/ai-competition-research-proof-of-usefulness-agent-harness/competitions/20-active/proof-of-usefulness-agent-harness/README.md)：主线开放 Agent/RAG 实用产品。
- [Kaggle Predicting F1 Pit Stops](D:/project/ai-competition-research/competitions/20-active/kaggle-f1-pit-stops/README.md)：第二线轻量算法 baseline 和提交练习。

## 算法赛优先策略

可主攻：

- Kaggle Playground / Getting Started：F1 Pit Stops、Store Sales Time Series、LLM Classification Finetuning。
- DrivenData Practice：Flu Shot、Pump it Up、DengAI、文档摘要类 LLM 练习。
- 国内 DataFountain / 天池：重点盯 Text-to-SQL、数据分析应用、时序预测、轻量 NLP、传统机器学习赛题。

谨慎参与：

- Kaggle BirdCLEF+、CAFA、ARC Prize、NVIDIA Nemotron 等。这些比赛含金量高，但对研究能力、算力或领域知识要求更高。
- DataFountain 的大模型微调/推理优化、AI 芯片算子、具身抓取等，通常需要平台或专用硬件，不适合 8GB 本地作为主攻。

## 后续动作

1. 每周固定更新候选矩阵，关注报名截止和新赛题。
2. 先选 1 个应用赛作为主线，再选 1 个轻量算法赛练手。
3. 为应用赛准备通用作品模板：问题调研、产品原型、RAG/Agent 后端、评测脚本、演示视频、答辩 PPT。
4. 为算法赛准备通用 baseline：EDA、CV 划分、LightGBM/XGBoost、提交脚本、实验记录表。
