# Tools 说明 — 工具注册与集成文档

本库 **tools/** 目录提供**营销/分析/SEO 等第三方工具的能力索引与集成说明**，供 AI 或开发者发现可用工具、了解集成方式（API/MCP/CLI/SDK）并查阅具体操作步骤。内容来自 [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) 的 `tools/`。

---

## 目录结构

```
tools/
├── README.md           # 来源与使用说明
├── REGISTRY.md         # 工具总表与按分类索引
├── integrations/       # 各工具的详细集成文档（约 50+ 个 .md）
│   ├── ga4.md
│   ├── ahrefs.md
│   ├── stripe.md
│   └── ...
└── clis/               #（可选）CLI 脚本，本库未拷贝
```

---

## REGISTRY.md 功能与用法

- **功能**：  
  - 工具总表：工具名、分类、是否支持 API/MCP/CLI/SDK、对应集成文档链接。  
  - 按分类的说明与推荐：Analytics、SEO、CRM、Payments、Email、Ads、CRO、Scheduling 等。  
- **使用场景**：  
  - 需要选型时（如「用哪个做分析/邮件/广告」）按分类浏览。  
  - 需要知道某工具是否支持 API/CLI 时查表。  
  - 确定工具后，到 `integrations/<tool>.md` 查看具体集成步骤与常用操作。

---

## 工具分类与典型工具

| 分类 | 典型工具 | 使用场景简述 |
|------|----------|-----------------------------|
| **Analytics** | ga4, mixpanel, amplitude, posthog, segment, plausible | 行为追踪、转化、漏斗、留存；选型见 REGISTRY 推荐。 |
| **SEO** | google-search-console, semrush, ahrefs, dataforseo, keywords-everywhere | 搜索数据、关键词、排名、反向链接、SERP；站内审计见 skills/seo-*。 |
| **CRM** | hubspot, salesforce | 客户与销售流程管理；SMB 多用 HubSpot，企业多用 Salesforce。 |
| **Payments** | stripe, paddle | 订阅与支付；Stripe 通用，Paddle 偏税务合规。 |
| **Referral & Affiliate** | rewardful, tolt, mention-me, partnerstack, dub-co | 推荐/联盟计划、链接追踪与分成。 |
| **Email** | mailchimp, customer-io, sendgrid, resend, klaviyo, beehiiv, activecampaign | 邮件营销、触达、交易邮件、新闻稿；见 REGISTRY 的 Agent recommendation。 |
| **Advertising** | google-ads, meta-ads, linkedin-ads, tiktok-ads | 付费广告投放与受众定向；与 skills/paid-ads 等配合。 |
| **Automation** | zapier | 无代码串联多工具。 |
| **CRO & A/B Testing** | hotjar, optimizely | 热力图、录屏、A/B 测试与实验。 |
| **Scheduling** | calendly, savvycal | 预约与会议预订。 |
| **Forms & Surveys** | typeform | 表单与问卷。 |
| **Messaging** | intercom | 站内消息、客服与产品导览。 |
| **Social** | buffer | 社媒发布与排期。 |
| **Video** | wistia | 营销视频托管与分析。 |
| **Data Enrichment** | clearbit, apollo | 公司与联系人信息补充、获客与外联。 |
| **Reviews** | trustpilot, g2 | 评价与口碑管理。 |
| **Commerce / CMS** | shopify, wordpress, webflow | 电商与内容站；与建站、落地页优化等配合。 |

---

## integrations/*.md 功能与用法

- **功能**：每个文件对应一个工具的详细集成说明，通常包括：  
  - 能力概述、典型用途  
  - API/CLI/MCP 的配置与认证  
  - 常见操作（如创建活动、拉取报表、同步数据）与示例  
- **使用场景**：  
  - 已选定工具（如 GA4、Ahrefs、Stripe），需要「如何接、怎么调」时直接打开 `tools/integrations/<tool>.md`。  
  - 与营销类 Skill（如 analytics-tracking、paid-ads、email-sequence）配合时，由 Skill 引用或由 Agent 按需读取对应集成文档。

---

## 与本库 Skill 的关系

- **tools/** 侧重「第三方工具有哪些、怎么集成」；**skills/** 侧重「在某个任务里如何用这些能力」。  
- 例如：SEO 数据用 `tools/integrations/google-search-console.md`、`ahrefs.md` 等；站内 SEO 审计与优化用 `skills/seo`、`skills/seo-audit` 等。  
- 营销流程设计用 `skills/email-sequence`、`skills/paid-ads` 等；具体对接 Mailchimp、Google Ads 时查 `tools/REGISTRY.md` 与 `tools/integrations/`。
