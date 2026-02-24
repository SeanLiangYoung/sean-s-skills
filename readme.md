# Sean's Skills — 私人 Skill 库

个人维护的 **Agent Skill 仓库**，用于集中管理自用技能，并集成来自开源项目的 Skill，便于在 Cursor / Codex 等环境中统一引用与迭代。

## 项目目的

- **私人技能库**：存放与复用自己编写或定制的 Skill（如文档处理、前端设计、主题与画布等）。
- **集成开源 Skill**：将 [skill-list.md](./skill-list.md) 中列出的开源项目提供的 Skill 纳入本库，统一格式、目录与依赖，便于安装与更新。**已完成首轮拷贝与合并**（2025-02-25），当前共 79 个 Skill；另已集成 **agents/**、**tools/**、**templates/** 等除 skills 外的 AI 能力，详见 [docs/integration-progress.md](./docs/integration-progress.md)。

## 目录结构

```
sean-s-skills/
├── readme.md              # 本说明
├── CLAUDE.md              # Claude 项目说明（本库即插件）
├── skill-list.md          # 能力列表（skills/ + agents、tools、templates）
├── .claude-plugin/        # Claude Code 插件清单（skills + agents 路径）
│   └── plugin.json
├── .claude/               # 本库 Claude 配置说明与示例
│   ├── README.md
│   └── settings.json.example
├── .cursor/               # Cursor 规则（优先使用本库能力）
│   ├── README.md
│   └── rules/
│       └── sean-s-skills.mdc
├── scripts/
│   └── integrate-into-project.sh   # 一键将本库能力集成到任意项目
├── agents/                # 子代理/角色定义（7 个 .md，来自 Claude SEO、Superpowers）
├── tools/                 # 工具注册与集成说明（REGISTRY + 50+ 集成文档，来自 Marketing）
├── templates/             # Skill 创建模板（来自 Anthropics）
├── docs/
│   ├── capabilities-index.md    # 能力说明文档索引（Agent/Tool/Skill/Template/Spec）
│   ├── cookbook.md              # 快速集成方法与配方（推荐）
│   ├── agents-reference.md      # 各 Agent 功能与使用场景
│   ├── tools-reference.md       # 工具注册与集成说明
│   ├── skills-reference.md      # 各 Skill 功能与使用场景
│   ├── templates-reference.md   # 模板说明
│   ├── spec-reference.md        # 规范说明
│   └── integration-progress.md  # 开源集成进度与「除 skills 外」能力记录
├── spec/                  # Agent Skill 格式规范（参考 agentskills 等）
│   └── specification.md
└── skills/                # 所有 Skill 的根目录（当前 79 个）
    ├── pdf/           # PDF 处理
    ├── docx/          # Word 文档
    ├── notebooklm/    # NotebookLM 查询（已集成）
    ├── seo/           # SEO 编排型 Skill（Claude SEO）
    ├── seo-*/         # Claude SEO、Marketing 等
    ├── baoyu-*/       # 宝雨系列
    ├── ...            # 详见 skill-list.md
```

- **skills/**：每个子目录对应一个 Skill，至少包含 `SKILL.md`，可含 `scripts/`、`references/`、`assets/` 等。
- **agents/**：可复用的子代理/角色定义（Markdown + YAML frontmatter），供主流程或子代理加载；来源见 [agents/README.md](./agents/README.md)。
- **tools/**：营销/分析等第三方工具的注册表与集成说明，供 AI 发现与调用；来源见 [tools/README.md](./tools/README.md)。
- **templates/**：创建新 Skill 时使用的模板，符合 [spec/specification.md](./spec/specification.md)；来源见 [templates/README.md](./templates/README.md)。
- **spec/**：Skill 的命名、frontmatter、目录约定等，见 [spec/specification.md](./spec/specification.md)。
- **skill-list.md**：能力列表（skills/ 路径 + agents、tools、templates）；原 GitHub 来源与「除 skills 外」集成说明见 [docs/integration-progress.md](./docs/integration-progress.md)。
- **docs/integration-progress.md**：各开源仓库的处理进度、能力清单、本地路径，以及**除 skills 外的 AI 能力集成**记录。  
- **能力说明文档**：各 Agent/Tool/Skill/Template/Spec 的详细功能与使用场景见 [docs/capabilities-index.md](./docs/capabilities-index.md)，可跳转至 agents-reference、tools-reference、skills-reference、templates-reference、spec-reference。

## 开源 Skill 来源与进度

- **能力列表（本库路径）**：[skill-list.md](./skill-list.md) — 每行为本库 `skills/` 下能力路径或来源说明。  
- **处理进度与能力记录**：[docs/integration-progress.md](./docs/integration-progress.md) — 各开源仓库的集成状态（已集成/已盘点）、能力清单、本地路径及 2025-02-25 拷贝合并记录。

## 规范与格式

- Skill 目录名 = `name`（小写、连字符）。
- 每个 Skill 必须有 `SKILL.md`，含 YAML frontmatter（`name`、`description` 等）和 Markdown 正文。
- 详细格式见 [spec/specification.md](./spec/specification.md)。

## 使用方式

### 在本库中直接使用

- **Claude Code**：本库根目录含 `.claude-plugin/plugin.json`，可作为插件加载；打开本库或使用 `claude --plugin-dir /path/to/sean-s-skills` 即可使用全部 skills 与 agents。
- **Cursor**：`.cursor/rules/` 下已配置 `sean-s-skills.mdc`，在本库中工作时 AI 会优先查阅 [docs/capabilities-index.md](./docs/capabilities-index.md) 与 skills/agents 路径。

### 快速集成到任意项目

- **一键脚本**：在目标项目根目录外执行  
  `./scripts/integrate-into-project.sh /path/to/your-project`  
  会在目标项目中生成 `.claude/settings.json` 与 `.cursor/rules/use-sean-s-skills.mdc`，引用本库路径。
- **详细步骤与配方**（以插件目录运行、只复制部分能力、仅 Cursor 规则等）：见 **[docs/cookbook.md](./docs/cookbook.md)**。

### 其它

- 将本仓库克隆到本地后，也可在 Cursor / Codex 的 Skill 配置中把 `skills/` 或具体子路径加入搜索/加载路径。
- 首轮开源集成已完成，能力列表见 [skill-list.md](./skill-list.md)。后续若需从新仓库集成：参考 [docs/integration-progress.md](./docs/integration-progress.md) 的流程，拷贝到 `skills/` 并更新该文档。

---

*私人 Skill 库，仅供个人与授权环境使用。*
