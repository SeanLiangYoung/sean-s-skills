# Skills 说明 — 功能与使用场景

本库 **skills/** 下共 **122 个** Skill，每个为符合 [Agent Skills 规范](../spec/specification.md) 的独立能力包（至少含 `SKILL.md`，可含 `scripts/`、`references/`、`assets/`）。其中 79 个为本库原有，12 个由原用户级 user-skills 合并而来（Vue 系列、element-plus-vue3、create-adaptable-composable、import-anthropic-skills、skill-usage-guide），其余为后续集成或新增。以下按**功能分类**列出各 Skill 的具体功能与使用场景。

---

## 一、文档与 Office（PDF / Word / Excel / PPT）

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **pdf** | 读写、合并、拆分、旋转、水印、填表、加解密、OCR 等 PDF 操作 | 用户提到 .pdf、需生成或处理 PDF、提取文字/表格、合并/拆分/填表时使用。 |
| **docx** | 创建、编辑、分析 Word 文档（.docx）；目录、页码、修订与批注 | 需要报告/备忘录/信函/模板为 Word、提取或重组 docx 内容、处理修订与批注时使用。 |
| **xlsx** | 读写、公式、图表、多表与 Excel 文件操作 | 需要生成或解析 Excel、做表格计算与图表时使用。 |
| **pptx** | 创建、编辑 PowerPoint；幻灯片、版式、媒体 | 需要演示文稿、幻灯片排版与内容编辑时使用。 |
| **doc-coauthoring** | 文档协作与共同编辑流程 | 多人协作撰写、审阅与合并文档时使用。 |

---

## 二、设计、前端与网页

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **frontend-design** | 前端页面与组件的视觉与交互设计 | 做页面/组件 UI、布局与交互设计时使用。 |
| **web-artifacts-builder** | 构建可交付的网页产物（静态页、小应用等） | 需要产出可部署的网页或前端产物时使用。 |
| **theme-factory** | 生成与管理主题（颜色、版式等） | 需要多套主题、品牌一致或主题切换时使用。 |
| **canvas-design** | 基于 Canvas 的图形与可视化设计 | 需要图表、插画或 Canvas 绘图时使用。 |
| **brand-guidelines** | 品牌规范与视觉/文案一致性 | 需要统一品牌视觉、用词与风格时使用。 |
| **algorithmic-art** | 算法艺术与程序化图形 | 需要程序生成图案、艺术风格或创意可视化时使用。 |
| **element-plus-vue3** | Element Plus Vue 3 组件库（安装、主题、国际化、API） | Vue 3 项目使用 Element Plus、定制主题或多语言时使用。 |
| **create-adaptable-composable** | 创建可接受 MaybeRef/MaybeRefOrGetter 的 Vue composable | 需要可适配 ref/getter 输入的 composable 时使用。 |
| **skill-usage-guide** | 帮助选择与使用 Cursor/Agent Skills | 不确定用哪个 Skill 或需要按场景选能力时使用。 |
| **import-anthropic-skills** | 从 Anthropic 官方仓库导入 skills 到 Cursor | 需要安装或使用 anthropics/skills 中的 PDF/docx/xlsx 等能力时使用。 |

---

## 三、SEO（含编排与专项）

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **seo** | 编排型：全站/单页 SEO 分析，调度 12 个子 Skill 与 6 个子代理 | 用户说「SEO」「audit」「sitemap」「E-E-A-T」「Core Web Vitals」等，需一站完成多维度 SEO 分析时使用。 |
| **seo-audit** | 站内 SEO 审计与问题诊断 | 「SEO audit」「technical SEO」「为什么没排名」「meta 检查」时使用。 |
| **seo-page** | 单页深度分析 | 针对某一 URL 做标题、描述、内容与结构优化时使用。 |
| **seo-content** | 内容质量与 E-E-A-T 评估 | 评估页面内容深度、可读性、E-E-A-T 与 AI 引用就绪度时使用。 |
| **seo-technical** | 技术 SEO：可抓取、可索引、移动端、CWV、JS 渲染 | 技术层面抓取、索引、移动友好与性能时使用。 |
| **seo-sitemap** | Sitemap 校验与生成 | 需要检查或生成 XML sitemap 时使用。 |
| **seo-schema** | Schema.org 检测、校验与生成 | 需要结构化数据、富摘要、FAQ/产品/面包屑等 schema 时使用。 |
| **seo-images** | 图片 SEO 与优化建议 | 针对图片 alt、格式、尺寸与加载做优化时使用。 |
| **seo-geo** | AI 概览 / 生成式引擎优化（GEO） | 针对 AI 摘要、引用与多引擎展示优化时使用。 |
| **seo-hreflang** | 多语言/多地区 hreflang 与国际化 | 多语言或多地区站点的语言/地区定向时使用。 |
| **seo-plan** | SEO 策略与执行计划 | 制定 SEO 方案、优先级与执行计划时使用。 |
| **seo-programmatic** | 规模化程序化 SEO 页面（模板+数据） | 「programmatic SEO」「大量模板页」「地区/目录页」时使用。 |
| **seo-competitor-pages** | 竞品页面分析与对比 | 分析竞品页面结构与关键词策略时使用。 |
| **ai-seo** | AI 与搜索引擎生态下的 SEO 策略 | 结合 AI 搜索与传统 SEO 做策略时使用。 |

---

## 四、营销、转化与增长（CRO / 广告 / 邮件 / 内容）

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **product-marketing-context** | 创建/维护产品营销上下文文档，供其他营销 Skill 引用 | 「product context」「positioning」「避免重复讲背景」时使用；产出 `.claude/product-marketing-context.md`。 |
| **content-strategy** | 内容策略与规划 | 制定内容日历、主题与渠道策略时使用。 |
| **copywriting** | 营销文案撰写与优化 | 需要广告语、落地页、邮件等文案时使用。 |
| **copy-editing** | 文案润色与风格统一 | 需要校对、语气与可读性优化时使用。 |
| **ad-creative** | 广告创意与素材生成/迭代 | 需要批量或迭代广告创意时使用。 |
| **paid-ads** | 付费广告策略与投放（Google/Meta/LinkedIn 等） | 「PPC」「ROAS」「受众定向」「广告优化」时使用。 |
| **cold-email** | 冷邮件与跟进序列 | 外联、开发信与跟进流程设计时使用。 |
| **email-sequence** | 邮件序列与自动化流程 | 设计欢迎邮件、培育序列、触发邮件时使用。 |
| **social-content** | 社媒内容创作、排期与优化（LinkedIn/X/Instagram 等） | 「LinkedIn post」「Twitter thread」「content calendar」「viral content」时使用。 |
| **page-cro** | 落地页转化优化 | 优化单页转化率、动线与时序时使用。 |
| **form-cro** | 表单转化优化 | 优化表单字段、步骤与流失时使用。 |
| **popup-cro** | 弹窗/模态/条幅转化优化 | 「exit intent」「lead capture popup」「announcement banner」时使用。 |
| **onboarding-cro** | 新用户引导与激活流程优化 | 优化注册后首次使用与激活时使用。 |
| **signup-flow-cro** | 注册/试用注册流程优化 | 「signup conversions」「registration friction」「trial signup」时使用。 |
| **paywall-upgrade-cro** | 应用内付费墙与升级流程优化 | 「paywall」「upgrade modal」「freemium conversion」时使用。 |
| **ab-test-setup** | A/B 测试设计与实施 | 设计实验、样本量与指标时使用。 |
| **analytics-tracking** | 分析与事件埋点设计与实施 | GA4/事件/转化埋点、GTM 等时使用。 |
| **churn-prevention** | 流失预警与挽留策略 | 减少取消、提升留存与复购时使用。 |
| **referral-program** | 推荐/联盟计划设计与优化 | 「referral」「affiliate」「viral loop」时使用。 |
| **competitor-alternatives** | 竞品与替代方案页面/内容策略 | 做「vs 竞品」「alternatives」类页面与内容时使用。 |
| **pricing-strategy** | 定价、套餐与变现策略 | 「pricing tiers」「freemium」「packaging」「Van Westendorp」时使用。 |
| **marketing-ideas** | 营销创意与活动点子 | 需要创意、活动主题或推广思路时使用。 |
| **marketing-psychology** | 营销心理学与说服原理 | 需要从心理学角度优化文案与流程时使用。 |
| **launch-strategy** | 产品/功能发布策略 | 制定发布节奏、渠道与信息时使用。 |
| **free-tool-strategy** | 免费工具/引流品策略 | 用免费工具获客与转化时使用。 |
| **schema-markup** | 结构化数据与富摘要（与 SEO 共用） | 需要 FAQ/产品/评价等 schema 时使用。 |

---

## 五、宝雨系列（图文、发布、排版与生成）

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **baoyu-article-illustrator** | 为文章配图：分析结构、选位、按类型×风格生成插图 | 「为文章配图」「add images to article」时使用。 |
| **baoyu-cover-image** | 文章封面图：类型/配色/渲染/文案/氛围 | 「generate cover image」「create article cover」时使用。 |
| **baoyu-image-gen** | AI 绘图（OpenAI/Google/DashScope），文生图、参考图、比例 | 「generate image」「draw」时使用。 |
| **baoyu-infographic** | 信息图：多版式与视觉风格、推荐组合并生成 | 「infographic」「信息图」「visual summary」时使用。 |
| **baoyu-xhs-images** | 小红书风格图：多风格与版式，拆分为 1–10 张图 | 「小红书图片」「XHS images」「种草图」时使用。 |
| **baoyu-comic** | 知识/教育漫画：多风格与分镜、顺序生成 | 「知识漫画」「教育漫画」「tutorial comic」时使用。 |
| **baoyu-slide-deck** | 幻灯片图：从内容生成提纲与单页图 | 「create slides」「make a presentation」「PPT」时使用。 |
| **baoyu-format-markdown** | 格式化 Markdown：frontmatter、标题、摘要、列表、代码块 | 「format markdown」「beautify article」时使用；输出 `*-formatted.md`。 |
| **baoyu-markdown-to-html** | Markdown 转样式 HTML（公众号兼容、代码/公式/PlantUML） | 「markdown to html」「md转html」时使用。 |
| **baoyu-post-to-wechat** | 发布到微信公众号（文章/图文） | 「发布公众号」「post to wechat」「贴图/图文/文章」时使用。 |
| **baoyu-post-to-x** | 发布到 X（Twitter）：帖文与 X Articles | 「post to X」「tweet」「publish to Twitter」时使用。 |
| **baoyu-url-to-markdown** | URL 转 Markdown（CDP 抓取，支持登录页） | 需要把网页保存为 Markdown 时使用。 |
| **baoyu-danger-x-to-markdown** | X 推文/长文转 Markdown（逆向 API，需用户同意） | 「X to markdown」「save tweet」、提供 x.com 链接时使用。 |
| **baoyu-danger-gemini-web** | 通过 Gemini Web 生成图文（逆向接口） | 需要 Gemini 作图像/文本后端、或「generate image with Gemini」时使用。 |
| **baoyu-compress-image** | 图片压缩（WebP/PNG、自动选工具） | 「compress image」「convert to webp」时使用。 |

---

## 六、开发流程、协作与质量（Superpowers 等）

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **using-superpowers** | 会话开始时建立「先找 Skill 再回答」的规则 | 对话开始时确保会查找并调用本库 Skill 时使用。 |
| **writing-plans** | 将需求/规格写成多步骤实施计划 | 有 spec 或需求、尚未写代码前，先产出可执行计划时使用。 |
| **executing-plans** | 按书面计划执行，带评审检查点 | 已有实施计划、在独立会话中执行并需 checkpoint 时使用。 |
| **dispatching-parallel-agents** | 将 2+ 独立任务分发给并行子代理 | 多个无依赖任务可并行时使用。 |
| **subagent-driven-development** | 按任务拆分子代理驱动开发 | 计划中任务相对独立、需分代理执行时使用。 |
| **test-driven-development** | TDD：先写测试、红-绿-重构 | 做功能或修 bug 前，采用 TDD 时使用。 |
| **vue-best-practices** | Vue 3 Composition API、&lt;script setup&gt;、TypeScript 等最佳实践 | Vue 开发时优先加载，规范写法与工程约定。 |
| **vue-development-guides** | Vue 开发、重构与代码审查的实践与技巧 | 开发/重构/评审 Vue 或 Nuxt 项目时使用。 |
| **vue-debug-guides** | Vue 3 运行时错误、警告、SSR/水合问题排查 | 诊断或修复 Vue 报错、控制台警告、水合错误时使用。 |
| **vue-testing-best-practices** | Vitest、Vue Test Utils、组件测试、E2E（Playwright） | Vue 单测与 E2E 时使用。 |
| **vue-router-best-practices** | Vue Router 4 路由、守卫、params 与生命周期 | 路由、导航守卫、动态路由时使用。 |
| **vue-pinia-best-practices** | Pinia 状态、store 设置与响应式 | Pinia 仓库、状态管理时使用。 |
| **vue-jsx-best-practices** | Vue 中 JSX 语法（class/className、插件配置） | 使用 JSX 写 Vue 时使用。 |
| **vue-options-api-best-practices** | Vue 3 Options API（data、methods、this） | 仅用 Options API 时参考。 |
| **systematic-debugging** | 系统性排查 bug/失败/异常 | 遇到 bug、测试失败或异常行为、在提出修复前系统排查时使用。 |
| **verification-before-completion** | 在声称完成/修复/通过前必须跑验证并出示结果 | 准备说「完成了」「修好了」「通过了」之前，先跑验证命令并确认输出时使用。 |
| **requesting-code-review** | 完成任务或大功能后请求代码评审 | 完成主要功能或合并前，请求评审时使用。 |
| **receiving-code-review** | 接收评审意见并严谨落实（不盲从） | 收到评审反馈、在改代码前理解并验证建议时使用。 |
| **finishing-a-development-branch** | 实现完成且测试通过后，选择合并/PR/清理方式 | 开发收尾、决定如何合入主线时使用。 |
| **using-git-worktrees** | 创建隔离的 git worktree 做功能开发 | 需要与当前工作区隔离做功能或按计划执行时使用。 |
| **brainstorming** | 创意与需求探索，再做实现 | 做功能、组件或行为修改等创意工作前，先澄清意图与设计时使用。 |
| **writing-skills** | 创建/编辑/校验 Skill，部署前验证 | 写新 Skill、改现有 Skill、或部署前验证 Skill 时使用。 |

---

## 七、Obsidian 与知识库

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **obsidian-bases** | 创建与编辑 Obsidian Bases（.base）：视图、筛选、公式、汇总 | 使用 .base、表格/卡片视图、筛选与公式时使用。 |
| **obsidian-cli** | Obsidian 命令行与脚本操作 | 需要命令行操作 Obsidian 或 vault 时使用。 |
| **obsidian-markdown** | Obsidian 风格 Markdown 与双链等 | 需要符合 Obsidian 语法的笔记与链接时使用。 |
| **defuddle** | 解混/澄清模糊内容（与 Obsidian 笔记配合） | 整理或澄清混乱/模糊文本时使用。 |
| **json-canvas** | JSON Canvas 格式的创建与编辑 | 使用 JSON Canvas 做画布/白板时使用。 |

---

## 八、NotebookLM 与 MCP / 内部协作

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **notebooklm** | 查询 Google NotebookLM 笔记本，获取基于文档的引用回答 | 用户提到 NotebookLM、分享 notebook 链接、或要「问我的文档」时使用。 |
| **zlibrary-to-notebooklm** | 一键从 Z-Library 下载书籍并上传到 Google NotebookLM（PDF/EPUB、自动转换与分块） | 用户提供 Z-Library 书籍链接、要求「上传到 NotebookLM」「自动下载并读这本书」时使用；需合法资源。 |
| **mcp-builder** | 构建与维护 MCP（Model Context Protocol）服务与工具 | 需要为 AI 提供自定义 MCP 工具或数据源时使用。 |
| **internal-comms** | 内部沟通与文档模板（如公告、变更说明） | 需要内部公告、变更说明等模板与流程时使用。 |

---

## 九、元能力与其它

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| **skill-creator** | 创建、校验、打包 Skill；符合规范与最佳实践 | 从零创建新 Skill、校验 frontmatter 与目录、打包发布时使用。 |
| **webapp-testing** | Web 应用测试（含浏览器自动化与断言） | 对 Web 应用做功能/端到端测试时使用。 |
| **slack-gif-creator** | 为 Slack 等场景创建 GIF | 需要制作 Slack 用 GIF 时使用。 |

---

## 使用建议

- **按关键词/意图选**：上述表格中的「使用场景」多为触发短语或任务类型，可按用户表述匹配。  
- **编排与组合**：全站 SEO 用 **seo**；单点 SEO 用对应 **seo-***；营销流程可组合 **product-marketing-context** + **email-sequence** + **paid-ads** 等。  
- **详细说明在 SKILL.md**：每个 Skill 的完整步骤、命令与约束见 `skills/<name>/SKILL.md`。


## 本地知识入库与安全审计（2026-10-09 新增）

| Skill | 功能简述 | 使用场景 |
|-------|----------|----------|
| [llm-wiki-ingest](../skills/llm-wiki-ingest/SKILL.md) | 分析文字、链接、文档、图片及音视频，提炼有依据的知识并整合保存到 llm-wiki | 资料入库、跨资料综合和知识页面更新；知识库位置见 skill 内的 wiki-config.md。 |
| [code-security-audit](../skills/code-security-audit/SKILL.md) | 审计源码、依赖与部署配置，验证并复测漏洞，生成中文报告、证据、复现脚本与 ZIP 包 | 已授权仓库安全审计、SaaS 权限审查及 Azure DevOps/AKS 审查。 |

## 2026-10-09 上游依赖补齐

新增 SEO 总控依赖与营销研究依赖：`seo-agentic`, `seo-backlinks`, `seo-cluster`, `seo-content-brief`, `seo-dataforseo`, `seo-drift`, `seo-ecommerce`, `seo-flow`, `seo-google`, `seo-image-gen`, `seo-local`, `seo-maps`, `seo-sxo`, `competitor-profiling`, `customer-research`。各技能的完整说明见对应 `skills/<name>/SKILL.md`；来源与同步记录见 [上游更新报告](upstream-skills-update-2026-10-09.md)。
