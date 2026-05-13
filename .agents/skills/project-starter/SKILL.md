---
name: project-starter
description: Starts a beginner-friendly vibecoding project from repo-root prd.md. Reads prd.md first, then progressively reads design/API docs as needed, writes the API plan back into prd.md, creates TODO.md as development plan for user confirmation, scaffolds or extends a Next.js app only after approval, then invokes update-prd after development to sync docs with implementation. Use when building a product from PRD, starting a Next.js project, generating a design system, planning TODOs, or deciding API usage.
disable-model-invocation: false
---

# Project Starter：PRD → 设计系统 → API 方案 → 开发计划 → Next.js → 更新 PRD

面向 **vibecoding 小白** 的项目脚手架 Skill。让用户只维护一个 `prd.md`，Agent 按步骤渐进式读取所需文档，产出开发计划（TODO.md），用户确认后再开始写代码；开发完成后再调用 `update-prd` 同步回 PRD。

---

## 执行流程（渐进式，按步骤读取）

### 第一步：读取 PRD，理解产品

- **只读取** 仓库根目录 `prd.md`（路径固定，不要求用户重复描述）。
- 从中提取：产品名称、用户画像、核心功能 MVP、交互流程、UI 设计风格。
- 不读取其他任何文档。

完成后进入第二步。

### 第二步：读取 UI 准则 + 产出设计系统

- **读取** `.cursor/skills/ui-ux-pro-max/SKILL.md`。
- 检查是否已有 `design-system/<产品名>/MASTER.md`：
  - **有** → 读取并对比 `prd.md`，确认是否需要更新。
  - **没有** → 基于 `prd.md` + ui-ux-pro-max 生成 MASTER.md。
- 设计系统产出物：

| 产出 | 说明 |
|------|------|
| `design-system/<产品名>/MASTER.md` | 颜色 token、字体、圆角、阴影、组件气质；引用 `prd.md` |
| `design-system/<产品名>/pages/*.md` | 可选；单页覆盖规则 |
| Next.js `globals.css` 或 `tailwind.config` | 将 Master 中 CSS 变量同步为可引用 token（开发阶段再创建） |

- 冲突规则：与 `prd.md` 冲突时以 **prd.md 的产品表述为准**，ui-ux-pro-max 补齐工程化细节（对比度、触控尺寸等）。

完成后进入第三步。

### 第三步：读取 API 文档，制定接入方案

- **读取** `API文档/` 目录下与 PRD 场景相关的文档（按需读取，不必全读）：
  1. 先读 `API文档/如何接入Token`（鉴权方式）。
  2. 根据 PRD 功能，只读取可能用到的 API 文档（参考下方「PRD 功能 × API 文档」对照表）。
- 判断哪些 API 对产品体验提升明显、哪些 MVP 阶段可用静态/本地方案替代。
- **写回 prd.md**：在末尾新增或更新「API 接入方案（待确认）」区块。

写回格式（若已存在同名区块，只更新内容，不重复追加）：

```markdown
【API 接入方案（待确认）】

### 会调用的 API
- API 名称：用于什么功能；为什么比纯本地实现更合适；失败时如何降级。

### 暂不调用 API 的功能
- 功能名称：为什么 MVP 阶段用静态内容、本地规则或本地状态即可。

### 安全与成本说明
- API Key 只放服务端环境变量，不写入前端代码。
- 高频或昂贵接口需要缓存、额度保护和失败降级。

### 待用户确认
- 请确认以上 API 接入方案是否符合预期；确认后再开始开发。
```

完成后进入第四步。

### 第四步：生成开发计划（TODO.md）并等待确认

- 在仓库根目录创建或更新 `TODO.md`，作为**开发计划**。
- 如果已存在，按最新 `prd.md` 和 API 方案更新，不保留过时任务。
- **格式见下方「TODO.md 模板」**。

写完后 **必须暂停**，向用户展示：

```
我已经把 API 接入方案写入 prd.md，并整理好了开发计划 TODO.md。请确认：
1. prd.md 中的 API 使用方式是否符合预期
2. TODO.md 中的开发范围、页面范围与接口范围是否正确

确认后我再开始开发。
```

**未获得用户确认前，不得创建页面、安装依赖、写业务代码或接入 API。** 此时只能解释 `prd.md` 和 `TODO.md`，或按用户反馈修改这两个文件。

### 第五步：确认后开发 Next.js

只有用户明确回复确认、同意、开始开发、没问题等表达后，才开始实现。

