# .claude — 本库作为 Claude Code 项目配置

本目录用于**本仓库**在 Claude Code 中的项目级配置说明与示例。  
将本库能力集成到**其他项目**时，请参考 [docs/cookbook.md](../docs/cookbook.md)。

## 本库即插件

本仓库根目录已包含 `.claude-plugin/plugin.json`，可直接作为 Claude Code 插件使用：

- **skills**：指向 `./skills/`（79 个 Skill）
- **agents**：指向 `./agents/`（7 个子代理）

## 在当前仓库中使用

在 Claude Code 中打开本仓库后，若已通过「从目录安装」加载本插件，则所有 skills 与 agents 会按 Claude 约定自动发现并可用。

## 在任意项目中使用本库能力

见 [docs/cookbook.md](../docs/cookbook.md) 的「快速集成」与「方式一：以插件目录运行」等章节。
