---
name: project-iterate
description: 已有代码库上的日常迭代开发。以 TODO.md 和 prd/ 为依据，实现本轮任务、更新 checkbox，按需读框架 reference 与 design-system。适用于继续 TODO、修 bug、小功能、用户说「接着做」且项目已可运行。不跑 update-prd、不全量重建 README。首版 MVP 用 03-project-develop；验收用 project-verify（可增量范围）。
---

# Project Iterate：TODO 驱动 → 增量实现 → 可选验证

## 与其它 Skill 的分工

| Skill | 何时用 |
| --- | --- |
| **本 Skill** | 已有代码 + `TODO.md`；日常改代码、做下一项任务、修 bug |
| `product-discovery` | 日常聊新想法、排优先级、pivot；想法尚未进 TODO 或 prd |
| `02-project-prepare` | 还没有合格 TODO / 规格，或要从粗 PRD 重新规划 |
| `03-project-develop` | **首版 MVP**：脚手架、全量实现、依赖交付、**全量 project-verify**、**update-prd**、README |
| `project-verify` | 执行验收打勾；本 Skill 完成后**按需**唤起（可指定范围） |
| `update-prd` | 里程碑同步文档；**不要**每次迭代默认跑 |
| `project-debug` | 报错、行为不对时排查 |

```text
首版：02 → 03 → project-verify → update-prd
日常：product-discovery（新想法）→ project-iterate →（可选）project-verify 增量 → 继续 TODO
```

## 何时使用 / 暂停

**使用：**

- 用户说继续 TODO、做下一项、修某个功能、小改 UI/API
- 仓库已有可运行代码（或至少已有项目结构与主框架）
- `TODO.md` 存在且写明本轮要做的事（或用户明确指定条目）

**暂停，改走其它 Skill：**

- 无 `TODO.md` 或主框架不明 → `02-project-prepare`
- 还没有代码库、要做首版 MVP → `03-project-develop`
- 只有模糊想法、尚未进 TODO → `product-discovery`（已有 prd/ 或 prd.md）或 `01-mvp-prd-builder`（从零）或 `02-project-prepare`（缺完整 TODO）
- 用户明确要求重建 `prd/`、归档、全量交付说明 → `03-project-develop` 或 `update-prd`

## 开发依据优先级

1. **`TODO.md`** — 本轮任务与验收标准（§2）
2. **`prd/`** — 已实现产品真相（读总览与各模块文档）
3. **`design-system/`** — 仅当本轮改 UI 时读取
4. **根目录 `prd.md`** — 仅当尚未迁移、且仍作为活跃产品说明时读取；**不得**读 `prd.original.md` 作开发依据

冲突时：`design-system/` → 视觉；`TODO.md` → 任务范围；`prd/` → 已实现产品行为。

## 渐进式加载（按需，不要全读）

| 条件 | 读取 |
| --- | --- |
| 本轮改 UI | `design-system/<产品名>/MASTER.md`；必要时 `ui-ux-pro-max`；需机器验收的 Web UI 读 `project-verify/references/selector-and-testid.md`（为触及的可交互元素补/维护 `data-testid`） |
| 本轮写/改 API、IPC、第三方请求 | `03-project-develop/references/logging-and-debugging.md` |
| 本轮动平台边界 | `03-project-develop/references/<主框架>.md` 一份（Next.js / Electron / vite-web-extension） |
| 其余 | 只读 `TODO.md` 相关章节 + `package.json` scripts + 涉及代码 |

主框架从 `TODO.md` §1 读取；**不要**每次迭代默认读 framework reference 或 `ui-ux-pro-max`。

## 调用日志（与 03 相同）

涉及 API / IPC / 第三方请求时，必须按 `03-project-develop/references/logging-and-debugging.md` 加日志（入口摘要、成功/失败、耗时；不输出 Key 与隐私原文）。

## 规格不足时使用专项视角

优先由主会话补齐单点规格。只有对应 Codex Profile 已加载且独立上下文有明显价值时才委派；不得因为 Profile 不可用而跳过这些检查。

| 缺口 | Profile / 检查视角 |
| --- | --- |
| TODO 条目太模糊 | `mvp-requirement-analyst` → 更新 TODO §2 |
| 新页面/入口缺 UI 细节 | `ui-interaction-planner` → 更新 TODO §3 |
| 改模块/Route/IPC | `project-architecture-planner` → 更新 TODO §4 |
| 新接 API | `api-integration-planner` → 更新 TODO §6 |
| 平台权限/manifest | `platform-capability-planner` → 更新 TODO §7 |
| 缺可执行验收标准 | `qa-acceptance-planner` → 更新 TODO §2 |

