---
name: ui-ux-pro-max
description: "面向 Web 与移动端的 UI/UX 设计知识库。包含 50+ 种风格、161 套配色、57 组字体搭配、161 种产品类型、99 条 UX 准则，以及 10 套技术栈（React、Next.js、Vue、Svelte、SwiftUI、React Native、Flutter、Tailwind、shadcn/ui、HTML/CSS）下的 25 种图表类型。适用动作：规划、搭建、创建、设计、实现、评审、修复、改进、优化、增强、重构与检查 UI/UX 代码。项目类型：网站、落地页、控制台、管理后台、电商、SaaS、作品集、博客与移动应用。元素：按钮、弹窗、导航栏、侧边栏、卡片、表格、表单与图表。风格：玻璃拟态、黏土拟态、极简、粗野主义、新拟态、便当格布局、深色模式、响应式、拟物与扁平。主题：配色体系、无障碍、动效、版式、字体与字重搭配、间距、交互状态、阴影与渐变。集成：可通过 shadcn/ui MCP 检索组件与示例。"
---

# UI/UX Pro Max - 设计知识库

面向 Web 与移动应用的综合性设计指南。内含 50+ 种风格、161 套配色、57 组字体搭配、带推理规则的 161 种产品类型、99 条 UX 准则，以及 10 套技术栈下的 25 种图表类型。数据可按优先级检索与推荐。

## 何时使用

当任务涉及 **界面结构、视觉设计取舍、交互模式或体验质量把控** 时，应使用本 Skill。

### 必须使用

以下情况必须调用本 Skill：

- 设计新页面（落地页、控制台、后台、SaaS、移动应用）
- 新建或重构 UI 组件（按钮、弹窗、表单、表格、图表等）
- 选择配色、字体体系、间距规范或布局体系
- 评审 UI 代码的体验、无障碍或视觉一致性
- 实现导航结构、动效或响应式行为
- 做产品级设计决策（风格、信息层级、品牌表达）
- 提升界面的观感、清晰度或易用性

### 建议使用

以下情况建议使用本 Skill：

- 界面「不够专业」但说不清原因
- 收到可用性或体验相关反馈
- 上线前做界面质量优化
- 对齐跨平台设计（Web / iOS / Android）
- 搭建设计系统或可复用组件库

### 可跳过

以下情况通常不需要本 Skill：

- 纯后端逻辑开发
- 仅涉及 API 或数据库设计
- 与界面无关的性能优化
- 基础设施或 DevOps 工作
- 非视觉类脚本或自动化任务

**判断标准**：若任务会改变功能的 **外观、手感、动效或可交互方式**，则应使用本 Skill。

## 按优先级划分的规则类别

*供人与 AI 参考：按优先级 1→10 决定先关注哪类规则；需要细节时用 `--domain <领域>` 查询。脚本不会读取本表。*

| 优先级 | 类别 | 影响 | 领域 | 关键检查（必备） | 反模式（避免） |
|--------|------|------|------|------------------|----------------|
| 1 | 无障碍 | 关键 | `ux` | 对比度 4.5:1、替代文本、键盘导航、aria-label | 去掉焦点环、无文案的纯图标按钮 |
| 2 | 触控与交互 | 关键 | `ux` | 最小 44×44px、间距 ≥8px、加载反馈 | 仅依赖悬停、瞬时状态切换（0ms） |
| 3 | 性能 | 高 | `ux` | WebP/AVIF、懒加载、预留空间（CLS < 0.1） | 布局抖动、累积布局偏移 |
| 4 | 风格选择 | 高 | `style`, `product` | 匹配产品类型、一致性、SVG 图标（不用 emoji） | 扁平与拟物随意混用、用 emoji 当图标 |
| 5 | 布局与响应式 | 高 | `ux` | 移动优先断点、viewport 元信息、禁止横向滚动 | 横向滚动、固定 px 容器、禁止缩放 |
| 6 | 字体与色彩 | 中 | `typography`, `color` | 正文 16px 基线、行高 1.5、语义色 token | 正文 <12px、灰底灰字、组件里写死 hex |
| 7 | 动效 | 中 | `ux` | 时长 150–300ms、动效表意、空间连续 | 纯装饰动效、动画改宽高、无减弱动效 |
| 8 | 表单与反馈 | 中 | `ux` | 可见标签、错误靠近字段、辅助文案、渐进披露 | 仅用占位符当标签、错误只在顶部、一上来信息过载 |
| 9 | 导航模式 | 高 | `ux` | 可预期的返回、底部导航 ≤5 项、深链 | 导航过载、返回行为错乱、无深链 |
| 10 | 图表与数据 | 低 | `chart` | 图例、提示、可访问配色 | 仅靠颜色传达含义 |

## 速查清单

### 1. 无障碍（关键）