工程约定：
- **框架**：Next.js（App Router）、TypeScript；样式可用 Tailwind + CSS 变量对齐 Master。
- **环境变量**：仅服务端读取 `MINIMAX_API_KEY`（见 `API文档/如何接入Token`）；`.env.local` 列入 `.gitignore`。
- **BFF 模式**：前端调用 `app/api/**` 路由，由服务端转发 MiniMax，返回 JSON 或流。
- **路由与 PRD 对齐**：按 PRD 交互流程组织路由（如 `/` 首页推荐、`/play` 冥想播放、`/journal` 情绪日志）。

按 TODO.md 中的阶段顺序开发，每完成一个阶段标记对应 TODO 项。

### 第六步：开发完成后同步 PRD

开发、验证与 TODO 收尾完成后：
1. 读取 `.cursor/skills/update-prd/SKILL.md`。
2. 对照实际代码更新 `prd.md`（功能范围、业务逻辑、数据结构、API 接入结果、代码文件映射）。
3. 若实现与开发前的「API 接入方案」不同，须在 `prd.md` 中说明最终方案与原因。
4. 更新 `TODO.md`：已完成项打勾，未完成项保留并注明原因。
5. 回复用户：已完成哪些开发、`prd.md` 更新了什么、`TODO.md` 还剩什么。

---

## PRD 功能 × API 文档（何处接入更佳）

第三步读取 API 文档时的参考对照表。能显著增强体验时使用；**MVP 可先用静态素材 + 本地规则**，再渐进接入。

| PRD 能力 | 可能相关的 API 文档 | 用途 |
|----------|---------------------|------|
| 每日推荐（文案/解释） | `API文档/LLM文本生成.md` | 时段 + 用户偏好 → 推荐语、简短理由 |
| 冥想引导语播报（非录制人声） | `API文档/同步语音合成.md` | 脚本转语音；注意配额与缓存 |
| 睡眠/放松氛围音乐 | `API文档/音乐生成.md` | 背景音乐或衔接音效；可与静态白噪音并存 |
| 课程封面、场景插画 | `API文档/图片生成.md` | 列表页视觉、分享图 |
| 情绪日志 → 温和反馈 | `API文档/LLM文本生成.md` | 短反馈，避免医疗诊断表述 |
| 视频类素材 | `API文档/视频生成.md` | 非 MVP 必备；成本高，按需 |

**不必强行接入**：固定时长呼吸训练、离线可播资源、纯本地情绪打卡与图表。

---

## TODO.md 模板（开发计划）

```markdown
# 开发计划

## 0. 用户确认
- [ ] 确认 prd.md 中的 API 接入方案
- [ ] 确认本开发计划的范围与优先级

## 1. 设计系统
- [ ] 读取 prd.md 与 ui-ux-pro-max
- [ ] 创建或更新 design-system/<产品名>/MASTER.md
- [ ] 将设计 token 同步到 Next.js 样式系统

## 2. Next.js 项目骨架
- [ ] 初始化或检查 Next.js App Router 项目
- [ ] 建立基础路由、布局、全局样式
- [ ] 配置 .env.local 示例与服务端环境变量读取

## 3. 页面与功能
- [ ] 首页：根据 PRD 展示核心推荐与入口
- [ ] 核心流程页：按 PRD 主路径实现
- [ ] 记录/结果页：按 PRD 数据与反馈需求实现

## 4. API 接入
- [ ] 为每个确认调用的 API 创建服务端 Route Handler
- [ ] 加入缓存、失败降级和错误提示
- [ ] 确保 API Key 不进入前端代码

## 5. 验证
- [ ] 运行 lint / build / 类型检查
- [ ] 按 PRD 主流程手动走查
- [ ] 列出未完成项与下一步建议

## 6. 开发完成后更新 PRD
- [ ] 调用 update-prd Skill
- [ ] 对照实际代码更新 prd.md
- [ ] 标记本 TODO 中已完成和未完成的事项
```

---

## 执行清单（自检）

每次执行完毕后对照：

- [ ] 第一步：已读 prd.md，列出 MVP 功能与主路径
- [ ] 第二步：已读 ui-ux-pro-max，设计系统与 PRD 视觉一致
- [ ] 第三步：已按需读取 API 文档，API 方案已写回 prd.md
- [ ] 第四步：已创建或更新 TODO.md 开发计划
- [ ] 第四步：已暂停并获得用户确认
- [ ] 第五步：API 调用仅在服务端，Token 来自环境变量
- [ ] 第五步：每个接入功能标注了缓存策略与失败降级方案
- [ ] 第六步：开发完成后已调用 update-prd，同步 prd.md 与 TODO.md
