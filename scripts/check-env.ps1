$errors = New-Object System.Collections.Generic.List[string]

if ($PSVersionTable.PSVersion.Major -lt 7) {
  $errors.Add("需要 PowerShell 7+。当前版本：$($PSVersionTable.PSVersion)")
}

$utf8 = [System.Text.Encoding]::UTF8.WebName
if ([Console]::OutputEncoding.WebName -ne $utf8) {
  Write-Warning "当前终端输出编码为 $([Console]::OutputEncoding.WebName)，建议使用 UTF-8。"
}

if (!(Test-Path "AGENTS.md")) {
  $errors.Add("请从项目根目录运行此脚本。")
}

if ($errors.Count -gt 0) {
  $errors | ForEach-Object { Write-Error $_ }
  exit 1
}

Write-Host "环境校验通过。PowerShell $($PSVersionTable.PSVersion)。"

