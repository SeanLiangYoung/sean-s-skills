# Cursor 在本项目中的配置说明

本文档记录 **Sean's Skills** 仓库在 Cursor 中的 Rules、Skills、Subagents（Agents）、MCP 配置，便于复现与协作。配置以本库为能力来源；MCP 由 Cursor 在项目缓存中管理，此处仅做文档记录。

---

## 配置同步状态与「新项目快速获取」

### 已在本项目中的配置（仓库内、可版本化）

| 类型 | 位置 | 说明 |
|------|------|------|
| **项目规则** | `.cursor/rules/sean-s-skills.mdc` | 本库专用规则：优先使用 skills/agents/tools，索引见 docs。 |
| **用户级规则（已同步）** | `rules/skill-usage.mdc`、`rules/confirmation-before-action.mdc`（项目根目录） | 原 Cursor 用户级规则，已纳入本库：充分利用 Skills、执行前二次确认。 |
| **Skills** | `skills/`（**107 个**） | 原 79 个本库 Skill 与 28 个用户级 Skill 已合并为一；重复项以本库为主并补入 user-skills 内容，仅 user-skills 有的 12 个已并入；当前共 107 个目录。 |
| **Subagents** | `agents/`（7 个） | 子代理定义均在仓库内。 |
| **MCP 推荐清单** | 见下方「4. MCP 配置」 | 推荐启用的 MCP 列表与恢复说明（MCP 实际由 Cursor 管理）。 |

以上内容已同步到当前项目；clone 本库即可获得。在新项目或新机器上复用方式见下方「新项目如何快速用上」。

### 未纳入本仓库的配置（仅由 Cursor 运行时管理）

| 类型 | 说明 |
|------|------|
| **MCP 运行时** | MCP 的启用与连接由 Cursor 在项目缓存中管理；本库在 [cursor-setup.md](./cursor-setup.md) 中记录推荐 MCP 列表便于复现。 |

### 新项目如何快速用上「本库」配置

1. **让新项目使用本库的 107 个 Skill + 7 个 Agent**
   在新项目根目录执行（或将本库 clone 到合适路径后执行）：
   ```bash
   # 从本库根目录执行
   ./scripts/integrate-into-project.sh /path/to/新项目
   ```
   脚本会：
   - 在新项目中创建 `.cursor/rules/use-sean-s-skills.mdc`（引用本库路径与能力索引）
   - 创建 `.claude/settings.json`（将本库作为插件 source）
2. **用户级规则（已纳入本库）**  
   - 规则文件位于项目根目录 `rules/`（skill-usage.mdc、confirmation-before-action.mdc）。  
   - **在新项目中复用**：将 `rules/` 下文件复制到新项目的 `.cursor/rules/` 或新项目的 `rules/`。  
   - **换机器 / 新账号**：clone 本库后，将 `rules/` 复制到 `%USERPROFILE%\.cursor\rules\` 即可恢复。
3. **MCP**  
   - 在 Cursor 设置中启用推荐 MCP（见下方「4. MCP 配置」）。

---

## 1. Rules（规则）

| 项目 | 说明 |
|------|------|
| **路径** | 项目根目录 `rules/` 或 `.cursor/rules/` |
| **文件** | **项目规则**：`.cursor/rules/sean-s-skills.mdc`（本库专用）。**用户级规则**：`rules/skill-usage.mdc`、`rules/confirmation-before-action.mdc`（充分利用 Skills、执行前二次确认）。 |
| **作用** | 项目规则说明本库能力与索引；用户级规则为通用工作习惯，已纳入本库便于复现与新项目复用。 |

将本库能力用到**其他项目**时，可在目标项目中添加规则引用本库路径，并可复制上述用户级规则，详见 [cookbook.md](./cookbook.md)。

---

## 2. Skills（技能）

| 项目 | 说明 |
|------|------|
| **路径** | `skills/<name>/` |
| **数量** | **107 个**（原 79 个本库 Skill 与 28 个用户级 Skill 已合并；重复 16 个以本库为主并补入 user-skills 内容，仅 user-skills 有的 12 个已并入；当前共 107 个目录）。 |
| **索引** | [docs/skills-reference.md](./skills-reference.md)（按分类列出功能与使用场景） |
| **清单** | 根目录 [skill-list.md](../skill-list.md)（按来源分类） |

每个 Skill 至少包含 `SKILL.md`，可含 `scripts/`、`references/`、`assets/`。在 Cursor 中通过规则引用上述文档后，AI 会按任务加载对应 `skills/<name>/SKILL.md`。

---

## 3. Subagents / Agents（子代理）

| 项目 | 说明 |
|------|------|
| **路径** | `agents/*.md` |
| **数量** | 7 个 |
| **索引** | [docs/agents-reference.md](./agents-reference.md) |

| Agent | 用途简述 |
|-------|----------|
| **code-reviewer** | 代码评审：对照计划与规范做实现与质量评审 |
| **seo-content** | 内容质量与 E-E-A-T、可读性、AI 引用就绪度评估 |
| **seo-performance** | Core Web Vitals 与页面性能分析 |
| **seo-technical** | 技术 SEO：可抓取、可索引、移动端、CWV、JS 渲染 |
| **seo-sitemap** | Sitemap 校验与生成、质量门控 |
| **seo-schema** | Schema.org 检测、校验与 JSON-LD 生成 |
| **seo-visual** | 截屏、移动端渲染、首屏内容分析 |

编排型 Skill `skills/seo` 会调度上述 6 个 SEO 子代理；`code-reviewer` 可由人工或流程在开发完成后加载。

---

## 4. MCP 配置

本项目中启用的 MCP（Model Context Protocol）由 Cursor 在**项目缓存**中管理（通常位于 `%USERPROFILE%\.cursor\projects\<project-id>\mcps\`），本仓库不包含 MCP 配置文件，此处仅记录当前使用的 MCP 以便复现。

| MCP 名称 | 用途简述 |
|----------|----------|
| **cursor-ide-browser** | 浏览器自动化：导航、截屏、与页面交互、性能分析等；用于前端/Web 应用开发与测试。 |
| **user-Figma** | 官方 Figma MCP：读取设计、截图、元数据、Code Connect、FigJam 图表；设计稿转代码或设计协作时使用。 |

若在新环境或新机器上打开本库，需在 Cursor 设置中为该项目启用上述 MCP（Settings → MCP / Integrations）。

---

## 相关文档

| 目的 | 文档 |
|------|------|
| 能力总览与文档索引 | [capabilities-index.md](./capabilities-index.md) |
| 快速集成到其他项目 | [cookbook.md](./cookbook.md) |
| MCP 推荐清单与恢复 | 见上文「4. MCP 配置」 |
