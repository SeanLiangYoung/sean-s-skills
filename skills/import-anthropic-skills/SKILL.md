---
name: import-anthropic-skills
description: 帮助用户将 Anthropic 官方发布的 skills 从 GitHub 仓库 https://github.com/anthropics/skills 导入到 Cursor。当用户想要导入、安装或使用 Anthropic 的 skills、提及 anthropics/skills 仓库或需要 PDF/docx/xlsx/pptx 等文档处理能力时使用此 skill。
---

# 导入 Anthropic 官方 Skills 到 Cursor

## 概述

Anthropic 在 [GitHub](https://github.com/anthropics/skills) 发布了官方 Agent Skills，包含文档处理（PDF、DOCX、XLSX、PPTX）、创意设计、Web 测试、MCP 构建等能力。本 skill 指导如何将这些 skills 导入 Cursor 供 Agent 使用。

## Cursor Skills 存储位置

| 类型 | 路径 (Windows) | 路径 (macOS/Linux) |
|------|----------------|-------------------|
| 个人 | `%USERPROFILE%\.cursor\skills\` | `~/.cursor/skills/` |
| 项目 | 项目根目录 `.cursor\skills\` | 项目根目录 `.cursor/skills/` |

**重要**：切勿在 `~/.cursor/skills-cursor/` 中创建 skills，该目录为 Cursor 内置 skill 保留。

## 导入流程

### 方式一：克隆完整仓库后复制（推荐）

1. **克隆仓库**（在临时目录或用户指定目录）：
   ```bash
   git clone https://github.com/anthropics/skills.git
   ```

2. **确定目标目录**：
   - 个人：`%USERPROFILE%\.cursor\skills\`（Windows）或 `~/.cursor/skills/`（macOS/Linux）
   - 项目：当前项目的 `.cursor/skills/`

3. **复制 skills**：将 `skills/skills/` 下的每个子文件夹（如 `pdf`、`docx`、`xlsx`）复制到目标目录，保持每个 skill 的完整结构（含 SKILL.md 及 scripts、reference 等）。

4. **Windows PowerShell 示例**：
   ```powershell
   $target = "$env:USERPROFILE\.cursor\skills"
   New-Item -ItemType Directory -Force -Path $target
   Copy-Item -Path "skills\skills\*" -Destination $target -Recurse -Force
   ```

5. **macOS/Linux 示例**：
   ```bash
   mkdir -p ~/.cursor/skills
   cp -r skills/skills/* ~/.cursor/skills/
   ```

### 方式二：仅导入指定 skill

若用户只需部分 skill，可单独复制对应文件夹，例如：
- `skills/skills/pdf` → PDF 处理
- `skills/skills/docx` → Word 文档
- `skills/skills/xlsx` → Excel 表格
- `skills/skills/pptx` → PowerPoint
- `skills/skills/webapp-testing` → Web 应用测试
- `skills/skills/mcp-builder` → MCP 服务器构建

## 可用 Skills 列表

| Skill 名称 | 用途 |
|-----------|------|
| pdf | PDF 读写、合并、拆分、表单填写、OCR |
| docx | Word 文档创建与编辑 |
| xlsx | Excel 表格处理 |
| pptx | PowerPoint 演示文稿 |
| algorithmic-art | 算法艺术生成 |
| brand-guidelines | 品牌指南 |
| canvas-design | 画布设计 |
| doc-coauthoring | 文档协作 |
| frontend-design | 前端设计 |
| internal-comms | 内部沟通 |
| mcp-builder | MCP 服务器构建 |
| skill-creator | Skill 创建 |
| slack-gif-creator | Slack GIF 创建 |
| theme-factory | 主题工厂 |
| web-artifacts-builder | Web 构件构建 |
| webapp-testing | Web 应用测试 |

## 验证导入

导入后，确认目标目录下每个 skill 文件夹内存在 `SKILL.md`。Cursor 会自动发现并加载这些 skills。

## 注意事项

- 文档类 skills（docx、pdf、pptx、xlsx）部分为 source-available，非完全开源，使用前请查看仓库中的 LICENSE
- 建议在非关键任务中先测试导入的 skills
- 可通过 `git pull` 更新已克隆的仓库，再重新复制以获取最新 skills

## 参考链接

- [anthropics/skills 仓库](https://github.com/anthropics/skills)
- [Agent Skills 规范](https://github.com/anthropics/skills/tree/main/spec)
- [Skill 模板](https://github.com/anthropics/skills/tree/main/template)
