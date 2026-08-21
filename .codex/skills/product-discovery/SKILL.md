---
name: product-discovery
description: 已有项目上的日常产品发现与 backlog 梳理。用户随口聊新功能、改方向、排优先级、评估与现有 prd 冲突时使用。通过自然对话澄清意图，可选使用 Codex 的 product-impact-analyst Profile 做影响分析，用户确认后将增量写入 prd/ 与 TODO.md，再交给 project-iterate 开发。不适用于冷启动（用 01-mvp-prd-builder）或全量重规划（用 02-project-prepare）。
---

# Product Discovery：日常聊想法 → prd/ + TODO 增量

## 概述

面向**已有代码或已有规格**的项目。用户用自然语言提出产品想法、调整方向、比较优先级时，本 Skill 负责陪聊澄清、评估影响、产出文档增量，**用户确认前不写 prd/、TODO.md，不写业务代码**。

解决的问题：`01` 太仪式化（6 题冷启动）、`02` 太重（全量 prepare）、`project-iterate` 假设决策已定——中间缺一条**增量产品发现**通道。

## 与其它 Skill 的分工

| Skill | 何时用 |
| --- | --- |
| **本 Skill** | 已有 `prd/` 或根目录 `prd.md` +（通常）`TODO.md` 或代码；日常聊想法、排优先级、pivot 评估 |
| `01-mvp-prd-builder` | **零 → 一**：还没有项目/PRD，要从想法生成根目录 `prd.md` |
| `02-project-prepare` | 首版或**大块**重规划：粗 PRD → 多 Agent → 完整 `TODO.md` |
| `project-iterate` | 想法已进 TODO、范围已对齐 → 写代码 |
| `update-prd` | 里程碑后实现与文档全量/增量对齐；**不是**产品探索入口 |
| `mvp-requirement-analyst` | **已决定要做**的条目太模糊 → 拆成可开发规格（本 Skill 确认后可 spawn） |

```text
冷启动：01 → 02 → 03 → update-prd
日常发现：product-discovery →（确认后）project-iterate → project-verify
大块新 MVP：product-discovery 结论 → 重跑 02-project-prepare
```

## 何时使用 / 暂停

**使用：**

- 「我想加个 XX」「能不能改成 YY」「先做 A 还是 B」
- 「和现有功能冲突吗」「这个 pivot 影响大吗」
- 已有 `prd/` 或活跃 `prd.md`，且仓库已有项目结构或 `TODO.md`
- 用户明确唤起本 Skill，或在闲聊中提出**尚未进入 TODO** 的产品变更

**暂停，改走其它 Skill：**

| 情况 | 改走 |
| --- | --- |
| 还没有任何 PRD、纯从零 | `01-mvp-prd-builder` |
| 还没有 `TODO.md`、需要首版完整开发计划 | `02-project-prepare` |
| 想法已写进 TODO、用户说「接着做 / 实现它」 | `project-iterate` |
| 用户要求全量同步 prd 与代码、里程碑收尾 | `update-prd` |
| 整块新 MVP、多模块并行规格缺失 | 本 Skill 结论为「重跑 02」→ `02-project-prepare` |

## Codex 专项审查

复杂想法可按需使用已安装的 Codex Profile；简单想法由主会话完成。不要假设其他编程 Agent 或特定委派工具存在。

### 调度原则

1. **主会话负责对话与编排**：读文档、陪用户澄清、决定是否需要专项审查、合并输出、**用户确认后**写 prd/TODO。
2. **默认先聊后审查**：简单想法（单功能、边界清晰）主会话可直接分析；复杂情况再按需使用 `product-impact-analyst` Profile 或其同等检查表。
3. **委派不嵌套**：专项角色只输出自己的分析，不再派生其它角色。
4. **轻量审查**：通常只需 0–1 个影响分析；确认要做且条目仍粗时，再按需进行 0–1 个需求或条件专项审查。禁止默认并行 5 个角色（那是 `02` 的职责）。
5. **Prompt 必须自包含**：写明用户原话、要读的文件路径、工具形态、期望输出格式。

