# Wiki 配置

- 状态：已配置，2026-10-09 已核实
- 用户提供的父目录：`C:/Users/SeanL/OneDrive/llm-wiki`
- 本地知识库根目录：`C:/Users/SeanL/OneDrive/llm-wiki/my-llm-wiki`
- 连接方式：直接维护本地文件
- 维护规则：读取根目录 `schema.md` 和 `purpose.md`；原始材料在 `raw/sources/`，编译页面在 `wiki/`；类型包括 source、concept、entity、query、comparison、synthesis、overview。
- 页面格式：遵守 schema.md 的 YAML frontmatter；来源页另含 authors、year、url、venue；未知值明确为未知或空值，不编造。
- 链接与维护：页面间使用 `[[page-slug]]`；更新 `wiki/index.md` 和逆序的 `wiki/log.md`；引用原件时使用正确相对路径。
- purpose.md 目前是空模板：不要代用户填入长期研究目标，按本次材料与问题确定范围。
- OneDrive 注意事项：写入前重读目标文件，避免覆盖其他对话或同步产生的修改；本地写入成功不等于云端同步完成。

首次明确知识库位置后，将实际位置记录在这里。只保存路径、连接名称和维护约定；不保存令牌、密码或其他凭据。用户本次指定位置优先于本配置。
