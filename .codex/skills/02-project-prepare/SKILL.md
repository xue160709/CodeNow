---
name: 02-project-prepare
description: 从仓库根目录 prd.md 准备一个 vibecoding 项目，但不写业务代码。读取 01-mvp-prd-builder 产出的粗粒度 PRD，通过 Codex 专项审查深度拆解 MVP 功能、动态判断网页/桌面软件/浏览器插件等项目形态，生成或更新设计系统（含 UI 技术栈、图标、占位图、用户画像适配）、数据来源与演示策略、API 接入方案、架构规格、验收标准和 TODO.md 开发计划，并在用户确认前停止。
---

# Project Prepare：粗 PRD → 多 Agent 深度拆解 → 开发规格 → TODO.md

## 概述

面向 vibecoding 小白的项目准备 Skill。用户只需要维护仓库根目录 `prd.md`；本 Skill 负责把 `01-mvp-prd-builder` 产出的简版 PRD 转成 `03-project-develop` 可稳定执行的开发规格（含可演示的数据来源与演示策略、占位图/icon 与 UI 技术栈合同），但不得创建页面、安装依赖、写业务代码或真正接入 API。

当前阶段的核心问题是：`prd.md` 的 `【核心功能 MVP】` 经常只有几个词或很短一句话，到了 03 开发时不知道具体要做什么，导致实现不稳定。本 Skill 必须先深度拆解这些 MVP 功能，再生成 TODO.md。

后续真正写代码时，使用 `03-project-develop` Skill 按 `TODO.md`、`prd.md`、`design-system/` 和项目规格执行。

`TODO.md` 是计划阶段产物，应该优先由本 Skill 生成。开发完成后如果实际实现没有覆盖 `prd.md` 的所有目标，由 `03-project-develop` 调用 `update-prd` 对比根目录 `prd.md`、当前代码和新生成的 `prd/` 文档体系，只把未完成差距新增或更新回 `TODO.md`。

**与 `product-discovery` 的分工**：已有 `prd/` 与代码后的**日常小想法、优先级讨论**用 `product-discovery` 写 prd/TODO 增量即可；只有**整块新 MVP**、TODO 严重缺失或用户明确要求重规划时，才重跑本 Skill。

## Codex Agent Profile

专项角色位于仓库根目录 `.codex/agents/*.toml`，Codex 会自动发现这些项目级 Profile。它们使用必填的 `name`、`description`、`developer_instructions` 和适合规划任务的只读沙箱；模型与推理强度默认继承当前会话或显式委派配置。详情见 `.codex/agents/README.md`。

Profile 只定义稳定的角色边界。每次委派仍要在 Prompt 中提供 PRD、项目形态、具体目标和预期产物。若当前客户端未加载 Profile 或任务不值得拆独立上下文，主会话按同样的专项检查表完成工作并在 TODO 中记录，不得跳过。

### TODO 生命周期（02 生成 → 日常维护）

| 阶段 | 规范 |
| --- | --- |
| 02 生成 TODO | 本 Skill 模板（含已完成模块索引、开发进度、卸货记录占位） |
| 每轮开发结束 | `.codex/rules/todo-writeback.md` |
| TODO 过长 / 功能闭环 | `.codex/rules/todo-prd-archive.md` → 增量写 `prd/`，精简 §2 |
| 里程碑 / 首版收尾 | `update-prd` 全量（可与卸货配合） |

### Agent 与 Skill 的关系

| 层级 | 职责 |
| --- | --- |
| `.codex/agents/*.toml` | Codex 自动发现的项目级 specialist Profile；由需要独立上下文的任务选择 |
| `02-project-prepare` | **计划阶段默认编排者**：启用矩阵、并行委派、合并、写 TODO |
| `references/orchestration.md` | **合并规则**，不是 Agent，也不应被委派 |

本 Skill **拥有** prepare 阶段的标准编排流程，但**不独占** specialist Profile 的调用权。

## Codex 委派规范

当 Codex 当前环境提供委派能力、对应 Profile 已加载且任务确实因独立上下文受益时，使用该能力。不能假设其他编程 Agent 或特定工具参数存在；没有可用 Profile 时，主会话照样完成每个已启用的专项审查。

