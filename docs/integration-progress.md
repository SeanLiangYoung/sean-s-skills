# 开源 Skill 集成进度与能力记录

本文档记录从 [skill-list.md](../skill-list.md) 中各开源仓库**获取的能力**、处理进度，以及纳入本库后对应的本地路径。  
**skills/ 当前共 107 个**（含 2025-02-25 合并的 Cursor 用户级 user-skills，及后续集成的 zlibrary-to-notebooklm，见 [skill-list.md](../skill-list.md)）。
最后更新：2025-02-25。

---

## 进度总览

| 序号 | 来源 | 状态 | 本库能力路径（skills/ 下） |
|------|------|------|-----------------------------|
| 1 | Anthropics skills | **已集成** 2025-02-25 | 见下方「Anthropics」 |
| 2 | NotebookLM skill | **已集成** 2025-02-25 | skills/notebooklm |
| 3 | Obsidian skills | **已集成** 2025-02-25 | obsidian-*（5 个） |
| 4 | Claude SEO | **已集成** 2025-02-25 | seo-*（12 个） |
| 5 | Marketing skills | **已集成** 2025-02-25 | 见下方「Marketing」 |
| 6 | 宝雨 skills (baoyu) | **已集成** 2025-02-25 | baoyu-*（15 个） |
| 7 | Skill prompt generator | 已盘点（参考工具） | 见说明 |
| 8 | Agent Skills (agentskills) | 已盘点 | 规范已纳入 spec/ |
| 9 | Article writer | 已盘点 | 见说明 |
| 10 | Superpowers | **已集成** 2025-02-25 | 见下方「Superpowers」 |
| 11 | Z-Library to NotebookLM (zstmfhy) | **已集成** 2025-02-25 | skills/zlibrary-to-notebooklm |

---

## 1. Anthropics skills

- **原仓库**: https://github.com/anthropics/skills  
- **状态**: **已集成** 2025-02-25。本库原有 12 个同源/同名能力，本次补充拷贝 4 个：internal-comms, mcp-builder, slack-gif-creator, webapp-testing。  
- **能力列表**（仓库内 `skills/` 下）:
  - algorithmic-art, brand-guidelines, canvas-design, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx  
