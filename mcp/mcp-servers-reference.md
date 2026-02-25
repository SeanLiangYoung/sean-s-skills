# MCP 配置参考（推荐启用列表）

本文件为**推荐在本项目（或复用本库配置的新项目）中启用的 MCP 清单**，便于在新环境或新机器上快速恢复 Cursor 的 MCP 配置。MCP 的实际启用需在 Cursor 的 **Settings → MCP** 中操作；此处仅作记录与复现参考。

---

## 推荐 MCP 列表

| 标识 / 名称 | 用途 | 说明 |
|-------------|------|------|
| **cursor-ide-browser** | 浏览器自动化 | 导航、截屏、与页面交互、性能分析；前端/Web 开发与测试。 |
| **user-Figma**（Figma） | 官方 Figma MCP | 读取设计、截图、元数据、Code Connect、FigJam 图表；设计稿转代码、设计协作。 |

---

## 如何在新环境恢复

1. 打开 Cursor → **Settings**（或 `Ctrl+,`）→ 找到 **MCP** / **Integrations** 相关设置。
2. 添加或启用上述 MCP 服务器（具体名称以 Cursor 当前版本为准）。
3. 若为第三方 MCP（如 Figma、Framelink），需按各自文档完成安装与认证。

---

## 说明

- MCP 的运行配置由 Cursor 存储在**项目缓存**（如 `%USERPROFILE%\.cursor\projects\<project-id>\mcps\`），本仓库不包含可执行配置。
- 本文件仅作为「推荐启用清单」版本化在项目中，便于团队或换机后复现相同 MCP 环境。
