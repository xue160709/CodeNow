---
name: 03-project-develop
description: 按仓库根目录 TODO.md、prd.md、design-system/ 设计系统和 ui-ux-pro-max Skill 写代码实现项目。适用于用户已经确认 Project Prepare 生成的 TODO.md，并要求开始开发、执行 TODO、实现 MVP、写代码、搭建 Next.js/Electron/Chrome Extension 项目时。根据 TODO 中的主框架选择 Next.js、Electron 或 vite-web-extension，以 prd.md 确认产品范围，以 design-system/ 作为完整设计来源，调用 ui-ux-pro-max 辅助 UI/UX 落地，完成实现、验证、更新 TODO.md，并调用 update-prd 创建或重建 prd/ 文档体系。
---

# Project Develop：TODO.md → 框架实现 → 验证 → 重建 prd/

## 概述

本 Skill 只负责写代码和验证。它以 `TODO.md` 为开发合同，以 `prd.md` 为简版产品依据，以仓库根目录 `design-system/` 为完整设计依据，并调用 `ui-ux-pro-max` Skill 辅助 UI/UX 落地。按 TODO 中声明的主框架执行：Next.js、Electron 或 vite-web-extension。开发完成后，必须调用 `update-prd` 创建或重建仓库根目录 `prd/` 文档体系。

如果项目还没有 `TODO.md`、TODO 未写明主框架，或用户还没确认开发范围，先使用 `project-prepare` 准备计划，不要自行跳过计划阶段。

## 开发依据优先级

- `TODO.md`：开发合同，决定主框架、阶段任务、页面/入口范围、API 接入范围和验证要求。
- `prd.md`：简版产品说明，只用于确认产品目标、核心功能、用户路径和 API 方案，不作为完整视觉设计来源。
- `design-system/`：完整设计系统来源。所有颜色、字体、间距、圆角、阴影、组件气质、布局密度、响应式规则和页面级设计约束，只读取并遵循 `design-system/` 下的内容。
- `ui-ux-pro-max`：必须调用/读取该 Skill 作为 UI/UX 工程落地和质量检查准则，但不能覆盖 `design-system/` 中的具体设计决定。

若 `prd.md`、`TODO.md` 和 `design-system/` 冲突，优先级为：`design-system/` 决定视觉与交互细节，`TODO.md` 决定开发任务与框架，`prd.md` 决定产品范围。不要从 `prd.md` 临时推断或补写完整设计系统。

## 执行流程

### 第一步：开发前检查

- 读取仓库根目录 `TODO.md` 和 `prd.md`。
- 从 `TODO.md` 提取：主框架、工具形态、阶段任务、页面/入口范围、API 接入范围、验证命令。
- 读取仓库根目录 `design-system/` 下的设计系统文档；优先读取 `design-system/<产品名>/MASTER.md`，再按需读取 `design-system/<产品名>/pages/*.md` 或其他局部规则。
- 设计系统只从 `design-system/` 读取。`prd.md` 是简单版本，不要把 `prd.md` 中的 UI 风格文字当作完整设计系统，也不要用它覆盖 `design-system/`。
- 读取/调用 `.agents/skills/ui-ux-pro-max/SKILL.md`；如果项目只存在 `.cursor/skills/ui-ux-pro-max/SKILL.md`，再读该路径。
- 若 `design-system/` 缺失或没有可用设计系统文档，暂停并要求先补齐设计系统，不要直接从 `prd.md` 推断完整 UI。
- 查看现有项目结构、`package.json`、锁文件和 `git status`，尊重用户已有改动。
- 如果 TODO 与 PRD 冲突，以 PRD 的产品目标为准，并把必要调整写回 TODO。

### 第二步：按框架开发

- 开发 UI 时必须同时对照 `design-system/` 和 `ui-ux-pro-max`：前者给出本项目的具体设计，后者用于检查可访问性、控件选择、布局密度、响应式、状态反馈和交互质量。
- 不要新增与 `design-system/` 不一致的配色、字体、圆角、阴影、卡片风格或装饰元素；缺失的工程细节可用 `ui-ux-pro-max` 补齐，但要保持克制并贴合 `design-system/`。

