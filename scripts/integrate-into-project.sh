#!/usr/bin/env bash
# 一键将 Sean's Skills 的 rules 与「引用本库」的规则配置到目标项目的 .cursor 中，无需人工参与，AI 可直接使用。
# 用法: ./scripts/integrate-into-project.sh <目标项目路径> [sean-s-skills 路径]
# 示例: ./scripts/integrate-into-project.sh ../my-app
#       ./scripts/integrate-into-project.sh /path/to/my-app /path/to/sean-s-skills

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SEAN_SKILLS_PATH="${2:-$(cd "$SCRIPT_DIR/.." && pwd)}"
TARGET="${1:?用法: $0 <目标项目路径> [sean-s-skills 路径]}"
TARGET="$(cd "$TARGET" && pwd)"
SEAN_SKILLS_PATH="$(cd "$SEAN_SKILLS_PATH" && pwd)"
test -d "$SEAN_SKILLS_PATH/skills"
test -d "$SEAN_SKILLS_PATH/agents"
REL_PATH=$(PYTHONIOENCODING=utf-8 python3 -c 'import os, sys; p = lambda x: x[1] + ":" + x[2:] if os.name == "nt" and len(x) > 2 and x[0] == "/" and x[2] == "/" else x; print(os.path.relpath(p(sys.argv[1]), p(sys.argv[2])).replace(os.sep, "/"))' "$SEAN_SKILLS_PATH" "$TARGET")

echo "目标项目: $TARGET"
echo "Sean's Skills 路径: $SEAN_SKILLS_PATH"
echo "相对路径: $REL_PATH"

SKILL_COUNT=$(find "$SEAN_SKILLS_PATH/skills" -mindepth 2 -maxdepth 2 -type f -name SKILL.md | wc -l | tr -d "[:space:]")
AGENT_COUNT=$(python3 -c 'import pathlib, sys; print(sum(p.read_text(encoding="utf-8-sig").startswith("---") for p in pathlib.Path(sys.argv[1]).glob("*.md")))' "$SEAN_SKILLS_PATH/agents")

# 创建 .cursor/rules
mkdir -p "$TARGET/.cursor/rules"

# 1. 写入「引用本库」规则（目标项目中用 REL_PATH 访问 skills/agents/tools）
RULE_FILE="$TARGET/.cursor/rules/use-sean-s-skills.mdc"
cat > "$RULE_FILE" << EOF
---
description: 使用 Sean's Skills 库中的 ${SKILL_COUNT} 个 Skill、${AGENT_COUNT} 个 Agent 与 tools；能力说明见该库 docs
globs: 
alwaysApply: true
---

# 使用 Sean's Skills 库

本规则使 Cursor 在本项目中可使用 Sean's Skills 库的能力，无需复制 skills 目录。

- **Skill 库路径**（相对本项目）：\`${REL_PATH}\`
- **能力索引**：\`${REL_PATH}/docs/capabilities-index.md\`
- **Skill 列表与场景**（${SKILL_COUNT} 个）：\`${REL_PATH}/docs/skills-reference.md\`
- **Agent 列表**：\`${REL_PATH}/docs/agents-reference.md\`
- **工具索引**：\`${REL_PATH}/tools/REGISTRY.md\`

在完成文档、SEO、营销、图文、知识入库、安全审计、开发流程等任务时，优先查阅上述文档并按需引用 \`${REL_PATH}/skills/<name>/SKILL.md\` 或 \`${REL_PATH}/agents/*.md\` 中的说明。
EOF
echo "已创建 $RULE_FILE"

# 2. 复制用户级规则（充分利用 Skills、执行前二次确认）
for f in skill-usage.mdc confirmation-before-action.mdc; do
  if [ -f "$SEAN_SKILLS_PATH/rules/$f" ]; then
    cp "$SEAN_SKILLS_PATH/rules/$f" "$TARGET/.cursor/rules/$f"
    echo "已复制 rules/$f -> .cursor/rules/$f"
  fi
done

echo ""
echo "集成完成。目标项目 .cursor/rules 已包含："
echo "  - use-sean-s-skills.mdc（引用本库路径，AI 可直接使用 ${SKILL_COUNT} 个 Skill + ${AGENT_COUNT} 个 Agent）"
echo "  - skill-usage.mdc、confirmation-before-action.mdc（用户级规则）"
echo "在 Cursor 中打开目标项目即可使用，无需其他配置。"
