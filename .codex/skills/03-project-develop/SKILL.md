---
name: 03-project-develop
description: 首版 MVP 专用：按 TODO.md、prd.md、design-system/ 搭建并交付可运行 TypeScript 项目（Next.js/Electron/Chrome Extension），含全量 project-verify、update-prd 与 README。已有代码库的日常迭代请用 project-iterate，不要用本 Skill。
---

# Project Develop：TODO.md → 框架实现 → 依赖安装 → 验证 → 重建 prd/ 与 README.md → 交付指引

## 首版 MVP 专用

本 Skill 面向**第一次**把项目做成可运行 MVP：脚手架、全量实现、依赖安装、**全量** `project-verify`、`update-prd`、README 与协作文件。

**已有代码库的日常迭代**（继续 TODO、修 bug、小功能）请用 **`project-iterate`**，不要每次唤起本 Skill。

| 场景 | 用哪个 |
| --- | --- |
| 首版 MVP、尚无 `prd/` | **本 Skill（03）** |
| 日常改代码、做 TODO 下一项 | **`project-iterate`** |
| 日常聊新想法、尚未进 TODO | **`product-discovery`** |

## 概述

本 Skill 负责把计划落成可运行项目。它以 `TODO.md` 为开发合同，以 `prd.md` 为简版产品依据，以仓库根目录 `design-system/` 为完整设计依据，并调用 `ui-ux-pro-max` Skill 辅助 UI/UX 落地。按 TODO 中声明的主框架执行：Next.js、Electron 或 vite-web-extension。开发完成后，必须安装/确认依赖、运行验证、调用 `update-prd` 创建或重建仓库根目录 `prd/` 文档体系，创建或更新仓库根目录 `README.md`，并向用户说明如何运行或安装成可使用的工具。

## TypeScript（硬约束）

首版开发默认使用 **TypeScript**。除非用户明确要求沿用既有 JavaScript 项目，否则新建、补齐或重写的前端、API、Electron main/preload、扩展 background/content/options/popup 代码都应使用 `.ts` / `.tsx`，并保留类型检查入口。

- Next.js：使用 App Router + TypeScript，页面、组件、Route Handler、服务封装优先 `.tsx` / `.ts`。
- Electron：使用 Electron + Vite + TypeScript，main、preload、renderer 与 `electron.vite.config.ts` 保持 TypeScript 结构。
- vite-web-extension：使用 React + TypeScript + Tailwind，Manifest V3 入口、background/service worker、content script 与 UI 入口使用 TypeScript。
- 验证阶段必须运行项目已有类型检查；若没有专门 script，优先补 `typecheck` 或使用 `tsc --noEmit`。

如果项目还没有 `TODO.md`、TODO 未写明主框架，或用户还没确认开发范围，先使用 `project-prepare` 准备计划，不要自行跳过计划阶段。

`TODO.md` 应由 `02-project-prepare` 在开发前生成。开发完成后，本 Skill 只负责更新 TODO 的完成状态，并把 `prd.md` 原始总目标中尚未实现的功能追加或更新到“未完成目标 / 后续功能”章节。

交付不是只把代码写完，还要让用户知道下一步怎么启动、配置和使用；尤其是浏览器插件、Electron 桌面端和需要 API Key 的项目，若不安装依赖、不给安装入口和运行说明，用户会停在“代码存在但工具不可用”的状态。

## 开发依据优先级

- `TODO.md`：开发合同，决定主框架、阶段任务、页面/入口范围、API 接入范围和验证要求。
- `prd.md`：简版产品说明，只用于确认产品目标、核心功能、用户路径和 API 方案，不作为完整视觉设计来源。
- `design-system/`：完整设计系统来源。所有颜色、字体、间距、圆角、阴影、组件气质、布局密度、响应式规则、**UI 技术栈（Tailwind/组件库）、图标库、占位图策略**和页面级设计约束，只读取并遵循 `design-system/` 下的内容。
- `ui-ux-pro-max`：必须调用/读取该 Skill 作为 UI/UX 工程落地和质量检查准则，但不能覆盖 `design-system/` 中的具体设计决定。

