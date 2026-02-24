# Claude 项目说明（本库）

本仓库是**私人 Skill 库**，已配置为 Claude Code 插件（见 `.claude-plugin/plugin.json`）。

- **Skills**：`skills/` 下 79 个能力（文档/Office、设计、SEO、营销、宝雨、开发流程、Obsidian 等），可直接通过 `/技能名` 或按任务上下文调用。
- **Agents**：`agents/` 下 7 个子代理（SEO 专项 + code-reviewer），可由编排型 Skill（如 `seo`）或人工触发。
- **能力索引**：各 Skill/Agent 的功能与使用场景见 [docs/capabilities-index.md](docs/capabilities-index.md) 与 [docs/skills-reference.md](docs/skills-reference.md)。
- **集成到其他项目**：见 [docs/cookbook.md](docs/cookbook.md)。
