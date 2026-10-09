# 本库能力列表（对应 skills/ 路径与来源）

以下能力已**完成拷贝与合并**（2025-02-25），每行为本库路径或来源说明。原仓库、集成状态与冲突说明见 [docs/integration-progress.md](docs/integration-progress.md)。

- **skills/**：当前共 **107 个** Skill 目录（原 79 个与用户级 user-skills 28 个已合并，去重后 12 个新增并入；后续有增补，含 zlibrary-to-notebooklm）。
- **除 skills 外**：agents/（7 个子代理）、tools/（REGISTRY + 58 个集成文档）、templates/（Skill 模板），见下方「除 skills 外的 AI 能力」。

**文档索引**：各 Skill 功能与使用场景见 [docs/skills-reference.md](docs/skills-reference.md)；能力总览与集成方式见 [docs/capabilities-index.md](docs/capabilities-index.md)、[docs/cookbook.md](docs/cookbook.md)。

---

## 除 skills 外的 AI 能力（2025-02-25 集成）

- **agents/** — 子代理/角色定义（供主流程或子代理调用）
  - seo-content.md, seo-performance.md, seo-technical.md, seo-sitemap.md, seo-schema.md, seo-visual.md（来源：Claude SEO）
  - code-reviewer.md（来源：Superpowers）
- **tools/** — 营销/分析工具注册与集成说明
  - REGISTRY.md, integrations/*.md（58 个）（来源：Marketing skills）
- **templates/** — Skill 创建模板
  - SKILL-template.md（来源：Anthropics skills）

---

## 本地自用 Skills（2026-10-09 新增）

- [skills/llm-wiki-ingest](skills/llm-wiki-ingest/SKILL.md) — 分析多模态资料，将知识整合写入 llm-wiki。
- [skills/code-security-audit](skills/code-security-audit/SKILL.md) — 执行代码安全审计，生成报告、证据、复现脚本与 ZIP 包。

---

## Anthropics skills（部分已集成）

- skills/algorithmic-art
- skills/brand-guidelines
- skills/canvas-design
- skills/doc-coauthoring
- skills/docx
- skills/frontend-design
- skills/internal-comms
- skills/mcp-builder
- skills/pdf
- skills/pptx
- skills/skill-creator
- skills/slack-gif-creator
- skills/theme-factory
- skills/web-artifacts-builder
- skills/webapp-testing
- skills/xlsx

---

## Cursor 用户级 Skills（已合并进 skills/）

以下原为 `user-skills` 独有，已并入 `skills/`，与本库原有 skill 同目录管理：

- skills/create-adaptable-composable
- skills/element-plus-vue3
- skills/import-anthropic-skills
- skills/skill-usage-guide
- skills/vue-best-practices
- skills/vue-debug-guides
- skills/vue-development-guides
- skills/vue-jsx-best-practices
- skills/vue-options-api-best-practices
- skills/vue-pinia-best-practices
- skills/vue-router-best-practices
- skills/vue-testing-best-practices

---

## NotebookLM（PleasePrompto）

- skills/notebooklm

---

## Z-Library to NotebookLM（zstmfhy）

- skills/zlibrary-to-notebooklm

---

## Obsidian skills（kepano）

- skills/defuddle
- skills/json-canvas
- skills/obsidian-bases
- skills/obsidian-cli
- skills/obsidian-markdown

---

## Claude SEO（AgriciDaniel）

- skills/seo（编排型，统一调用 12 个子 Skill 与 6 个子代理）
- skills/seo-audit
- skills/seo-competitor-pages
- skills/seo-content
- skills/seo-geo
- skills/seo-hreflang
- skills/seo-images
- skills/seo-page
- skills/seo-plan
- skills/seo-programmatic
- skills/seo-schema
- skills/seo-sitemap
- skills/seo-technical

---

## Marketing skills（coreyhaines31）

- skills/ab-test-setup
- skills/ad-creative
- skills/ai-seo
- skills/analytics-tracking
- skills/churn-prevention
- skills/cold-email
- skills/competitor-alternatives
- skills/content-strategy
- skills/copy-editing
- skills/copywriting
- skills/email-sequence
- skills/form-cro
- skills/free-tool-strategy
- skills/launch-strategy
- skills/marketing-ideas
- skills/marketing-psychology
- skills/onboarding-cro
- skills/page-cro
- skills/paid-ads
- skills/paywall-upgrade-cro
- skills/popup-cro
- skills/pricing-strategy
- skills/product-marketing-context
- skills/programmatic-seo
- skills/referral-program
- skills/schema-markup
- skills/seo-audit
- skills/signup-flow-cro
- skills/social-content

---

## 宝雨 skills（JimLiu/baoyu-skills）

- skills/baoyu-article-illustrator
- skills/baoyu-comic
- skills/baoyu-compress-image
- skills/baoyu-cover-image
- skills/baoyu-danger-gemini-web
- skills/baoyu-danger-x-to-markdown
- skills/baoyu-format-markdown
- skills/baoyu-image-gen
- skills/baoyu-infographic
- skills/baoyu-markdown-to-html
- skills/baoyu-post-to-wechat
- skills/baoyu-post-to-x
- skills/baoyu-slide-deck
- skills/baoyu-url-to-markdown
- skills/baoyu-xhs-images

---

## Skill prompt generator（huangserva）

- 参考工具，非标准 Skill 目录；见 docs/integration-progress.md

---

## Agent Skills（agentskills）

- 规范与文档已纳入 spec/；见 docs/integration-progress.md

---

## Article writer（wordflowlab）

- 完整应用，可参考其 AGENTS.md/CLAUDE.md；见 docs/integration-progress.md

---

## Superpowers（obra）

- skills/brainstorming
- skills/dispatching-parallel-agents
- skills/executing-plans
- skills/finishing-a-development-branch
- skills/receiving-code-review
- skills/requesting-code-review
- skills/subagent-driven-development
- skills/systematic-debugging
- skills/test-driven-development
- skills/using-git-worktrees
- skills/using-superpowers
- skills/verification-before-completion
- skills/writing-plans
- skills/writing-skills

---

*本列表按来源分类；完整 107 个 Skill 的目录名见 `skills/` 或 [docs/skills-reference.md](docs/skills-reference.md)。*
