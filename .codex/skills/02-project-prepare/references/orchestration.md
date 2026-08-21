# Project Prepare Orchestrator（主会话合并规则）

## 定位

**这不是 Agent，不要委派。** 它是主会话使用的合并规则文档，不是 worker。

本文件定义：在收集全部专项 Agent 输出后，如何合并成一份无冲突、可写入 `TODO.md` 的统一开发规格。

**谁读它：** 执行完整 prepare 流程的主会话（通常是 `02-project-prepare`）。其它 Skill 若并行委派多个专项 Agent 后需要合并规格，也可读取本文件，但日常单点补规格不必经过完整 orchestration 流程。

## 主会话职责（Orchestrator 角色）

主会话在委派专项 Agent 之前和之后分别负责：

**委派前：**
- 读取 `prd.md`，提取工具形态、产品目标、MVP 功能
- 判断 Agent 启用矩阵（必选 + 条件启用 + 未启用及原因）
- 映射主框架：Next.js / Electron / vite-web-extension
- 并行委派所有已启用的专项 Agent

**专项返回后（按本文件合并规则）：**
- 收集各专项 Agent 的标准化输出
- 去重、消冲突
- 形成统一开发规格
- 驱动设计系统、API 方案写回和 `TODO.md` 生成

## Agent 启用矩阵判断

### 必选（始终委派）

- `mvp-requirement-analyst`
- `project-architecture-planner`
- `qa-acceptance-planner`

### 条件启用

| Agent | 启用条件 |
|---|---|
| `ui-interaction-planner` | 网站、桌面软件、浏览器插件（通常有可视入口）；或 PRD 描述页面/窗口/表单/列表/设置 |
| `api-integration-planner` | PRD/API 文档涉及远程 API、AI、Token、鉴权、同步、第三方服务 |
| `platform-capability-planner` | 桌面软件、浏览器插件；或 PRD 涉及本地文件、剪贴板、通知、manifest、权限、content script |

如果当前 Codex 客户端未加载某个项目级 Profile，主会话不得跳过对应专项视角：由主会话按同一规范完成，并在 TODO 的 Agent 启用矩阵中记录降级原因。

### 默认不启用

- 纯展示型网站且无浏览器特殊权限 → 可不启用 `platform-capability-planner`
- MVP 完全本地、无远程服务 → 不启用 `api-integration-planner`

## 合并规则

按「开发者需要知道什么才能稳定实现」合并，**不要**按 Agent 名称堆叠原始输出。

### 1. 去重

- 同一功能点在需求、UI、架构、QA 中重复出现时，保留最具体、可执行的描述
- 相同验收标准只保留一份
- 架构模块与 UI 入口对齐，合并为「入口 + 模块 + 验收」三元组

### 2. 冲突处理

| 冲突类型 | 裁决规则 |
|---|---|
| 产品范围 | 以 `prd.md` 的目标和用户路径为准 |
| 技术路线 / 框架 | 以工具形态和 `02-project-prepare` 框架映射为准 |
| 安全策略 | 选更严格且符合平台约束的方案 |
| UI vs 架构入口 | 以 UI Agent 的用户入口为准，架构 Agent 负责实现边界 |
| API 必要性 | 以 API Agent 的 MVP 必要性判断为准；无 API Agent 时主会话按 PRD 判断 |

### 3. 合并顺序

1. **需求拆解** → 功能清单、子功能、流程、状态、数据、边界（骨架）
2. **架构** → 模块、入口、数据流、安全边界（工程结构）
3. **UI/交互** → 界面入口、组件、状态（用户可见层）
4. **API/集成** → API 清单、鉴权、降级（如有）
5. **平台能力** → 权限、生命周期、平台验证（如有）
6. **QA** → 验收标准覆盖以上全部，补异常和验证命令

### 4. 输出质量门槛

合并后的规格必须满足：

- 每个 MVP 功能有：入口、子功能、流程、状态、数据、验收标准
- 粗关键词没有原样作为唯一 TODO 项
- 未默认规划后端（除非 PRD/API 明确需要）
- 浏览器插件没有把 background 描述成服务端
- 可直接映射到 `TODO.md` 模板各章节

## 统一开发规格结构

主会话合并后应产出以下内部结构（不必单独写文件，供写 TODO 使用）：

```markdown
## 合并开发规格

### 项目框架
- 工具形态 / 主框架 / 选择理由 / Agent 启用矩阵

### 功能拆解（来自 mvp-requirement-analyst，经 UI/架构补充）
### 界面与交互（来自 ui-interaction-planner，如有）
### 架构与模块（来自 project-architecture-planner）
### API 与集成（来自 api-integration-planner，如有）
### 平台能力（来自 platform-capability-planner，如有）
### 验收与验证（来自 qa-acceptance-planner，覆盖全部上文）
```

## 不负责

- 不委派其他 Agent
- 不实现产品代码、不安装依赖、不运行脚手架
- 不把多个 Agent 原始输出直接拼接进 TODO.md
- 不扩大 PRD 的 MVP 范围

## 验收标准

- [ ] Agent 启用矩阵已写入 TODO 第 1 节。
- [ ] 全部已启用专项 Agent 的输出已合并，无重复段落。
- [ ] 冲突已按规则裁决，无未解决的矛盾描述。
- [ ] 合并规格可直接填入 TODO.md 模板。
- [ ] 未写业务代码、未安装依赖。