### 调度原则

1. **主会话负责编排**：读取 PRD、判断启用矩阵、按需委派、合并结论、写 TODO。主会话即编排者，不委派合并规则。
2. **委派不嵌套**：专项角色只交付自己的分析，不再派生其它角色。
3. **并行优先**：彼此独立的已启用专项可在同一轮并行；有前后依赖的审查必须等待必要结论。
4. **Prompt 必须自包含**：每个独立上下文都要写明待读文件、工具形态、主框架、具体目标和期望输出；不要假设它继承主会话上下文。
5. **合并规则**：所有专项结论完成后，主会话读取 `references/orchestration.md` 去重、消冲突，形成统一开发规格。

### 标准 Prompt 上下文块

委派任一 specialist 时，Prompt 开头应包含：

```text
你是 <agent-name> 专项分析者（当前由 02-project-prepare 编排）。

请先读取仓库根目录 prd.md。
工具形态：<来自 prd.md>
主框架：<Next.js | Electron | vite-web-extension>
产品名称：<来自 prd.md>

只输出规格，不写业务代码、不安装依赖、不运行脚手架，也不再委派其他 Agent。
```

### 可用专项视角

#### 必选（始终审查；按需委派）

| name | 职责 |
|---|---|
| `mvp-requirement-analyst` | 粗粒度 MVP → 可开发功能规格 |
| `project-architecture-planner` | 架构、框架、模块边界、安全边界 |
| `qa-acceptance-planner` | 验收标准、测试点、验证清单 |

#### 条件启用（主会话先判断，再审查或委派）

| name | 启用条件 |
|---|---|
| `ui-interaction-planner` | 有页面、窗口、popup、options、side panel、new tab 或其他可视界面 |
| `api-integration-planner` | PRD/API 文档涉及远程 API、AI、Token、鉴权、同步或第三方服务 |
| `platform-capability-planner` | 桌面软件、浏览器插件，或 PRD 涉及本地文件、剪贴板、通知、manifest、权限等 |

#### 不参与委派

| name | 用途 |
|---|---|
| `references/orchestration.md` | **合并规则**，供主会话读取；不是 Agent |

### 启用原则

- 架构和 QA 永远启用。
- UI/交互：网站、桌面软件、浏览器插件通常启用。
- API/集成：只有确有远程服务、鉴权、同步或 Key 保护需求时启用。
- 平台能力：桌面软件、浏览器插件通常启用；纯网站仅在 PRD 明确涉及浏览器权限/本地能力时启用。
- 平台能力 ≠ 后端；Electron main/preload 和插件 background/service worker 是平台边界，不是传统服务端。

## 执行流程

### 第一步：读取 PRD

- 只读取仓库根目录 `prd.md`。
- 提取：产品名称、Slogan、工具形态、用户画像、场景故事、核心功能 MVP、交互流程、ASCII 流程图、UI 设计风格。
- 优先使用 `prd.md` 里的 `工具形态:` 字段；该字段通常由 `01-mvp-prd-builder` 在材料吸收和按需澄清后最终确认：
  - `网站，优先在桌面使用`
  - `网站，优先在移动端使用`
  - `桌面软件`
  - `浏览器插件`
- 如果 `prd.md` 缺少工具形态，先暂停并让用户从以上四项中选一项，不要继续生成 TODO。
- 如果 `【核心功能 MVP】` 中有功能只有几个词或一句很泛的描述，必须进入深度拆解流程，不要直接用这些词生成 TODO。

### 第二步：选择开发框架

根据工具形态写入唯一主框架：

| 工具形态 | 开发框架 | 说明 |
|---|---|---|
| 网站，优先在桌面使用 | Next.js | App Router + TypeScript，适合桌面优先 Web 产品 |
| 网站，优先在移动端使用 | Next.js | App Router + TypeScript，按移动端优先响应式设计 |
| 桌面软件 | Electron | Electron + Vite + TypeScript，优先使用 electron-vite 结构 |
| 浏览器插件 | vite-web-extension | 使用 `https://github.com/JohnBra/vite-web-extension`，Manifest V3、React、TypeScript、Tailwind |

