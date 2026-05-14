---
name: 02-project-prepare
description: 从仓库根目录 prd.md 准备一个 vibecoding 项目，但不写业务代码。读取 PRD，按工具形态选择框架（网站用 Next.js，桌面软件用 Electron，浏览器插件用 vite-web-extension），生成或更新设计系统、API 接入方案和 TODO.md 开发计划，并在用户确认前停止。适用于从 PRD 启动项目、规划 TODO、选择 Next.js/Electron/Chrome Extension 技术路线、准备 API 方案或生成设计系统。
---

# Project Prepare：PRD → 工具形态 → 设计系统 → API 方案 → TODO.md

## 概述

面向 vibecoding 小白的项目准备 Skill。用户只需要维护仓库根目录 `prd.md`；本 Skill 负责把 PRD 转成可执行的开发计划，但不得创建页面、安装依赖、写业务代码或接入 API。

后续真正写代码时，使用 `project-develop` Skill 按 `TODO.md` 和框架选择执行。

## 执行流程

### 第一步：读取 PRD

- 只读取仓库根目录 `prd.md`。
- 提取：产品名称、Slogan、工具形态、用户画像、核心功能 MVP、交互流程、UI 设计风格。
- 优先使用 `prd.md` 里的 `工具形态:` 字段；该字段通常来自 `01-mvp-prd-builder` 的第 1 题：
  - `网站，优先在桌面使用`
  - `网站，优先在移动端使用`
  - `桌面软件`
  - `浏览器插件`
- 如果 `prd.md` 缺少工具形态，先暂停并让用户从以上四项中选一项，不要继续生成 TODO。

### 第二步：选择开发框架

根据工具形态写入唯一主框架：

| 工具形态 | 开发框架 | 说明 |
|---|---|---|
| 网站，优先在桌面使用 | Next.js | App Router + TypeScript，适合桌面优先 Web 产品 |
| 网站，优先在移动端使用 | Next.js | App Router + TypeScript，按移动端优先响应式设计 |
| 桌面软件 | Electron | Electron + Vite + React + TypeScript，适合需要桌面窗口、系统能力或本地文件能力的产品 |
| 浏览器插件 | vite-web-extension | 使用 `https://github.com/JohnBra/vite-web-extension`，适合 Chrome Extension，默认按 Manifest V3、React、TypeScript、Tailwind 路线规划 |

不要把工具形态改写成技术方案；在 `TODO.md` 中同时保留原始工具形态和最终框架选择。

### 第三步：读取 UI 准则并产出设计系统

- 读取 `.agents/skills/ui-ux-pro-max/SKILL.md`；如果项目只存在 `.cursor/skills/ui-ux-pro-max/SKILL.md`，再读该路径。
- 检查是否已有 `design-system/<产品名>/MASTER.md`：
  - 有：读取并对比 `prd.md`，只更新过时或冲突内容。
  - 没有：基于 `prd.md` 和 UI 准则生成 `MASTER.md`。
- 设计系统至少覆盖：颜色 token、字体、圆角、阴影、组件气质、响应式/窗口尺寸原则。
- 与 `prd.md` 冲突时，以 `prd.md` 的产品表达为准，UI 准则只补齐工程化细节。

### 第四步：读取 API 文档并制定接入方案

- 按需读取 `API文档/` 中与 PRD 场景相关的文档；不要整目录盲读。
- 若存在 `API文档/如何接入Token`，先读取鉴权方式。
- 判断哪些 API 对 MVP 价值明显，哪些可以先用静态内容、本地规则或本地状态替代。
- 在 `prd.md` 末尾新增或更新 `【API 接入方案（待确认）】`，已存在时只更新，不重复追加。

写回格式：

```markdown

### 会调用的 API
- API 名称：用于什么功能；为什么比纯本地实现更合适；失败时如何降级。

```

### 第五步：生成 TODO.md 并停止

- 在仓库根目录创建或更新 `TODO.md`。
- 如果已存在，按最新 `prd.md`、设计系统和 API 方案重写计划，不保留过时任务。
- TODO 必须明确写出工具形态、主框架和框架映射：Next.js、Electron、vite-web-extension。
- 不要包含 `## 0. 用户确认` 章节。
- 写完后必须停止，向用户请求确认；确认前只能解释或修改 `prd.md` / `TODO.md`。

交付提示：

```text
我已经把 API 接入方案写入 prd.md，并整理好了开发计划 TODO.md。请确认：
1. prd.md 中的 API 使用方式是否符合预期
2. TODO.md 中的开发范围、页面范围、接口范围和框架选择是否正确

确认后我再使用 project-develop 开始开发。
```

## TODO.md 模板

```markdown
# 开发计划

## 1. 项目框架
- 工具形态：<直接来自 prd.md 的工具形态>
- 主框架：<Next.js | Electron | vite-web-extension>
- 框架映射：网站 → Next.js；桌面软件 → Electron；浏览器插件 → vite-web-extension
- 选择理由：<结合 PRD 的一句话理由>

## 2. 设计系统
- [ ] 读取 prd.md 与 ui-ux-pro-max
- [ ] 创建或更新 design-system/<产品名>/MASTER.md
- [ ] 将设计 token 落地到所选框架的样式系统

## 3. 项目骨架
- [ ] 按主框架初始化或检查项目结构
- [ ] 建立基础布局、全局样式和核心入口
- [ ] 配置环境变量示例与安全读取方式

## 4. 页面与核心功能
- [ ] 首页/主界面：根据 PRD 展示核心价值入口
- [ ] 核心流程：按 PRD 主路径实现主要任务
- [ ] 记录/结果/设置：按 PRD 数据和反馈需求实现

## 5. API 接入
- [ ] 为每个确认调用的 API 建立安全封装
- [ ] 加入缓存、失败降级和错误提示
- [ ] 确保 API Key 不进入公开前端代码或插件包

## 6. 验证
- [ ] 运行 lint / build / 类型检查
- [ ] 按 PRD 主流程手动走查
- [ ] 列出未完成项与下一步建议

## 7. 开发完成后更新 PRD
- [ ] 调用 update-prd Skill
- [ ] 对照实际代码更新 prd.md
- [ ] 标记本 TODO 中已完成和未完成的事项
```

## 框架规划要求

### Next.js

- 使用 App Router、TypeScript 和 CSS 变量/Tailwind 对齐设计系统。
- API Key 只能由服务端 Route Handler 或 Server Action 读取。
- 页面路由按 PRD 交互流程组织。

### Electron

- 使用 Electron + Vite + React + TypeScript。
- 明确主进程、预加载脚本和渲染进程边界。
- 系统能力、本地文件、密钥读取等只能放在主进程或安全 preload API 后面。

### vite-web-extension

- 使用 `JohnBra/vite-web-extension` 作为 Chrome Extension 起点。
- TODO 中写明需要哪些插件入口：popup、options、content script、background、side panel 或 new tab。
- 默认按 Chrome Manifest V3 规划，构建目标为 `dist_chrome`。
- 不得把私密 API Key 打进浏览器插件包；需要远程 API 时优先规划后端代理、用户自填密钥或纯本地降级。

## 自检清单

- [ ] 已读取 `prd.md` 并提取工具形态。
- [ ] 已把工具形态映射到 Next.js、Electron 或 vite-web-extension。
- [ ] 已生成或更新设计系统。
- [ ] 已按需读取 API 文档并写回 `### 会调用的 API`。
- [ ] 已创建或更新 `TODO.md`。
- [ ] 已停止在计划阶段，没有写业务代码或安装依赖。
