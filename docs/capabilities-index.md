# 能力说明文档索引

本目录下的文档详细说明项目中 **Agent**、**Tool**、**Skill**、**Template**、**Spec** 的具体功能与使用场景。

---

## 文档列表

| 文档 | 内容 |
|------|------|
| [cookbook.md](./cookbook.md) | **快速将本库能力集成到任意项目**：一键脚本、Claude/Cursor 配置、配方示例 |
| [cursor-setup.md](./cursor-setup.md) | **Cursor 在本项目中的配置**：Rules（含项目根 rules/）、Skills（122 个）、Subagents（Agents）、MCP 列表与说明 |
| [agents-reference.md](./agents-reference.md) | 各 Agent（子代理/角色）的功能、触发场景与用法 |
| [tools-reference.md](./tools-reference.md) | 工具注册表、分类、集成文档及使用场景 |
| [skills-reference.md](./skills-reference.md) | 各 Skill（122 个）的功能与使用场景（按分类） |
| [templates-reference.md](./templates-reference.md) | Skill 模板的用途与使用方式 |
| [spec-reference.md](./spec-reference.md) | Agent Skills 规范的作用与适用场景 |
| [upstream-skills-update-2026-10-09.md](./upstream-skills-update-2026-10-09.md) | 上游版本核验、兼容策略及验证结果 |
| [integration-progress.md](./integration-progress.md) | 开源集成进度与来源记录（非能力说明） |

---

## 能力类型速览

| 类型 | 路径 | 数量 | 用途简述 |
|------|------|------|----------|
| **Agent** | `agents/*.md` | 20 | 子代理/角色定义，供主流程或编排 Skill 调用 |
| **Tool** | `tools/` | REGISTRY + 50+ 集成文档 | 营销/分析等第三方工具的能力索引与集成说明 |
| **Skill** | `skills/<name>/` | 122 | 按规范封装的完整能力（SKILL.md + 可选 scripts/references）；已合并原 user-skills 与本库 skills。 |
| **Template** | `templates/` | 1 | 创建新 Skill 时的最小模板 |
| **Spec** | `spec/` | 1 | Agent Skills 格式规范，约束 Skill 的目录与 frontmatter |

---

## 集成到其他项目

要将本库的 skills/agents/tools 用到任意项目，请直接看 **[cookbook.md](./cookbook.md)**：含一键脚本 `scripts/integrate-into-project.sh`、Claude 以插件目录运行、项目级 .claude/.cursor 配置、只复制部分能力、以及 SEO/宝雨/开发流程等配方示例。

---

## 使用建议

- **先看场景**：根据任务类型（文档处理、SEO、营销、开发流程、图文/发布等）在 [skills-reference.md](./skills-reference.md) 中找对应 Skill。
- **编排与子代理**：需要 SEO 全站分析时用 `skills/seo`，其会调用 `agents/` 下 SEO 子代理；需要代码评审时可直接加载 `agents/code-reviewer.md`。
- **对接第三方**：营销/分析/广告等需用 GA4、Ahrefs、Stripe 等时，查 [tools-reference.md](./tools-reference.md) 与 `tools/integrations/<tool>.md`。
- **新建 Skill**：按 [spec-reference.md](./spec-reference.md) 与 [templates-reference.md](./templates-reference.md) 使用 `templates/SKILL-template.md` 创建。


新增场景：资料分析与知识库写入使用 [llm-wiki-ingest](../skills/llm-wiki-ingest/SKILL.md)；已授权代码安全审计与报告生成使用 [code-security-audit](../skills/code-security-audit/SKILL.md)。