#### Next.js

- 使用 Next.js App Router + TypeScript。
- 将设计 token 落地到 `globals.css`、Tailwind 配置或现有样式系统。
- 按 PRD 主路径创建页面、布局、组件和状态逻辑。
- 需要 API 时使用 `app/api/**` Route Handler 或服务端代码封装，前端只调用自己的后端接口。
- API Key 只从服务端环境变量读取，不写入客户端 bundle。

#### Electron

- 使用 Electron + Vite + React + TypeScript，或沿用仓库已有 Electron 栈。
- 区分主进程、预加载脚本和渲染进程：
  - 主进程：窗口、系统能力、本地文件、密钥读取、后端 API 代理。
  - preload：用 `contextBridge` 暴露最小安全 API。
  - renderer：只做 UI 和交互，不直接读取 Node 私密能力。
- 默认开启 `contextIsolation`，避免启用不必要的 `nodeIntegration`。
- 将 PRD 核心流程实现为桌面窗口中的实际可用界面。

#### vite-web-extension

- 使用 `https://github.com/JohnBra/vite-web-extension` 作为 Chrome Extension 实现路线，或沿用仓库已有插件结构。
- 默认目标为 Chrome Manifest V3；按 TODO 保留需要的入口：
  - popup
  - options
  - content script
  - background/service worker
  - side panel
  - new tab
- 更新 `manifest.json` / `manifest.dev.json` 的名称、描述、权限和入口声明。
- 将 PRD 主流程放到最合适的插件入口中；删除或忽略不需要的模板页面。
- 构建产物默认检查 `dist_chrome`。
- 不得把私密 API Key 打进插件包；需要远程 API 时使用后端代理、用户本地配置或降级为本地能力。

### 第三步：按 TODO 分阶段实现

- 按 `TODO.md` 的章节顺序开发。
- 每完成一个阶段，更新对应 checkbox。
- 若发现 TODO 缺少必要工程任务，可以补充到对应章节，但不要扩张 PRD 未要求的产品范围。
- 若某项无法完成，保留未勾选并注明原因和下一步。

### 第四步：项目配置、gitignore 与密钥文件

- 创建或更新仓库根目录 `.gitignore`，至少覆盖当前框架的构建产物、依赖目录、缓存、日志、系统文件和本地密钥文件。
- `.gitignore` 必须包含：`node_modules/`、构建输出（如 `.next/`、`dist/`、`dist_chrome/`、`build/`、`out/`）、日志、缓存、`.DS_Store`、`.env`、`.env.local`、`.env.*.local`。
- 如果使用 API 文档里的 API，不要只创建 `.env.local.example`，也必须创建 `.env.local`。
- `.env.local.example` 写入变量名和占位说明；`.env.local` 写入同样变量名，但不得编造真实 Key，可使用 `MINIMAX_API_KEY=这里粘贴你的_Token_Plan_API_Key` 这类占位值。
- 如果项目运行时明确读取 `.env` 而不是 `.env.local`，也创建 `.env`，并保持 `.gitignore` 覆盖它。
- 在最终回复中提示用户按 Token Plan 流程获取并写入 API Key。

Token Plan 提示文案：

