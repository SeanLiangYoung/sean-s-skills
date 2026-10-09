# Agents 说明 — 子代理 / 角色定义

当前有 **20 个 Agent**：19 个 SEO 角色及 1 个代码评审角色。角色提示保存在 `agents/*.md`，不把 README 计入数量。

| Agent | 功能与使用场景 |
|---|---|
| [code-reviewer](../agents/code-reviewer.md) | 对照需求与计划评审代码，给出问题分级与验证建议 |
| [seo-agentic](../agents/seo-agentic.md) | 检查面向 AI 代理的可访问性、接口与内容发现 |
| [seo-backlinks](../agents/seo-backlinks.md) | 分析外链质量、风险和机会 |
| [seo-cluster](../agents/seo-cluster.md) | 规划主题集群、内部链接与内容结构 |
| [seo-content](../agents/seo-content.md) | 评估内容质量、E-E-A-T 与 AI 引用就绪度 |
| [seo-dataforseo](../agents/seo-dataforseo.md) | 通过 DataForSEO 获取搜索、关键词与竞争数据 |
| [seo-drift](../agents/seo-drift.md) | 比较审计基线与当前状态，识别指标漂移 |
| [seo-ecommerce](../agents/seo-ecommerce.md) | 审计电商商品、分类页与结构化数据 |
| [seo-flow](../agents/seo-flow.md) | 按 FLOW 方法组织搜索发现与转化分析 |
| [seo-geo](../agents/seo-geo.md) | 评估 AI 搜索、生成式引擎引用与可见性 |
| [seo-google](../agents/seo-google.md) | 结合 GSC、GA4、CrUX 数据分析索引、流量与性能 |
| [seo-image-gen](../agents/seo-image-gen.md) | 按 SEO 页面与内容需求规划图片生成 |
| [seo-local](../agents/seo-local.md) | 分析本地商家、门店与地域搜索信号 |
| [seo-maps](../agents/seo-maps.md) | 分析地图排名、GBP 与地域网格 |
| [seo-performance](../agents/seo-performance.md) | 分析 Core Web Vitals、加载性能与瓶颈 |
| [seo-schema](../agents/seo-schema.md) | 检测、校验与生成结构化数据 |
| [seo-sitemap](../agents/seo-sitemap.md) | 校验与规划 XML sitemap |
| [seo-sxo](../agents/seo-sxo.md) | 分析搜索体验与转化衔接 |
| [seo-technical](../agents/seo-technical.md) | 检查抓取、索引、URL、移动端与 JS 渲染 |
| [seo-visual](../agents/seo-visual.md) | 分析截图、移动端渲染与首屏布局 |

SEO 角色来自 AgriciDaniel/claude-seo；代码评审来自 obra/superpowers。具体工具、输入和输出要求以各角色文件为准。

`skills/seo` 按任务选择 SEO 角色。使用需要脚本的能力时，先按其 setup 流程配置运行环境；本库中的启动器为 `skills/seo/scripts/claude-seo`。`seo-audit` 保留 Marketing 来源，同名含义差异见 [更新报告](upstream-skills-update-2026-10-09.md)。

可将对应文件加载为系统提示或子代理指令；实际工具与模型支持由当前客户端决定。