- **本库路径**: 上述 16 个均在 `skills/` 下（与目录名一致）。  
- **除 skills 外已集成**（2025-02-25）：  
  - **templates/**：`templates/SKILL-template.md` 来自仓库 `template/SKILL.md`，用于按规范创建新 Skill。

---

## 2. NotebookLM skill

- **原仓库**: https://github.com/PleasePrompto/notebooklm-skill  
- **状态**: **已集成** 2025-02-25。  
- **能力**: 单一 Skill，用于从 Claude 查询 Google NotebookLM、基于文档的溯源回答与浏览器自动化。  
- **本库对应路径**: `skills/notebooklm`（已拷贝仓库根目录内容：SKILL.md、scripts/、references/、images/、LICENSE 等）。

---

## 3. Obsidian skills (kepano)

- **原仓库**: https://github.com/kepano/obsidian-skills  
- **状态**: **已集成** 2025-02-25。  
- **能力列表**（仓库内 `skills/` 下）:
  - defuddle, json-canvas, obsidian-bases, obsidian-cli, obsidian-markdown  
- **本库对应路径**:  
  `skills/defuddle`, `skills/json-canvas`, `skills/obsidian-bases`, `skills/obsidian-cli`, `skills/obsidian-markdown`

---

## 4. Claude SEO (AgriciDaniel)

- **原仓库**: https://github.com/AgriciDaniel/claude-seo  
- **状态**: **已集成** 2025-02-25。  
- **能力列表**（仓库内 `skills/` 下）:
  - seo-audit, seo-competitor-pages, seo-content, seo-geo, seo-hreflang, seo-images, seo-page, seo-plan, seo-programmatic, seo-schema, seo-sitemap, seo-technical  
- **本库对应路径**:  
  `skills/seo-audit`, `skills/seo-competitor-pages`, `skills/seo-content`, `skills/seo-geo`, `skills/seo-hreflang`, `skills/seo-images`, `skills/seo-page`, `skills/seo-plan`, `skills/seo-programmatic`, `skills/seo-schema`, `skills/seo-sitemap`, `skills/seo-technical`  
- **除 skills 外已集成**（2025-02-25）：  
  - **skills/seo**：编排型 Skill（仓库内 `seo/`），统一调用上述 12 个子 Skill 与 6 个子代理。  
  - **agents/**：6 个子代理角色定义（seo-content, seo-performance, seo-technical, seo-sitemap, seo-schema, seo-visual），来自仓库 `agents/`。

---

## 5. Marketing skills (coreyhaines31)

- **原仓库**: https://github.com/coreyhaines31/marketingskills  
- **状态**: **已集成** 2025-02-25。  
- **能力列表**（仓库内 `skills/` 下）:  
  ab-test-setup, ad-creative, ai-seo, analytics-tracking, churn-prevention, cold-email, competitor-alternatives, content-strategy, copy-editing, copywriting, email-sequence, form-cro, free-tool-strategy, launch-strategy, marketing-ideas, marketing-psychology, onboarding-cro, page-cro, paid-ads, paywall-upgrade-cro, popup-cro, pricing-strategy, product-marketing-context, programmatic-seo, referral-program, schema-markup, seo-audit, signup-flow-cro, social-content  
- **本库对应路径**:  
  同上名称均在 `skills/` 下（与 Marketing 仓库 skills/ 子目录一致；seo-audit 与 Claude SEO 同名，本库保留后拷贝版本）。  
- **除 skills 外已集成**（2025-02-25）：  
  - **tools/**：`tools/REGISTRY.md` + `tools/integrations/*.md`（约 50+ 个工具集成说明），供 AI 发现与调用营销/分析类第三方工具。

---

## 6. 宝雨 skills (JimLiu/baoyu-skills)

- **原仓库**: https://github.com/JimLiu/baoyu-skills (tree/main)  
- **状态**: **已集成** 2025-02-25。  
- **能力列表**（仓库内 `skills/` 下）:  
  baoyu-article-illustrator, baoyu-comic, baoyu-compress-image, baoyu-cover-image, baoyu-danger-gemini-web, baoyu-danger-x-to-markdown, baoyu-format-markdown, baoyu-image-gen, baoyu-infographic, baoyu-markdown-to-html, baoyu-post-to-wechat, baoyu-post-to-x, baoyu-slide-deck, baoyu-url-to-markdown, baoyu-xhs-images（共 15 个）  
- **本库对应路径**:  
  同上名称均在 `skills/` 下。  
- **除 skills 外已集成**（2025-02-25）：  
  - **agents/**：`agents/code-reviewer.md` 来自仓库 `agents/`，用于完成主要开发步骤后的代码评审子代理。

---

## 7. Skill prompt generator (huangserva)

- **原仓库**: https://github.com/huangserva/skill-prompt-generator  
- **状态**: 已盘点。  
- **说明**: 项目为 Prompt/Skill 生成器工具（含 core、design-logic、YAML 配置等），非标准 Agent Skill 目录结构。  
- **建议**: 可作为「生成/维护 Skill 提示」的参考工具；若需纳入本库，可单独建 `skills/skill-prompt-generator` 并放入使用说明与引用链接，或仅保留在文档中引用。

---

## 8. Agent Skills (agentskills)

- **原仓库**: https://github.com/agentskills/agentskills  
- **状态**: 已盘点。  
- **说明**: 提供 Agent Skill 规范、文档与 `skills-ref` 等；本库已采用其规范（见 `spec/specification.md`）。  
- **本库对应**: 规范与文档来源，已纳入 `spec/`；无额外独立 Skill 目录需拷贝。

---

## 9. Article writer (wordflowlab)

- **原仓库**: https://github.com/wordflowlab/article-writer (tree/main)  
- **状态**: 已盘点。  
- **说明**: 项目为完整写作应用（plugins、src、templates 等），非单一 skills 目录。  
- **建议**: 可参考其 AGENTS.md/CLAUDE.md 作为「写作/排版」能力说明；若需以 Skill 形式集成，可新增 `skills/article-writer` 并在 SKILL.md 中描述工作流与指向该仓库的引用。

---

## 10. Superpowers (obra)

- **原仓库**: https://github.com/obra/superpowers  
- **状态**: **已集成** 2025-02-25。  
- **能力列表**（仓库内 `skills/` 下）:  
  brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills（共 14 个）  
- **本库对应路径**:  
  同上名称均在 `skills/` 下。

---

## 11. Z-Library to NotebookLM（zstmfhy）

- **原仓库**: https://github.com/zstmfhy/zlibrary-to-notebooklm  
- **状态**: **已集成** 2025-02-25。  
- **能力**: 一键将 Z-Library 书籍自动下载并上传到 Google NotebookLM；支持 PDF/EPUB、自动转换与智能分块（>350k 词）；需 Playwright、NotebookLM CLI，会话保存在 `~/.zlibrary/`。  
- **本库对应路径**: `skills/zlibrary-to-notebooklm`（已拷贝 SKILL.md、scripts/、docs/、requirements.txt、LICENSE、INSTALL.md；路径与 frontmatter 已适配本库规范）。

---

## 获取过程中增加的能力（汇总）

从上述仓库**盘点得到**、本库可新增或已部分具备的能力归纳如下：

- **NotebookLM**: 1 个 Skill（notebooklm）。  
- **Obsidian**: 5 个 Skill（defuddle, json-canvas, obsidian-bases, obsidian-cli, obsidian-markdown）。  
- **Claude SEO**: 12 个 SEO 相关 Skill。  
- **Marketing**: 约 29 个营销/转化/SEO 类 Skill。  
- **宝雨**: 15 个 baoyu-* Skill（图文、排版、发布等）。  
- **Superpowers**: 14 个开发流程与协作类 Skill。  
- **Anthropics**: 4 个本库尚未包含的 Skill（internal-comms, mcp-builder, slack-gif-creator, webapp-testing）。  

**说明**: 序号 1–6、10、11 已完成拷贝合并（2025-02-25）；序号 7–9 为参考/规范来源，未拷贝为独立 Skill 目录。各仓库 LICENSE 与版权归属仍以原仓库为准，本库仅汇总使用。

---

## 除 skills 外的 AI 能力集成（2025-02-25）

在保留 Agent Skills 规范（`skills/` + SKILL.md）的前提下，从同一批仓库中抽取**可复用且结构清晰**的 AI 能力，统一纳入本库：

| 类型 | 本库路径 | 来源 | 说明 |
|------|----------|------|------|
| **子代理 / 角色** | agents/ | Claude SEO agents/、Superpowers agents/ | 7 个 .md（6 个 SEO 专项 + 1 个 code-reviewer），YAML frontmatter + 正文，可作子代理或角色提示。 |
| **工具索引与集成** | tools/ | Marketing tools/ | REGISTRY.md + integrations/*.md（约 50+），供 Agent 发现与调用营销/分析/SEO 等第三方工具。 |
| **Skill 模板** | templates/ | Anthropics template/ | SKILL-template.md，符合 spec 的最小模板，用于创建新 Skill。 |
| **编排型 Skill** | skills/seo | Claude SEO seo/ | 统一编排 12 个 seo-* 子 Skill 与 6 个子代理的 SEO 总控 Skill。 |

上述内容均已拷贝并附带各目录下 README.md 注明来源；使用方式见各目录 README。

---

## 集成记录（2025-02-25）

- 使用临时目录 `.tmp-integration` 对各仓库执行 `git clone --depth 1`，再将对应 `skills/` 或仓库根目录拷贝至本库 `skills/`。  
- 命名冲突：Marketing 与 Claude SEO 均含 `seo-audit`，本库保留后拷贝的 Marketing 版本；其余无覆盖。  
- 集成后本库 `skills/` 下共 **79 个** Skill 目录（含原有 + 本次新增 **skills/seo** 编排 Skill）。  
- **除 skills 外**：已集成 agents/（7 个）、tools/（REGISTRY + 50+ 集成文档）、templates/（1 个模板）、详见上文「除 skills 外的 AI 能力集成」。  
- 临时克隆目录 `.tmp-integration` 可删除以释放空间：`rm -rf .tmp-integration`。


## 本地 Skills 同步（2026-10-09）

从本地 Codex 用户级 skills 导入以下完整能力包，当前共 107 个 Skill；历史集成数量保留原记录。

| Skill | 用途 | 本库路径 |
|-------|------|----------|
| llm-wiki-ingest | 多模态资料分析、知识综合与知识库写入 | [SKILL.md](../skills/llm-wiki-ingest/SKILL.md) |
| code-security-audit | 源码与部署安全审计、漏洞复测、报告及证据打包 | [SKILL.md](../skills/code-security-audit/SKILL.md) |

保留配置、agents 元数据、references 和 scripts，排除 Python 缓存。
