# Agents 说明 — 子代理 / 角色定义

本库 **agents/** 目录下的 Markdown 文件为可复用的 **AI 角色定义**（子代理提示），格式为 YAML frontmatter（`name`、`description`、`tools` 等）+ 正文指令。可被主流程、编排型 Skill（如 `skills/seo`）或人工指定加载，作为专项分析/评审角色使用。

---

## 1. code-reviewer

| 项目 | 说明 |
|------|------|
| **文件** | `agents/code-reviewer.md` |
| **来源** | obra/superpowers |
| **功能** | 担任高级代码评审角色：对照原计划与编码标准，对已完成的主要开发步骤做实现与质量评审。 |
| **工具** | 继承（model: inherit） |
| **使用场景** | • 用户完成某一功能或步骤后，要求「按计划与规范做一次代码评审」<br>• 完成规划中的某一步（如「步骤 3：用户认证」）后，在合并或提 PR 前做一次检查<br>• 需要结构化反馈：计划对齐、代码质量、架构与设计、文档与规范、问题分级（Critical/Important/Suggestion）与建议 |

---

## 2. seo-content

| 项目 | 说明 |
|------|------|
| **文件** | `agents/seo-content.md` |
| **来源** | AgriciDaniel/claude-seo |
| **功能** | 内容质量评审：基于 Google 质量评估指南，评估 E-E-A-T、可读性、内容深度、AI 引用就绪度、薄内容等。 |
| **工具** | Read, Bash, Write, Grep |
| **使用场景** | • 对单页或整站内容做 E-E-A-T 与可读性评估<br>• 检查字数是否满足页面类型最低要求（如博客 1500+、产品页 300+）<br>• 评估内容是否适合被 AI 引用（事实清晰、结构明确）<br>• 识别疑似低质量 AI 内容特征（泛化表述、缺乏一手经验等） |

---

## 3. seo-performance

| 项目 | 说明 |
|------|------|
| **文件** | `agents/seo-performance.md` |
| **来源** | AgriciDaniel/claude-seo |
| **功能** | 性能分析：围绕 Core Web Vitals（LCP、INP、CLS）与页面加载性能做评估与建议。 |
| **工具** | Read, Bash, Write |
| **使用场景** | • 评估页面或站点是否达到「Good」阈值（如 LCP≤2.5s、INP≤200ms、CLS≤0.1）<br>• 分析 LCP/INP/CLS 常见问题并给出可执行优化建议<br>• 需要基于 75th 分位数的评估方法说明 |

---

## 4. seo-technical

| 项目 | 说明 |
|------|------|
| **文件** | `agents/seo-technical.md` |
| **来源** | AgriciDaniel/claude-seo |
| **功能** | 技术 SEO 专项：分析可抓取性、可索引性、安全、URL 结构、移动端优化、Core Web Vitals、JS 渲染等。 |
| **工具** | Read, Bash, Write, Grep |
| **使用场景** | • 技术 SEO 审计（爬虫可访问性、索引设置、robots/meta）<br>• 移动端友好性与 JS 渲染对 SEO 的影响分析<br>• 与性能、结构化数据等配合做全站技术评估 |

---

## 5. seo-sitemap

| 项目 | 说明 |
|------|------|
| **文件** | `agents/seo-sitemap.md` |
| **来源** | AgriciDaniel/claude-seo |
| **功能** | Sitemap 架构：校验现有 XML sitemap、按行业模板生成新 sitemap、对位置页等实施质量门控。 |
| **工具** | Read, Bash, Write |
| **使用场景** | • 校验或生成 XML sitemap<br>• 多地域/多类型页面（如门店页）的 sitemap 规范与质量要求<br>• 与 `skills/seo-sitemap` 等 Skill 配合使用 |

---

## 6. seo-schema

| 项目 | 说明 |
|------|------|
| **文件** | `agents/seo-schema.md` |
| **来源** | AgriciDaniel/claude-seo |
| **功能** | Schema 标记专家：检测、校验并生成 Schema.org 结构化数据（JSON-LD）。 |
| **工具** | Read, Bash, Write |
| **使用场景** | • 检测页面现有 JSON-LD 并校验语法与类型<br>• 为产品、FAQ、面包屑等生成或补全 Schema<br>• 与 `skills/seo-schema` 等 Skill 配合使用 |

---

## 7. seo-visual

| 项目 | 说明 |
|------|------|
| **文件** | `agents/seo-visual.md` |
| **来源** | AgriciDaniel/claude-seo |
| **功能** | 视觉分析：截屏、移动端渲染测试、首屏内容分析（常配合 Playwright 等）。 |
| **工具** | Read, Bash, Write |
| **使用场景** | • 评估首屏内容与移动端展示效果<br>• 配合内容与性能分析做「所见即所得」的页面质量评估<br>• 需要截图或自动化浏览器时作为子代理调用 |

---

## 使用方式

- **单独加载**：将对应 `.md` 内容（含 frontmatter）作为系统提示或子代理指令传入。
- **被编排 Skill 调用**：`skills/seo` 在运行全站/单页 SEO 分析时会调度上述 6 个 SEO 子代理（seo-content、seo-performance、seo-technical、seo-sitemap、seo-schema、seo-visual）；code-reviewer 可在完成开发步骤后由人工或流程触发。
- **与 Skill 的区别**：Agent 仅为角色/提示定义，无独立目录与 scripts；Skill 为完整能力包（含 SKILL.md、可选 scripts/references）。
