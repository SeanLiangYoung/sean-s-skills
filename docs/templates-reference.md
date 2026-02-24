# Templates 说明 — Skill 创建模板

本库 **templates/** 目录提供创建新 Skill 时使用的**最小可用模板**，保证新 Skill 符合 [Agent Skills 规范](../spec/specification.md)。内容来自 [anthropics/skills](https://github.com/anthropics/skills) 的 `template/`。

---

## 现有模板

### SKILL-template.md

| 项目 | 说明 |
|------|------|
| **路径** | `templates/SKILL-template.md` |
| **功能** | 符合规范的最小 SKILL.md 骨架：YAML frontmatter（`name`、`description`）+ 占位正文。 |
| **格式** | 与 [spec/specification.md](../spec/specification.md) 要求一致：`name` 小写字母数字连字符、与目录名一致；`description` 说明技能做什么与何时使用。 |

**模板内容示例**：

```yaml
---
name: template-skill
description: Replace with description of the skill and when Claude should use it.
---

# Insert instructions below
```

---

## 使用场景

| 场景 | 用法 |
|------|------|
| **新建一个 Skill** | 1）在 `skills/` 下创建 `skill-name/` 目录；2）将 `templates/SKILL-template.md` 复制为 `skills/skill-name/SKILL.md`；3）把 `name` 改为与目录名一致（如 `skill-name`）；4）填写 `description` 和正文说明。 |
| **保证规范符合** | 以该模板为起点可避免漏写必填 frontmatter；命名与字段约束见 [spec-reference.md](./spec-reference.md)。 |
| **扩展为完整 Skill** | 在 `skills/<name>/` 下按需增加 `scripts/`、`references/`、`assets/` 等，并在 SKILL.md 中说明用法。 |

---

## 与 spec、skill-creator 的关系

- **spec** 定义「什么是合法 Skill」；**templates** 提供「从零写一个合法 SKILL.md」的起点。  
- **skill-creator**（Skill）提供创建、校验、打包的完整流程；若只需快速起一个 SKILL.md，用本模板即可；若需要校验、打包或与仓库流程集成，可配合 skill-creator 使用。
