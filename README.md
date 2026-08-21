# CodeNow：Codex 优先的 Agentic Coding 脚手架

CodeNow 把长期项目约定放在 `AGENTS.md`，把可复用流程放在 `.codex/skills/`，把可选的专业分工放在 `.codex/agents/*.toml`。它不依赖 `CLAUDE.md`、Cursor Rules 或其他编辑器专属目录。

## 使用入口

1. 在 Codex 中打开本仓库根目录，先阅读 `AGENTS.md` 与 `TODO.md`。
2. 根据任务读取匹配的 `.codex/skills/<skill-name>/SKILL.md`；Skill 内的参考资料按需读取。
3. 实施前先确认 TODO 中有可执行验收标准；完成后回写 TODO 和验证记录。
4. 需要独立专项审查时，直接使用 Codex 从 `.codex/agents/` 自动发现的项目级 Profile；Profile 不可用时，主会话按同样的检查表完成审查。

## 目录说明

| 路径 | 用途 |
| --- | --- |
| `AGENTS.md` | Codex 自动读取的项目协议与长期约束 |
| `TODO.md` | 当前任务、验收标准、进度与验证记录的单一事实来源 |
| `.codex/skills/` | PRD、准备、开发、验收、调试和文档维护流程 |
| `.codex/agents/` | Codex 自动发现的项目级 TOML Agent Profile |
| `.codex/rules/` | 由 `AGENTS.md` 按需加载的教学、TODO 回写和归档规则 |
| `API文档/` | 按需读取的外部服务接入资料 |

`Books/` 与 `docs/` 是教程和配图素材，不是 Codex 的运行时配置。
