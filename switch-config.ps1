#Requires -Version 5.1
<#
.SYNOPSIS
  Switch daily-flywheel local.config.md and local.article.config.md
  between live and demo profiles.

.USAGE
  .\switch-config.ps1 live
  .\switch-config.ps1 demo
  .\switch-config.ps1 status
#>
param(
  [Parameter(Position = 0)]
  [ValidateSet('live', 'demo', 'status')]
  [string]$Profile = 'status'
)

$ErrorActionPreference = 'Stop'
$skillDir = $PSScriptRoot

$activeConfig = Join-Path $skillDir 'local.config.md'
$liveConfig = Join-Path $skillDir 'local.config.live.md'
$demoConfig = Join-Path $skillDir 'local.config.demo.md'

$activeArticle = Join-Path $skillDir 'local.article.config.md'
$liveArticle = Join-Path $skillDir 'local.article.config.live.md'
$demoArticle = Join-Path $skillDir 'local.article.config.demo.md'

function Get-ConfigField {
  param([string]$Path, [string]$Key)
  if (-not (Test-Path -LiteralPath $Path)) { return $null }
  $line = Select-String -LiteralPath $Path -Pattern ("^\s*{0}\s*:" -f [regex]::Escape($Key)) | Select-Object -First 1
  if (-not $line) { return $null }
  return ($line.Line -split ':', 2)[1].Trim().Trim('"')
}

function Show-Status {
  param([string]$Path, [string]$Label)
  if (-not (Test-Path -LiteralPath $Path)) {
    Write-Host ("[{0}] missing: {1}" -f $Label, $Path)
    return
  }
  $vault = Get-ConfigField -Path $Path -Key 'DAILY_VAULT'
  $obj = Get-ConfigField -Path $Path -Key 'OBJECTIVE_FILE'
  $export = Get-ConfigField -Path $Path -Key 'export_dir'
  if ($vault -or $obj) {
    Write-Host ("[{0}] DAILY_VAULT={1}" -f $Label, $vault)
    Write-Host ("[{0}] OBJECTIVE_FILE={1}" -f $Label, $obj)
  }
  if ($export) {
    Write-Host ("[{0}] export_dir={1}" -f $Label, $export)
  }
}

if ($Profile -eq 'status') {
  Show-Status -Path $activeConfig -Label 'active(local.config.md)'
  Show-Status -Path $liveConfig -Label 'live config'
  Show-Status -Path $demoConfig -Label 'demo config'
  Show-Status -Path $activeArticle -Label 'active(local.article.config.md)'
  Show-Status -Path $liveArticle -Label 'live article'
  Show-Status -Path $demoArticle -Label 'demo article'
  exit 0
}

$sourceConfig = if ($Profile -eq 'live') { $liveConfig } else { $demoConfig }
$sourceArticle = if ($Profile -eq 'live') { $liveArticle } else { $demoArticle }

if (-not (Test-Path -LiteralPath $sourceConfig)) {
  throw "Profile file not found: $sourceConfig"
}
if (-not (Test-Path -LiteralPath $sourceArticle)) {
  throw "Article profile file not found: $sourceArticle"
}

Copy-Item -LiteralPath $sourceConfig -Destination $activeConfig -Force
Copy-Item -LiteralPath $sourceArticle -Destination $activeArticle -Force
Write-Host ("Switched local.config.md <- local.config.{0}.md" -f $Profile)
Write-Host ("Switched local.article.config.md <- local.article.config.{0}.md" -f $Profile)
Show-Status -Path $activeConfig -Label 'active config'
Show-Status -Path $activeArticle -Label 'active article'
if ($Profile -eq 'demo') {
  Write-Host 'Demo: df ship/final export to demo-ai-obsidian\insights-to-share. Switch back: .\switch-config.ps1 live'
}