不要把工具形态改写成技术方案；在 `TODO.md` 中同时保留原始工具形态和最终框架选择。

### 第三步：判断 Agent 启用矩阵

主会话根据 PRD 写出启用矩阵（写入最终 TODO.md 第 1 节），例如：

```text
必选：mvp-requirement-analyst、project-architecture-planner、qa-acceptance-planner
条件启用：ui-interaction-planner（网站有可视入口）
未启用：api-integration-planner（MVP 无远程 API）；platform-capability-planner（非桌面/插件）
```

### 第四步：专项深度拆解

对启用矩阵中的每个视角完成专项审查。Profile 已加载且并行可降低等待时间时可在同一轮委派；否则主会话依次完成并记录审查结论。

#### 4.1 必选专项视角

**mvp-requirement-analyst**

```text
你是 mvp-requirement-analyst 专项分析者（当前由 02-project-prepare 编排）。
读取 prd.md，逐条拆解【核心功能 MVP】。
对每个功能输出：功能名称、用户目标、使用入口、子功能、主流程、输入/输出/反馈、
默认/空/加载/成功/错误态、数据读写、MVP 必做、暂不实现、待确认点及推荐默认值。
粗关键词不得原样作为唯一任务描述。
使用标准输出格式章节输出。
```

**project-architecture-planner**

```text
你是 project-architecture-planner 专项分析者（当前由 02-project-prepare 编排）。
读取 prd.md，按工具形态选择主框架并产出架构规格：
主框架与理由、入口规划、模块边界、数据对象、本地/远程存储、API Key 与安全边界、
是否需要后端或平台边界、开发顺序、架构风险。
不要默认规划后端。
使用标准输出格式章节输出。
```

**qa-acceptance-planner**

```text
你是 qa-acceptance-planner 专项分析者（当前由 02-project-prepare 编排）。
读取 prd.md，为每个 MVP 功能产出验收标准、主流程走查、异常流程、
自动验证命令建议、平台专项验证。
使用标准输出格式章节输出。
```

#### 4.2 条件专项视角

仅审查启用矩阵中标记为启用的视角：

- **ui-interaction-planner**：界面入口、信息架构、组件、状态、演示内容与素材、设计系统补充约束（UI 栈/icon/占位）、响应式/窗口要求
- **api-integration-planner**：按需读 `API文档/`，产出 API 清单、鉴权、降级、`【API 接入方案（待确认）】` 草案
- **platform-capability-planner**：权限、入口、生命周期、Electron/插件边界、平台验证

各角色的稳定边界见对应 `.codex/agents/<name>.toml` 的 `developer_instructions`；任务上下文仍以本 Skill 的 Prompt 为准。

#### 4.3 等待并收集结果

- 等待所有已委派的专项结论完成后再进入合并。
- 若某个委派失败，最多重试 1 次；仍失败则主会话按该 Profile 的职责补做，并在 TODO 中标注「⚠️ 由主会话补写」。

#### 4.4 主会话合并规格

读取 `references/orchestration.md`，按其中合并规则处理全部专项输出：

- 去重、消冲突
- 产品范围以 `prd.md` 为准
- 技术路线以工具形态和框架映射为准
- 安全策略选更严格且符合平台约束的方案
- 产出一份统一开发规格，供第五～七步使用

不得把合并规则当作 Agent 委派。

### 第五步：读取 UI 准则并产出设计系统

本步目标：产出 **03 可直接安装的 UI 技术栈合同**（组件、图标、占位图）和 **视觉 token**，而不只写颜色/字体。

- 读取 `.codex/skills/ui-ux-pro-max/SKILL.md`。
- 图标检索：`ui-ux-pro-max` 的 `icons.csv` 仅作语义参考；**工程默认以 SKILL 正文与下方 MASTER「图标 Iconography」为准（React 栈默认 `lucide-react`）**，不要因 csv 示例而默认 Phosphor。
- 在调用/使用 `ui-ux-pro-max` 前，先回到第一步已读取的 `prd.md` 内容，确认是否存在 `【UI 设计风格】`：
  - 有：把该章节作为设计系统的主风格来源，`ui-ux-pro-max` 只用于补齐工程化 token、组件规范、响应式和可访问性细节。
  - 没有：不要暂停要求用户补 UI 风格；必须基于 `prd.md` 里的产品名称、Slogan、工具形态、用户画像、场景故事、核心功能 MVP、交互流程和 UI/交互 Agent 输出，先选择最适合的设计系统方向，再用 `ui-ux-pro-max` 补齐具体规则。