若 `prd.md`、`TODO.md` 和 `design-system/` 冲突，优先级为：`design-system/` 决定视觉与交互细节，`TODO.md` 决定开发任务与框架，`prd.md` 决定产品范围。不要从 `prd.md` 临时推断或补写完整设计系统。

## 渐进式加载（Progressive Disclosure）

主 `SKILL.md` 只保留**所有框架通用**的流程；框架细节放在 `references/`，**按 TODO 主框架只读对应一份**，不要一次读完全部 reference。

| TODO 主框架 | 开发第二步必须读取 |
| --- | --- |
| Next.js | `references/nextjs.md` |
| Electron | `references/electron.md` |
| vite-web-extension | `references/vite-web-extension.md` |

**始终读取**（与框架无关）：

- `references/logging-and-debugging.md` — 写 API / IPC / 第三方请求代码前读一遍，写完后按自检核对。
- `references/assets-data-and-fixtures.md` — 实现列表/卡片数据、LIVE/FIXTURE/EMPTY、占位图、Unsplash 可选接入、安装 `lucide-react` 等 icon 依赖前读一遍。

Reference 仅一层深度：从本 `SKILL.md` 直接链接，不要再嵌套引用。

## 调用日志（必做，不可省略）

涉及 **API 调用、IPC、第三方服务、降级/重试** 的代码，必须增加调用日志。这是 03 开发的硬约束，与仓库根目录 `AGENTS.md` 一致；**不能**因为「功能已写完」而跳过。

最低要求（每条调用链）：

- 入口 log：模块名 + 关键参数摘要（mode、id、**输入长度**，不是原文）
- 成功 log：结果摘要 + 耗时
- 失败 log：`console.error` + 错误原因（不含 Key/隐私）

禁止：输出 API Key、Token、用户隐私原文。

详细模板与示例见 **`references/logging-and-debugging.md`**。自检清单里必须有「API/IPC 路径已打日志」一项。

## 按需复用 Specialist Agents

开发过程中若 `TODO.md` 规格不足，**可**委派项目级 Agent（不限于本 Skill 独占）：

| 缺口 | 建议委派 |
| --- | --- |
| TODO §2 只有关键词、缺子功能/流程/状态 | `mvp-requirement-analyst` → 补写后更新 TODO |
| 大改模块、新增 Route/IPC | `project-architecture-planner` → 更新 TODO §4 |
| 新页面/入口、缺 UI 细节 | `ui-interaction-planner` → 更新 TODO §3 |
| 新增远程 API / 改鉴权 | `api-integration-planner` → 更新 prd + TODO §6 |
| Electron/插件平台能力 | `platform-capability-planner` → 更新 TODO §7 |
| 新功能无验收标准 | `qa-acceptance-planner` → 更新 TODO §2 |

单点补规格时：**不必**走完整 prepare 并行编排；委派对应 Agent → 主会话写回 TODO 相关章节即可。完整多 Agent 合并读取 `.codex/skills/02-project-prepare/references/orchestration.md`。

## 执行流程

### 第一步：开发前检查

- **意图判断**（本条消息）：用户明显只在答疑/讨论 → 只解释不改仓库；否则按 TODO 推进，遇到会改变产品范围或安全边界的歧义再暂停确认。
- 读取仓库根目录 `TODO.md` 和 `prd.md`。
- 从 `TODO.md` 提取：**主框架**、工具形态、阶段任务、页面/入口范围、API 接入范围、各 §2 **数据来源与演示策略**、包管理器、安装/启动/构建/验证命令。
- 根据主框架读取对应 reference（见上文「渐进式加载」表）、`references/logging-and-debugging.md` 与 `references/assets-data-and-fixtures.md`。
- 读取仓库根目录 `design-system/` 下的设计系统文档；优先读取 `design-system/<产品名>/MASTER.md`，再按需读取 `design-system/<产品名>/pages/*.md` 或其他局部规则。
- **校验 MASTER.md 必备章节**（02 应已写好；缺则暂停并补 MASTER 或委派 `ui-interaction-planner`，禁止从 `prd.md` 临时猜 UI 栈）：
  - 设计取向依据（含用户画像适配表）
  - UI 技术栈与组件策略
  - 图标 Iconography（含库名、如 `lucide-react`）
  - 媒体与占位图
