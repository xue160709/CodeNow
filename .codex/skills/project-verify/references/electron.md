# Electron 验证参考

仅在 `TODO.md` 主框架为 **Electron** 时读取本文件。

若验证 renderer Web UI，可同时读取：

- `selector-and-testid.md`：renderer 交互元素稳定选择器
- `browser-playwright.md`：能用 URL 预览 renderer 时的截图/console 证据

## 环境准备

```bash
npm install
mkdir -p test-results
npm run dev    # 应为 electron-vite dev --watch 或等效 watch 配置
```

## 静态验证（必做）

- `npm run lint`（若有）
- `npm run test`（若有）
- 类型检查（若有 script 或 `tsc --noEmit`）
- `npm run build` 默认不跑；仅在打包、发布或 TODO 明确要求验证构建产物时按需执行

## 动态验证策略

Electron GUI 自动化成本高；MVP 阶段采用 **「静态 + smoke + 配置核对 + 可选半自动」**：

### 1. 启动 smoke

- dev 命令能拉起窗口或进程不立即 crash
- 终端无致命 error；main 日志有窗口创建成功类输出

### 2. 配置核对（TODO 若要求三类刷新）

| 项 | 核对方式 |
| --- | --- |
| `dev` 含 `--watch` 或 config 开 `build.watch` | 读 `package.json` / `electron.vite.config.ts` |
| main dev 用 `ELECTRON_RENDERER_URL` | grep main 入口，无硬编码 localhost 端口 |
| renderer HMR | 改 renderer 文案，观察是否热更新（或用户确认） |
| preload 刷新 | 改 preload 暴露 API，观察 renderer 是否刷新 |
| main 重启 | 改 main，观察 app 是否重启 |

无法在 Agent 环境跑 GUI 时：完成配置核对 + 启动 smoke，其余标 `⚠️ 跳过：需本地 GUI 确认`，并在验证记录列出用户本地步骤。

### 3. IPC / API（若有）

- 通过 devtools console 或预埋日志验证 preload 暴露方法可调用
- main 进程 API 调用应有日志（见 03 logging reference）
- renderer 可通过 Web URL 预览时，按 `browser-playwright.md` 截图并捕获 console；不可预览时写清 GUI 手动步骤。

## 写回 TODO 建议

- lint/test/typecheck 通过 + dev 启动 smoke 通过 → §8 静态项可勾
- 三类刷新若仅配置核对 → §2 相关项标跳过或部分通过，勿虚假打勾
