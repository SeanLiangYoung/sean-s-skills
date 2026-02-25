# Changelog

本文件记录 Sean's Skills 库的 notable 变更。

---

## [未版本号] — 2025-02-25 — 合并 user-skills 与 skills

### 变更

- **合并**：将 `user-skills/`（28 个）与 `skills/`（79 个）合并为单一 `skills/` 目录，共 **91 个** Skill。
- **去重策略**：重名 16 个以本库 `skills/` 为主，用 `user-skills` 内容覆盖/补全；仅 `user-skills` 有的 12 个（create-adaptable-composable、element-plus-vue3、import-anthropic-skills、skill-usage-guide、vue-best-practices、vue-debug-guides、vue-development-guides、vue-jsx-best-practices、vue-options-api-best-practices、vue-pinia-best-practices、vue-router-best-practices、vue-testing-best-practices）整体复制进 `skills/`。
- **删除**：合并完成后已删除 `user-skills/` 目录。

### 文档更新

- **docs/cursor-setup.md**：配置表与 Skills 章节改为单一 `skills/`（91 个）；规则路径改为项目根 `rules/`；移除对 .cursor/user-skills、.cursor/README、cursor-config 的引用；MCP 列表移除 Framelink。
- **docs/capabilities-index.md**：Skill 数量 79 → 91；文档列表中 cursor-setup、skills-reference 补充数量或说明。
- **docs/skills-reference.md**：79 → 91；新增「二、设计、前端」中 element-plus-vue3、create-adaptable-composable、skill-usage-guide、import-anthropic-skills；「六、开发流程」中补充 vue-* 系列与 Vue 相关 Skill。
- **skill-list.md**：79 → 91；新增「Cursor 用户级 Skills（已合并进 skills/）」清单。
- **readme.md**：项目目的与目录结构更新为 91 个 Skill、rules/、cursor-setup；使用方式与快速集成补充 rules/ 与 [docs/cursor-setup.md](docs/cursor-setup.md)。
- **docs/cookbook.md**：文件与目录速查表增加 Cursor 用户级规则路径、Skill 数量 91；配方 5 更新为 91 个 Skill 与 cursor-setup 引用。
- **docs/integration-progress.md**：开头注明 skills/ 共 91 个（含 user-skills 合并）。

---

## [未版本号] — 2025-02-25 — 用户级 Cursor 配置纳入项目

### 新增

- **.cursor/rules/skill-usage.mdc**、**.cursor/rules/confirmation-before-action.mdc**：原 Cursor 用户级规则（充分利用 Skills、执行前二次确认）同步到项目，可版本化与新项目复用。
- **.cursor/user-skills/**：28 个用户级 Agent Skills 的副本（原 `%USERPROFILE%\.cursor\skills\`），便于换机或新项目复现。
- **.cursor/mcp-servers-reference.md**：推荐启用的 MCP 列表（cursor-ide-browser、Figma）及在新环境中恢复的说明。
- **cursor-config/**：`.cursor/` 内 rules、user-skills、MCP 配置在项目根目录的同步副本，便于在 .cursor 外直接查阅或复制到其他项目；见 [cursor-config/README.md](cursor-config/README.md)。

### 更新

- **docs/cursor-setup.md**：已在本项目中的配置表增加「用户级规则」「用户级 Skills」「MCP 推荐清单」；新项目复用方式补充复制规则与 user-skills 的步骤；Rules/Skills 章节区分项目规则与用户级规则、本库 Skills 与 user-skills。
- **.cursor/README.md**：说明用户级规则与 user-skills 已同步，并指向 mcp-servers-reference.md。

### 说明

- 用户级规则、用户级 Skills、MCP 推荐清单均已纳入本库，具备高复用价值；MCP 实际启用仍由 Cursor 在设置中管理。

---

## [未版本号] — 2025-02-25 — Cursor 配置同步

### 新增

- **docs/cursor-setup.md**：Cursor 在本项目中的配置说明，包含 Rules、Skills、Subagents（Agents）、MCP 列表与引用。

### 更新

- **.cursor/README.md**：补充 Rules / Skills / Agents / MCP 说明，并指向 `docs/cursor-setup.md` 与能力索引。
- **docs/capabilities-index.md**：文档列表增加 [cursor-setup.md](docs/cursor-setup.md)。
- **docs/cookbook.md**：文件与目录速查表增加「Cursor 配置说明（Rules/Skills/Agents/MCP）」入口。

### 说明

- Rules、Skills、Agents 以本库为唯一来源；MCP 配置由 Cursor 在项目缓存中管理，本库仅做文档记录便于复现与协作。
