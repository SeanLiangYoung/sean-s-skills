# 将 Sean's Skills 安装到 Cursor 用户级（最顶层）
# 用法: .\install-cursor-user-level.ps1 [-SkillsSource <path>] [-CursorUserDir <path>]
# 示例: .\install-cursor-user-level.ps1
#       .\install-cursor-user-level.ps1 -SkillsSource "D:\repos\sean-s-skills\skills" -CursorUserDir "$env:USERPROFILE\.cursor"

[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$SkillsSource = "",
    [string]$CursorUserDir = (Join-Path $env:USERPROFILE ".cursor")
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
if (-not $SkillsSource) { $SkillsSource = Join-Path $RepoRoot "skills" }
$RulesSource = Join-Path $RepoRoot "rules"

if (-not (Test-Path $SkillsSource)) {
    Write-Error "Skills 源目录不存在: $SkillsSource"
}

$skillsDest = Join-Path $CursorUserDir "skills"
$rulesDest = Join-Path $CursorUserDir "rules"

# Resolve paths before replacing managed skill directories.
$SkillsSource = (Resolve-Path -LiteralPath $SkillsSource).ProviderPath
$skillsDest = [IO.Path]::GetFullPath($skillsDest).TrimEnd('\', '/')
$sourceFull = $SkillsSource.TrimEnd('\', '/')
$separator = [IO.Path]::DirectorySeparatorChar
if ($sourceFull.Equals($skillsDest, [StringComparison]::OrdinalIgnoreCase) -or
    $sourceFull.StartsWith($skillsDest + $separator, [StringComparison]::OrdinalIgnoreCase) -or
    $skillsDest.StartsWith($sourceFull + $separator, [StringComparison]::OrdinalIgnoreCase)) {
    throw "源和目标 Skill 目录不能相同或互相包含。"
}
$skills = @(Get-ChildItem -LiteralPath $SkillsSource -Directory | Where-Object {
    Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md') -PathType Leaf
})
if ($skills.Count -eq 0) { throw "源目录没有有效的 Skill。" }
$AgentCount = @(Get-ChildItem -LiteralPath (Join-Path $RepoRoot 'agents') -File -Filter '*.md' | Where-Object {
    (Get-Content -LiteralPath $_.FullName -TotalCount 1) -eq '---'
}).Count
if (-not $PSCmdlet.ShouldProcess($CursorUserDir, "备份并同步 $($skills.Count) 个 Skill 与用户级规则")) { return }
if (Test-Path -LiteralPath $skillsDest) {
    if ((Get-Item -LiteralPath $skillsDest -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) {
        throw "目标 skills 目录是链接，请选择普通目录。"
    }
}
$backupRoot = Join-Path $CursorUserDir ('.sean-s-skills-backups/' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
$backupSkills = Join-Path $backupRoot 'skills'
# Finish all backups before replacing the first skill.
foreach ($skill in $skills) {
    $destination = [IO.Path]::GetFullPath((Join-Path $skillsDest $skill.Name))
    if ([IO.Path]::GetDirectoryName($destination) -ne $skillsDest) { throw "目标不在 Skill 安装目录内: $destination" }
    if (Test-Path -LiteralPath $destination) {
        if ((Get-Item -LiteralPath $destination -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) {
            throw "目标 Skill 是链接，不能替换: $destination"
        }
        New-Item -ItemType Directory -Path $backupSkills -Force | Out-Null
        Copy-Item -LiteralPath $destination -Destination $backupSkills -Recurse -Force
    }
}
foreach ($existing in @($rulesDest, (Join-Path $CursorUserDir 'SKILLS_GUIDE.md'))) {
    if (Test-Path -LiteralPath $existing) {
        New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
        Copy-Item -LiteralPath $existing -Destination $backupRoot -Recurse -Force
    }
}
New-Item -ItemType Directory -Path $skillsDest -Force | Out-Null
$count = 0
foreach ($skill in $skills) {
    $destination = [IO.Path]::GetFullPath((Join-Path $skillsDest $skill.Name))
    if ([IO.Path]::GetDirectoryName($destination) -ne $skillsDest) { throw "非法目标路径: $destination" }
    try {
        if (Test-Path -LiteralPath $destination) { Remove-Item -LiteralPath $destination -Recurse -Force }
        Copy-Item -LiteralPath $skill.FullName -Destination $skillsDest -Recurse -Force
    } catch {
        $saved = Join-Path $backupSkills $skill.Name
        if (Test-Path -LiteralPath $saved) {
            if (Test-Path -LiteralPath $destination) { Remove-Item -LiteralPath $destination -Recurse -Force }
            Copy-Item -LiteralPath $saved -Destination $skillsDest -Recurse -Force
        }
        throw
    }
    $count++
}
Write-Host "[OK] 已同步 $count 个 Skill 到 $skillsDest"
if (Test-Path -LiteralPath $backupRoot) { Write-Host "[OK] 更新前副本: $backupRoot" }

# 2. 创建并复制 Rules
if (-not (Test-Path $rulesDest)) { New-Item -ItemType Directory -Path $rulesDest -Force | Out-Null }
foreach ($f in @("skill-usage.mdc", "confirmation-before-action.mdc")) {
    $src = Join-Path $RulesSource $f
    if (Test-Path $src) {
        Copy-Item $src $rulesDest -Force
        Write-Host "[OK] 已复制规则 $f"
    }
}

# 3. 写入全局 Sean's Skills 规则（指向本库文档）
$globalRule = @"
---
description: 全局使用 Sean's Skills 库（$count 个 Skill、$AgentCount 个 Agent）；能力索引与场景见下方
alwaysApply: true
---

# 使用 Sean's Skills 库（用户级）

本规则使 Cursor 在**任意项目**中均可使用 Sean's Skills 库的能力。Skills 已安装在用户级目录，Agent 会自动发现。

- **Skill 目录（用户级）**：``$CursorUserDir\skills\``（$count 个 Skill，已自动加载）
- **能力索引与文档**（本库）：``$RepoRoot\docs\capabilities-index.md``
- **Skill 列表与使用场景**：``$RepoRoot\docs\skills-reference.md``
- **Agent 列表**：``$RepoRoot\docs\agents-reference.md``
- **工具注册表**：``$RepoRoot\tools\REGISTRY.md``

知识入库使用 llm-wiki-ingest；已授权安全审计及报告打包使用 code-security-audit。

需要文档/SEO/营销/图文/知识入库/安全审计/开发流程等能力时，优先查阅上述文档并按需引用 ``$CursorUserDir\skills\<name>\SKILL.md`` 或本库 ``agents/*.md``。
"@
$globalRulePath = Join-Path $rulesDest "sean-s-skills-global.mdc"
[System.IO.File]::WriteAllText($globalRulePath, $globalRule, [System.Text.UTF8Encoding]::new($false))
Write-Host "[OK] 已写入 $globalRulePath"

# 4. 写入 SKILLS_GUIDE.md
$guidePath = Join-Path $CursorUserDir "SKILLS_GUIDE.md"
$guide = @"
# Sean's Skills — 能力列表与使用指南

本机已安装 **Sean's Skills** 到 Cursor 用户级目录，**任意项目**打开 Cursor 均可使用。

## 安装位置

| 类型 | 路径 |
|------|------|
| **Skills（$count 个）** | ``$CursorUserDir\skills\`` |
| **用户级规则** | ``$CursorUserDir\rules\`` |

## 能力索引（本库）

- **能力总览**：``$RepoRoot\docs\capabilities-index.md``
- **Skill 列表与场景**：``$RepoRoot\docs\skills-reference.md``
- **Agent 列表**：``$RepoRoot\docs\agents-reference.md``
- **工具注册表**：``$RepoRoot\tools\REGISTRY.md``

## 更新

若本库有更新，重新运行本脚本即可同步。脚本先备份已有对应目录，再整体替换，清除上游已移除的文件；其他 Skill 目录保留。备份位置：``$CursorUserDir\.sean-s-skills-backups\``。
"@
[System.IO.File]::WriteAllText($guidePath, $guide, [System.Text.UTF8Encoding]::new($false))
Write-Host "[OK] 已写入 $guidePath"
Write-Host ""
Write-Host "安装完成。请重启 Cursor 或打开任意项目后，在 Agent 中通过 / 查看已加载的 Skills。"