- 设计系统只从 `design-system/` 读取。`prd.md` 是简单版本，不要把 `prd.md` 中的 UI 风格文字当作完整设计系统，也不要用它覆盖 `design-system/`。
- 读取/调用 `.codex/skills/ui-ux-pro-max/SKILL.md`。
- 若 `design-system/` 缺失或没有可用设计系统文档，暂停并要求先补齐设计系统，不要直接从 `prd.md` 推断完整 UI。
- 查看现有项目结构、`package.json`、锁文件和 `git status`，尊重用户已有改动。
- 如果 TODO 与 PRD 冲突，以 PRD 的产品目标为准，并把必要调整写回 TODO。

### 第二步：按框架开发

- 开发 UI 时必须同时对照 `design-system/` 和 `ui-ux-pro-max`：前者给出本项目的具体设计，后者用于检查可访问性、控件选择、布局密度、响应式、状态反馈和交互质量。
- **UI 技术栈与依赖**：`package.json` 中的 Tailwind、Radix/shadcn、**图标库**（默认 `lucide-react`）、图表库（仅 MASTER 写明时安装）须与 `MASTER.md`「UI 技术栈」「图标 Iconography」一致；禁止临时改用 Phosphor/Heroicons 或其他库。
- 不要新增与 `design-system/` 不一致的配色、字体、圆角、阴影、卡片风格或装饰元素；缺失的工程细节可用 `ui-ux-pro-max` 补齐，但要保持克制并贴合 `design-system/`。
- **按 TODO 主框架执行**（细节在 reference，此处不重复）：
  - **Next.js** → 读并遵循 `references/nextjs.md`
  - **Electron** → 读并遵循 `references/electron.md`（含 dev watch / HMR 验收）
  - **vite-web-extension** → 读并遵循 `references/vite-web-extension.md`
- 新建或补齐源码时遵循上文 TypeScript 硬约束；发现脚手架默认生成 `.js` / `.jsx` 时，应改为 `.ts` / `.tsx` 并更新配置、脚本和类型检查。
- 实现任何 API / IPC / 第三方请求前，先读 `references/logging-and-debugging.md`，写完后按其中自检项核对。

### 第三步：按 TODO 分阶段实现

- 按 `TODO.md` 的章节顺序开发。
- **数据与可演示内容**（见 `references/assets-data-and-fixtures.md`）：
  - 按 §2「数据来源 / 演示策略」实现：`FIXTURE` → 集中路径 + 可选「示例数据」标识；`LIVE` → 未配置态；`LIVE + FIXTURE_DEMO` → 示例模式必须明示；`EMPTY` → 空态 + CTA。
  - 首屏须可感知：示例数据、未配置引导或空态之一，且与数据来源/演示策略一致；禁止无说明的 JSX 内硬编码 mock。
  - **占位图**：按 MASTER「媒体与占位图」；本地 fallback；Unsplash/远程图源仅在 MASTER/TODO 明确启用时接入，并须处理超时、失败态和大陆/离线默认关闭。
  - **图标**：仅用 MASTER 指定库；纯图标按钮带 `aria-label`。
- 同一用户请求若覆盖多个 TODO 子项，本会话尽量连续完成；仅阻塞时写回 TODO。
- 每完成一个阶段，**立即**更新对应 checkbox；不要等全部做完再统一改 TODO。
- 若某项无法完成，保留未勾选并在条目下写**进度 / 阻塞 / 下步**（格式见 `.codex/rules/todo-writeback.md`）。
- 若发现 TODO 缺少必要工程任务，可以补充到对应章节，但不要扩张 PRD 未要求的产品范围。
- **会话结束前**（含用户中断、上下文将满）：必须回写 TODO，再结束回复。

