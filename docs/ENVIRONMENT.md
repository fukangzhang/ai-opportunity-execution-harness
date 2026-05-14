# 环境规范

检查日期：2026-05-14。

## Windows Shell

本项目在 Windows 上统一使用 PowerShell 7（`pwsh`）运行脚本和自动化。

当前已确认版本：

```plain
PowerShell 7.6.1
```

原因：

- UTF-8 行为比旧版 Windows PowerShell 更稳定；
- 跨平台行为更接近 Linux/macOS shell；
- JSON、错误处理和现代命令行体验更好；
- Windows 社区最佳实践越来越默认使用 PowerShell 7。

## 编码规则

项目文件默认使用 UTF-8。

如果终端显示中文乱码，先在当前会话执行：

```powershell
$OutputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::InputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
```

Git 中文路径显示建议：

```powershell
git config --global core.quotepath false
```

## 脚本规则

- 优先使用 `pwsh`，避免使用旧版 `powershell.exe`。
- 本地自动化脚本放在 `scripts/*.ps1`。
- 脚本应尽量幂等：重复运行不应破坏状态。
- 环境或比赛库异常时，脚本应明确失败。
- 面向人阅读的调研资料优先用 Markdown，不用 CSV 作为主入口。

## 本地硬件约束

当前主要机器：

- Windows
- 8GB GPU 显存

比赛可行性标签：

| 标签 | 含义 |
|---|---|
| A | 本地 CPU / 8GB GPU 足够 |
| B | 本地工程 + API 或普通云服务 |
| C | 大概率需要平台 Notebook 或外部云算力 |
| D | 不建议作为 8GB Windows 主攻目标 |

