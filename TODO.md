# CodeNow 脚手架待办

## 1. Codex 主导迁移

- [x] 将 `.codex/agents/` 中的 11 个专业角色迁移为 Codex 原生 `*.toml` Agent Profile。
  - 验收：每个 Profile 含 `name`、`description`、`developer_instructions`；使用 `tomllib` 可解析；不保留伪字段 `tools`、`color`。
- [x] 将 `project-prepare-orchestrator` 从伪 Agent 移为 `02-project-prepare` 的参考文档，并修复所有引用。
  - 验收：`.codex/agents/` 不再存在旧式角色 Markdown（目录说明 `README.md` 除外）；`02-project-prepare` 指向新的参考路径。
- [x] 清理主流程中对 Claude Code、Cursor 和 `CLAUDE.md` 的运行时依赖。
  - 验收：`.codex/skills/`、`.codex/rules/`、`AGENTS.md` 中不再把其他工具目录或 `CLAUDE.md` 作为 Codex 的必经路径。
- [x] 将 Rules 调整为由 `AGENTS.md` 显式加载的 Codex 项目规则，并保留教学、TODO 回写与归档约束。
  - 验收：Rules 不再包含 Cursor 专属 `alwaysApply` / `globs` 字段；`AGENTS.md` 说明加载关系。

## 2. Agent Profile 内容保真修复

- [x] 恢复 11 个专业角色的详细规范，避免 TOML 迁移丢失职责、边界、输入、标准输出、执行规则与验收标准。
  - 验收：每个 TOML Profile 的 `developer_instructions` 都自包含完整角色规范；原文中有业务价值的章节均被保留，旧 YAML frontmatter、`tools`、`color` 和旧平台专属调用话术不进入新规范。
- [x] 按 Codex 原生发现与继承机制修正 Profile 配置。
  - 验收：11 个 Profile 均位于项目级 `.codex/agents/`，设置只读沙箱，不硬编码模型或推理强度，并由当前会话或显式委派配置决定模型。
- [x] 恢复并审查 Prepare 编排规则的完整内容。
  - 验收：编排参考保留启用矩阵、主会话职责、去重/冲突裁决、合并顺序、质量门槛、统一输出结构与验收标准；不再把它注册成 Agent。
- [x] 完成 Codex 兼容性与内容回归验证。
  - 验收：TOML 可解析且字段/文件名/引用一致；Markdown 本地引用无断链；`.codex/agents/` 无旧式 Agent YAML；扫描出的遗留 `spawn/subagent` 表述均已判定为 Codex 多 Agent 语义或完成改写；验证结果回写本文件。

## 验证记录

### 2026-08-21

- 已发现：根目录此前缺失 `TODO.md`，与现有 `AGENTS.md` 的强制入口冲突；本轮已补建并写入可执行验收标准。
- 已完成：11 个 Markdown 伪 Agent 迁为自包含 TOML Profile；编排规则迁至 `.codex/skills/02-project-prepare/references/orchestration.md`；新增项目级 Profile 使用说明与 Codex 优先 README。
- 已纠正：此前误把 `.codex/skills` 当作跨工具目录移除；依据当前 Codex 文档，仓库级 Skills 已迁回 Codex 自动发现的 `.codex/skills/`。仍保留对 `tools`/`color`、`alwaysApply`/`globs`、`CLAUDE.md`、`.cursor/skills` 和跨工具专属参数的清理。
- 已纠正：`git-commit` Skill 的 `allowed-tools: Bash` 不是 Codex 权限边界，已移除并改为正文工具约束；项目级 Profile 自动发现与模型继承说明也已修正。
- 已纠正：可复用 Planner 不再强制读取根目录 `prd.md`；统一为优先读取当前 `prd/`，冷启动阶段才读取活跃的 `prd.md`，并禁止把 `prd.original.md` 当作当前事实。
- ✅ 内容回归：从 Git 对象恢复的 11 份角色正文共 1101 行；新 TOML 共 1200 行，原职责、边界、输入、输出格式、流程和验收章节覆盖检查无缺失。Prepare orchestration 的启用矩阵、合并与裁决规则也已完整恢复。
- ✅ Codex 验证：官方 `migrate-to-codex --validate-target` 通过 10 个 Skills、11 个 Agents 与 `AGENTS.md`；11 个 TOML 经 `tomllib` 解析，必填字段、文件名/名称、只读沙箱和模型继承检查通过。
- ✅ Skill 与引用验证：10/10 Skills 通过 `skill-creator/quick_validate.py`；Markdown 链接与正文中的本地 reference 路径检查通过；旧 `.codex/skills`、`allowed-tools`、`tools`、`color`、`alwaysApply`、`globs` 和失效 orchestrator 路径扫描无残留。
- ✅ 术语审查：保留的 `subagent` / `spawn` 只表示 Codex 官方多 Agent 工作流；旧平台专属调用参数已经移除或改写为“委派”。
- ℹ️ `.codex/config.toml` 当前不存在；本项目没有需要覆盖的 MCP、Hook、默认模型或并发设置，Codex 的 Agent/Skill 自动发现不依赖空配置，因此不为消除可选项警告而新增文件。
- ⚠️ 未提供 `package.json`，因此本轮无 `npm run lint`、`npm run test`、`npm run typecheck` 可执行。后续加入可运行样例项目时，应补齐三项 script。
- ✅ 环境验证：桌面应用内置 Codex CLI 可启动并加载配置；项目级 Profile 不需要复制到用户目录。`codex doctor` 的本地状态库和网络诊断告警属于当前机器环境，不属于本仓库迁移项。

## 审计保留项

- `Books/第01章-什么是AgenticCoding/1.1-VibeCoding的价值和边界.md` 仍以 Google AI Studio / Gemini 作为历史对比示例；它是教程正文，不参与脚手架运行。若教程也要只介绍 Codex，可另行统一改写示例与配图。
