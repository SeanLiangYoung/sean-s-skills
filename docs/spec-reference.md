# Spec 说明 — Agent Skills 规范

本库 **spec/** 目录存放 **Agent Skills 格式规范**，用于定义什么是合法的 Skill、SKILL.md 应包含哪些字段、目录与命名规则等。规范来源为 [agentskills/agentskills](https://github.com/agentskills/agentskills) 等社区标准，本库已纳入并统一引用。

---

## 文档位置与作用

| 项目 | 说明 |
|------|------|
| **路径** | `spec/specification.md` |
| **功能** | 定义 Agent Skill 的目录结构、SKILL.md 的 YAML frontmatter 与正文要求、可选目录（scripts、references、assets）及字段约束。 |
| **适用对象** | 本库中所有 `skills/<name>/` 下的 Skill；新建或修改 Skill 时应遵循该规范。 |

---

## 规范要点摘要

- **目录结构**：一个 Skill 对应一个目录，至少包含一个 `SKILL.md`；可选用 `scripts/`、`references/`、`assets/` 等。  
- **SKILL.md 格式**：  
  - **必填 frontmatter**：`name`（1–64 字符，小写字母数字连字符，且与父目录名一致）、`description`（1–1024 字符，说明技能做什么与何时使用）。  
  - **可选**：`license`、`compatibility`、`metadata`、`allowed-tools` 等。  
- **命名规则**：`name` 不得以连字符开头或结尾、不得含连续连字符，且必须与 Skill 目录名一致。

详细约束与示例见 [spec/specification.md](../spec/specification.md)。

---

## 使用场景

| 场景 | 用法 |
|------|------|
| **创建新 Skill** | 按 spec 确定目录名与 `name`、编写 SKILL.md frontmatter 与正文；可配合 [templates-reference.md](./templates-reference.md) 使用。 |
| **校验现有 Skill** | 检查 `name` 是否与目录一致、`description` 长度与内容是否符合要求；可用 skill-creator 中的校验脚本辅助。 |
| **统一本库格式** | 集成外部 Skill 时，按 spec 调整 frontmatter 或目录名，保证与本库其他 Skill 一致。 |
| **理解「Skill」与「Agent」区别** | Spec 只约束 Skill（目录 + SKILL.md）；agents/ 下的角色定义采用类似 frontmatter 但独立于 skills/，不强制符合 spec 的目录与命名。 |

---

## 与其它能力的关系

- **templates/**：提供符合 spec 的最小 SKILL.md 模板。  
- **skills/skill-creator**：提供创建、校验、打包 Skill 的流程，内部依赖对 spec 的理解。  
- **skills/writing-skills**：编写或修改 Skill 内容时，应遵循 spec 中的命名与 frontmatter 要求。
