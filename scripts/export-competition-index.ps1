param(
  [string]$CsvPath = "D:\project\ai-competition-research\competition_matrix.csv",
  [string]$OutPath = "D:\project\ai-competition-research\docs\registry\competition-index.md"
)

$rows = Import-Csv -Path $CsvPath
$now = Get-Date -Format "yyyy-MM-dd HH:mm:ss zzz"

function Escape-Cell([string]$s) {
  if ($null -eq $s) { return "" }
  return ($s -replace "\|", "\/" -replace "`r?`n", " ").Trim()
}

$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("# 比赛索引")
$lines.Add("")
$lines.Add("由 ``competition_matrix.csv`` 于 $now 生成。")
$lines.Add("")
$lines.Add("参赛资格采用保守判断；官方规则始终优先于本索引。")
$lines.Add("")

foreach ($group in ($rows | Group-Object priority | Sort-Object Name)) {
  $lines.Add("## $($group.Name)")
  $lines.Add("")
  $lines.Add("| 比赛 | 平台 | 类型 | 状态 / 时间 | 8GB | 资格 | 建议 | 来源 |")
  $lines.Add("|---|---|---|---|---|---|---|---|")
  foreach ($row in $group.Group) {
    $name = Escape-Cell $row.name
    $platform = Escape-Cell $row.platform
    $type = Escape-Cell $row.type
    $window = Escape-Cell "$($row.status_on_2026_05_14); $($row.deadline_or_window)"
    $fit = Escape-Cell $row.'8gb_fit'
    $eligibility = Escape-Cell $row.eligibility
    $rec = Escape-Cell $row.recommendation
    $source = Escape-Cell $row.source
    $lines.Add("| $name | $platform | $type | $window | $fit | $eligibility | $rec | [链接]($source) |")
  }
  $lines.Add("")
}

$lines.Add("## 8GB 标签说明")
$lines.Add("")
$lines.Add("| 标签 | 含义 |")
$lines.Add("|---|---|")
$lines.Add("| A | 本地 CPU / 8GB GPU 足够 |")
$lines.Add("| B | 本地工程 + API 或普通云服务 |")
$lines.Add("| C | 大概率需要平台 Notebook 或外部云算力 |")
$lines.Add("| D | 不建议作为 8GB Windows 主攻目标 |")

Set-Content -Path $OutPath -Value $lines -Encoding UTF8
Write-Host "已生成 Markdown 比赛索引：$OutPath"
