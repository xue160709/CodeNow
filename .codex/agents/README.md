# CodeNow Codex Agent Profiles

本目录保存 CodeNow 的 **Codex 原生项目级 Agent Profile**。每个 `*.toml` 使用必填的 `name`、`description`、`developer_instructions`，并用 `sandbox_mode = "read-only"` 收紧专项规划角色的写入边界。旧版 Markdown 的 YAML frontmatter、`tools` 和 `color` 不是 Codex Profile 字段，已移除。

## 使用方式

Codex 会自动发现两类 Profile：用户级 `~/.codex/agents/` 和仓库级 `.codex/agents/`。因此，在 Codex 中打开本仓库即可使用这些角色，**不需要复制到用户目录**。

每个文件都是自包含的角色配置，`name` 是 Codex 识别角色的真实标识。Profile 不固定 `model` 或 `model_reasoning_effort`，默认继承父会话或显式委派设置，避免脚手架绑定单一模型。任务 Prompt 仍须包含本次目标、要读取的项目文件和预期产物；Profile 只固化角色边界，不替代任务上下文。

| Profile | 适用场景 |
| --- | --- |
| `mvp-*.toml` | 冷启动 PRD 的用户、范围、交互和质量审查 |
| `product-impact-analyst.toml` | 已有项目的新想法、优先级或影响分析 |
| `*-planner.toml` | 需求、架构、UI、API、平台、验收的专项规格 |

`project-prepare-orchestrator` 不是可委派 Agent，完整合并规则在 `.codex/skills/02-project-prepare/references/orchestration.md`。
