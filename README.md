# CodeNow

本仓库在 `.agents/` 下提供一组 **Cursor Agent Skills**（每个技能对应一个目录里的 `SKILL.md`），用于把「产品想法」一路推进到「可运行的 vibecoding 项目」。

## Skills 一览

路径均在 `.agents/skills/`：

| 目录 | 技能名（YAML `name`） | 作用简述 |
|------|----------------------|----------|
| `01-mvp-prd-builder/` | `01-mvp-prd-builder` | 用 **6 道递进选择题** 把想法落成仓库根目录 **`prd.md`**（可选追加 UI 参考图后的设计章节） |
| `02-project-prepare/` | `02-project-prepare` | 读 **`prd.md`**，选框架、生成 **`design-system/`**、写 **`【API 接入方案】`** 到 `prd.md`、生成 **`TODO.md`**；**不写业务代码**，做完停在你确认前 |
| `03-project-develop/` | `03-project-develop` | 在用户确认 **`TODO.md`** 后按 TODO 实现代码；完成后安装依赖、验证、调用 **`update-prd`** 维护 `prd/`、更新根目录 **`README.md`** |
| `ui-ux-pro-max/` | `ui-ux-pro-max` | UI/UX 设计知识库；**被 02、03 在流程中读取**，也可单独用于界面评审、配色与组件规范 |
| `update-prd/` | `update-prd` | 维护 **`prd/`** 下结构化 PRD，与代码实现同步；**03 开发结束时会调用** |
| `git-commit/` | `git-commit` | 按 **Conventional Commits** 分析 diff、生成说明并执行 `git commit`；需要提交时用 |

## 推荐先后顺序（主流程）

整体是 **一条流水线**，不要跳过「准备」直接开发：

```text
01-mvp-prd-builder  →  02-project-prepare  →  【你确认 TODO.md】→  03-project-develop
         ↓                      ↓                              ↓
     prd.md              design-system/                    可运行代码
                        TODO.md + prd.md API 段落              + prd/ + README
```

1. **`01-mvp-prd-builder`**  
   - 触发：有大致产品想法，或只说「生成 PRD」等。  
   - 产出：根目录 **`prd.md`**（含工具形态、MVP、流程等；可选 UI 章节）。  
   - 说明：若只唤起技能没说想法，技能会先引导你补一句产品描述，再进入 6 题。

2. **`02-project-prepare`**  
   - 触发：已有 **`prd.md`**，要从 PRD 生成可执行计划。  
   - 产出：**`design-system/<产品名>/MASTER.md`**、更新 **`prd.md`** 中的 API 方案段落、根目录 **`TODO.md`**。  
   - 约束：**不写业务代码**；写完会请你确认，确认后再进入下一步。  
   - 内部会读取 **`ui-ux-pro-max`** 补齐设计系统工程细节。

3. **（人工）确认 `TODO.md`**  
   - 与 Agent 说明：确认范围、框架（Next.js / Electron / vite-web-extension）无误后再开发。

4. **`03-project-develop`**  
   - 触发：已确认 **`TODO.md`**，要求开始写代码、实现 MVP。  
   - 依据优先级：**`TODO.md`**（任务与框架）→ **`design-system/`**（视觉与交互细节）→ **`prd.md`**（产品范围）；**`ui-ux-pro-max`** 作质量与工程准则，不覆盖设计系统里的已定稿。  
   - 收尾：依赖与验证、**`update-prd`** 同步 **`prd/`**、更新项目 **`README.md`**。

## 辅助技能何时用

- **`ui-ux-pro-max`**：主流程里由 02/03 自动用到；你也可在改界面、选风格、做体验评审时直接 @ 该技能。  
- **`update-prd`**：大改版、长期维护时，可单独要求「按实现更新 `prd/`」；正常走 03 也会触发。  
- **`git-commit`**：需要规范提交时（例如说「按约定式提交 commit」或 `/commit`）。

## 在 Cursor 里怎么「用」这些 Skills

1. 在 Cursor 中把本仓库（或包含 `.agents/skills` 的路径）作为工作区，确保 Agent 能读到对应 **`SKILL.md`**。  
2. 用自然语言说明阶段即可，例如：  
   - 「按 **01-mvp-prd-builder** 帮我从想法生成 `prd.md`」  
   - 「**02-project-prepare**，根据当前 `prd.md` 更新 TODO 和设计系统」  
   - 「**03-project-develop**，TODO 已确认，开始实现」  
3. 若你的 Cursor 通过「技能列表」绑定路径，请将 `.agents/skills/<技能目录>` 指向各技能的 **`SKILL.md`**（以 Cursor 当前版本的 Skills 配置方式为准）。

## 产物与目录速查

| 产物 | 说明 |
|------|------|
| `prd.md` | 仓库根目录产品说明；02 会追加 API 方案段落 |
| `TODO.md` | 开发合同；03 严格按此执行 |
| `design-system/` | 项目设计系统（如 `MASTER.md`） |
| `prd/` | 与代码对齐的模块化 PRD（由 `update-prd` 维护） |

更细的步骤、约束与交付要求以各目录下的 **`SKILL.md`** 为准。