- `color-contrast` - 正文最低对比度 4.5:1（大字号 3:1）；Material Design
- `focus-states` - 可聚焦元素需可见焦点环（2–4px；Apple HIG、MD）
- `alt-text` - 有意义的图片需描述性替代文本
- `aria-labels` - 纯图标按钮需 aria-label；原生端用 accessibilityLabel（Apple HIG）
- `keyboard-nav` - Tab 顺序与视觉顺序一致；完整键盘支持（Apple HIG）
- `form-labels` - 使用带 `for` 的 label 关联控件
- `skip-links` - 为键盘用户提供「跳到主内容」链接
- `heading-hierarchy` - h1→h6 顺序使用，不跳级
- `color-not-only` - 不单靠颜色传达信息（辅以图标/文字）
- `dynamic-type` - 支持系统字号缩放；随文字变大避免不当截断（Apple Dynamic Type、MD）
- `reduced-motion` - 遵守 prefers-reduced-motion；在系统请求时减少/关闭动效（Apple Reduced Motion API、MD）
- `voiceover-sr` - 有意义的 accessibilityLabel/accessibilityHint；VoiceOver/读屏逻辑顺序（Apple HIG、MD）
- `escape-routes` - 弹窗与多步流程提供取消/返回（Apple HIG）
- `keyboard-shortcuts` - 保留系统与无障碍快捷键；拖拽提供键盘替代方案（Apple HIG）

### 2. 触控与交互（关键）

- `touch-target-size` - 最小 44×44pt（Apple）/ 48×48dp（Material）；可视区域小时扩大点击热区
- `touch-spacing` - 触控目标之间至少 8px/8dp 间距（Apple HIG、MD）
- `hover-vs-tap` - 主操作以点击/点按为准；不要只靠悬停
- `loading-buttons` - 异步进行中禁用按钮；显示转圈或进度
- `error-feedback` - 在问题附近给出清晰错误信息
- `cursor-pointer` - 可点击 Web 元素加 cursor-pointer
- `gesture-conflicts` - 主内容避免横向滑动手势；优先纵向滚动
- `tap-delay` - 使用 touch-action: manipulation 减少约 300ms 点按延迟（Web）
- `standard-gestures` - 一致使用平台标准手势；勿随意重定义（如侧滑返回、双指缩放）（Apple HIG）
- `system-gestures` - 勿遮挡系统手势（控制中心、侧滑返回等）（Apple HIG）
- `press-feedback` - 按下时有视觉反馈（涟漪/高亮；MD 状态层）
- `haptic-feedback` - 确认与重要操作用触觉反馈；避免滥用（Apple HIG）
- `gesture-alternative` - 关键操作勿仅依赖手势；始终提供可见控件
- `safe-area-awareness` - 主要触控区避开刘海、灵动岛、手势条与屏幕边缘
- `no-precision-required` - 避免要求用户像素级点中小图标或细边
- `swipe-clarity` - 滑动操作需明确可发现性（箭头、文案、引导）
- `drag-threshold` - 拖拽前先有位移阈值，避免误拖

### 3. 性能（高）

- `image-optimization` - 使用 WebP/AVIF、响应式图片（srcset/sizes），非首屏资源懒加载
- `image-dimension` - 声明宽高或使用 aspect-ratio 防止布局偏移（Core Web Vitals：CLS）
- `font-loading` - 使用 font-display: swap/optional 避免不可见文字（FOIT）；预留空间减少位移（MD）
- `font-preload` - 仅预加载关键字体；避免每种字重都 preload
- `critical-css` - 优先首屏 CSS（内联关键 CSS 或尽早加载样式表）
- `lazy-loading` - 非首屏组件用动态 import / 路由级拆分懒加载
- `bundle-splitting` - 按路由/功能拆分（React Suspense / Next.js dynamic）降低首包与 TTI
- `third-party-scripts` - 第三方脚本 async/defer；审计并移除不必要脚本（MD）
- `reduce-reflows` - 避免频繁读布局再写布局；批量读 DOM 再写
- `content-jumping` - 异步内容预留占位，避免跳动（Core Web Vitals：CLS）
- `lazy-load-below-fold` - 首屏以下图片与重媒体使用 loading="lazy"
- `virtualize-lists` - 列表 50+ 项时虚拟化，改善内存与滚动性能
- `main-thread-budget` - 60fps 时每帧主线程工作约 <16ms；重任务移出主线程（HIG、MD）
- `progressive-loading` - >1s 的操作用骨架屏/微光，而非长时间阻塞转圈（Apple HIG）
- `input-latency` - 点按/滚动的输入延迟约 <100ms（Material 响应标准）
- `tap-feedback-speed` - 点按后约 100ms 内给出视觉反馈（Apple HIG）
- `debounce-throttle` - 高频事件（滚动、resize、输入）使用防抖/节流
- `offline-support` - 离线状态提示与基本降级（PWA / 移动端）
- `network-fallback` - 慢网提供降级（低分辨率图、减少动效）

### 4. 风格选择（高）

- `style-match` - 风格与产品类型匹配（用 `--design-system` 获取推荐）
- `consistency` - 全站/全应用风格一致
- `no-emoji-icons` - 使用 SVG 图标（Heroicons、Lucide），不用 emoji
- `color-palette-from-product` - 按产品/行业选色板（检索 `--domain color`）
- `effects-match-style` - 阴影、模糊、圆角与所选风格一致（玻璃/扁平/黏土等）
- `platform-adaptive` - 遵守平台习惯（iOS HIG 与 Material）：导航、控件、字体、动效
- `state-clarity` - 悬停/按下/禁用状态在风格内清晰可辨（Material 状态层）
- `elevation-consistent` - 卡片、底栏、弹窗使用统一 elevation/阴影刻度；避免随意数值
- `dark-mode-pairing` - 明暗模式成对设计，保持品牌、对比度与风格一致
- `icon-style-consistent` - 全产品统一图标集/视觉语言（线宽、圆角）
- `system-controls` - 优先原生/系统控件；仅在品牌需要时深度定制（Apple HIG）
- `blur-purpose` - 模糊用于表达「背后可关闭」（弹窗、底栏），不作纯装饰（Apple HIG）
- `primary-action` - 每屏单一主 CTA；次要操作视觉层级更低（Apple HIG）

