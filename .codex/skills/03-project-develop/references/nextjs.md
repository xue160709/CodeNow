# Next.js 开发参考（03-project-develop）

仅在 `TODO.md` 主框架为 **Next.js** 时读取本文件。

## 栈与结构

- 使用 Next.js **App Router + TypeScript**。
- 将设计 token 落地到 `globals.css`、Tailwind 配置或现有样式系统。
- 按 PRD 主路径创建页面、布局、组件和状态逻辑。
- 可交互元素（button、link、input、select、对话框/模态等）须预埋 `data-testid`，命名与范围见 `project-verify/references/selector-and-testid.md`，供 `project-verify` 使用 Playwright 验收。

## API 与安全

- 需要远程 API 时使用 `app/api/**` Route Handler 或 Server Action 封装；**前端只调用同源接口**，不直连第三方。
- API Key 只从服务端环境变量读取，不写入客户端 bundle。
- 每个 Route Handler 必须有调用日志（见 [logging-and-debugging.md](logging-and-debugging.md)）。

## 常用命令

以项目 `package.json` scripts 为准，常见为：

- `npm run dev` — 本地开发
- `npm run lint` / `npm run test` / 类型检查 — 默认验证
- `npm run build` — 按需生产构建，仅发布/部署或构建产物验证时执行

## 交付说明

- 写明实际启动命令与访问 URL（含端口）。
- 若使用 API Key，说明 `.env.local` 变量名与 Token Plan 配置步骤。

## Dev 刷新

- Renderer 使用 Vite/Next 自带 Fast Refresh；改 Server Component / Route Handler 后通常需刷新页面或重新请求。