### 第四步：项目配置、gitignore 与密钥文件

- 创建或更新仓库根目录 `.gitignore`，至少覆盖当前框架的构建产物、依赖目录、缓存、日志、系统文件和本地密钥文件。
- `.gitignore` 必须包含：`node_modules/`、构建输出（如 `.next/`、`dist/`、`dist_chrome/`、`build/`、`out/`）、日志、缓存、`.DS_Store`；若当前框架使用环境变量，还必须包含 `.env`、`.env.local`、`.env.*.local`。
- 只有 Next.js 网站或 Electron 桌面软件使用 API 文档里的 API 时，才创建 `.env.local.example` 和 `.env.local`。
- `.env.local.example` 写入变量名和占位说明；`.env.local` 写入同样变量名，但不得编造真实 Key，可使用 `MINIMAX_API_KEY=这里粘贴你的_Token_Plan_API_Key` 这类占位值。
- 如果 Next.js/Electron 项目运行时明确读取 `.env` 而不是 `.env.local`，也创建 `.env`，并保持 `.gitignore` 覆盖它。
- 浏览器插件使用 API 文档里的 API 时，不创建 `.env` 或 `.env.local` 作为默认方案；必须实现 options/popup 中的 Key 输入、保存、读取和清除能力，并把 Key 保存在 `localStorage` / `chrome.storage.local` 这类插件本地存储。
- 在最终回复中按实际框架提示用户保存 API Key：Next.js/Electron 写入本地环境变量；Chrome Extension 进入扩展的 options/popup 填写并保存到 `localStorage` / `chrome.storage.local` 这类插件本地存储。

Token Plan 提示文案：