### 5. 布局与响应式（高）

- `viewport-meta` - width=device-width initial-scale=1（勿禁用缩放）
- `mobile-first` - 移动优先，再扩展到平板与桌面
- `breakpoint-consistency` - 系统化断点（如 375 / 768 / 1024 / 1440）
- `readable-font-size` - 移动端正文至少 16px（避免 iOS 自动放大输入框）
- `line-length-control` - 移动每行约 35–60 字符；桌面约 60–75 字符
- `horizontal-scroll` - 移动端禁止横向滚动；内容适配视口宽度
- `spacing-scale` - 使用 4pt/8dp 递增间距体系（Material Design）
- `touch-density` - 组件间距利于触控：不紧不疏、减少误触
- `container-width` - 桌面统一最大宽度（如 max-w-6xl / 7xl）
- `z-index-management` - 定义分层 z-index 刻度（如 0 / 10 / 20 / 40 / 100 / 1000）
- `fixed-element-offset` - 固定顶栏/底栏为下方内容预留安全区内边距
- `scroll-behavior` - 避免嵌套滚动干扰主滚动
- `viewport-units` - 移动端优先 min-h-dvh 而非 100vh
- `orientation-support` - 横屏仍可读、可操作
- `content-priority` - 移动优先展示核心内容；次要内容折叠或后置
- `visual-hierarchy` - 用字号、间距、对比建立层级，不单靠颜色

### 6. 字体与色彩（中）

- `line-height` - 正文行高 1.5–1.75
- `line-length` - 每行约限制在 65–75 字符
- `font-pairing` - 标题与正文字体气质匹配
- `font-scale` - 统一字号阶梯（如 12 14 16 18 24 32）
- `contrast-readability` - 浅色背景上用更深正文色（如 slate-900 on white）
- `text-styles-system` - 使用平台字体体系：iOS 11 Dynamic Type / Material 5 字重角色（display、headline、title、body、label）（HIG、MD）
- `weight-hierarchy` - 用字重强化层级：标题粗（600–700）、正文常规（400）、标签中等（500）（MD）
- `color-semantic` - 使用语义色 token（primary、secondary、error、surface、on-surface），组件内不写死 hex（Material 色彩体系）
- `color-dark-mode` - 深色模式用去饱和/更亮的色阶变体，而非简单反色；单独测对比度（HIG、MD）
- `color-accessible-pairs` - 前景/背景需满足 4.5:1（AA）或 7:1（AAA）；用工具校验（WCAG、MD）
- `color-not-decorative-only` - 功能色（错误红、成功绿）需配图标/文字，避免仅靠颜色表意（HIG、MD）
- `truncation-strategy` - 优先换行；必须省略时用省略号并通过 tooltip/展开提供全文（Apple HIG）
- `letter-spacing` - 遵守平台默认字距；正文避免过紧 tracking（HIG、MD）
- `number-tabular` - 数据列、价格、计时器使用等宽数字，减少跳动
- `whitespace-balance` - 有意用留白分组与分区，避免视觉拥挤（Apple HIG）

### 7. 动效（中）

- `duration-timing` - 微交互 150–300ms；复杂过渡 ≤400ms；避免 >500ms（MD）
- `transform-performance` - 仅动画 transform/opacity；避免动画化 width/height/top/left
- `loading-states` - 加载超过约 300ms 时显示骨架或进度
- `excessive-motion` - 每视图最多动 1–2 个关键元素
- `easing` - 进入用 ease-out，离开用 ease-in；UI 过渡避免 linear
- `motion-meaning` - 每个动效需表达因果，而非纯装饰（Apple HIG）
- `state-transition` - 状态变化（悬停/激活/展开/折叠/弹窗）应平滑过渡，避免瞬间跳变
- `continuity` - 页面/屏幕切换保持空间连续（共享元素、方向滑动）（Apple HIG）
- `parallax-subtle` - 视差少用；须尊重减弱动效且不造成迷失感（Apple HIG）
- `spring-physics` - 优先弹簧/物理曲线，而非线性或单一 cubic-bezier（Apple HIG 流体动效）
- `exit-faster-than-enter` - 退出动画短于进入（约进入时长的 60–70%）更显跟手（MD motion）
- `stagger-sequence` - 列表/网格逐项入场间隔约 30–50ms；避免同时出现或过慢揭示（MD）
- `shared-element-transition` - 用共享元素/hero 过渡保持跨屏视觉连续（MD、HIG）
- `interruptible` - 动效可被中断；用户点按/手势应立即取消进行中的动画（Apple HIG）
- `no-blocking-animation` - 动效期间勿阻塞输入；界面保持可交互（Apple HIG）
- `fade-crossfade` - 同容器内替换内容用交叉淡入淡出（MD）
- `scale-feedback` - 可点卡片/按钮按下时轻微缩放（0.95–1.05），松手恢复（HIG、MD）
- `gesture-feedback` - 拖拽、滑动、捏合需实时跟随手指的视觉反馈（MD Motion）
- `hierarchy-motion` - 用平移/缩放方向表达层级：自下进入=更深，向上离开=返回（MD）
- `motion-consistency` - 全局统一 duration/easing token；所有动效同一节奏与气质
- `opacity-threshold` - 淡出元素不要长时间停在 opacity 0.2 以下；要么完全淡出要么保持可见
- `modal-motion` - 弹窗/底栏应从触发源方向动画（缩放+淡入或滑入）以建立空间关系（HIG、MD）
- `navigation-direction` - 前进向左/上，返回向右/下，方向逻辑一致（HIG）
- `layout-shift-avoid` - 动效不得引起重排或 CLS；位移变化用 transform