- 当 `prd.md` 没有 UI 设计风格时，设计方向选择必须服务产品语境，而不是泛泛追求“好看”：重点判断用户注意力状态、使用频率、内容密度、平台入口、任务严肃度、情绪调性和核心转化动作。
- 检查是否已有 `design-system/<产品名>/MASTER.md`：
  - 有：读取并对比 `prd.md` 与新开发规格，只更新过时或冲突内容。
  - 没有：基于 `prd.md`、UI/交互规格和 UI 准则生成 `MASTER.md`。
- **`MASTER.md` 必须包含下方「MASTER 必备章节」全部小节**（不可只写 token 表）；缺任一小节视为设计系统未完成。
- 与 `prd.md` 冲突时，以 `prd.md` 的产品表达为准，UI 准则只补齐工程化细节。

#### MASTER 必备章节（`design-system/<产品名>/MASTER.md`）

生成或更新 `MASTER.md` 时**必须**包含以下结构（标题可微调，内容不可缺）：

```markdown
# <产品名> 设计系统

## 设计取向依据
（2～4 句：本产品视觉/交互气质来自哪些 PRD 事实）

### 用户画像适配
| 维度 | 来自 prd.md 的要点 | 对应设计决策 |
| --- | --- | --- |
| 用户熟练度 | （引用画像/场景，勿空话） | 如：术语密度、是否需引导 |
| 使用频率 | | 如：默认页、快捷操作 |
| 注意力状态 | | 如：单任务 vs 扫读 |
| 任务严肃度 | | 如：配色克制、错误态强调 |
| 信息密度 | | 如：紧凑列表 vs 卡片留白 |
| 情绪调性 | | 如：鼓励型空态 vs 专业型 |
| 核心转化动作 | | 如：主 CTA 位置与尺寸 |

（至少 1 行「画像/场景原文 → 具体 token 或布局」可追溯，禁止只写「现代简洁」）

## UI 技术栈与组件策略
- **样式**：Tailwind CSS + CSS variables（全局样式入口写法：<如 `@import "tailwindcss"` 或项目约定>）
- **组件**：默认 Tailwind 组合；复杂 Dialog / Dropdown / Select / Tabs 等：<无 | 采用 Radix/shadcn 风格，列出会用到的组件>
- **图表**（仅 PRD/界面需要时）：<无 | recharts | 其他 + 理由>
- **禁止**：独立 CSS 文件堆叠（除非 PRD 要求）、CSS-in-JS、用 emoji 充当功能图标

## 图标 Iconography
- **图标库**（全站唯一）：<Next.js/Electron/插件 React 栈默认 `lucide-react`；若 PRD 明确要求其他库须写明理由>
- **安装包名**：`lucide-react`（与上一致）
- **尺寸 token**：导航 `--icon-nav` 20px；按钮内 `--icon-inline` 16px；空态/插画区 `--icon-empty` 48px（可按产品调整，须全站统一）
- **线宽 / 风格**：如 stroke 1.5～2，与字重一致；禁止多套线宽混用
- **无障碍**：纯图标按钮必须 `aria-label` 或 sr-only 文案；导航项图标+文字
- **动作映射**（摘自 ui-interaction-planner）：<主导航用哪些图标语义；保存/删除/关闭等>

## 媒体与占位图
- **默认策略**：`public/placeholders/` 静态资源 + 或 token 渐变/SVG 占位组件；**不**默认依赖海外 CDN
- **Unsplash API / 远程图源**（可选）：<无 | Unsplash | 其他 — 仅 PRD 明确需要图库/摄影内容时启用；须写 `IMAGE_PROVIDER=none|unsplash`、`UNSPLASH_ACCESS_KEY`、超时、失败回退本地图、署名/来源要求；大陆用户默认 `IMAGE_PROVIDER=none`>
- **尺寸与 a11y**：固定宽高比、必有 `alt`、加载失败显示本地 fallback，避免 CLS
- **按界面**（摘自 ui-interaction-planner）：<头像/封面/卡片图用占位还是实拍资产>

## 数据与演示内容（设计侧约定）
- **数据来源类型**：`LIVE` | `FIXTURE` | `EMPTY`
- **演示策略类型**：`LIVE_UNCONFIGURED` | `FIXTURE_DEMO` | `EMPTY_CTA`（可为 `LIVE + FIXTURE_DEMO`，但 UI 必须标明示例模式）
- **FIXTURE 默认路径**（若 TODO 有 FIXTURE_DEMO 功能）：`src/fixtures/` 或 `src/data/demo/`
- **FIXTURE 是否显示「示例数据」角标**：<是/否>
- **LIVE 未配置态**：文案与 CTA 基调（与情绪调性一致）

## 视觉 Token
- 颜色、字体、圆角、阴影、间距…
## 组件气质与关键界面状态
- 默认 / 空 / 加载 / 成功 / 错误 / 未配置 …
## 响应式或窗口尺寸
- …
```

