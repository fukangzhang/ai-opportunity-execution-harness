# 录制清单

## 当前推荐

优先使用 HyperFrames 生成的视频草版，而不是手动屏幕录制。手录只作为补充，用于替换片段或增加真人讲解。

当前视频产物：

- `competitions/20-active/proof-of-usefulness-agent-harness/video/pou-demo-video/renders/pou-demo-video.mp4`

如果后续部署 URL 和 GitHub URL 确定，先更新 HyperFrames `index.html` 末尾 CTA，再重新渲染。

## 录制前

- 关闭通知和无关应用。
- 浏览器只保留 demo 页面和项目目录页面。
- 浏览器缩放设置为 110% 到 125%，保证录屏压缩后仍能看清字。
- 先跑一次：

```powershell
python .\competitions\20-active\proof-of-usefulness-agent-harness\app\src\harness.py --all-samples
```

- 确认本地 demo 可访问：

```text
http://127.0.0.1:8502
```

## 录制参数

- 分辨率：1080p 起步。
- 画幅：16:9。
- 主视频长度：75 秒。
- 扩展视频长度：不超过 3 分钟。
- 鼠标移动放慢，每个关键结果出现后停 1 到 2 秒。
- 每个 workflow 单独录一段，后期更容易剪。

## 必拍画面

- `proof-of-usefulness.md` 样例输出：active、开放参赛、B API/云端、风险、证据行。
- `microsoft-agent-academy.md` 样例输出：reference、Copilot Studio / M365 生态绑定风险。
- `internal-rag-support-bot.md` 样例输出：candidate、非比赛 AI idea。
- 点击“保存 JSON 和运行日志”后的成功提示。
- `app/out/` JSON 输出文件。
- `app/run-logs/` 运行日志。
- `app/docs/screenshots/` 截图目录。

## 录制后

- 检查静音播放是否能看懂：字幕或画面必须能表达主要价值。
- 开头 5 秒不能是 logo 或自我介绍，必须直接展示问题或结果。
- 删除所有无关等待、登录、刷新、报错片段。
- 导出后把视频链接写回 `submissions/submission-draft.md`。

## 需要用户协作

- 如果要录真人旁白，请用户确认用中文、英文或双语。
- 如果要公开发布，需要用户确认 GitHub 仓库可公开。
- 如果要部署 demo，需要用户协作登录部署平台或提供目标平台。