### 8. 表单与反馈（中）

- `input-labels` - 每个输入框有可见标签（不要只有占位符）
- `error-placement` - 错误信息显示在对应字段下方
- `submit-feedback` - 提交后依次展示加载与成功/失败状态
- `required-indicators` - 必填项有标识（如星号）
- `empty-states` - 无内容时给出说明与可操作引导
- `toast-dismiss` - Toast 约 3–5 秒自动消失
- `confirmation-dialogs` - 破坏性操作前需确认
- `input-helper-text` - 复杂输入在下方提供常驻辅助说明，而非仅靠占位符（Material Design）
- `disabled-states` - 禁用态降低不透明度（0.38–0.5）+ 指针样式 + 语义属性（MD）
- `progressive-disclosure` - 复杂选项渐进展示；避免一上来信息过载（Apple HIG）
- `inline-validation` - 失焦时校验（非逐键）；用户完成输入后再显错（MD）
- `input-type-keyboard` - 使用语义 input 类型（email、tel、number）唤起合适移动键盘（HIG、MD）
- `password-toggle` - 密码框提供显示/隐藏切换（MD）
- `autofill-support` - 使用 autocomplete / textContentType 便于系统自动填充（HIG、MD）
- `undo-support` - 破坏性或大批量操作允许撤销（如「撤销删除」Toast）（Apple HIG）
- `success-feedback` - 完成操作后简短视觉确认（对勾、Toast、颜色闪烁）（MD）
- `error-recovery` - 错误信息须含明确恢复路径（重试、编辑、帮助链接）（HIG、MD）
- `multi-step-progress` - 多步流程显示步骤或进度条；允许返回（MD）
- `form-autosave` - 长表单自动保存草稿，防止误关丢数据（Apple HIG）
- `sheet-dismiss-confirm` - 有未保存更改时，关闭底栏/弹窗前需确认（Apple HIG）
- `error-clarity` - 错误须说明原因 + 如何修复（不要只有「输入无效」）（HIG、MD）
- `field-grouping` - 相关字段逻辑分组（fieldset/legend 或视觉分组）（MD）
- `read-only-distinction` - 只读态在视觉与语义上区别于禁用（MD）
- `focus-management` - 提交校验失败后自动聚焦第一个无效字段（WCAG、MD）
- `error-summary` - 多错误时在顶部汇总并带锚点链到各字段（WCAG）
- `touch-friendly-input` - 移动端输入框高度 ≥44px 以满足触控目标（Apple HIG）
- `destructive-emphasis` - 危险操作用语义危险色（红）并与主操作视觉分离（HIG、MD）
- `toast-accessibility` - Toast 不抢焦点；读屏用 aria-live="polite"（WCAG）
- `aria-live-errors` - 表单错误用 aria-live 区域或 role="alert" 通知读屏（WCAG）
- `contrast-feedback` - 错误/成功状态色对比度须 ≥4.5:1（WCAG、MD）
- `timeout-feedback` - 请求超时须明确反馈并提供重试（MD）

### 9. 导航模式（高）

- `bottom-nav-limit` - 底部导航最多 5 项；图标配文字标签（Material Design）
- `drawer-usage` - 抽屉/侧栏用于次要导航，不承载主操作（Material Design）
- `back-behavior` - 返回须可预期且一致；保留滚动/状态（Apple HIG、MD）
- `deep-linking` - 关键屏幕须可通过深链/URL 到达，便于分享与通知（Apple HIG、MD）
- `tab-bar-ios` - iOS：顶层导航用底部 Tab Bar（Apple HIG）
- `top-app-bar-android` - Android：顶层结构用带导航图标的 Top App Bar（Material Design）
- `nav-label-icon` - 导航项须图标+文字；纯图标导航损害可发现性（MD）
- `nav-state-active` - 当前位置在导航中高亮（颜色、字重、指示条）（HIG、MD）
- `nav-hierarchy` - 主导航（Tab/底栏）与次导航（抽屉/设置）层级分明（MD）
- `modal-escape` - 弹窗/底栏提供明确关闭；移动端支持下拉关闭（Apple HIG）
- `search-accessible` - 搜索易达（顶栏或 Tab）；提供最近/建议查询（MD）
- `breadcrumb-web` - Web：层级 ≥3 时用面包屑帮助定位（MD）
- `state-preservation` - 返回须恢复滚动位置、筛选状态与输入（HIG、MD）
- `gesture-nav-support` - 支持系统返回手势（iOS 侧滑返回、Android 预测性返回）且不冲突（HIG、MD）
- `tab-badge` - 导航角标少用，表示未读/待处理；用户进入后清除（HIG、MD）
- `overflow-menu` - 操作过多时用溢出/更多菜单，勿硬塞（MD）
- `bottom-nav-top-level` - 底栏仅用于顶层屏幕；勿在其中嵌套子导航（MD）
- `adaptive-navigation` - 大屏（≥1024px）倾向侧栏；小屏用底栏/顶栏（Material Adaptive）
- `back-stack-integrity` - 勿静默重置导航栈或意外跳首页（HIG、MD）
- `navigation-consistency` - 导航位置全站一致；勿随页面类型改变
- `avoid-mixed-patterns` - 同一层级勿混用 Tab + 侧栏 + 底栏
- `modal-vs-navigation` - 弹窗不应用于主导航流程，会破坏路径感（HIG）
- `focus-on-route-change` - 路由切换后将焦点移到主内容区（WCAG）
- `persistent-nav` - 深层页面仍能到达核心导航；子流程中勿完全隐藏（HIG、MD）
- `destructive-nav-separation` - 危险操作（删账号、退出）须与普通导航在视觉与空间上分离（HIG、MD）
- `empty-nav-state` - 导航目标不可用时说明原因，勿静默隐藏（MD）