````markdown
1. **订阅 Token Plan**  
   打开 [Token Plan](https://platform.minimaxi.com/subscribe/token-plan?code=JBlROVn3gJ&source=link)，选择套餐并完成支付。

2. **复制 Key**  
   订阅生效后，进入 [用户中心 → Token Plan / 支付与套餐](https://platform.minimaxi.com/user-center/payment/token-plan)，在套餐详情中复制 **Token Plan API Key**。

3. **写入本地环境变量（推荐）**  
   在项目根目录新建或打开 `.env.local`（与运行代码的目录一致即可），填入你从控制台复制的 Key，不要加引号、不要多空格：

   ```env
   MINIMAX_API_KEY=这里粘贴你的_Token_Plan_API_Key
   ```
````

### 第五步：API 与数据安全

- 为每个确认调用的 API 建立独立服务封装。
- 加入失败降级、加载状态、错误提示和必要缓存。
- Web：密钥只在服务端。
- Electron：密钥只在主进程或用户本地安全配置中。
- Chrome Extension：插件包内不保存私密密钥；优先通过后端代理或用户显式配置。

### 第六步：验证

- 运行项目已有的 lint、typecheck、test、build 命令；如果没有命令，至少运行可用的 build 或类型检查。
- 对照 PRD 主流程做一次手动走查。
- 前端或插件有可视界面时，启动本地预览并用浏览器/截图检查关键页面是否可用。
- 如果验证命令失败，优先修复由本次实现引入的问题；无法修复时在最终回复中说明。

### 第七步：调用 update-prd 重建 prd/ 与 TODO

开发、验证和 TODO 收尾完成后：

1. 读取 `.agents/skills/update-prd/SKILL.md`；如果项目只存在 `.cursor/skills/update-prd/SKILL.md`，再读该路径。
2. 明确向 `update-prd` 声明本次任务：创建仓库根目录 `prd/` 文件夹；读取整个项目；基于实际代码重新构建 `prd/` 文件夹里的 PRD 文档，而不是只局部修补根目录 `prd.md`。
3. 读取整个项目时必须覆盖产品代码、路由/入口、组件、状态与数据模型、API 封装、配置文件和构建脚本；跳过 `.git/`、`node_modules/`、`.next/`、`dist/`、`build/`、覆盖率产物、日志、缓存和密钥文件。
4. 若 `prd/` 不存在，先创建；若已存在，读取旧文档作为参考，但以当前代码实现为准重建内容，移除过时描述。
5. 按 `update-prd` 的标准章节为每个核心模块生成或更新 PRD 文档：功能概述、核心功能列表、数据结构、业务逻辑、相关代码文件、关联 PRD 文档。
6. 在 `prd/` 下至少维护一个总览文档（如 `prd/README.md` 或 `prd/index.md`），说明产品整体结构、模块划分、入口路径、数据流和 PRD 文档之间的关系。
7. 若最终实现与根目录 `prd.md` 中的 `【API 接入方案（待确认）】` 不同，在 `prd/` 的相关文档中说明最终方案与原因。
8. 更新 `TODO.md`：完成项打勾，未完成项保留并注明原因。
9. 回复用户：已完成哪些开发、验证结果、`prd/` 重建了哪些文档、`TODO.md` 还剩什么。

调用 `update-prd` 时使用类似下面的任务声明：

```text
请创建或更新仓库根目录 prd/ 文件夹，读取整个项目代码与配置，基于当前实际实现重新构建 prd/ 下的 PRD 文档体系。不要只同步根目录 prd.md；请按模块生成标准化 PRD，维护总览文档、代码文件映射、数据结构、业务逻辑和 PRD 间关联关系。
```

## 自检清单

- [ ] 已读取 `TODO.md`、`prd.md` 和 `design-system/`。
- [ ] 已调用/读取 `ui-ux-pro-max` Skill 辅助 UI/UX 落地。
- [ ] 已确认 `prd.md` 只作为简版产品说明，完整设计只来自 `design-system/`。
- [ ] 已识别主框架：Next.js、Electron 或 vite-web-extension。
- [ ] 已按 TODO 分阶段实现并更新 checkbox。
- [ ] 已创建或更新 `.gitignore`。
- [ ] 若使用 API 文档里的 API，已创建 `.env.local.example` 和 `.env.local`，并提示 Token Plan 获取 Key 流程。
- [ ] 已保护 API Key，不进入公开前端代码或插件包。
- [ ] 已运行可用验证命令并处理结果。
- [ ] 已调用 update-prd 创建或重建 `prd/` 文档体系。
