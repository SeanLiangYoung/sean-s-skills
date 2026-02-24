# 本库能力列表（对应 skills/ 路径与来源）

以下能力已**完成拷贝与合并**（2025-02-25），每行为本库路径或来源说明。原仓库、集成状态与冲突说明见 [docs/integration-progress.md](docs/integration-progress.md)。

- **skills/**：当前共 **79 个** Skill 目录。  
- **除 skills 外**：agents/（7 个子代理）、tools/（REGISTRY + 50+ 集成文档）、templates/（Skill 模板），见下方「除 skills 外的 AI 能力」。

---

## 除 skills 外的 AI 能力（2025-02-25 集成）

- **agents/** — 子代理/角色定义（供主流程或子代理调用）
  - seo-content.md, seo-performance.md, seo-technical.md, seo-sitemap.md, seo-schema.md, seo-visual.md（来源：Claude SEO）
  - code-reviewer.md（来源：Superpowers）
- **tools/** — 营销/分析工具注册与集成说明
  - REGISTRY.md, integrations/*.md（约 50+）（来源：Marketing skills）
- **templates/** — Skill 创建模板
  - SKILL-template.md（来源：Anthropics skills）

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

## NotebookLM（PleasePrompto）

- skills/notebooklm

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
