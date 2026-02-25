# 被 integrate-into-project.bat 调用：根据相对路径生成 use-sean-s-skills.mdc 并写入目标路径。
# 用法: .\integrate-into-project-impl.ps1 -RelPath "..\sean-s-skills" -OutFile "D:\proj\my-app\.cursor\rules\use-sean-s-skills.mdc"
param([Parameter(Mandatory)]$RelPath, [Parameter(Mandatory)]$OutFile)
$p = $RelPath -replace '\\', '/'
$content = @"
---
description: 使用 Sean's Skills 库中的 91 个 Skill、7 个 Agent 与 tools；能力说明见该库 docs
globs: 
alwaysApply: true
---

# 使用 Sean's Skills 库

本规则使 Cursor 在本项目中可使用 Sean's Skills 库的能力，无需复制 skills 目录。

- **Skill 库路径**（相对本项目）：``$p``
- **能力索引**：``$p/docs/capabilities-index.md``
- **Skill 列表与场景**（91 个）：``$p/docs/skills-reference.md``
- **Agent 列表**：``$p/docs/agents-reference.md``
- **工具索引**：``$p/tools/REGISTRY.md``

在完成文档、SEO、营销、图文、开发流程等任务时，优先查阅上述文档并按需引用 ``$p/skills/<name>/SKILL.md`` 或 ``$p/agents/*.md`` 中的说明。
"@
$dir = [System.IO.Path]::GetDirectoryName($OutFile)
if (-not [System.IO.Directory]::Exists($dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
[System.IO.File]::WriteAllText($OutFile, $content, [System.Text.UTF8Encoding]::new($false))
