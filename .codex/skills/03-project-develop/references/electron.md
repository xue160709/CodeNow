# Electron 开发参考（03-project-develop）

仅在 `TODO.md` 主框架为 **Electron** 时读取本文件。

## 脚手架与栈选择（硬约束）

- 使用官方 npm 包 `electron`。新建或补齐栈时按大版本 30 规划：`package.json` 写 `electron: ^30.0.1`；以锁文件实际解析版本为准。
- **新建项目必须用** `npm create electron-vite@latest`；不要手搓「frontend Vite + client electron-forge」双项目结构，除非 TODO 明确要求沿用已有仓库且 dev 刷新已验证。
- UI 框架按 PRD、TODO 或脚手架选择 Vanilla / Vue / React。
- 常见目录（以脚手架生成为准）：
  - 渲染进程：`src/`
  - 主进程：`electron/main/index.ts` 或 `electron/main.ts`
  - 预加载：`electron/preload/index.ts` 或 `electron/preload.ts`
  - 配置：`electron.vite.config.ts`

## 进程边界

| 进程 | 职责 |
| --- | --- |
| **main** | 窗口、系统能力、本地文件、环境变量密钥、API 封装 |
| **preload** | `contextBridge` 暴露最小安全 API；路径指向**构建产物** |
| **renderer** | UI 与交互；不直接读 Node 私密能力 |

- 默认 `contextIsolation: true`，避免不必要的 `nodeIntegration`。

## 三类开发刷新

| 进程 | 机制 | 默认是否自动 |
| --- | --- | --- |
| **Renderer** | Vite HMR | ✅ 配置正确时 |
| **Preload** | 重建 + 刷新 renderer | ❌ 需 `--watch` 或 `build.watch` |
| **Main** | 重建 + **重启整个 app** | ❌ 需 `--watch` 或 `build.watch` |

官方：[electron-vite HMR and Hot Reloading](https://electron-vite.org/guide/hmr-and-hot-reloading)

## Dev 脚本（必做）

**方式 A（推荐）**：

```json
{
  "scripts": {
    "dev": "electron-vite dev --watch",
    "build": "electron-vite build",
    "preview": "electron-vite preview"
  }
}
```

**方式 B**：`electron.vite.config.ts` 中 `main.build.watch` 与 `preload.build.watch` 设为 `{}`。

禁止 `"dev": "electron-vite dev"` 却期望 main/preload 自动生效。

## Main 窗口加载（Renderer HMR 前提）

```ts
if (!app.isPackaged && process.env.ELECTRON_RENDERER_URL) {
  mainWindow.loadURL(process.env.ELECTRON_RENDERER_URL)
} else {
  mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'))
}
```

**禁止**：硬编码 `localhost:5173`；dev 态 `loadFile` 源码 html；混用 `VITE_DEV_SERVER_URL` 与 `ELECTRON_RENDERER_URL`。

## 开发顺序（业务代码之前）

1. `npm run dev` → 窗口非白屏
2. 改 renderer 可见文本 → HMR 无需手动刷新
3. 改 preload → renderer 自动刷新
4. 改 main → app 自动重启

失败则先修 config / scripts / loadURL，再写业务。

## 故障排查

| 现象 | 修复 |
| --- | --- |
| 白屏 / 旧页 | 改用 `ELECTRON_RENDERER_URL` |
| 改 UI 无反应 | dev 分支 loadURL |
| 改 preload/main 无反应 | dev 加 `--watch` |
| IPC undefined | preload 指向构建产物 |

## API Key 与日志

- Key 只在 main 或安全 preload 后读取；renderer 不持有 Key。
- main / preload 的 IPC 与 API 调用必须打日志（见 [logging-and-debugging.md](logging-and-debugging.md)）。

## 交付说明

- `npm run dev` 须含 watch；说明 main 重启会丢状态。
- 日常 UI 开发依赖 renderer HMR。
