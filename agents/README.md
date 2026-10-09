# Agents — 子代理 / 角色定义

本目录现有 **20 个角色定义**，不计 README.md。每个角色以 YAML frontmatter 和 Markdown 正文说明任务范围与工具需求。

- 19 个 `seo-*.md` 来自 [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) 的 `agents/`。
- `code-reviewer.md` 来自 [obra/superpowers](https://github.com/obra/superpowers) 的 `skills/requesting-code-review/code-reviewer.md`。

完整功能与使用场景见 [Agent 说明](../docs/agents-reference.md)，上游提交记录见 [更新报告](../docs/upstream-skills-update-2026-10-09.md)。按需加载角色；SEO 启动器位于 `skills/seo/scripts/claude-seo`，环境配置遵循该 Skill 的 setup 流程。
