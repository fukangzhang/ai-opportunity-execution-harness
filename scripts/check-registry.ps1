param(
  [string]$CsvPath = "D:\project\ai-competition-research\competition_matrix.csv",
  [string]$IndexPath = "D:\project\ai-competition-research\docs\registry\competition-index.md"
)

$errors = New-Object System.Collections.Generic.List[string]
$validEligibility = @("开放参赛", "企业/组织限定", "邀请制", "未知")
$validFit = @("A", "B", "C", "D", "A-C", "A-D", "B/C", "C/D")

if (!(Test-Path $CsvPath)) {
  $errors.Add("缺少 CSV：$CsvPath")
} else {
  $rows = Import-Csv -Path $CsvPath
  foreach ($row in $rows) {
    if ([string]::IsNullOrWhiteSpace($row.name)) { $errors.Add("存在缺少比赛名称的行") }
    if ([string]::IsNullOrWhiteSpace($row.source)) { $errors.Add("缺少来源链接：$($row.name)") }
    if ([string]::IsNullOrWhiteSpace($row.eligibility)) { $errors.Add("缺少参赛资格：$($row.name)") }
    if ($row.eligibility -and $validEligibility -notcontains $row.eligibility) {
      $errors.Add("参赛资格标签非法：$($row.name) = $($row.eligibility)")
    }
    if ([string]::IsNullOrWhiteSpace($row.'8gb_fit')) { $errors.Add("缺少 8GB 可行性：$($row.name)") }
    if ($row.'8gb_fit' -and $validFit -notcontains $row.'8gb_fit') {
      $errors.Add("8GB 可行性标签非法：$($row.name) = $($row.'8gb_fit')")
    }
    if ($row.source -notmatch "^https?://") { $errors.Add("来源不像 URL：$($row.name)") }
  }
}

if (!(Test-Path $IndexPath)) {
  $errors.Add("缺少 Markdown 索引：$IndexPath")
}

if ($errors.Count -gt 0) {
  $errors | ForEach-Object { Write-Error $_ }
  exit 1
}

Write-Host "比赛库校验通过。"
