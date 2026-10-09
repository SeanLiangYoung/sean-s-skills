# Exercise installation and integration in an ignored temporary directory.
$ErrorActionPreference = 'Stop'
$repo = Split-Path -Parent $PSScriptRoot
$testRoot = Join-Path $repo ('.tmp-integration/script-tests-' + [Guid]::NewGuid().ToString('N'))
$userDir = Join-Path $testRoot 'cursor user'
$targetProject = Join-Path $testRoot "项目 with space and ' quote"
New-Item -ItemType Directory -Path $targetProject -Force | Out-Null

function Assert-True($Condition, $Message) {
    if (-not $Condition) { throw $Message }
}

$preview = Join-Path $testRoot 'preview'
& (Join-Path $PSScriptRoot 'install-cursor-user-level.ps1') -CursorUserDir $preview -WhatIf
Assert-True (-not (Test-Path -LiteralPath $preview)) 'WhatIf created files'

$obsolete = Join-Path $userDir 'skills/seo/obsolete.py'
$unrelated = Join-Path $userDir 'skills/local-only/keep.txt'
foreach ($file in @($obsolete, $unrelated)) {
    New-Item -ItemType Directory -Path (Split-Path -Parent $file) -Force | Out-Null
    [IO.File]::WriteAllText($file, 'keep for regression check')
}
& (Join-Path $PSScriptRoot 'install-cursor-user-level.ps1') -CursorUserDir $userDir
Assert-True (-not (Test-Path -LiteralPath $obsolete)) 'Obsolete upstream file was retained'
Assert-True (Test-Path -LiteralPath $unrelated) 'Unrelated local skill was changed'
Assert-True (@(Get-ChildItem -LiteralPath (Join-Path $userDir '.sean-s-skills-backups') -Recurse -Filter 'obsolete.py').Count -eq 1) 'Backup did not retain obsolete file'
$expected = @(Get-ChildItem -LiteralPath (Join-Path $repo 'skills') -Directory | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') }).Count
$installed = @(Get-ChildItem -LiteralPath (Join-Path $userDir 'skills') -Directory | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') }).Count
Assert-True ($installed -eq $expected) 'Installed skill count mismatch'
Assert-True (Test-Path -LiteralPath (Join-Path $userDir 'skills/seo/scripts/runtime.py')) 'SEO runtime not installed'

# A second run must replace the same directories rather than nest them.
& (Join-Path $PSScriptRoot 'install-cursor-user-level.ps1') -CursorUserDir $userDir
Assert-True (-not (Test-Path -LiteralPath (Join-Path $userDir 'skills/seo/seo'))) 'Repeated install nested skill directory'
Assert-True (Test-Path -LiteralPath $unrelated) 'Repeated install removed local skill'

$selfRejected = $false
try { & (Join-Path $PSScriptRoot 'install-cursor-user-level.ps1') -CursorUserDir $repo }
catch { $selfRejected = $true }
Assert-True $selfRejected 'Installer did not reject copying the source into itself'

& (Join-Path $PSScriptRoot 'integrate-into-project.bat') $targetProject $repo
Assert-True ($LASTEXITCODE -eq 0) 'Batch integration failed'
$ruleFile = Join-Path $targetProject '.cursor/rules/use-sean-s-skills.mdc'
$rule = Get-Content -LiteralPath $ruleFile -Raw -Encoding UTF8
Assert-True ($rule.Contains("$expected 个 Skill、20 个 Agent")) 'Generated capability counts are stale'
$match = [regex]::Match($rule, '库路径[^\r\n]*：`([^`]+)`')
Assert-True $match.Success 'Library path missing from rule'
$resolvedLibrary = [IO.Path]::GetFullPath((Join-Path $targetProject $match.Groups[1].Value))
Assert-True ($resolvedLibrary.TrimEnd('\', '/') -eq $repo.TrimEnd('\', '/')) 'Generated relative path does not resolve to library'
Assert-True (Test-Path -LiteralPath (Join-Path $targetProject '.cursor/rules/skill-usage.mdc')) 'Usage rule was not copied'
Assert-True (-not (Test-Path -LiteralPath (Join-Path $targetProject '.claude/settings.json'))) 'Integration wrote undocumented Claude configuration'

$legacyRule = Join-Path $testRoot 'legacy/use-sean-s-skills.mdc'
& (Join-Path $PSScriptRoot 'integrate-into-project-impl.ps1') -RelPath '../library' -OutFile $legacyRule
Assert-True (Test-Path -LiteralPath $legacyRule) 'Legacy integration parameters failed'
Write-Host "PASS: preview, backups, stale-file cleanup, unrelated skills, full install, repeat install, self-copy rejection, quoted paths, batch and legacy integration. Artifacts: $testRoot"