### 10. 图表与数据（低）

- `chart-type` - 图表类型匹配数据：趋势→折线，对比→条形，占比→饼/环
- `color-guidance` - 使用可访问配色；色弱用户避免仅靠红绿对比（WCAG、MD）
- `data-table` - 提供表格替代方案；单靠图表对读屏不友好（WCAG）
- `pattern-texture` - 用纹样/纹理/形状补充颜色，使无颜色也能区分（WCAG、MD）
- `legend-visible` - 始终显示图例；靠近图表，勿放在需滚动才看到的远处（MD）
- `tooltip-on-interact` - Web 悬停或移动端点按显示精确数值的提示（HIG、MD）
- `axis-labels` - 坐标轴带单位与可读刻度；移动端避免截断或过度旋转标签
- `responsive-chart` - 小屏须重排或简化（如横条替代竖条、减少刻度）
- `empty-data-state` - 无数据时展示有意义空状态（「暂无数据」+ 引导），勿留白图（MD）
- `loading-chart` - 数据加载中用骨架或微光占位；勿只显示空坐标轴
- `animation-optional` - 图表入场动效须尊重 prefers-reduced-motion；数据应立即可读（HIG）
- `large-dataset` - 1000+ 点时聚合或抽样；详情用下钻而非一次渲染全部（MD）
- `number-formatting` - 轴与标签使用区域化数字、日期、货币格式（HIG、MD）
- `touch-target-chart` - 可点图表元素（点、段）触控区 ≥44pt 或触摸时扩大（Apple HIG）
- `no-pie-overuse` - 类别 >5 时少用饼/环；改用条形更清晰
- `contrast-data` - 数据线/条与背景 ≥3:1；数据文字标签 ≥4.5:1（WCAG）
- `legend-interactive` - 图例可点击切换系列显隐（MD）
- `direct-labeling` - 数据量小时直接在图上标注数值，减少视线移动
- `tooltip-keyboard` - 提示内容须键盘可达，不单靠悬停（WCAG）
- `sortable-table` - 数据表支持排序，并用 aria-sort 表示当前排序（WCAG）
- `axis-readability` - 刻度勿过密；小屏自动间隔刻度保持可读
- `data-density` - 控制单图信息密度，避免认知过载；必要时拆成多图
- `trend-emphasis` - 强调数据趋势而非装饰；避免厚重渐变/阴影遮挡数据
- `gridline-subtle` - 网格线低对比（如 gray-200），不与数据争抢视觉
- `focusable-elements` - 可交互图表元素须支持键盘导航（WCAG）
- `screen-reader-summary` - 提供文字摘要或 aria-label 描述图表关键结论（WCAG）
- `error-state-chart` - 加载失败须显示错误与重试，勿显示破损/空白图
- `export-option` - 数据型产品可提供 CSV/图片导出
- `drill-down-consistency` - 下钻须保留清晰返回路径与层级面包屑
- `time-scale-clarity` - 时间序列须标明粒度（日/周/月）并允许切换

## 如何使用

使用下方 CLI 工具按领域检索。

---

## 环境准备

检查是否已安装 Python：

```bash
python3 --version || python --version
```

若未安装，按操作系统安装：

**macOS：**
```bash
brew install python3
```

**Ubuntu/Debian：**
```bash
sudo apt update && sudo apt install python3
```

**Windows：**
```powershell
winget install Python.Python.3.12
```

---

## 本 Skill 的使用方式

当用户提出以下任一类需求时使用本 Skill：

| 场景 | 触发示例 | 从哪一步开始 |
|------|------------|--------------|
| **新项目 / 新页面** | 「做一个落地页」「做一个控制台」 | 步骤 1 → 步骤 2（设计系统） |
| **新组件** | 「做一个定价卡片」「加一个弹窗」 | 步骤 3（领域检索：style、ux） |
| **选风格 / 配色 / 字体** | 「金融科技类 App 适合什么风格？」「推荐一套配色」 | 步骤 2（设计系统） |
| **评审现有 UI** | 「评审这页的体验问题」「检查无障碍」 | 上文速查清单 |
| **修 UI Bug** | 「按钮悬停坏了」「加载时布局会跳」 | 速查清单 → 对应小节 |
| **改进 / 优化** | 「让这页更快」「改善移动端体验」 | 步骤 3（领域检索：ux、react） |
| **实现深色模式** | 「加深色模式支持」 | 步骤 3（领域 style，关键词含 dark mode） |
| **加图表 / 数据可视化** | 「控制台里加一张分析图」 | 步骤 3（领域 chart） |
| **技术栈最佳实践** | 「React 性能技巧」「SwiftUI 导航」 | 步骤 4（栈检索） |