### 何时使用 product-impact-analyst

满足**任一**即建议专项审查：

- 想法涉及 **2 个以上** prd 模块或 unclear 边界
- 与现有 prd/TODO **可能冲突**或重复
- 用户在做 **优先级 / pivot** 决策
- 可能触及 **架构、API、平台权限**（仅需影响提示，详细规格另 spawn）
- 主会话无法从现有文档判断已实现范围

**不必专项审查**：单屏小改、文案/交互微调、用户已明确「就加这一条且范围如下」。

### 何时使用其它专项视角（确认要做之后）

| 缺口 | Agent |
| --- | --- |
| §2 条目仍只有关键词 | `mvp-requirement-analyst` |
| 新页面/入口缺 UI 流程 | `ui-interaction-planner` → 更新 TODO §3 |
| 跨模块/Route/IPC | `project-architecture-planner` → 更新 TODO §4 |
| 新远程 API | `api-integration-planner` → 更新 TODO §6 |
| 桌面/插件权限 | `platform-capability-planner` → 更新 TODO §7 |
| 缺可执行验收标准 | `qa-acceptance-planner` → 更新 TODO §2 |

单点补规格即可；**只有整块新 MVP 级能力**才在汇报中建议重跑 `02-project-prepare`。

### 示例 prompt（product-impact-analyst）

```text
你是 product-impact-analyst 专项分析者（当前由 product-discovery 编排）。

用户想法：<用户原文>
请先读取 prd/（及 prd/README.md 若存在）、TODO.md、根目录 prd.md（若仍存在）。
工具形态：<来自 prd 或 TODO §1>  主框架：<...>  产品名称：<...>

评估影响与优先级，输出 prd/TODO 增量建议。不要写代码。
使用 Profile 的 `developer_instructions` 所列结构输出。
```

## 执行流程

### 第一步：读取现状（最小上下文）

按优先级读取：

1. `prd/README.md` 或 `prd/` 总览（若存在）
2. 与用户想法相关的 `prd/<模块>/README.md`，必要时读取同模块 `technical.md`
3. `TODO.md`（§2 未完成项、§10 backlog、§1 工具形态/框架）
4. 根目录 `prd.md`（**仅当** `prd/` 尚未建立且仍作活跃说明时）
5. **不得**把 `prd.original.md` 当作活跃产品依据

若 `prd/` 与 `TODO.md` 均不存在：暂停，改走 `01` 或 `02`，不要硬跑 discovery。

从 `TODO.md` §1 或 prd 读取：工具形态、主框架、产品名称（供 subagent prompt 使用）。

### 第二步：对话澄清（自然语言，非 6 题仪式）

目标：在写文档前对齐**意图、边界、优先级**。按需追问，不要一次问超过 **3** 个开放式问题。

**建议澄清维度**（按想法类型选用，不必全问）：

| 维度 | 示例问题 |
| --- | --- |
| 目标 | 用户想解决什么？怎样算成功？ |
| 范围 | MVP 最小版本是什么？明确不做什么？ |
| 优先级 | 相对当前 TODO，现在做还是进 backlog？ |
| 冲突 | 和现有 XX 功能关系：替代 / 并存 / 扩展？ |
| 约束 | 时间、平台、是否依赖新 API？ |

**对话原则：**

- 用用户语言复述理解，请用户确认或纠正
- 对明显缺失且阻塞决策的点才追问；其余在影响分析里给**推荐默认值**
- 用户说「你看着办」时：给出带理由的默认建议，仍要**确认后再写文件**

### 第三步：影响分析

- **简单想法**：主会话直接输出简短影响摘要
- **复杂想法**：spawn `product-impact-analyst`，合并其输出

主会话向用户呈现**决策摘要**（必须包含）：

```markdown
## 发现结论（待你确认）

- **我们理解你想做**：…
- **建议优先级**：P0 / P1 / P2 / 暂不做
- **影响**：prd 模块 …；TODO …；是否动架构/API …
- **建议下一步**：写入 TODO §2 开做 / 只进 §10 / 重跑 02 / 直接 project-iterate
- **将写入的变更预览**：（prd 段落标题 + TODO 条目草案）
```