**按主框架的默认 UI 栈（PRD 未反对时写入 MASTER，可被 PRD 覆盖）：**

| 主框架 | 样式 | 图标库 | 复杂组件 |
| --- | --- | --- | --- |
| Next.js | Tailwind + CSS variables | `lucide-react` | 需要表单/弹层/菜单时采用 shadcn/Radix 风格 |
| Electron（React renderer） | 同左 | `lucide-react` | 同左 |
| vite-web-extension（React） | 同左 | `lucide-react` | 同左；注意 popup 窄屏密度 |

图表库：**仅** PRD 或界面规格明确有图表时，在 MASTER 写 `recharts`；否则写「无」。

### 第六步：读取 API 文档并制定接入方案

- 只有 `api-integration-planner` 启用时才执行本步骤；没有 API 需求时，在 TODO 中写明“当前 MVP 不需要远程 API”。
- 优先采用 `api-integration-planner` 专项 Agent 输出的 API 方案草案；主会话核对后写回 `prd.md`。
- 按需读取 `API文档/` 中与 PRD 场景相关的文档；不要整目录盲读。
- 若存在 `API文档/如何接入Token`，先读取鉴权方式。
- 在 `prd.md` 末尾新增或更新 `【API 接入方案（待确认）】`，已存在时只更新，不重复追加。

写回格式：

```markdown

【API 接入方案（待确认）】

### 会调用的 API
- API 名称：用于什么功能；为什么比纯本地实现更合适；失败时如何降级。

### 暂不接入的 API
- API 名称：暂不接入原因；后续什么条件下再接入。
```

### 第七步：生成 TODO.md 并停止

- 在仓库根目录创建或更新 `TODO.md`。
- 如果已存在，按最新 `prd.md`、合并后的开发规格、设计系统和 API 方案重写计划，不保留过时任务。
- TODO 必须明确写出工具形态、主框架和框架映射。
- TODO 必须包含“多 Agent 需求拆解结果”，不能只写“实现核心功能”。
- TODO 应覆盖完整 MVP 开发计划。
- 预留“未完成目标 / 后续功能”章节。
- 模板须含 **§ 已完成模块（详见 prd/）**、**§ 开发进度**、**§ TODO 卸货记录** 占位（首版留空；后续见 `.codex/rules/todo-writeback.md` 与 `todo-prd-archive.md`）。
- 不要包含 `## 0. 用户确认` 章节。
- 写完后必须停止，向用户请求确认；确认前只能解释或修改 `prd.md` / `TODO.md` / `design-system/`。

交付提示：

```text
我已经把 PRD 的粗粒度 MVP 拆成了可开发规格，并整理好了设计系统、API 接入方案和 TODO.md。请确认：
1. TODO.md 中每个功能的子功能、页面/入口、数据来源、演示策略、状态和验收标准是否符合预期
2. design-system/<产品名>/MASTER.md 是否写清：用户画像适配、UI 技术栈、图标库（默认 lucide-react）、占位图/Unsplash 可选策略
3. prd.md 中的 API 使用方式是否符合预期
4. 主框架和平台能力规划是否正确

确认后我再使用 03-project-develop 开始首版开发；之后日常迭代用 project-iterate。
```

