param(
  [Parameter(Mandatory = $true)]
  [string]$Slug,

  [string]$BaseBranch = "main",

  [string]$Branch,

  [string]$WorktreePath,

  [string]$CompetitionPath,

  [switch]$CreateActiveDirectory
)

$ErrorActionPreference = "Stop"

function Invoke-Git {
  & git @args
  if ($LASTEXITCODE -ne 0) {
    throw "git $($args -join ' ') 执行失败"
  }
}

$repoRoot = (& git rev-parse --show-toplevel).Trim()
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($repoRoot)) {
  throw "当前目录不在 Git 仓库中。请在项目根目录或其子目录运行。"
}

if ([string]::IsNullOrWhiteSpace($Branch)) {
  $Branch = "competition/$Slug"
}

if ([string]::IsNullOrWhiteSpace($WorktreePath)) {
  $repoName = Split-Path -Leaf $repoRoot
  $parent = Split-Path -Parent $repoRoot
  $WorktreePath = Join-Path $parent "$repoName-$Slug"
}

if ([string]::IsNullOrWhiteSpace($CompetitionPath)) {
  $CompetitionPath = "competitions/20-active/$Slug"
}

$resolvedWorktreeParent = Resolve-Path (Split-Path -Parent $WorktreePath)
if (Test-Path -LiteralPath $WorktreePath) {
  throw "目标 worktree 已存在：$WorktreePath"
}

Push-Location $repoRoot
try {
  Invoke-Git @("fetch", "--all", "--prune")

  $branchExists = $false
  & git show-ref --verify --quiet "refs/heads/$Branch"
  if ($LASTEXITCODE -eq 0) {
    $branchExists = $true
  }

  if ($branchExists) {
    Invoke-Git @("worktree", "add", $WorktreePath, $Branch)
  } else {
    Invoke-Git @("worktree", "add", $WorktreePath, "-b", $Branch, $BaseBranch)
  }

  if ($CreateActiveDirectory) {
    $activeDir = Join-Path $WorktreePath $CompetitionPath
    $submissionsDir = Join-Path $activeDir "submissions"
    New-Item -ItemType Directory -Force -Path $submissionsDir | Out-Null

    $readme = Join-Path $activeDir "README.md"
    $plan = Join-Path $activeDir "plan.md"
    $evidence = Join-Path $activeDir "evidence.md"
    $gitkeep = Join-Path $submissionsDir ".gitkeep"

    if (!(Test-Path -LiteralPath $readme)) {
      @"
# 比赛卡片：$Slug

## 快照

| 字段 | 内容 |
|---|---|
| 平台 | |
| 官方链接 | |
| 来源核验时间 | |
| 优先级 | P0 / P1 / P2 / P3 |
| 状态 | active |
| 截止时间 | |
| 参赛资格 | 开放参赛 / 企业/组织限定 / 邀请制 / 未知 |
| 队伍规则 | |
| 8GB 可行性 | A 本地可做 / B API或云端 / C 平台 Notebook / D 不建议主攻 |
| 方向 | |

## 为什么值得关注

-

## 交付物

-

## 前 48 小时目标

-

## 风险

-

## 当前决策

-
"@ | Set-Content -LiteralPath $readme -Encoding UTF8
    }

    if (!(Test-Path -LiteralPath $plan)) {
      @"
# $Slug 执行计划

## 本轮目标

-

## 工作边界

- 本比赛对话框只修改 `$CompetitionPath` 及明确约定的比赛专属代码目录。
- 共享文件变更需要单独协调。

## 里程碑

| 日期 | 目标 | 证据 |
|---|---|---|
| | | |

## 当前下一步

1.
"@ | Set-Content -LiteralPath $plan -Encoding UTF8
    }

    if (!(Test-Path -LiteralPath $evidence)) {
      @"
# $Slug 证据与验收

## 官方规则证据

- 官方页面：
- 核验日期：
- 关键事实：

## 最小可提交定义

-

## 验收检查

| 项目 | 状态 | 备注 |
|---|---|---|
| 资格确认 | 待做 | |
| 截止时间确认 | 待做 | |
| 交付物确认 | 待做 | |
| 最小可运行版本 | 待做 | |
"@ | Set-Content -LiteralPath $evidence -Encoding UTF8
    }

    if (!(Test-Path -LiteralPath $gitkeep)) {
      "" | Set-Content -LiteralPath $gitkeep -Encoding UTF8
    }
  }

  Write-Host "已创建比赛 worktree"
  Write-Host "分支：$Branch"
  Write-Host "目录：$WorktreePath"
  Write-Host "主要比赛路径：$CompetitionPath"
  Write-Host "父目录：$resolvedWorktreeParent"
} finally {
  Pop-Location
}