单点补规格即可；只有大块新 MVP 级功能才考虑重跑 `02-project-prepare`。

## 执行流程

### 1. 确定本轮范围

- 读 `TODO.md`，明确本轮要完成的 checkbox 或用户指定条目。
- 若范围不清，向用户确认一项再继续。

### 2. 最小上下文

- 读 `prd/` 中与本轮功能相关的文档（如有）。
- 读将要修改的文件及邻近模块；尊重 `git status` 中用户已有改动。
- 按上表**按需**加载 design-system / framework reference / logging 文档。

### 3. 实现

- 只改本轮范围；不顺手重构无关代码。
- 改 UI 时遵循 `design-system/`。
- 为本轮新增或修改且需机器验收的 Web UI 交互元素补/维护 `data-testid`（命名与范围见 `project-verify/references/selector-and-testid.md`）；若将唤起 `project-verify`，须先具备 testid，勿把埋点留给验收阶段。
- `package.json` 有变更时才安装依赖；不默认 `npm install`。
- 不默认创建/更新 `.gitignore`、`.env.example`、README（除非本轮任务明确要求）。

### 4. 验证（按需，默认轻量）

**默认（小改动）：**

- 若项目有 `lint` / `test` / 类型检查，跑与改动相关的命令；本轮触及非 UI 逻辑时优先跑相关单测或 smoke。
- 默认不跑 `build`；仅在用户明确要求、发布/打包或需要验证构建产物时按需执行。
- 在回复中说明验证了哪些点。

**建议跑 `project-verify` 时：**

- 本轮完成一个 MVP 功能块或用户要求验收
- 改动涉及主流程、API 安全、平台入口

唤起时**带范围**，例如：

```text
按 project-verify 执行，仅验证 TODO §2.3 模板写作相关验收标准，不做全量 §2 扫描。
```

增量验证时，**不必**每次完整读 `project-verify` 全部 reference；只读与本轮入口、testid、框架相关的 reference 即可。

### 5. TODO 回写（必做，结束前不可跳过）

**每轮迭代结束前必须写回 `TODO.md`**，规范见 `.codex/rules/todo-writeback.md`。

| 情况 | 写法 |
| --- | --- |
| 已完成 | `[x]` |
| 只做了一部分 | `[ ]` + 子项或「进度：…；下步：…」 |
| 被阻塞 | `[ ]` + `⚠️ 阻塞：原因；解除条件` |
| 主动延后 | 写入 §10 或条目旁注明 |
| 验证未过 | `[ ]` + `❌ 日期：原因` |

- 可追加文末 **`## 开发进度`**（按日期记录本轮摘要与下轮建议）。
- **禁止**代码已改、TODO 状态未变就结束回复。

### 6. 汇报

说明：本轮做了什么、**TODO 中哪些已 `[x]` / 仍 `[ ]` 及原因**、跑了哪些验证、下轮建议从哪条 TODO 继续。

### 7. TODO 卸货（按需）

当 TODO **过长**（约 >180 行）或某 **§2.x 已全部 `[x]` 且已验证** 时，按 `.codex/rules/todo-prd-archive.md` 将已完成块写入对应 `prd/` 并精简 TODO。不必为此跑全量 `update-prd`，除非架构大改或用户要求全量同步。

## 本 Skill 明确不做

- 不调用 `update-prd`（除非用户明确要求）
- 不重命名/归档 `prd.md`
- 不重建 `README.md` / `AGENTS.md`（除非用户要求）
- 不跑 `02-project-prepare` 全量并行 agent 编排
- 不初始化新框架脚手架（那是 `03-project-develop`）

## 协作 Skill

- **`project-debug`** — 实现或验证失败时
- **`git-commit`** — 用户要求提交时
- **`project-verify`** — 需要证据化打勾时（优先增量范围）

## 自检清单

- [ ] 已明确本轮 TODO 范围并完成实现
- [ ] 已读 `prd/`（如存在）且未读 `prd.original.md` 作依据
- [ ] UI/API/平台类改动已按需读 design-system / logging / framework reference
- [ ] API/IPC 路径已加必要日志
- [ ] 已按 `.codex/rules/todo-writeback.md` 回写 TODO（含部分完成/阻塞；禁止 silent drift）
- [ ] 未完成项有进度、阻塞或下步之一
- [ ] 若 TODO 过长或有关块已闭环，已按 `todo-prd-archive.md` 卸货到 `prd/`（或已在汇报中建议下轮卸货）
- [ ] 未默认跑 update-prd / 全量 README / 全量 project-verify
- [ ] 汇报中包含验证方式与剩余项
