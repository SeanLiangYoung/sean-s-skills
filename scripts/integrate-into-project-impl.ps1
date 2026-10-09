# 被 integrate-into-project.bat 调用：根据相对路径生成 use-sean-s-skills.mdc 并写入目标路径。
# 用法: .\integrate-into-project-impl.ps1 -RelPath "..\sean-s-skills" -OutFile "D:\proj\my-app\.cursor\rules\use-sean-s-skills.mdc"
param(
    [string]$RelPath,
    [string]$OutFile,
    [string]$SkillsRoot,
    [string]$TargetProject,
    [string]$LibraryRoot = (Split-Path -Parent $PSScriptRoot)
)
$ErrorActionPreference = "Stop"
$LibraryRoot = (Resolve-Path -LiteralPath $LibraryRoot).ProviderPath
if (-not $SkillsRoot) { $SkillsRoot = Join-Path $LibraryRoot "skills" }
if ($TargetProject) {
    $target = (Resolve-Path -LiteralPath $TargetProject).ProviderPath
    if (-not (Test-Path -LiteralPath $target -PathType Container)) { throw "目标项目不是目录: $target" }
    # Uri.MakeRelativeUri also works in Windows PowerShell 5.1, which lacks Path.GetRelativePath.
    $targetUri = [Uri]($target.TrimEnd('\', '/') + [IO.Path]::DirectorySeparatorChar)
    $libraryUri = [Uri]($LibraryRoot.TrimEnd('\', '/') + [IO.Path]::DirectorySeparatorChar)
    if ($targetUri.Scheme -eq $libraryUri.Scheme -and $targetUri.Host -eq $libraryUri.Host -and [IO.Path]::GetPathRoot($target) -eq [IO.Path]::GetPathRoot($LibraryRoot)) {
        $RelPath = [Uri]::UnescapeDataString($targetUri.MakeRelativeUri($libraryUri).ToString()).TrimEnd('/')
        if (-not $RelPath) { $RelPath = '.' }
    } else { $RelPath = $LibraryRoot }
    $OutFile = Join-Path $target '.cursor/rules/use-sean-s-skills.mdc'
}
if (-not $RelPath -or -not $OutFile) { throw "指定 TargetProject，或同时指定 RelPath 和 OutFile。" }
$SkillCount = @(Get-ChildItem -LiteralPath $SkillsRoot -Directory | Where-Object { Test-Path -LiteralPath (Join-Path $_.FullName "SKILL.md") -PathType Leaf }).Count
$AgentCount = @(Get-ChildItem -LiteralPath (Join-Path $LibraryRoot 'agents') -File -Filter '*.md' | Where-Object { (Get-Content -LiteralPath $_.FullName -TotalCount 1) -eq '---' }).Count
$p = $RelPath -replace '\\', '/'
$content = @"
---
description: 使用 Sean's Skills 库中的 $SkillCount 个 Skill、$AgentCount 个 Agent 与 tools；能力说明见该库 docs
globs: 
alwaysApply: true
---

# 使用 Sean's Skills 库

本规则使 Cursor 在本项目中可使用 Sean's Skills 库的能力，无需复制 skills 目录。

- **Skill 库路径**（相对本项目）：``$p``
- **能力索引**：``$p/docs/capabilities-index.md``
- **Skill 列表与场景**（$SkillCount 个）：``$p/docs/skills-reference.md``
- **Agent 列表**：``$p/docs/agents-reference.md``
- **工具索引**：``$p/tools/REGISTRY.md``

在完成文档、SEO、营销、图文、知识入库、安全审计、开发流程等任务时，优先查阅上述文档并按需引用 ``$p/skills/<name>/SKILL.md`` 或 ``$p/agents/*.md`` 中的说明。
"@
$dir = [System.IO.Path]::GetDirectoryName($OutFile)
if (-not [System.IO.Directory]::Exists($dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
[System.IO.File]::WriteAllText($OutFile, $content, [System.Text.UTF8Encoding]::new($false))
if ($TargetProject) {
    foreach ($name in @('skill-usage.mdc', 'confirmation-before-action.mdc')) {
        $source = Join-Path $LibraryRoot "rules/$name"
        if (Test-Path -LiteralPath $source -PathType Leaf) {
            Copy-Item -LiteralPath $source -Destination (Join-Path $dir $name) -Force
        }
    }
}
Write-Host "[OK] $SkillCount 个 Skill、$AgentCount 个 Agent；规则: $OutFile"