````markdown
1. **订阅 Token Plan**  
   打开 [Token Plan](https://platform.minimaxi.com/subscribe/token-plan?code=JBlROVn3gJ&source=link)，选择套餐并完成支付。

2. **复制 Key**  
   订阅生效后，进入 [用户中心 → Token Plan / 支付与套餐](https://platform.minimaxi.com/user-center/payment/token-plan)，在套餐详情中复制 **Token Plan API Key**。

3. **保存 Key**  
   - Next.js / Electron：在项目根目录新建或打开 `.env.local`（与运行代码的目录一致即可），填入你从控制台复制的 Key，不要加引号、不要多空格：

     ```env
     MINIMAX_API_KEY=这里粘贴你的_Token_Plan_API_Key
     ```

   - Chrome Extension：加载扩展后打开 options/popup，把 Key 粘贴到 API Key 输入框并保存到 `localStorage` / `chrome.storage.local` 这类插件本地存储；不要创建或编辑 `.env.local`。
````

### 第五步：API 与数据安全

- 为每个确认调用的 API 建立独立服务封装。
- 加入失败降级、加载状态、错误提示和必要缓存。
- **每个 API / IPC / background 请求封装必须按 `references/logging-and-debugging.md` 添加日志**（入口、摘要、成功/失败、耗时；脱敏）。
- Web：密钥只在服务端环境变量中。
- Electron：密钥只在主进程读取的环境变量或用户本地安全配置中。
- Chrome Extension：密钥由用户在扩展界面显式填写，保存到 `localStorage` / `chrome.storage.local` 这类插件本地存储；background/service worker 读取后发起请求，content script 不直接持有密钥。

### 第六步：依赖安装与本地预览准备

- 根据锁文件、`packageManager` 字段和既有脚本选择包管理器：优先沿用项目已有选择；常见顺序为 `pnpm-lock.yaml` → `pnpm`，`yarn.lock` → `yarn`，`bun.lockb` / `bun.lock` → `bun`，`package-lock.json` → `npm`；都不存在时默认 `npm`。
- 如果新增或修改了 `package.json` 里的 `dependencies`、`devDependencies`、`scripts`，或当前项目缺少可用的 `node_modules/`，必须运行对应安装命令并让锁文件与 `package.json` 保持一致。
- 不要跳过依赖安装去做“看起来完成”的验证；依赖安装失败时，先判断是否是网络、权限或沙箱限制，按当前环境请求授权后重试。若仍无法安装，在最终回复中说明阻塞原因，并给出用户可直接执行的精确安装命令。
- Monorepo 或多包项目中，只在实际运行应用的包目录安装和验证；若根目录工作区统一管理依赖，则在根目录执行安装。
- 安装依赖后，按项目脚本启动本地预览或开发服务；如果已有服务占用端口，换可用端口并在最终回复中写明实际 URL。

### 第七步：验证

- 读取并执行 `.codex/skills/project-verify/SKILL.md`。**按 TODO §2 验收标准逐条验证并回写打勾**，不要只做 lint/test/typecheck 后口头说「手动走查通过」。
- 默认验证运行 lint / test / 类型检查；`build` 不作为默认验证项，仅在用户明确要求、发布/打包、验证构建产物或浏览器插件加载目录时按需执行。
- 若 project-verify 因阻塞（lint/test/typecheck 失败、服务起不来）无法继续，先修复 03 引入的问题并重跑 project-verify；无法修复时在最终回复说明，且不得无证据勾选 §2 验收标准。
- 交付 MVP Web UI 前，为 `project-verify/references/selector-and-testid.md` 范围内的可交互元素预埋 `data-testid`；动态验收方式见 `project-verify/references/browser-playwright.md` 与对应框架 reference。缺 testid 不得无证据勾选 §2。

### 第八步：调用 update-prd 重建 prd/ 与 TODO

开发、依赖安装、**project-verify** 和 TODO 收尾完成后：

1. 读取 `.codex/skills/update-prd/SKILL.md`。
2. 明确向 `update-prd` 声明本次任务：创建仓库根目录 `prd/` 文件夹；读取整个项目；基于实际代码重新构建 `prd/` 文件夹里的 PRD 文档，而不是只局部修补根目录 `prd.md`。
3. 读取整个项目时必须覆盖产品代码、路由/入口、组件、状态与数据模型、API 封装、配置文件和构建脚本；跳过 `.git/`、`node_modules/`、`.next/`、`dist/`、`build/`、覆盖率产物、日志、缓存和密钥文件。
4. 若 `prd/` 不存在，先创建；若已存在，读取旧文档作为参考，但以当前代码实现为准重建内容，移除过时描述。
5. 按 `update-prd` 的当前结构为每个核心模块生成或更新 `prd/<module>/README.md`、`prd/<module>/technical.md` 和必要的 `sync.json`；产品能力写 README，代码入口、数据结构、调用链、日志、测试和边界情况写 technical。
6. 在 `prd/README.md` 维护总览和模块索引，说明产品整体结构、模块划分、入口路径、数据流和模块文档之间的关系。
7. 把根目录 `prd.md` 当作原始总目标，不把其中未实现的功能写进 `prd/` 的已实现描述。
8. 对比原始 `prd.md` 与新生成的 `prd/` 文档体系，把未实现、部分实现、降级实现或实现方式变化的功能写入 `TODO.md` 的“未完成目标 / 后续功能”章节。
9. 若最终实现与根目录 `prd.md` 中的 `【API 接入方案（待确认）】` 不同，在 `prd/` 的相关文档中说明最终方案与原因，并把仍需补齐的 API 能力写入 `TODO.md`。
10. 按需更新仓库根目录 `AGENTS.md`，使其继续说明后续任务以 `TODO.md` 为准；不要创建或维护平行的工具专属指令文件。
11. 在 `prd/`、`TODO.md` 和 `AGENTS.md` 完成后，按 `update-prd` 规则将根目录 `prd.md` **重命名**为 `prd.original.md`（不删除内容）。后续 Agent 以 `prd/` 表示当前已实现产品文档，以 `TODO.md` 表示继续开发计划；**不得**再把 `prd.original.md` 当作开发依据读取。
12. 更新 `TODO.md`：完成项打勾，未完成项保留并注明原因。
13. 若 TODO 已很长且多模块已验收闭环，可按 `.codex/rules/todo-prd-archive.md` 将已完成块卸货到 `prd/` 并精简 TODO（可与本步 update-prd 全量一并做，或留给后续 `project-iterate`）。

调用 `update-prd` 时使用类似下面的任务声明：

```text
请创建或更新仓库根目录 prd/ 文件夹，读取整个项目代码与配置，基于当前实际实现重新构建 prd/ 下的模块文件夹文档体系：prd/README.md、prd/<module>/README.md、prd/<module>/technical.md 和必要的 sync.json。根目录 prd.md 是原始总目标，不代表全部已完成；请对比 prd.md 与 prd/ 已实现文档，把尚未实现、部分实现、降级实现或实现方式变化的功能写入 TODO.md 的“未完成目标 / 后续功能”章节。按需更新 AGENTS.md，说明后续基于 TODO.md 继续任务，并明确 Agent 不得读取 prd.original.md 作为开发依据。完成 prd/、TODO.md 和 AGENTS.md 后，将根目录 prd.md 重命名为 prd.original.md。
```

### 第九步：生成根目录 README.md

在 `prd/` 文档体系重建、`TODO.md` 收尾后，必须创建或更新仓库根目录 `README.md`。README 面向项目使用者和后续开发者，必须基于当前实际代码、脚本和配置生成，不要从模板臆测不存在的能力。

README 至少包含：

- 产品名称、简短介绍和核心功能列表；只写已经实现的功能。
- 技术栈、运行环境和实际包管理器。
- 安装、开发启动、验证命令，以及构建/打包命令（如有，标注按需）；命令必须来自当前 `package.json` 的 scripts 或本次实际执行过的命令。
- 项目目录结构概览，列出主要入口、组件、服务/API 封装、配置和 `prd/` 文档位置。
- 使用说明：Next.js 写访问 URL；Electron 写开发启动与按需打包方式；Chrome Extension 写按需构建、加载已解压扩展的步骤和实际入口。
- 若项目需要 API Key 或本地配置，说明保存位置和占位格式，不得写入真实密钥；Chrome Extension 说明在 options/popup 中保存到 `localStorage` / `chrome.storage.local` 这类插件本地存储。
- 文档索引，链接到根目录 `TODO.md`、`AGENTS.md` 和 `prd/` 下的总览文档。可注明 `prd.original.md` 为归档的原始总目标（仅供人类回顾），**不要**把它列为 Agent 的开发文档入口；根目录不应再保留活跃的 `prd.md`。

如果 README 已存在，读取旧内容作为参考，但以当前实现为准更新，移除过时功能、错误命令和不再存在的路径。

### 第十步：最终交付说明

最终回复必须让用户能从当前仓库继续操作，不只汇报“代码已完成”：

- 说明已完成哪些开发、依赖是否已安装、验证命令与结果、`prd/` 重建了哪些文档、根目录 `README.md` 与 `AGENTS.md` 是否已创建或更新、**`TODO.md` 还剩什么（含 §10 与开发进度中的阻塞项）**。
- 列出实际使用的包管理器和关键命令；命令必须来自当前 `package.json` 的 scripts 或本次实际执行过的命令，不要编造不存在的脚本。
- 给出项目运行方式：Next.js 说明启动命令和实际访问 URL；Electron 说明 `npm run dev`（须为 `electron-vite dev --watch` 或等效 watch 配置）、三类开发刷新差异（renderer HMR / preload 刷新 / main 重启）和 `npm run preview`（如有）；`npm run build` 仅作为打包/发布或构建产物验证的按需命令说明；普通 Web/Vite 项目说明预览或开发服务 URL。
- 浏览器插件如需安装到 Chrome，必须给出按需构建与安装步骤：运行构建命令生成实际输出目录（默认 `dist_chrome`，以项目真实配置为准），打开 `chrome://extensions/`，开启「开发者模式」，点击「加载已解压的扩展程序」，选择该输出目录；后续修改代码后仅在需要更新已加载扩展时重新构建，并在扩展管理页点击刷新。该构建不属于默认验收项。
- 如果插件包含 popup、options、side panel、content script 或 new tab，说明用户应从哪个入口开始使用；只写本项目实际存在的入口。
- 若项目需要 API Key，提醒用户按实际框架保存：Next.js/Electron 写入 `.env.local` 或项目实际读取的本地配置文件；Chrome Extension 在 options/popup 中填写并保存到 `localStorage` / `chrome.storage.local` 这类插件本地存储。
- 若因网络、权限或用户环境无法安装依赖、启动服务或加载插件，清楚说明未完成项、原因和用户下一步要执行的命令。

## 自检清单

- [ ] 已读取 `TODO.md`、`prd.md` 和 `design-system/`。
- [ ] 已调用/读取 `ui-ux-pro-max` Skill 辅助 UI/UX 落地。
- [ ] 已确认 `prd.md` 只作为简版产品说明，完整设计只来自 `design-system/`。
- [ ] 已识别主框架，并读取对应 `references/<框架>.md`、`references/logging-and-debugging.md` 与 `references/assets-data-and-fixtures.md`。
- [ ] 新建或补齐的源码默认使用 TypeScript（`.ts` / `.tsx`），并已确认类型检查入口可用。
- [ ] `MASTER.md` 含 UI 技术栈、图标 Iconography、媒体与占位图；实现与 MASTER 一致（默认 `lucide-react`，无多库混用）。
- [ ] §2 数据来源与演示策略已落地（FIXTURE 集中路径 / LIVE 未配置态 / LIVE+FIXTURE_DEMO 明示示例模式 / 无静默 mock）。
- [ ] 占位图离线可渲染或有失败 fallback；关键图有 `alt`。
- [ ] 已按 TODO 分阶段实现，且**每阶段**已回写 checkbox（含未完成/阻塞说明）
- [ ] 会话结束前已按 `.codex/rules/todo-writeback.md` 更新 TODO（禁止 silent drift）
- [ ] **所有 API Route、LLM 封装、IPC handler、background fetch 已加 enter/success/fail 日志，且无 Key/隐私泄露。**
- [ ] 已创建或更新 `.gitignore`。
- [ ] 若 Next.js/Electron 使用 API 文档里的 API，已创建 `.env.local.example` 和 `.env.local`，并提示 Token Plan 获取 Key 流程。
- [ ] 若 Chrome Extension 使用 API 文档里的 API，未创建 `.env` / `.env.local` 作为默认方案，已实现 options/popup 的 Key 输入、`localStorage` / `chrome.storage.local` 插件本地存储、读取和清除能力。
- [ ] 已保护 API Key，不进入公开前端代码或插件包。
- [ ] 已安装/确认依赖并保持锁文件与 `package.json` 一致；若未能安装，已说明原因和用户可执行命令。
- [ ] 已运行 `project-verify`，§2 验收标准与 §8 验证项已按证据回写 TODO（无无证据打勾）
- [ ] 若是 Electron：`package.json` 的 `dev` 已含 `electron-vite dev --watch` 或 config 已开 main/preload `build.watch`。
- [ ] 若是 Electron：main 在 dev 态使用 `process.env.ELECTRON_RENDERER_URL`，未硬编码 localhost 端口。
- [ ] 若是 Electron：已按「开发顺序」验收 renderer HMR、preload 刷新、main 重启；若无法跑 GUI，已在回复中说明配置已核对项与用户本地验证步骤。
- [ ] 已调用 update-prd 创建或重建 `prd/` 文档体系。
- [ ] 已对比原始 `prd.md` 与当前实现，把未完成差距写入 `TODO.md`。
- [ ] 已按需更新 `AGENTS.md`，说明后续基于 `TODO.md` 继续任务。
- [ ] 已在 `prd/` 和 `TODO.md` 完成迁移收尾后将根目录 `prd.md` 归档为 `prd.original.md`（Agent 后续不读取）。
- [ ] 已创建或更新仓库根目录 `README.md`，并确保内容与当前代码、脚本、配置和 `prd/` 文档一致。
- [ ] 已在最终回复中提供运行、安装或加载工具的操作说明；浏览器插件已说明 Chrome 加载已解压扩展的步骤。
