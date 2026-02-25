---
name: skill-usage-guide
description: 帮助 Agent 和用户选择正确的 Cursor skill。当用户请求不明确应使用哪个 skill、需要了解可用 skills、或需要 skill 选择决策时使用。提供按场景分类的 skill 列表和快速决策流程。
---

# Skill 使用指南

当收到用户请求时，根据以下规则选择最匹配的 skill。

## 文档类 → 直接对应

| 用户需求 | 使用 Skill |
|----------|------------|
| PDF 相关（读、写、合并、表单、OCR） | pdf |
| Word 文档（.docx） | docx |
| Excel/表格（.xlsx、.csv） | xlsx |
| PowerPoint（.pptx、幻灯片） | pptx |

## Vue 开发 → 按技术栈选择

| 用户需求 | 使用 Skill |
|----------|------------|
| Vue 3 通用开发、Composition API | vue-best-practices |
| Vue/Nuxt 项目开发、重构、审查 | vue-development-guides |
| Vue 3 报错、水合问题、调试 | vue-debug-guides |
| Options API（data、methods） | vue-options-api-best-practices |
| Vue Router 4 | vue-router-best-practices |
| Pinia 状态管理 | vue-pinia-best-practices |
| Vue 中 JSX | vue-jsx-best-practices |
| Vue 测试（Vitest、Playwright） | vue-testing-best-practices |
| 创建 composable | create-adaptable-composable |
| Element Plus 组件（Vue 3） | element-plus-vue3 |

## 设计与创意

| 用户需求 | 使用 Skill |
|----------|------------|
| 网页 UI、落地页、仪表盘 | frontend-design |
| 海报、静态视觉 | canvas-design |
| 算法艺术、p5.js、粒子 | algorithmic-art |
| 主题、配色、字体 | theme-factory |
| 品牌规范 | brand-guidelines |

## 工具与基础设施

| 用户需求 | 使用 Skill |
|----------|------------|
| 测试 Web 应用（Playwright） | webapp-testing |
| 构建 MCP 服务器 | mcp-builder |
| 复杂 HTML 构件（React、shadcn） | web-artifacts-builder |
| 创建新 skill | skill-creator |
| 文档协作、提案 | doc-coauthoring |
| 内部沟通（周报、FAQ） | internal-comms |
| Slack GIF | slack-gif-creator |
| 导入 Anthropic skills | import-anthropic-skills |

## 决策原则

1. **文件类型优先**：涉及 .pdf/.docx/.xlsx/.pptx 时，直接选对应文档 skill
2. **技术栈匹配**：Vue 3 用 vue-*，Element Plus 用 element-plus-vue3
3. **可组合**：如「Vue 3 + Element Plus 表单」可同时用 vue-best-practices 与 element-plus-vue3
4. **不确定时**：参考 `~/.cursor/SKILLS_GUIDE.md` 完整列表
