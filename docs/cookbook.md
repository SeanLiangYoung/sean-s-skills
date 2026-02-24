# Cookbook — 快速集成与用法

本文档提供**将 Sean's Skills 能力集成到任意项目**的几种方式，以及常见场景的「配方」示例。

---

## 快速集成：一键脚本

在任意目标项目中，通过脚本自动写入 Claude 与 Cursor 配置并引用本库：

```bash
# 从本库根目录执行
./scripts/integrate-into-project.sh /path/to/your-project

# 或指定本库路径（当不在本库中执行时）
./scripts/integrate-into-project.sh /path/to/your-project /path/to/sean-s-skills
```

**脚本会：**

1. 在目标项目下创建 `.claude/settings.json`，将本库作为插件路径（`source`）加入。
2. 在目标项目下创建 `.cursor/rules/use-sean-s-skills.mdc`，规则中写明本库相对路径与能力索引文档位置，供 Cursor 优先查阅并引用 skills/agents。

**注意**：若 Claude Code 在 project 作用域下不支持通过 `settings.json` 的 `plugins` 路径加载，请在目标项目中改用「方式一」以插件目录启动。

---

## 方式一：Claude Code — 以插件目录运行

在**任意项目**中启动 Claude Code 时，将本库作为插件目录传入，当前会话即可使用本库所有 skills 与 agents：

```bash
# 在目标项目目录下
claude --plugin-dir /path/to/sean-s-skills
```

或先进入本库再打开目标项目（视 Claude Code 实际用法而定）。  
这样无需修改目标项目文件，适合临时或本机一次性使用。

---

## 方式二：Claude Code — 项目级配置（推荐用于长期使用）

1. **克隆或引用本库**  
   将 `sean-s-skills` 放在固定路径（如 `~/repos/sean-s-skills`），或作为目标项目的 git submodule。

2. **在目标项目中添加 .claude 配置**  
   在目标项目根目录创建 `.claude/settings.json`（若已有则合并），例如：

   ```json
   {
     "plugins": [
       {
         "source": "../sean-s-skills",
         "strict": false
       }
     ]
   }
   ```
   `source` 可为相对路径（相对目标项目根）或绝对路径。

3. **用 Cursor 时**  
   在目标项目 `.cursor/rules/` 下增加一条规则，说明本库路径与能力索引（可复制 `scripts/integrate-into-project.sh` 生成的 `use-sean-s-skills.mdc` 内容，或见下方「方式四」）。

---

## 方式三：只复制部分能力到目标项目

若不想依赖本库路径，只希望把部分 Skill/Agent 拷贝到目标项目：

1. **复制 Skill**  
   从本库 `skills/<name>/` 整目录拷贝到目标项目的 `.claude/skills/<name>/` 或目标项目内任意约定目录（若 Claude/Cursor 支持自定义技能路径）。

2. **复制 Agent**  
   从本库 `agents/*.md` 拷贝到目标项目的 `.claude/agents/` 或约定目录。

3. **复制工具索引（可选）**  
   将本库 `tools/REGISTRY.md` 与 `tools/integrations/` 下需要的 .md 拷贝到目标项目，便于 AI 查阅第三方工具集成方式。

本库 `skill-list.md` 与 `docs/skills-reference.md` 可作挑选清单。

---

## 方式四：Cursor — 仅添加规则引用本库

不装 Claude 插件、只在 Cursor 中使用本库能力时：

1. 在目标项目创建 `.cursor/rules/use-sean-s-skills.mdc`（或同名 .mdc）。
2. 内容示例（将 `REL_PATH` 换成目标项目到本库的相对路径，如 `../sean-s-skills`）：

```markdown
---
description: 使用 Sean's Skills 库；能力与场景见该库 docs
globs: 
alwaysApply: true
---

# 使用 Sean's Skills 库

- 能力索引：<本库路径>/docs/capabilities-index.md
- Skill 列表与使用场景：<本库路径>/docs/skills-reference.md
- Agent 列表：<本库路径>/docs/agents-reference.md
- 工具注册表：<本库路径>/tools/REGISTRY.md

需要文档/SEO/营销/图文/开发流程等能力时，优先查阅上述文档并引用 <本库路径>/skills/<name>/SKILL.md 或 <本库路径>/agents/*.md。
```

这样 Cursor 会根据规则在对话中引用本库文档与 SKILL/Agent 内容。

---

## 配方示例

### 配方 1：在新项目中启用「SEO + 文档」能力

- **Claude**：`claude --plugin-dir /path/to/sean-s-skills`，或按方式二在项目 `.claude/settings.json` 中加入本库插件。
- **使用**：在对话中提及「SEO audit」「sitemap」「PDF」「Word」等，Claude 会调用本库 `seo`、`seo-audit`、`pdf`、`docx` 等 Skill。

### 配方 2：在内容项目中启用「宝雨」图文与发布

- 按方式二或方式四在目标项目中配置本库。
- 使用：提及「小红书图片」「公众号发布」「Markdown 转 HTML」「配图」等，调用 `baoyu-xhs-images`、`baoyu-post-to-wechat`、`baoyu-markdown-to-html`、`baoyu-article-illustrator` 等。

### 配方 3：在开发项目中启用「计划 + 评审 + TDD」

- 按方式二或方式四配置本库。
- 使用：先 `writing-plans` 产出实施计划，开发中用 `test-driven-development`，完成后用 `requesting-code-review` 或加载 `agents/code-reviewer.md` 做评审。

### 配方 4：仅用「工具注册表」查第三方集成

- 将本库 `tools/REGISTRY.md` 与 `tools/integrations/<tool>.md` 复制到目标项目某目录，或在 Cursor 规则中写明路径。
- 在对话中需要对接 GA4、Ahrefs、Stripe 等时，让 AI 查阅该目录下的 REGISTRY 与对应 integrations 文档。

### 配方 5：本库自身开发与迭代

- 本库已包含 `.claude-plugin/plugin.json`、`.claude/`、`.cursor/rules/`，在 Claude Code 或 Cursor 中直接打开本库即可使用全部能力。
- 新增或修改 Skill 时参考 `spec/specification.md` 与 `templates/SKILL-template.md`，并更新 `docs/skills-reference.md` 与 `skill-list.md`。

---

## 文件与目录速查

| 目的           | 路径或文件 |
|----------------|------------|
| Claude 插件清单 | `.claude-plugin/plugin.json` |
| 本库 Claude 说明 | `CLAUDE.md` |
| 项目级 Claude 示例 | `.claude/settings.json.example` |
| Cursor 规则     | `.cursor/rules/sean-s-skills.mdc` |
| 集成脚本        | `scripts/integrate-into-project.sh` |
| 能力索引        | `docs/capabilities-index.md` |
| Skill 列表与场景 | `docs/skills-reference.md` |
| Agent 说明      | `docs/agents-reference.md` |
| 工具注册与集成  | `tools/REGISTRY.md`、`tools/integrations/*.md` |
