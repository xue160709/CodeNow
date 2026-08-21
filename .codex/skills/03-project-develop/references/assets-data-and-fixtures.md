# 数据、Fixture 与占位资产（03 通用）

写列表/仪表盘/卡片类 UI、占位图或安装 icon 依赖前读本文。与 `design-system/<产品名>/MASTER.md` 及 TODO §2「数据来源 / 演示策略」一致。

## 数据来源与演示策略（与 02 对齐）

| 数据来源 | 含义 | 03 必须 |
| --- | --- | --- |
| **LIVE** | 真实 API/OAuth；PRD 含「我的 xxx」默认 LIVE | 未配置 → **未配置态**（引导填 Key/连接），禁止用假列表冒充已连接 |
| **FIXTURE** | 纯演示或本地示例数据 | 数据集中在 `src/fixtures/` 或 `src/data/demo/`（与 TODO 一致）；可选 UI 角标「示例数据」；禁止冒充第三方已同步 |
| **EMPTY** | 内容须用户自己产生 | **空态** + CTA，禁止默认塞 10 条假记录 |

| 演示策略 | 适用来源 | 03 必须 |
| --- | --- | --- |
| **LIVE_UNCONFIGURED** | LIVE 无 Key/OAuth/连接 | 显示未配置态、连接 CTA、隐私/Key 提示，不展示假同步结果 |
| **FIXTURE_DEMO** | FIXTURE 或 LIVE 的示例模式 | 集中 fixture；界面按 TODO/MASTER 决定是否显示「示例数据」角标；不得写成“已同步/已连接” |
| **EMPTY_CTA** | EMPTY | 明确空态说明和创建/导入 CTA |

- 允许 `LIVE + FIXTURE_DEMO`：用于无 Key 时仍可看产品形态，但必须有示例模式标识或上下文说明。
- 禁止在 JSX 内硬编码大段 mock 数组；FIXTURE 从单一模块 `import`。
- 禁止静默 mock：FIXTURE_DEMO 须在 TODO/MASTER 写明，且与 LIVE 切换路径清晰。

## 占位图

1. 优先 `MASTER.md`「媒体与占位图」策略。
2. 默认：`public/placeholders/` 静态图，或 `PlaceholderImage`（固定 `aspect-ratio` + design token 渐变/SVG）。
3. 每张图：`width`/`height` 或比例、`alt`、加载失败回退本地占位（避免断图与 CLS）。
4. **Unsplash API / 远程图源**：仅当 MASTER/TODO 明确启用；默认不接入。若启用 Unsplash，须提供 `IMAGE_PROVIDER=none|unsplash`、`UNSPLASH_ACCESS_KEY`（仅写入 `*.example` 占位）、请求超时、失败回退、署名/来源说明；**大陆/离线场景默认 `IMAGE_PROVIDER=none`**，README 说明如何关闭远程图源。

## 图标

- **只使用** `MASTER.md`「图标 Iconography」指定的库（React 栈默认 `lucide-react`）。
- 禁止 emoji 作导航/设置/主操作图标；禁止 Lucide + Phosphor 等多库混用。
- 纯图标按钮：`aria-label` 或 visually hidden 文案（tooltip 不能替代）。
- 尺寸遵循 MASTER（常见：导航 20px、按钮内 16px、空态 48px）。

## UI 技术栈（安装依赖时）

以 `MASTER.md`「UI 技术栈与组件策略」为准，常见默认：

- 样式：Tailwind + CSS variables（`@import "tailwindcss"` 或项目已有配置）
- 组件：原生 + Tailwind；复杂 Dialog/Menu/Select 可用 Radix/shadcn 风格（MASTER 写明才安装）
- 图表：仅 PRD/界面需要时安装 `recharts`（或 MASTER 指定库）

## 自检（03 收尾前）

- [ ] 各 §2 功能的「数据来源 / 演示策略」与实现一致
- [ ] FIXTURE_DEMO 有集中路径；LIVE 有未配置态；LIVE+FIXTURE_DEMO 明示示例模式
- [ ] 占位图离线可渲染；Unsplash/远程图有超时与 fallback，默认可关闭
- [ ] `package.json` 的 icon/图表依赖与 MASTER 一致，无临时另选图标库