按以下工作流执行：

### 步骤 1：分析用户需求

从用户描述中提取：
- **产品类型**：娱乐（社交、视频、音乐、游戏）、工具（扫描、编辑、转换）、效率（待办、笔记、日历）或混合型
- **目标用户**：C 端消费者；考虑年龄段与使用场景（通勤、休闲、办公）
- **风格关键词**：活泼、高饱和、极简、深色模式、内容优先、沉浸感等
- **技术栈**：以项目为准（文档示例为 React Native，可按实际栈改用 `--stack`）

### 步骤 2：生成设计系统（必填）

**务必先用 `--design-system`**，获得带推理的完整推荐：

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<产品类型> <行业> <关键词>" --design-system [-p "项目名称"]
```

该命令会：
1. 并行检索多个领域（product、style、color、landing、typography）
2. 依据 `ui-reasoning.csv` 中的规则选出最匹配项
3. 返回完整设计系统：版式模式、风格、色彩、字体、动效
4. 包含应避免的反模式

**示例：**
```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

### 步骤 2b：持久化设计系统（主文件 + 页面覆盖）

若需在**多次会话中分层读取**设计系统，加上 `--persist`：

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<查询>" --design-system --persist -p "项目名称"
```

将生成：
- `design-system/<项目slug>/MASTER.md` — 全局设计规则（单一事实来源）
- `design-system/<项目slug>/pages/` — 存放各页面覆盖规则

**带页面级覆盖时：**
```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<查询>" --design-system --persist -p "项目名称" --page "dashboard"
```

还会生成：
- `design-system/<项目slug>/pages/dashboard.md` — 相对 Master 的页面级差异

**分层读取逻辑：**
1. 实现具体页面（如「结账」）时，先看 `design-system/<项目slug>/pages/checkout.md`
2. 若该文件存在，其规则**覆盖** Master
3. 若不存在，仅使用 `design-system/<项目slug>/MASTER.md`

**可粘贴给模型的检索提示：**
```
我正在实现 [页面名] 页面。请先阅读 design-system/<项目slug>/MASTER.md。
再检查是否存在 design-system/<项目slug>/pages/[页面名].md。
若页面文件存在，优先遵守其中的规则。
若不存在，仅使用 Master 中的规则。
接下来请生成代码……
```

### 步骤 3：按需补充细粒度检索

拿到设计系统后，可用领域检索补充细节：

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<关键词>" --domain <领域> [-n <最多条数>]
```

**何时做细粒度检索：**

| 需求 | 领域 | 示例 |
|------|------|------|
| 产品类型版式 | `product` | `--domain product "entertainment social"` |
| 更多风格选项 | `style` | `--domain style "glassmorphism dark"` |
| 配色方案 | `color` | `--domain color "entertainment vibrant"` |
| 字体搭配 | `typography` | `--domain typography "playful modern"` |
| 图表建议 | `chart` | `--domain chart "real-time dashboard"` |
| UX 最佳实践 | `ux` | `--domain ux "animation accessibility"` |
| 备选字体 | `typography` | `--domain typography "elegant luxury"` |
| 单个 Google Font | `google-fonts` | `--domain google-fonts "sans serif popular variable"` |
| 落地页结构 | `landing` | `--domain landing "hero social-proof"` |
| React Native 性能 | `react` | `--domain react "rerender memo list"` |
| 应用界面无障碍 | `web` | `--domain web "accessibilityLabel touch safe-areas"` |
| AI 提示 / CSS 关键词 | `style` | `--domain style "minimalism AI CSS variables"` |

### 步骤 4：栈级指南（如 React Native）

获取与具体实现栈相关的最佳实践：

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<关键词>" --stack react-native
```

---

## 检索参考

### 可用领域（Domain）

| 领域 | 用途 | 示例关键词 |
|------|------|------------|
| `product` | 产品类型与版式建议 | SaaS、e-commerce、portfolio、healthcare、beauty、service |
| `style` | UI 风格、色彩、动效 | glassmorphism、minimalism、dark mode、brutalism |
| `typography` | 字体搭配、Google Fonts | elegant、playful、professional、modern |
| `color` | 按产品类型的配色 | saas、ecommerce、healthcare、beauty、fintech、service |
| `landing` | 页面结构、CTA 策略 | hero、hero-centric、testimonial、pricing、social-proof |
| `chart` | 图表类型、库建议 | trend、comparison、timeline、funnel、pie |
| `ux` | 最佳实践与反模式 | animation、accessibility、z-index、loading |
| `google-fonts` | 单个字体查询 | sans serif、monospace、japanese、variable font、popular |
| `react` | React/Next.js 性能 | waterfall、bundle、suspense、memo、rerender、cache |
| `web` | 应用界面指南（iOS/Android/React Native） | accessibilityLabel、touch targets、safe areas、Dynamic Type |

（`style` 检索列含 AI/CSS 相关关键词，无单独 `prompt` 领域。）

### 可用技术栈（Stack）

| 栈 | 侧重点 |
|----|--------|
| `react-native` | 组件、导航、列表 |

（完整栈列表见 `scripts/search.py` 的 `--stack` 可选值。）

---

## 示例工作流

**用户：**「做一个 AI 搜索首页。」

### 步骤 1：分析需求
- 产品类型：工具（AI 搜索引擎）
- 目标用户：需要快速、智能搜索的 C 端用户
- 风格关键词：现代、极简、内容优先、深色模式
- 技术栈：按项目（示例为 React Native）

### 步骤 2：生成设计系统（必填）

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "AI search tool modern minimal" --design-system -p "AI Search"
```

