# AI 机会可行性与执行助手

这是 Proof of Usefulness 参赛项目的最小产品骨架。第一版目标不是做复杂 Agent，而是先把“AI 机会说明 / 比赛规则 Markdown -> 结构化判断 -> 48 小时计划”的闭环跑通。

## 当前能力

- 读取 `samples/` 下的真实机会样例。
- 抽取来源、资格、截止时间、8GB 可行性、生态绑定风险。
- 生成统一 JSON，后续可转成 `README.md`、`evidence.md`、`plan.md`。
- 对学生限定、强生态绑定、8GB 不友好的机会给出降级理由。

## 运行

安装依赖：

```powershell
python -m pip install -r .\app\requirements.txt
```

启动 UI：

```powershell
python -m streamlit run .\app\streamlit_app.py
```

运行 CLI：

```powershell
python .\app\src\harness.py --input .\app\samples\proof-of-usefulness.md --output .\app\out\proof-of-usefulness.json
```

批量跑样例：

```powershell
python .\app\src\harness.py --all-samples
```

## 下一步

- 把规则抽取从关键词启发式升级为 LLM + schema 校验。
- 增加证据片段定位，输出每个判断来自哪一行。
- 增加 Streamlit UI，用于粘贴官网规则或 AI idea 并人工复核。
- 保存每次运行日志，形成 Proof of Usefulness 的真实使用证据。
