# Agents — 子代理 / 角色定义

本目录为**可复用的 AI 角色定义**（Agent 提示），供主流程调用或作为子代理使用。格式为 Markdown + YAML frontmatter（`name`、`description`、`tools` 等）。

## 来源与规范

- **seo-*.md**（6 个）：来自 [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) 的 `agents/`，用于 SEO 内容、性能、技术、Sitemap、Schema、视觉等专项分析。
- **code-reviewer.md**：来自 [obra/superpowers](https://github.com/obra/superpowers) 的 `agents/`，用于在完成主要开发步骤后进行代码评审。

使用方式：在需要对应角色时加载该文件内容作为系统提示或子代理指令。
