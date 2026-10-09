# 安装 Sean's Skills 到 Cursor 用户级（最顶层）

将本库的 **Skills** 与 **Rules** 安装到 Cursor 用户目录，使**当前账户下任意项目**均可使用，无需在每个项目中单独配置。

## 安装位置（Windows）

| 内容 | 目标路径 |
|------|----------|
| **122 个 Skill** | `%USERPROFILE%\.cursor\skills\` |
| **用户级规则** | `%USERPROFILE%\.cursor\rules\` |
| **能力指南** | `%USERPROFILE%\.cursor\SKILLS_GUIDE.md` |

## 一键安装（PowerShell）

在本库根目录执行：

```powershell
.\scripts\install-cursor-user-level.ps1
```

可选参数：
- `-SkillsSource "d:\projects\sean-s-skills\skills"` — 本库 skills 路径（默认：脚本所在目录的上级 `skills`）
- `-CursorUserDir "$env:USERPROFILE\.cursor"` — Cursor 用户目录（默认：`%USERPROFILE%\.cursor`）

## 手动安装

1. **复制 Skills**
   将 `skills\` 下所有子目录复制到 `%USERPROFILE%\.cursor\skills\`（每个子目录一个 Skill，如 `skills\pdf` → `.cursor\skills\pdf`）。

2. **复制 Rules**
   将 `rules\skill-usage.mdc`、`rules\confirmation-before-action.mdc` 复制到 `%USERPROFILE%\.cursor\rules\`。
   可选：复制 `scripts\install-cursor-user-level.ps1` 生成的 `sean-s-skills-global.mdc` 到同一目录（或由脚本生成）。

3. **Cursor 读取用户级 Rules**
   - 若 Cursor 已支持从 `%USERPROFILE%\.cursor\rules\` 加载规则，无需额外设置。
   - 否则在 **Cursor → Settings → Rules** 中手动添加规则，或粘贴上述 `.mdc` 内容。

## 验证

- 打开任意项目，在 Agent 中输入 `/`，应能看到多个 Skill 供选择。
- 在 **Cursor Settings → Rules** 中可查看是否加载了用户级规则。

## 更新

本库更新后，重新执行 `.\scripts\install-cursor-user-level.ps1` 即可同步对应 Skill 与规则。已有 Skill、规则和指南先备份到 `.cursor\.sean-s-skills-backups\<时间戳>\`，随后整体替换同名 Skill 目录，清除上游已删除的文件；其他本地 Skill 保留。


## 新增能力与同步

本库当前包含 122 个 Skill，含知识入库 `llm-wiki-ingest` 和审计报告 `code-security-audit`。脚本复制完整 Skill 目录并按实际有效目录生成规则和指南中的数量；重新运行可更新已有 Skill，不产生同名嵌套目录。知识库配置 `wiki-config.md` 随 Skill 同步，使用前确认其目标路径适用于当前机器。

## 预览与恢复

```powershell
.\scripts\install-cursor-user-level.ps1 -WhatIf
```

`-WhatIf` 只预览，不创建目录或复制文件。可使用 `-CursorUserDir` 指定测试安装位置。源与目标不能相同或互相包含；脚本拒绝替换链接目录。

备份包含更新前的完整 Skill、规则和指南。若已有个性化配置，更新后从备份中取回所需配置，例如 `llm-wiki-ingest/wiki-config.md`。Agent、工具索引和文档仍通过规则引用本库，当前有 20 个 Agent。
