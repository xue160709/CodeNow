# Chrome Extension 验证参考

仅在 `TODO.md` 主框架为 **vite-web-extension** 时读取本文件。

若 popup/options/side panel/new tab 可作为普通 Web 页面预览，可同时读取：

- `selector-and-testid.md`：扩展页面交互元素稳定选择器
- `browser-playwright.md`：`file://` 或 dev server 预览、截图、console 证据

## 环境准备

```bash
npm install
mkdir -p test-results
```

确认 `manifest.json` / 扩展入口与 TODO 一致。`npm run build` 默认不跑；仅在需要验证已解压扩展加载目录、发布/打包或用户明确要求时执行。

## 静态验证（必做）

- `npm run lint`（若有）
- `npm run test`（若有）
- 类型检查（若有 script 或 `tsc --noEmit`）

## 动态验证策略

浏览器扩展通常无法在无头环境完整自动化加载；默认采用 **manifest/入口核对 + 测试脚本 + 可选 popup 预览**。只有确实需要加载已解压扩展目录时，才增加构建验证。

### 1. 构建验证（按需）

- 构建 exit 0
- `dist_chrome`（或实际目录）含 `manifest.json`、background、popup/options 等 TODO 要求的入口文件

### 2. 加载走查（文档化 + 用户或 playwright 有限支持）

在 `TESTING_CHECKLIST.md` 写明：

1. 打开 `chrome://extensions/`
2. 开启「开发者模式」
3. 「加载已解压的扩展程序」→ 选择构建输出目录
4. 点击扩展图标 / 打开 options / side panel（按 TODO 实际入口）

Agent 无法操作 Chrome UI 时：构建通过 + 清单步骤完整 → 动态项标 `⚠️ 跳过：需 Chrome 手动加载`，**不要**假打勾「popup 可打开」类条目。

### 3. 可自动化部分（若 popup 为普通 HTML 且可本地预览）

- 对 options/popup 的**静态 HTML 构建产物**做 playwright 打开 `file://` 或 dev server 预览（仅当项目支持）
- 交互控件优先用 `data-testid` 定位；缺失时记录后续补齐任务，不假打勾
- `chrome.storage.local` 逻辑：在单元/脚本层测读写（可选，非 MVP 必做）

### 4. API Key（插件常见）

- 无 Key：验 options 保存 UI、空 Key 提示
- 有 Key：验 background fetch（看 service worker 日志）

## 写回 TODO 建议

- lint/test/typecheck + manifest 入口核对齐全 → §4/§8 部分项可勾
- 按需构建 + manifest 入口齐全 → 构建产物相关项可勾
- 真实「加载扩展后 popup 可用」→ 需人工或截图证据后再勾 §2