**输出：** 含版式模式、风格、色彩、字体、动效与反模式的完整设计系统。

### 步骤 3：按需补充检索

```bash
# 现代工具类产品的风格选项
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "minimalism dark mode" --domain style

# 搜索交互与加载相关的 UX
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "search loading animation" --domain ux
```

### 步骤 4：栈级指南

```bash
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "list performance navigation" --stack react-native
```

**然后：** 综合设计系统与细粒度检索结果，再落地实现。

---

## 输出格式

`--design-system` 支持两种输出：

```bash
# ASCII 框（默认）— 适合终端查看
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system

# Markdown — 适合写入文档
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "fintech crypto" --design-system -f markdown
```

---

## 提升检索效果的建议

### 查询策略

- 使用**多维关键词** — 组合产品 + 行业 + 气质 + 信息密度：`"entertainment social vibrant content-dense"`，不要只搜 `"app"`
- 同一需求可换词尝试：`"playful neon"` → `"vibrant dark"` → `"content-first minimal"`
- 先 `--design-system` 拿全局推荐，再对不确定的维度用 `--domain` 深挖
- 需要实现层建议时加上 `--stack <你的栈>`

### 常见卡点

| 问题 | 建议做法 |
|------|----------|
| 定不下风格/配色 | 换关键词重新跑 `--design-system` |
| 深色模式对比度 | 速查第 6 节：`color-dark-mode` + `color-accessible-pairs` |
| 动效不自然 | 速查第 7 节：`spring-physics` + `easing` + `exit-faster-than-enter` |
| 表单体验差 | 速查第 8 节：`inline-validation` + `error-clarity` + `focus-management` |
| 导航混乱 | 速查第 9 节：`nav-hierarchy` + `bottom-nav-limit` + `back-behavior` |
| 小屏布局崩 | 速查第 5 节：`mobile-first` + `breakpoint-consistency` |
| 性能卡顿 | 速查第 3 节：`virtualize-lists` + `main-thread-budget` + `debounce-throttle` |

### 交付前自检（文档级）

- 实现前可跑一遍：`--domain ux "animation accessibility z-index loading"` 做体验校验
- 最后用速查 **第 1–3 节**（关键 + 高优先级）过一遍
- 在 375px 小屏与横屏下查看
- 开启 **减弱动态效果**、**最大字号** 验证布局
- 深色模式对比度单独测（勿默认沿用浅色数值）
- 确认触控目标 ≥44pt，内容不被安全区遮挡

---

## 专业级 App 界面的常见规则

下列问题常被忽略，导致界面显得不专业：  
**范围说明：** 以下针对 **App UI**（iOS / Android / React Native / Flutter），不是桌面 Web 专属交互范式。

### 图标与视觉元素

| 规则 | 建议做法 | 避免 | 原因 |
|------|----------|------|------|
| **不要用 Emoji 当结构图标** | 使用矢量图标（如 Lucide、react-native-vector-icons、@expo/vector-icons）。 | 用 Emoji（🎨 🚀 ⚙️）做导航、设置或系统级控件。 | Emoji 依赖字体、跨平台不一致，无法用设计 token 精确控制。 |
| **尽量只用矢量资源** | 使用 SVG 或平台矢量图标，清晰缩放且易主题化。 | 易糊、易锯齿的栅格 PNG 小图标。 | 保证清晰度与明暗模式适配。 |
| **稳定的按下态** | 用颜色、不透明度或 elevation 过渡表示按下，不改变布局占位。 | 会挤动周围内容的 transform，造成视觉抖动。 | 避免不稳定交互，保持移动端观感顺滑。 |
| **品牌 Logo 规范** | 使用官方素材并遵守间距、颜色、留白规范。 | 随意改比例、非官方改色、路径乱猜。 | 避免品牌误用与合规风险。 |
| **图标尺寸一致** | 用设计 token 定义尺寸（如 icon-sm / icon-md=24pt / icon-lg）。 | 20pt / 24pt / 28pt 随意混用。 | 保持节奏与层级一致。 |
| **线宽一致** | 同一视觉层级内线宽统一（如 1.5px 或 2px）。 | 同一层级粗细混用。 | 粗细不一会降低精致感与统一感。 |
| **实心 / 线框图标纪律** | 同一层级只用一种图标风格。 | 同一层级混用实心与线框。 | 语义与风格更清晰。 |
| **触控目标下限** | 可点区域至少 44×44pt（图标小时用 hitSlop 扩大）。 | 小图标无扩展热区。 | 满足无障碍与平台可用性。 |
| **图标对齐** | 与文字基线对齐，周围留白一致。 | 图标歪斜、间距忽大忽小。 | 避免细微失衡拉低质感。 |
| **图标对比度** | 小元素遵循 WCAG 4.5:1；较大图形符号至少约 3:1。 | 与背景融为一体的低对比图标。 | 明暗模式下都可辨识。 |