## TODO.md 模板

```markdown
# 开发计划

## 1. 项目框架
- 工具形态：<直接来自 prd.md 的工具形态>
- 主框架：<Next.js | Electron | vite-web-extension>
- 框架映射：网站 → Next.js；桌面软件 → Electron；浏览器插件 → vite-web-extension
- 选择理由：<结合 PRD 的一句话理由>
- Agent 启用矩阵：
  - 必选：mvp-requirement-analyst、project-architecture-planner、qa-acceptance-planner
  - 条件启用：<ui-interaction-planner | api-integration-planner | platform-capability-planner>
  - 未启用：<列出未启用 Agent 与原因>

## 已完成模块（详见 prd/）

> 首版留空。某 §2.x 功能全部 `[x]` 且经 project-verify 验证后，按 `.codex/rules/todo-prd-archive.md` 写入对应 `prd/<模块>/README.md` 和 `prd/<模块>/technical.md`，并在此追加索引；§2 中该块折叠为「已归档 → prd/<模块>/README.md」。

（暂无）

## 2. MVP 功能拆解

### 2.1 <功能名>
- 用户目标：<用户为什么需要它>
- 使用入口：<页面/窗口/插件入口/命令入口>
- 子功能：
  - [ ] <可开发子功能 1>
  - [ ] <可开发子功能 2>
- 主流程：
  1. <用户动作>
  2. <系统反馈>
  3. <完成结果>
- 状态要求：
  - 默认态：<要求>
  - 空态：<要求>
  - 加载态：<要求>
  - 成功态：<要求>
  - 错误态：<要求>
- 数据需求：<本地状态/本地存储/API 返回/用户配置>
- 数据来源：`LIVE` | `FIXTURE` | `EMPTY`（PRD 含「我的 xxx」→ 默认 LIVE，禁止 FIXTURE 冒充已连接）
- 演示策略：`LIVE_UNCONFIGURED` | `FIXTURE_DEMO` | `EMPTY_CTA`（可写 `LIVE + FIXTURE_DEMO`，但必须标明示例模式）
- FIXTURE 说明：<路径如 src/fixtures/xxx.ts、示例条数、是否显示「示例数据」角标；或 EMPTY 时的空态文案>
- 首屏可演示形态：<示例列表 | 未配置引导 | 空态 CTA>
- MVP 边界：<必须做什么>
- 暂不实现：<后续功能>
- 验收标准：
  - [ ] <可检查标准>
  - [ ] <可检查标准>

## 3. 界面与交互规格
- [ ] <入口/页面/窗口/popup/options/side panel/new tab：具体要展示和支持的操作>
- [ ] <核心组件与状态>
- [ ] <响应式或窗口尺寸要求>

## 4. 架构与模块边界
- [ ] 按主框架初始化或检查项目结构
- [ ] 建立基础布局、全局样式和核心入口
- [ ] 按模块实现：<模块 A>、<模块 B>、<模块 C>
- [ ] 数据对象：<核心数据对象>
- [ ] 状态流：<用户输入 → 处理 → 存储/API → 展示/反馈>
- [ ] 数据与演示汇总：各 §2 的数据来源（LIVE/FIXTURE/EMPTY）与演示策略（LIVE_UNCONFIGURED/FIXTURE_DEMO/EMPTY_CTA）已对齐；FIXTURE 集中路径 <src/fixtures/ 或 src/data/demo/>；禁止 JSX 内散落 mock
- [ ] 按工具形态配置密钥保存方式：网站/桌面软件使用环境变量或安全本地配置，浏览器插件使用 `chrome.storage.local` 或 PRD 指定的插件本地存储
- [ ] **（Electron 专用）** `npm create electron-vite@latest` 脚手架；`dev` 脚本为 `electron-vite dev --watch`；main dev 态 `loadURL(ELECTRON_RENDERER_URL)`；业务开发前先验收 renderer HMR / preload 刷新 / main 重启

## 5. 设计系统
- [ ] 读取 prd.md 与 ui-ux-pro-max，并在缺少 UI 设计风格时基于 PRD（含用户画像、场景故事）和界面规格推导设计取向
- [ ] 创建或更新 design-system/<产品名>/MASTER.md，且含必备章节：设计取向依据（含用户画像适配表）、UI 技术栈与组件策略、图标 Iconography、媒体与占位图、数据与演示内容约定、视觉 Token、关键界面状态
- [ ] MASTER 已写明图标库（React 栈默认 lucide-react）、尺寸 token、禁止 emoji 功能图标与多库混用
- [ ] MASTER 已写明占位图策略（默认 public/placeholders/ 或 SVG/渐变；Unsplash API/远程图源仅可选且有 Key、超时、大陆/失败回退说明）
- [ ] 将设计 token 与 UI 栈落地到所选框架（Tailwind、依赖与 MASTER 一致）
- [ ] 覆盖关键界面的默认态、空态、加载态、成功态、错误态和未配置态

## 6. API 与集成
- [ ] <如果需要 API：为每个确认调用的 API 建立安全封装>
- [ ] <如果需要 API：API 封装须含调用日志（入口、关键参数摘要脱敏、成功/失败与错误原因；不输出 Key/Token/隐私原文）>
- [ ] <如果需要 API：加入缓存、失败降级和错误提示>
- [ ] <如果需要 Unsplash API：仅在 PRD/MASTER 明确启用时接入，提供 IMAGE_PROVIDER=none|unsplash、UNSPLASH_ACCESS_KEY、超时、失败回退本地占位和署名/来源说明>
- [ ] <如果不需要 API：当前 MVP 使用本地状态/静态内容即可>
- [ ] 确保 API Key 不进入公开前端代码或插件包

## 7. 平台能力与权限
- [ ] <Electron：main/preload/renderer 边界，dev watch 与 ELECTRON_RENDERER_URL，或浏览器插件：manifest/permissions/入口>
- [ ] <本地文件/剪贴板/通知/storage/content script 等平台能力>
- [ ] <平台专项失败降级>

## 8. 验证
- [ ] 开发完成后运行 `project-verify` Skill，按 §2 验收标准逐条执行并回写打勾
- [ ] 运行 lint / test / 类型检查（由 project-verify 执行并记入验证记录）；`build` 不作为默认验证项，仅在发布/打包/构建产物验证时按需执行
- [ ] Web UI 的 §2 验收步骤与 `TESTING_CHECKLIST.md` 使用稳定 `data-testid` 定位（命名见 `project-verify/references/selector-and-testid.md`）；由 `03-project-develop` / `project-iterate` 实现时预埋，不由本阶段写业务代码
- [ ] 非 UI 逻辑（纯函数、数据转换、API/IPC/background、脚本）使用单测、集成测试、fixture、curl/CLI smoke 或日志证据验收（见 `project-verify/references/non-ui-verification.md`）
- [ ] 生成或更新 `TESTING_CHECKLIST.md` 与 `test-results/` 证据
- [ ] 验证空态、加载态、错误态和未配置态
- [ ] 按平台验证：Next.js 页面访问 / Electron dev 启动且三类刷新可用 / Chrome Extension 默认核对 manifest/入口与 popup/options 可预览；需要加载已解压扩展时再按需构建
- [ ] 列出失败/跳过项与下一步建议

## 9. 开发完成后更新 PRD
- [ ] 调用 update-prd Skill
- [ ] 基于实际代码创建或更新 prd/ 文档体系
- [ ] 对照原始 prd.md 总目标与 prd/ 已实现文档，把未完成差距写入本 TODO
- [ ] 将根目录 prd.md 归档为 prd.original.md（保留原始总目标；Agent 后续不读取，仅供人类回顾）
- [ ] 更新 `AGENTS.md`（如项目协议或文档入口发生变化），提示后续基于 TODO.md 继续任务

## 10. 未完成目标 / 后续功能
- [ ] 开发完成后由 update-prd 填写：来自原始 prd.md 但尚未在当前实现中完成的功能、差距原因和下一步任务

## 开发进度

> 每轮 `project-iterate` 或开发 session 结束前追加一条；规范见 `.codex/rules/todo-writeback.md`。

（首版尚未开始开发）

## TODO 卸货记录

> 每次将已完成块从 §2 归档到 `prd/` 时追加；规范见 `.codex/rules/todo-prd-archive.md`。

（暂无）
```

