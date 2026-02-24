#!/usr/bin/env bash
# 将 Sean's Skills 能力快速集成到任意项目
# 用法: ./scripts/integrate-into-project.sh <目标项目路径> [sean-s-skills 路径]
# 示例: ./scripts/integrate-into-project.sh ../my-app
#       ./scripts/integrate-into-project.sh ../my-app /path/to/sean-s-skills

set -e
SEAN_SKILLS_PATH="${2:-$(cd "$(dirname "$0")/.." && pwd)}"
TARGET="${1:?用法: $0 <目标项目路径> [sean-s-skills 路径]}"
TARGET="$(cd "$TARGET" && pwd)"
REL_PATH=$(python3 -c "import os.path; print(os.path.relpath('$SEAN_SKILLS_PATH', '$TARGET'))")

echo "目标项目: $TARGET"
echo "Sean's Skills 路径: $SEAN_SKILLS_PATH"
echo "相对路径: $REL_PATH"

# Claude Code：创建 .claude 配置
mkdir -p "$TARGET/.claude"
if [ ! -f "$TARGET/.claude/settings.json" ]; then
  cat > "$TARGET/.claude/settings.json" << EOF
{
  "plugins": [
    {
      "source": "${REL_PATH}",
      "strict": false
    }
  ]
}
EOF
  echo "已创建 $TARGET/.claude/settings.json（引用本库为插件）"
else
  echo "已存在 $TARGET/.claude/settings.json，请手动添加 plugins 条目，source 为: $REL_PATH"
fi

# Cursor：创建规则
mkdir -p "$TARGET/.cursor/rules"
RULE="$TARGET/.cursor/rules/use-sean-s-skills.mdc"
cat > "$RULE" << EOF
---
description: 使用 Sean's Skills 库中的 skills/agents/tools；能力说明见该库 docs/capabilities-index.md
globs: 
alwaysApply: true
---

# 使用 Sean's Skills 库

本规则使 Cursor 在本项目中可使用 Sean's Skills 库的能力。

- **Skill 库路径**（相对本项目）：\`${REL_PATH}\`
- **能力索引**：\`${REL_PATH}/docs/capabilities-index.md\`
- **Skill 列表与场景**：\`${REL_PATH}/docs/skills-reference.md\`
- **Agent 列表**：\`${REL_PATH}/docs/agents-reference.md\`
- **工具索引**：\`${REL_PATH}/tools/REGISTRY.md\`

在完成文档、SEO、营销、图文、开发流程等任务时，优先查阅上述文档并按需引用 \`${REL_PATH}/skills/<name>/SKILL.md\` 或 \`${REL_PATH}/agents/*.md\` 中的说明。
EOF
echo "已创建 $RULE"

echo ""
echo "集成完成。Claude Code 可在该项目中通过 project 作用域加载本库插件；Cursor 已通过规则引用本库路径。"
echo "若 Claude 不支持 project 下 plugins 路径，请在该项目中运行: claude --plugin-dir \"$SEAN_SKILLS_PATH\""
