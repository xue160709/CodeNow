# vite-web-extension 开发参考（03-project-develop）

仅在 `TODO.md` 主框架为 **vite-web-extension**（浏览器插件）时读取本文件。

## 起点

- 使用 [JohnBra/vite-web-extension](https://github.com/JohnBra/vite-web-extension) 或沿用仓库已有插件结构。
- 新建或补齐源码时使用 **React + TypeScript + Tailwind**；popup、options、side panel、content script、background/service worker 等入口优先使用 `.tsx` / `.ts`。
- 默认 **Chrome Manifest V3**；构建产物默认 `dist_chrome`（以项目配置为准）。

## 入口（按 TODO 保留）

- popup
- options
- content script
- background / service worker
- side panel
- new tab

更新 `manifest.json` / `manifest.dev.json` 的名称、描述、权限和入口；删除不需要的模板页面。

## API Key 与安全

- **没有服务端后端**；不得把私密 Key 写进 `.env`、源码或构建包。
- 默认：用户在 options/popup 填写 Key → 存 `chrome.storage.local`（PRD 明确要求 `localStorage` 时仅用于扩展页面上下文）。
- background/service worker 读取 storage 并发起请求；**不是**服务端后端。
- content script **不直接持有** Key。
- 只有 PRD 明确要求时才规划代理；否则不要默认加代理服务。

## 调用日志

- background 发起远程请求时必须打日志（见 [logging-and-debugging.md](logging-and-debugging.md)）。
- options/popup 保存 Key 时只 log 脱敏摘要（如 `keyLength`），不 log 原文。

## Dev 刷新

- 只有需要验证或加载构建产物时才重新 build，并在 `chrome://extensions/` 点击扩展「刷新」；日常代码验收优先跑 lint/test/typecheck 与可预览入口。
- service worker 可能被浏览器休眠；调试时注意重新加载扩展。

## 交付说明

1. 运行构建命令生成输出目录（通常 `dist_chrome`）
2. 打开 `chrome://extensions/` → 开发者模式 → 加载已解压扩展
3. 说明用户应从哪个入口开始使用（popup / options / side panel 等）