**在用户明确确认前，不修改 prd/ 与 TODO.md。**

用户可回复：确认 / 修改 / 取消 / 只做 backlog。

### 第四步：用户确认后写入文档

#### 写 prd/（增量）

- 已有模块 → 更新 `prd/<模块>/README.md` 的「待实现 / 规划中 / 变更说明」小节；若涉及实现边界、API、数据或验收，再同步更新 `prd/<模块>/technical.md`
- 新模块 → 新建 `prd/<模块-slug>/README.md`，必要时新建 `prd/<模块-slug>/technical.md`，并在 `prd/README.md` 索引追加
- 遵循 `.codex/rules/todo-prd-archive.md` 的**增量**原则，不覆盖无关已实现内容
- 若 `prd/` 尚不存在仅有 `prd.md`：在根目录 `prd.md` 对应章节追加，并注明「待迁移到 prd/ 模块文件夹」

#### 写 TODO.md

| 内容 | 位置 |
| --- | --- |
| 确认本轮要做的开发任务 | **§2** 新 checkbox（可含 P0/P1 标注） |
| 仅记录想法、暂不开发 | **§10 未完成目标 / 后续功能** |
| UI/API/架构/验收补充 | §3–§7（若已 spawn 对应 planner） |
| 本轮 discovery 摘要 | 文末 **## 产品发现记录**（追加，不覆盖历史） |

**TODO 不存在时**：按 `02-project-prepare` 模板创建最小 `TODO.md`（§1 从 prd 抄工具形态/框架 + 本次 §2/§10 + 发现记录），并告知用户完整计划仍建议跑 `02`。

发现记录示例：

```markdown
## 产品发现记录

### 2026-05-30
- 想法：…
- 结论：确认进 §2.4；prd/share/README.md 追加待实现
- 下步：project-iterate 实现 §2.4
```

写入规范与 checkbox 状态见 `.codex/rules/todo-writeback.md`（discovery 阶段新条目默认 `[ ]`）。

### 第五步：按需补规格

若确认进 §2 但条目仍粗：

1. spawn `mvp-requirement-analyst`（或 §3–§7 对应 planner）
2. 合并输出进 TODO 对应章节
3. 再次向用户展示更新后的 §2 预览（短确认即可，不必重复全流程）

### 第六步：汇报与路由

说明：

- 写入了哪些 prd/ 文件与 TODO 章节
- 建议下一步 Skill：`project-iterate`（最常见）/ `02-project-prepare` / 继续 discovery
- 若用户想立刻开发且 §2 已够细：可直接唤起 `project-iterate`

## 本 Skill 明确不做

- 不写业务代码、不安装依赖、不跑脚手架
- 不默认 spawn `02` 全套并行 Agent
- 不默认跑 `update-prd` 全量重建
- 不把冷启动 6 题流程当作日常 discovery 模板
- 不在用户未确认时改 prd/TODO
- 不读 `prd.original.md` 作活跃依据

## 协作 Skill 与 Agent

| 名称 | 关系 |
| --- | --- |
| `product-impact-analyst` | 复杂想法的影响与优先级分析 |
| `mvp-requirement-analyst` | 已确认条目拆细 |
| `project-iterate` | 确认并写 TODO 后的默认开发入口 |
| `02-project-prepare` | 整块新 MVP 或 TODO 严重缺失 |
| `update-prd` | 用户明确要求文档与代码里程碑对齐时 |

## 自检清单

- [ ] 已读 `prd/` 与 `TODO.md`（或已说明缺失并改路由）
- [ ] 已与用户对齐意图；复杂项已 spawn impact analyst 或等价分析
- [ ] **用户已确认**后才写入 prd/TODO
- [ ] prd 为增量写入；TODO 新条目位置正确（§2 vs §10）
- [ ] 已追加「产品发现记录」
- [ ] 已说明下一步 Skill（iterate / 02 / 继续 discovery）
- [ ] 未写代码、未误跑 02 全量编排
