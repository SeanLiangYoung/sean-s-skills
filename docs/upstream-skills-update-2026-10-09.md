# 外源 Skills 更新核验报告

核验日期：2026-10-09（Asia/Shanghai）。直接获取 9 个上游仓库的默认发布分支，按内容比较同步，不仅依赖版本号。

现有外源 Skill：**91 个更新，10 个内容未变**；补齐 **15 个依赖 Skill**。另保留 2 个来源/发布状态不明确的 Skill 和 4 个本地 Skill。项目顶层现有 **122 个 Skill**。

## 上游快照

| 上游 | 分支 | 提交 | 提交时间 | 更新 / 未变 / 新增 |
|---|---|---|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | main | [683bc88e56f3](https://github.com/anthropics/skills/commit/683bc88e56f3e09ba94f7055977f3d3aa499f202) | 2026-10-05T06:46:42-07:00 | 14 / 2 / 0 |
| [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill) | master | [c80722d3f27d](https://github.com/PleasePrompto/notebooklm-skill/commit/c80722d3f27d65e06b6579add201bf69b99101d0) | 2026-09-10T09:43:42+02:00 | 0 / 1 / 0 |
| [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) | main | [3ccff5338ea7](https://github.com/kepano/obsidian-skills/commit/3ccff5338ea700537839b21900aa5358a0402c98) | 2026-09-15T07:43:57-07:00 | 5 / 0 / 0 |
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | main | [4b99de2f7de7](https://github.com/AgriciDaniel/claude-seo/commit/4b99de2f7de7e7d5247042e5fb5b4ea9368ef734) | 2026-10-05T02:40:56+03:00 | 12 / 0 / 13 |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | main | [1efedbc5148b](https://github.com/coreyhaines31/marketingskills/commit/1efedbc5148b54b2f0f6c6c9fe0be62e151c7fff) | 2026-10-08T14:51:37-07:00 | 29 / 0 / 2 |
| [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) | main | [1567581c26ec](https://github.com/JimLiu/baoyu-skills/commit/1567581c26ec29f4216c6e6835415bf30343b0e3) | 2026-09-10T10:13:43-05:00 | 15 / 0 / 0 |
| [obra/superpowers](https://github.com/obra/superpowers) | main | [8ca22dba9a94](https://github.com/obra/superpowers/commit/8ca22dba9a94f28898bbce59f2537ff4d87c747d) | 2026-09-25T11:06:27-07:00 | 14 / 0 / 0 |
| [zstmfhy/zlibrary-to-notebooklm](https://github.com/zstmfhy/zlibrary-to-notebooklm) | main | [4eb1f04a49e9](https://github.com/zstmfhy/zlibrary-to-notebooklm/commit/4eb1f04a49e9bd2f846c26be4b025f8f9b9e7249) | 2026-01-15T03:23:46-08:00 | 0 / 1 / 0 |
| [vuejs-ai/skills](https://github.com/vuejs-ai/skills) | main | [c9d355ff23f6](https://github.com/vuejs-ai/skills/commit/c9d355ff23f654309dd02006be671859df0a134c) | 2026-03-26T06:50:25+01:00 | 2 / 6 / 0 |

## 兼容与保留策略

- Marketing 的 18 个旧目录保留原名；内容对应上游重命名后的 Skill。`form-cro` 与 `page-cro` 都使用上游合并后的 `cro`，包含最新表单参考资料。明确的技能引用同步适配；产品上下文文件名保持上游规则。
- `seo-audit` 按原集成记录继续使用 Marketing 版本，Claude SEO 的同名版本未覆盖它。Claude SEO 全审计仍存在两个来源对同名 Skill 含义不同的集成限制，使用时需选对工作流。
- 补齐 Claude SEO 当前主技能目录的 13 个依赖 Skill，以及对应 agents、脚本、数据、schema、资源与扩展目录。将启动器路径适配到本库 `skills/seo/scripts/claude-seo`。扩展目录随运行时携带，未单独添加为顶层 Skill。
- 补齐 `paid-ads` 资料链接依赖的 `competitor-profiling` 和 `customer-research`。其他上游新增可选技能未整批导入。
- NotebookLM 内容未变，保留现有 README；Z-Library 的源码未变，完整保留原有 frontmatter、路径适配及安装包装。
- `vue-development-guides`：来源组织已确认，但当前 `vuejs-ai/skills` 发布分支不再包含此目录；保留本地版本，不用另一技能替换。
- `element-plus-vue3`：未找到可确认的 Skill 原始仓库；其文档里的 Element Plus 链接是组件库来源，不能据此确认 Skill 的更新。
- 本地 `import-anthropic-skills`、`skill-usage-guide`、`llm-wiki-ingest`、`code-security-audit` 保留。
- 同步前已有的本库修改均保留；按用户后续要求，与本次更新一起提交到本地 Git，未推送。

## 文件清单

完整来源、提交、文件增删和安装文件 SHA-256 记录在 [upstream-skills-lock.json](upstream-skills-lock.json)。哈希格式为 `sha256-utf8-lf`：UTF-8 文本统一 LF 后计算 SHA-256，二进制按原始字节计算，兼容 Git 的换行转换。运行 `python scripts/validate-skills.py` 可复核。

| 本库 Skill | 上游路径 | 结果 |
|---|---|---|
| `skills/algorithmic-art` | `anthropics/skills/skills/algorithmic-art` | 更新 |
| `skills/brand-guidelines` | `anthropics/skills/skills/brand-guidelines` | 更新 |
| `skills/canvas-design` | `anthropics/skills/skills/canvas-design` | 更新 |
| `skills/doc-coauthoring` | `anthropics/skills/skills/doc-coauthoring` | 未变 |
| `skills/docx` | `anthropics/skills/skills/docx` | 更新 |
| `skills/frontend-design` | `anthropics/skills/skills/frontend-design` | 更新 |
| `skills/internal-comms` | `anthropics/skills/skills/internal-comms` | 更新 |
| `skills/mcp-builder` | `anthropics/skills/skills/mcp-builder` | 更新 |
| `skills/pdf` | `anthropics/skills/skills/pdf` | 未变 |
| `skills/pptx` | `anthropics/skills/skills/pptx` | 更新 |
| `skills/skill-creator` | `anthropics/skills/skills/skill-creator` | 更新 |
| `skills/slack-gif-creator` | `anthropics/skills/skills/slack-gif-creator` | 更新 |
| `skills/theme-factory` | `anthropics/skills/skills/theme-factory` | 更新 |
| `skills/web-artifacts-builder` | `anthropics/skills/skills/web-artifacts-builder` | 更新 |
| `skills/webapp-testing` | `anthropics/skills/skills/webapp-testing` | 更新 |
| `skills/xlsx` | `anthropics/skills/skills/xlsx` | 更新 |
| `skills/defuddle` | `kepano/obsidian-skills/skills/defuddle` | 更新 |
| `skills/json-canvas` | `kepano/obsidian-skills/skills/json-canvas` | 更新 |
| `skills/obsidian-bases` | `kepano/obsidian-skills/skills/obsidian-bases` | 更新 |
| `skills/obsidian-cli` | `kepano/obsidian-skills/skills/obsidian-cli` | 更新 |
| `skills/obsidian-markdown` | `kepano/obsidian-skills/skills/obsidian-markdown` | 更新 |
| `skills/baoyu-article-illustrator` | `JimLiu/baoyu-skills/skills/baoyu-article-illustrator` | 更新 |
| `skills/baoyu-comic` | `JimLiu/baoyu-skills/skills/baoyu-comic` | 更新 |
| `skills/baoyu-compress-image` | `JimLiu/baoyu-skills/skills/baoyu-compress-image` | 更新 |
| `skills/baoyu-cover-image` | `JimLiu/baoyu-skills/skills/baoyu-cover-image` | 更新 |
| `skills/baoyu-danger-gemini-web` | `JimLiu/baoyu-skills/skills/baoyu-danger-gemini-web` | 更新 |
| `skills/baoyu-danger-x-to-markdown` | `JimLiu/baoyu-skills/skills/baoyu-danger-x-to-markdown` | 更新 |
| `skills/baoyu-format-markdown` | `JimLiu/baoyu-skills/skills/baoyu-format-markdown` | 更新 |
| `skills/baoyu-image-gen` | `JimLiu/baoyu-skills/skills/baoyu-image-gen` | 更新 |
| `skills/baoyu-infographic` | `JimLiu/baoyu-skills/skills/baoyu-infographic` | 更新 |
| `skills/baoyu-markdown-to-html` | `JimLiu/baoyu-skills/skills/baoyu-markdown-to-html` | 更新 |
| `skills/baoyu-post-to-wechat` | `JimLiu/baoyu-skills/skills/baoyu-post-to-wechat` | 更新 |
| `skills/baoyu-post-to-x` | `JimLiu/baoyu-skills/skills/baoyu-post-to-x` | 更新 |
| `skills/baoyu-slide-deck` | `JimLiu/baoyu-skills/skills/baoyu-slide-deck` | 更新 |
| `skills/baoyu-url-to-markdown` | `JimLiu/baoyu-skills/skills/baoyu-url-to-markdown` | 更新 |
| `skills/baoyu-xhs-images` | `JimLiu/baoyu-skills/skills/baoyu-xhs-images` | 更新 |
| `skills/brainstorming` | `obra/superpowers/skills/brainstorming` | 更新 |
| `skills/dispatching-parallel-agents` | `obra/superpowers/skills/dispatching-parallel-agents` | 更新 |
| `skills/executing-plans` | `obra/superpowers/skills/executing-plans` | 更新 |
| `skills/finishing-a-development-branch` | `obra/superpowers/skills/finishing-a-development-branch` | 更新 |
| `skills/receiving-code-review` | `obra/superpowers/skills/receiving-code-review` | 更新 |
| `skills/requesting-code-review` | `obra/superpowers/skills/requesting-code-review` | 更新 |
| `skills/subagent-driven-development` | `obra/superpowers/skills/subagent-driven-development` | 更新 |
| `skills/systematic-debugging` | `obra/superpowers/skills/systematic-debugging` | 更新 |
| `skills/test-driven-development` | `obra/superpowers/skills/test-driven-development` | 更新 |
| `skills/using-git-worktrees` | `obra/superpowers/skills/using-git-worktrees` | 更新 |
| `skills/using-superpowers` | `obra/superpowers/skills/using-superpowers` | 更新 |
| `skills/verification-before-completion` | `obra/superpowers/skills/verification-before-completion` | 更新 |
| `skills/writing-plans` | `obra/superpowers/skills/writing-plans` | 更新 |
| `skills/writing-skills` | `obra/superpowers/skills/writing-skills` | 更新 |
| `skills/create-adaptable-composable` | `vuejs-ai/skills/skills/create-adaptable-composable` | 未变 |
| `skills/vue-best-practices` | `vuejs-ai/skills/skills/vue-best-practices` | 更新 |
| `skills/vue-debug-guides` | `vuejs-ai/skills/skills/vue-debug-guides` | 更新 |
| `skills/vue-jsx-best-practices` | `vuejs-ai/skills/skills/vue-jsx-best-practices` | 未变 |
| `skills/vue-options-api-best-practices` | `vuejs-ai/skills/skills/vue-options-api-best-practices` | 未变 |
| `skills/vue-pinia-best-practices` | `vuejs-ai/skills/skills/vue-pinia-best-practices` | 未变 |
| `skills/vue-router-best-practices` | `vuejs-ai/skills/skills/vue-router-best-practices` | 未变 |
| `skills/vue-testing-best-practices` | `vuejs-ai/skills/skills/vue-testing-best-practices` | 未变 |
| `skills/ab-test-setup` | `coreyhaines31/marketingskills/skills/ab-testing` | 更新 |
| `skills/ad-creative` | `coreyhaines31/marketingskills/skills/ad-creative` | 更新 |
| `skills/ai-seo` | `coreyhaines31/marketingskills/skills/ai-seo` | 更新 |
| `skills/analytics-tracking` | `coreyhaines31/marketingskills/skills/analytics` | 更新 |
| `skills/churn-prevention` | `coreyhaines31/marketingskills/skills/churn-prevention` | 更新 |
| `skills/cold-email` | `coreyhaines31/marketingskills/skills/cold-email` | 更新 |
| `skills/competitor-alternatives` | `coreyhaines31/marketingskills/skills/competitors` | 更新 |
| `skills/content-strategy` | `coreyhaines31/marketingskills/skills/content-strategy` | 更新 |
| `skills/copy-editing` | `coreyhaines31/marketingskills/skills/copy-editing` | 更新 |
| `skills/copywriting` | `coreyhaines31/marketingskills/skills/copywriting` | 更新 |
| `skills/email-sequence` | `coreyhaines31/marketingskills/skills/emails` | 更新 |
| `skills/form-cro` | `coreyhaines31/marketingskills/skills/cro` | 更新 |
| `skills/free-tool-strategy` | `coreyhaines31/marketingskills/skills/free-tools` | 更新 |
| `skills/launch-strategy` | `coreyhaines31/marketingskills/skills/launch` | 更新 |
| `skills/marketing-ideas` | `coreyhaines31/marketingskills/skills/marketing-ideas` | 更新 |
| `skills/marketing-psychology` | `coreyhaines31/marketingskills/skills/marketing-psychology` | 更新 |
| `skills/onboarding-cro` | `coreyhaines31/marketingskills/skills/onboarding` | 更新 |
| `skills/page-cro` | `coreyhaines31/marketingskills/skills/cro` | 更新 |
| `skills/paid-ads` | `coreyhaines31/marketingskills/skills/ads` | 更新 |
| `skills/paywall-upgrade-cro` | `coreyhaines31/marketingskills/skills/paywalls` | 更新 |
| `skills/popup-cro` | `coreyhaines31/marketingskills/skills/popups` | 更新 |
| `skills/pricing-strategy` | `coreyhaines31/marketingskills/skills/pricing` | 更新 |
| `skills/product-marketing-context` | `coreyhaines31/marketingskills/skills/product-marketing` | 更新 |
| `skills/programmatic-seo` | `coreyhaines31/marketingskills/skills/programmatic-seo` | 更新 |
| `skills/referral-program` | `coreyhaines31/marketingskills/skills/referrals` | 更新 |
| `skills/schema-markup` | `coreyhaines31/marketingskills/skills/schema` | 更新 |
| `skills/seo-audit` | `coreyhaines31/marketingskills/skills/seo-audit` | 更新 |
| `skills/signup-flow-cro` | `coreyhaines31/marketingskills/skills/signup` | 更新 |
| `skills/social-content` | `coreyhaines31/marketingskills/skills/social` | 更新 |
| `skills/seo` | `AgriciDaniel/claude-seo/skills/seo` | 更新 |
| `skills/seo-agentic` | `AgriciDaniel/claude-seo/skills/seo-agentic` | 新增依赖 |
| `skills/seo-backlinks` | `AgriciDaniel/claude-seo/skills/seo-backlinks` | 新增依赖 |
| `skills/seo-cluster` | `AgriciDaniel/claude-seo/skills/seo-cluster` | 新增依赖 |
| `skills/seo-competitor-pages` | `AgriciDaniel/claude-seo/skills/seo-competitor-pages` | 更新 |
| `skills/seo-content` | `AgriciDaniel/claude-seo/skills/seo-content` | 更新 |
| `skills/seo-content-brief` | `AgriciDaniel/claude-seo/skills/seo-content-brief` | 新增依赖 |
| `skills/seo-dataforseo` | `AgriciDaniel/claude-seo/skills/seo-dataforseo` | 新增依赖 |
| `skills/seo-drift` | `AgriciDaniel/claude-seo/skills/seo-drift` | 新增依赖 |
| `skills/seo-ecommerce` | `AgriciDaniel/claude-seo/skills/seo-ecommerce` | 新增依赖 |
| `skills/seo-flow` | `AgriciDaniel/claude-seo/skills/seo-flow` | 新增依赖 |
| `skills/seo-geo` | `AgriciDaniel/claude-seo/skills/seo-geo` | 更新 |
| `skills/seo-google` | `AgriciDaniel/claude-seo/skills/seo-google` | 新增依赖 |
| `skills/seo-hreflang` | `AgriciDaniel/claude-seo/skills/seo-hreflang` | 更新 |
| `skills/seo-image-gen` | `AgriciDaniel/claude-seo/skills/seo-image-gen` | 新增依赖 |
| `skills/seo-images` | `AgriciDaniel/claude-seo/skills/seo-images` | 更新 |
| `skills/seo-local` | `AgriciDaniel/claude-seo/skills/seo-local` | 新增依赖 |
| `skills/seo-maps` | `AgriciDaniel/claude-seo/skills/seo-maps` | 新增依赖 |
| `skills/seo-page` | `AgriciDaniel/claude-seo/skills/seo-page` | 更新 |
| `skills/seo-plan` | `AgriciDaniel/claude-seo/skills/seo-plan` | 更新 |
| `skills/seo-programmatic` | `AgriciDaniel/claude-seo/skills/seo-programmatic` | 更新 |
| `skills/seo-schema` | `AgriciDaniel/claude-seo/skills/seo-schema` | 更新 |
| `skills/seo-sitemap` | `AgriciDaniel/claude-seo/skills/seo-sitemap` | 更新 |
| `skills/seo-sxo` | `AgriciDaniel/claude-seo/skills/seo-sxo` | 新增依赖 |
| `skills/seo-technical` | `AgriciDaniel/claude-seo/skills/seo-technical` | 更新 |
| `skills/notebooklm` | `PleasePrompto/notebooklm-skill/.` | 未变 |
| `skills/zlibrary-to-notebooklm` | `zstmfhy/zlibrary-to-notebooklm/.` | 未变 |
| `skills/competitor-profiling` | `coreyhaines31/marketingskills/skills/competitor-profiling` | 新增依赖 |
| `skills/customer-research` | `coreyhaines31/marketingskills/skills/customer-research` | 新增依赖 |

## 验证

- 122 个顶层 Skill 的 YAML frontmatter 可解析，名称与目录匹配且 description 存在。
- 1579 个同步文件的 SHA-256 校验通过；150 个 Python 文件语法解析通过；42 个 JSON 文件解析通过。
- 检查真实 Markdown 依赖链接，补齐缺失 Marketing 依赖，修正 FLOW 资源路径与文章插图样式资料路径。示例中的占位链接不作为文件依赖。
- 未执行浏览器自动化、第三方 API 或部署功能；以上为内容与静态完整性验证。新版 SEO 的依赖环境需在实际使用时按其 setup 流程建立。

## 恢复副本

同步前的技能和已覆盖配套资源保存在本地忽略目录：

`D:/projects/sean-s-skills/.tmp-integration/update-2026-10-09/before-update.zip`

压缩包含同步前的本地内容，用于检查或恢复个性化修改；不进入 Git。上游克隆也保留在该目录，便于对照。

## 文档、安装脚本与提交准备

- 能力文档与规则同步为 122 个顶层 Skill、20 个 Agent。
- Windows/Unix 集成脚本动态统计 Skill 和 Agent；Windows PowerShell 5.1 使用 URI 计算相对路径，支持空格、单引号与跨盘符路径。
- 用户级安装先备份后替换对应目录，避免旧文件残留；保留其他本地 Skill，支持 `-WhatIf`。
- 补齐 README 所引用的 Claude 插件清单；集成脚本只生成 Cursor 规则。
- 增加可重复运行的静态校验脚本，临时克隆、备份与 Python 缓存不纳入提交。

验证补充：Windows PowerShell 5.1 安装回归检查通过；Git Bash 集成、Bash 语法及生成路径回指仓库的检查通过。测试覆盖 122 个 Skill 完整安装、重复更新、备份、旧文件清理、保留其他本地 Skill、预览无副作用、拒绝自复制、中文与引号路径、批处理和旧参数兼容。校验脚本确认 20 个 Agent。

提交前额外核验：暂存区的 1579 个上游快照文件全部匹配记录哈希；相关文档链接无缺失，文档和维护脚本的 Git whitespace 检查通过。
