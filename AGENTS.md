# CodeNow 的 Codex 项目协议

- 使用中文回复用户。
- 后续任务以仓库根目录 `TODO.md` 为准。
- 本项目以 Codex 的 `AGENTS.md`、Skills 和 TOML Agent Profile 为唯一运行时约定；不依赖 `CLAUDE.md`、Cursor Rules 或其他工具目录。

开始工作前请按需读取：

- `TODO.md`
- `.codex/rules/coach.md`（教学、解释或排错时）
- `.codex/rules/todo-writeback.md`（会修改仓库时）
- `.codex/rules/todo-prd-archive.md`（TODO 过长、已完成模块需要归档到 `prd/` 时）

本地 Skills 位于 `.codex/skills/<skill-name>/SKILL.md`。用户明确点名某个 Skill，或任务明显符合其说明时，先读取该 Skill；必要的参考资料只按 Skill 中的路由读取。

`.codex/agents/*.toml` 是 Codex 自动发现的项目级 Agent Profile，说明见 `.codex/agents/README.md`。当用户明确要求多 Agent，或适用 Skill 明确要求委派时，优先按角色边界委派可独立完成的专项任务；如果当前客户端未加载某个 Profile，主会话按同样的职责清单完成工作，不能因此跳过验收、架构或安全审查。

执行时请优先完成 `TODO.md` 中未勾选的任务；如果实际代码、`prd/` 与 `TODO.md` 冲突，以当前代码事实和 `prd/` 已实现文档为依据，并把新的差距或后续任务更新回 `TODO.md`。

**日常产品想法**（已有 `prd/` 或 `prd.md`、尚未定稿进 TODO）：用 **`product-discovery`** Skill 陪聊澄清并写 prd/TODO 增量；定稿后再用 **`project-iterate`** 开发。冷启动用 `01-mvp-prd-builder`，大块重规划用 `02-project-prepare`。

**每轮开发结束前必须回写 `TODO.md`**（含未做完、部分完成、阻塞项），规范见 `.codex/rules/todo-writeback.md`。禁止只改代码、不更新 TODO。

**TODO 过长时**：将已稳定完成且已验证的功能块卸货到对应 `prd/` 文档，再精简 TODO，规范见 `.codex/rules/todo-prd-archive.md`。

**验收驱动开发**：开发任何 TODO 前，先确认对应验收标准具体、可执行、可观察；若缺失或只有“功能正常”等空泛描述，先补 TODO 验收标准，或使用 `qa-acceptance-planner` Profile（已安装时）/ `project-verify` 生成验证清单，再开始写代码。写完代码后必须运行项目已有的 `npm run lint`、`npm run test` 和类型检查（如 `npm run typecheck` 或 `tsc --noEmit`），并把结果写入 TODO / 验证记录；若脚本不存在，记录为 `⚠️ 未提供该 script` 并追加补齐建议。`npm run build` 不作为默认验证项，只有用户明确要求、发布/打包、验证构建产物或插件加载目录时才按需执行。

写代码时请遵守：
- **Web UI 项目**（Next.js、Electron renderer、浏览器插件页面等）：可交互 UI 须提供稳定 `data-testid`（命名与验收见 `.codex/skills/project-verify/references/selector-and-testid.md`）；由 `03-project-develop` / `project-iterate` 在实现时落实，`project-verify` 执行验收。
- **非 UI 逻辑**（纯函数、数据转换、API/IPC/background handler、脚本等）：须提供可复现的单元测试、集成测试、fixture、curl/CLI smoke 或日志证据；验收方式见 `.codex/skills/project-verify/references/non-ui-verification.md`。
- 涉及 API 调用、IPC 调用、第三方服务请求或降级逻辑时，必须增加必要的调用日志，至少覆盖调用入口、关键参数摘要、成功/失败结果和错误原因，方便本地调试与问题定位。
- 日志不得输出 API Key、Token、用户隐私原文等敏感信息；需要记录时只保留脱敏后的摘要。
- 复杂逻辑和关键代码请补充中文注释，注释应解释“为什么这样做”和调试观察点，避免只重复代码表面含义。