### 交互（App）

| 规则 | 建议 | 不建议 |
|------|------|--------|
| **点按反馈** | 80–150ms 内给出明确按下反馈（涟漪/透明度/elevation） | 点按无任何视觉反馈 |
| **动效时长** | 微交互约 150–300ms，缓动贴近系统默认 | 瞬时切换或过长动效（>500ms） |
| **无障碍焦点** | 读屏焦点顺序与视觉一致，标签描述清楚 | 无标签或焦点顺序混乱 |
| **禁用态清晰** | 使用 `disabled` 等语义、降低强调、不可点 | 看起来像可点但实际无响应 |
| **触控目标** | iOS ≥44×44pt，Android ≥48×48dp；图标小时扩大热区 | 极小热区或无内边距的纯图标区 |
| **手势冲突** | 同一区域单一主手势，避免嵌套点按/拖拽冲突 | 手势重叠导致误操作 |
| **语义化原生控件** | 优先 `Button`、`Pressable` 等并设好无障碍角色 | 无角色的通用容器冒充主控件 |

### 明暗模式对比

| 规则 | 建议 | 不建议 |
|------|------|--------|
| **浅色表面可读** | 卡片/表面与背景有足够对比或 elevation | 过度透明导致层级不清 |
| **浅色正文对比** | 正文与浅色表面 ≥4.5:1 | 浅灰低对比正文 |
| **深色正文对比** | 主文 ≥4.5:1，次级文深色底上 ≥3:1 | 深色模式文字融进背景 |
| **分割线可见性** | 两种主题下分割线都可见 | 某一主题下分割线「消失」 |
| **状态对比一致** | 按下/聚焦/禁用在两套主题下都可区分 | 只给浅色定义交互态 |
| **Token 驱动主题** | 用语义色 token 映射各主题的表面/文字/图标 | 每屏写死 hex |
| **遮罩与弹窗可读** | 弹窗遮罩足够深（常见约 40–60% 黑）以隔离前景 | 遮罩过浅导致背景抢戏 |

### 布局与间距

| 规则 | 建议 | 不建议 |
|------|------|--------|
| **安全区** | 固定顶栏、Tab、底栏 CTA 遵守上下安全区 | 内容顶到刘海、状态栏、手势条 |
| **系统栏留白** | 为状态栏、导航栏、Home 指示条留间距 | 可点内容与系统栏重叠 |
| **内容宽度一致** | 手机/平板各类设备宽度策略可预期 | 各屏宽度随意 |
| **8dp 间距节奏** | 内边距/间距/分区用统一 4/8dp 体系 | 无节奏的任意间距 |
| **长文可读行长** | 大屏长文控制行长，避免通栏段落 | 平板通栏长段落难读 |
| **分区垂直节奏** | 按层级定义 16/24/32/48 等阶梯 | 同级界面间距忽大忽小 |
| **响应式左右留白** | 大屏与横屏增大水平 inset | 所有尺寸同一窄边距 |
| **滚动与固定栏共存** | 列表底部/顶部加 inset，避免被固定栏挡住 | 内容被粘性头/底遮挡 |

---

## 交付前自检清单

交付 UI 代码前请核对：  
**范围：** 适用于 App UI（iOS / Android / React Native / Flutter）。

### 视觉质量
- [ ] 未用 Emoji 代替图标（使用 SVG 等）
- [ ] 图标来自统一图标族与线宽风格
- [ ] 品牌素材比例与留白正确
- [ ] 按下态不改变布局占位、不引起抖动
- [ ] 统一使用语义主题 token，无每屏随意硬编码色值

### 交互
- [ ] 可点元素有清晰按下反馈（涟漪/透明度/elevation）
- [ ] 触控目标满足下限（iOS ≥44×44pt，Android ≥48×48dp）
- [ ] 微交互时长在约 150–300ms，缓动自然
- [ ] 禁用态一眼可辨且不可交互
- [ ] 读屏焦点顺序与视觉一致，交互控件标签清楚
- [ ] 手势区域避免点按/拖拽/系统返回手势冲突

### 明暗模式
- [ ] 主文在浅色与深色下对比度均 ≥4.5:1
- [ ] 次级文在两种模式下对比度均 ≥3:1
- [ ] 分割线、边框与交互态在两种模式下都可区分
- [ ] 弹窗/抽屉遮罩足够深，前景可读（常见约 40–60% 黑）
- [ ] 两套主题均实测过（勿只凭一套推断另一套）

### 布局
- [ ] 顶栏、Tab、底栏 CTA 遵守安全区
- [ ] 滚动内容不被固定/粘性头底遮挡
- [ ] 小屏手机、大屏手机、平板（竖屏+横屏）均查看过
- [ ] 水平留白随设备尺寸与方向合理变化
- [ ] 组件、分区、页面级均保持 4/8dp 间距节奏
- [ ] 大屏长文行长可读，避免通栏长段落

### 无障碍
- [ ] 有意义的图片/图标有读屏标签
- [ ] 表单有标签、提示与清晰错误信息
- [ ] 不单靠颜色传达状态
- [ ] 支持减弱动效与动态字号且布局不崩
- [ ] selected、disabled、expanded 等特征/角色/状态读屏播报正确