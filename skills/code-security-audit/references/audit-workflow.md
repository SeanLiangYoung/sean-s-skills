# 技术栈参考

只读适用段落。检查清单不是通过证明。

## 资料与执行环境

- 记录 commit/dirty、时间/时区、部署版本、工具和规则版本，建立资产/权限映射。
- rg 搜索 manifest、锁文件、部署、身份/权限及已有用例，避免输出 .env、kubeconfig 或连接串全文。
- 多锁文件先确认真实构建来源；过时锁文件不能代表现部署。
- 检查测试 setup 是否加载 .env/连接外部数据库；优先局部合成配置，不清空全局环境。
- 使用官方工具发布、核查校验信息，记录版本，不默认执行未知安装脚本。

## Node.js / Vue / HTML

- npm audit --package-lock-only --ignore-scripts --json，另做 omit=dev；pnpm/yarn 用其实际锁文件兼容方式。
- 区分依赖图、最终镜像与浏览器 bundle。父依赖传播不是独立漏洞。
- 路由顺序、租户/对象授权、SQL、文件/命令、JWT 算法/issuer/audience、代理头、CORS/CSRF、邀请/重置及撤销。
- Vue：v-html、DOM sink、净化配置、URL scheme、iframe 和 postMessage origin。
- SSRF：IPv4/IPv6/映射地址、全部 DNS 结果、固定连接地址、重定向、协议、大小限制。本地注入 DNS 需注明前提。
- 限流：真实来源、账号、共享代理、多副本、过期回收和键数；不在真实登录入口做压力验证。

## C# / .NET

- 按 SDK 使用 dotnet list package 或 dotnet package list 的 --vulnerable --include-transitive，审查 restore 副作用。
- 授权 policy、资源/租户过滤、EF/raw SQL、模型绑定、路径、反序列化、JWT、异常及日志。
- 生产 fail-closed；mock 全部认证不能证明真实身份服务有效。

## Python

- pip-audit 或项目锁文件扫描，依赖在隔离环境安装。
- eval/exec、subprocess、pickle/YAML、模板、SQL、路径、网络及任务身份传播。

## 秘密

- Gitleaks 等覆盖当前文件及可获得全历史，使用 redaction；扫描器可能打印值，输出落盘前确认。
- 检查 CI、私钥 JSON、构建上下文、制品和日志暴露。
- 区分非空候选、结构确认、授权验证有效；audience/TTL 不因名称含 TOKEN 就是秘密。
- Git 提交数不是已扫描历史版本数。先轮换再清理历史，签名迁移明确过渡窗口。

## Azure DevOps / AKS

- Repos 实际分支保护、绕过、成员；pr:none 不证明无 PR validation policy。
- Pipeline 修改权、服务连接范围、生产/测试身份、变量组、Secure Files、Agent 隔离、任务来源与制品追踪。
- AKS Entra/RBAC、API Server、local accounts、节点版本、身份、准入、Job、ServiceAccount、Secret、网络、Ingress、Pod 安全与资源限制。
- az aks show 用白名单 query；kubectl 显式 --context/-n。先成功一条，再扩大只读采集；失败及时收敛。
- live 与仓库分别取证；原始 spec 可有明文 env，投影后保存。
- 不读 Secret 内容不等于确认权限最小化，仍需服务所需字段和实际引用矩阵。

## 动态与关闭

- 源码确认认证与路由，低频验证自己测试数据，保留响应结构不保留正文。
- 两租户/两角色覆盖对象、查询、下载、导出、缓存、任务及令牌撤销。
- ZAP 先被动再限定已登录主动；浏览本身可有业务副作用。未认证/未爬取记录缺口。
- 修复后同一探针正确拒绝，同时正常流程回归；只看代码不能关闭。
- 参考 ASVS/WSTG/官方基线，只有逐条验证适用性才能声称达到标准等级。