## 框架规划要求

### Next.js

- 使用 App Router、TypeScript 和 CSS 变量/Tailwind 对齐设计系统。
- API Key 只能由服务端 Route Handler 或 Server Action 从环境变量读取。
- 页面路由按 PRD 交互流程和 UI/交互规格组织。
- 如果 MVP 不需要远程 API，不要为了“架构完整”新增后端接口。
- **可机器验收**：§2 验收标准的主流程步骤须可被 `project-verify` + Playwright 执行（步骤具体、可观察）；`qa-acceptance-planner` 输出宜引用 `data-testid=` 或「对应 testid 见 `project-verify/references/selector-and-testid.md` 命名」；细则不写入本 Skill，见 `.codex/skills/project-verify/SKILL.md` 与相关 references。

### Electron

- 使用官方 npm 包 `electron`，当前推荐按大版本 30 规划：`package.json` 写 `electron: ^30.0.1`，以锁文件实际解析版本为准。
- 使用 Electron + Vite + TypeScript，**必须**采用 `electron-vite` 官方脚手架（`npm create electron-vite@latest`），不要规划手搓双 Vite 结构。
- TODO 中**必须**写明 dev 刷新要求：
  - `"dev": "electron-vite dev --watch"`（或在 `electron.vite.config.ts` 为 main/preload 开启 `build.watch`）
  - dev 态 main 使用 `process.env.ELECTRON_RENDERER_URL` 加载 renderer，禁止硬编码端口
  - 03 开发前先验收：renderer HMR、preload 改动能刷新、main 改动能重启 app
