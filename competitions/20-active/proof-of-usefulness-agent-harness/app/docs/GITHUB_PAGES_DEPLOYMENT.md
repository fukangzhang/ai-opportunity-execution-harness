# GitHub Pages 零成本部署流程

## 结论

GitHub Pages 可以满足当前 Proof of Usefulness 的 `Project Homepage URL` 需求，前提是我们把 demo 做成静态可运行版本。

本项目当前采用：

- GitHub Pages 托管 `site/` 静态站点。
- `site/app.js` 在浏览器里执行 harness v0 规则。
- `site/samples/*.md` 提供真实样例。
- `site/assets/pou-demo-video.mp4` 提供 75 秒英文演示视频。

这样评委打开页面时可以直接选择样例、粘贴 Markdown、生成结构化机会卡片并下载 JSON。它不是纯展示页，而是一个无需后端的 live demo。

## 为什么不用额外服务器

GitHub Pages 只能托管 HTML、CSS、JavaScript、图片、视频等静态文件，不能直接运行 Python/Streamlit/FastAPI 后端。

但我们的 v0 harness 是规则抽取：

1. 从 Markdown 读取标题、来源、时间窗口。
2. 用关键词判断资格、8GB 可行性和推荐状态。
3. 汇总风险、48 小时计划和证据行。
4. 输出 JSON。

这些逻辑可以完整移植到浏览器端 JavaScript，所以不需要服务器、GPU、数据库或域名。

## GitHub Pages 能提供的 URL

项目页默认 URL：

```text
https://<github-user>.github.io/<repository-name>/
```

本项目计划 URL：

```text
https://fukangzhang.github.io/ai-opportunity-execution-harness/
```

不买域名也可以用。自定义域名只是可选项，不是比赛提交的必要条件。

## 当前仓库结构

```text
site/
  index.html
  styles.css
  app.js
  assets/
    pou-demo-video.mp4
    proof-analysis.png
    save-run-log.png
  samples/
    proof-of-usefulness.md
    microsoft-agent-academy.md
    kaggle-f1-pit-stops.md
    internal-rag-support-bot.md

.github/workflows/pages.yml
```

## 本地验证

在仓库根目录运行：

```powershell
cd site
python -m http.server 8091
```

浏览器打开：

```text
http://localhost:8091/
```

检查：

- 页面能打开。
- 视频能加载。
- 默认样例能自动分析。
- 切换样例后结果会更新。
- 点击 `Analyze` 能重新生成卡片。
- 点击 `Download JSON` 能下载当前卡片。

## 发布步骤

### 1. 创建公开 GitHub 仓库

```powershell
gh repo create fukangzhang/ai-opportunity-execution-harness --public --source . --remote origin
```

如果远端已经存在，则改为：

```powershell
git remote add origin https://github.com/fukangzhang/ai-opportunity-execution-harness.git
```

### 2. 提交代码

```powershell
git add .gitignore .github site competitions docs scripts README.md claude-progress.txt competition_matrix.csv AGENTS.md ARCHITECTURE.md WORKFLOW.md
git commit -m "Build Proof of Usefulness live demo"
```

### 3. 推送到远端 main

当前本地分支可以继续叫 `competition/proof-of-usefulness-agent-harness`。为了让 GitHub Pages workflow 在 `main` 上运行，可以把当前 HEAD 推到远端 `main`：

```powershell
git push -u origin HEAD:main
```

### 4. 启用 GitHub Pages Actions

仓库已包含：

```text
.github/workflows/pages.yml
```

这个 workflow 会在 `main` 更新时上传 `site/` 文件夹并部署到 GitHub Pages。

如果 GitHub 没有自动启用 Pages，需要在网页上检查：

```text
Repository -> Settings -> Pages -> Build and deployment -> Source: GitHub Actions
```

### 5. 查看部署状态

```powershell
gh run list --workflow pages.yml --limit 5
gh run watch
```

部署成功后，GitHub Pages 会生成：

```text
https://fukangzhang.github.io/ai-opportunity-execution-harness/
```

也可以用：

```powershell
gh api repos/fukangzhang/ai-opportunity-execution-harness/pages
```

查看 `html_url`。

## 更新页面

后续改代码或替换视频：

```powershell
git add site competitions/20-active/proof-of-usefulness-agent-harness
git commit -m "Update demo site"
git push origin HEAD:main
```

GitHub Actions 会自动重新部署。

## 注意事项

- GitHub Pages 不适合需要私密 API key 的功能。浏览器端代码会公开给所有人。
- 当前 v0 静态 demo 不调用模型 API，所以没有密钥泄露风险。
- 如果后续加入 LLM 抽取，需要改成后端部署，例如 Streamlit Community Cloud、Hugging Face Spaces、Render、Cloudflare Workers 或 Vercel Serverless。
- GitHub Pages 默认地址已经足够提交；自定义域名只是品牌增强，不是必需。

## 来源

- GitHub Pages 创建站点官方文档：https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- GitHub Pages 自定义域名官方文档：https://docs.github.com/github/working-with-github-pages/managing-a-custom-domain-for-your-github-pages-site
- Proof of Usefulness 官方站：https://proofofusefulness.com/
- Proof of Usefulness 提交页：https://proofofusefulness.com/submit