- TODO 中写明：`npm run dev`（开发）、`npm run preview`（仅预览前端，如有）；`npm run build` 仅打包/发布或构建产物验证时按需执行，不纳入默认验收。
- 系统能力、本地文件、环境变量密钥读取等只能放在主进程或安全 preload API 后面。

### vite-web-extension

- 使用 `JohnBra/vite-web-extension` 作为 Chrome Extension 起点。
- TODO 中写明需要哪些插件入口：popup、options、content script、background、side panel 或 new tab。
- 默认按 Chrome Manifest V3 规划，构建目标为 `dist_chrome`。
- 浏览器插件没有服务端后端，不得把私密 API Key 写进 `.env`、源码或构建包。
- 需要远程 API 时，默认规划为用户在 options/popup 中手动填写 API Key，并保存到 `chrome.storage.local`。
- background/service worker 只作为扩展后台脚本，不是服务端后端。

## 自检清单

- [ ] 已读取 `prd.md` 并提取工具形态。
- [ ] 已把工具形态映射到 Next.js、Electron 或 vite-web-extension。
- [ ] 已写出 Agent 启用矩阵。
- [ ] **已通过 Codex Subagent 能力并行委派必选 Agent**（不是主会话模拟）。
- [ ] 已按项目形态委派条件 Agent（或未启用并写明原因）。
- [ ] 已按 orchestration 合并规则整合全部专项 Agent 输出。
- [ ] 已将几个词级别的 MVP 功能拆成子功能、流程、状态、数据和验收标准。
- [ ] 未默认规划后端；只在确有 API、安全或同步需求时规划。
- [ ] 若 `prd.md` 缺少 `【UI 设计风格】`，已基于 PRD（含用户画像）、界面规格和工具形态选择设计系统方向，且 MASTER「用户画像适配」表可追溯。
- [ ] 已生成或更新设计系统，且 MASTER.md 含 UI 技术栈、图标 Iconography、媒体与占位图各一节。
- [ ] TODO §2 各功能已标注数据来源（LIVE/FIXTURE/EMPTY）和演示策略（LIVE_UNCONFIGURED/FIXTURE_DEMO/EMPTY_CTA）。
- [ ] 已按需写回 `【API 接入方案（待确认）】`。
- [ ] 已创建或更新 `TODO.md`（含 §「已完成模块」、§「开发进度」、§「TODO 卸货记录」占位）。
- [ ] 已停止在计划阶段，没有写业务代码、安装依赖或初始化框架。
