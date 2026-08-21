# Next.js 验证参考

仅在 `TODO.md` 主框架为 **Next.js** 时读取。

## 前置

1. 读 `references/selector-and-testid.md`，确认本轮触及的交互元素有稳定 `data-testid`。
2. 读 `references/browser-playwright.md`，准备 `playwright-cli` / `test-results/`。
3. 启动实际 dev 或 preview 服务，记录端口。

## 静态验证

按项目 scripts 跑：

- `lint`
- `test`
- 类型检查（若有）

`build` 默认不跑；仅在用户要求、发布/部署前或 TODO 明确要求验证构建产物时按需执行。`lint` / `test` / 类型检查失败时，UI 项和相关非 UI 项不得打勾；先记录阻塞或交给开发 Skill 修复。

## 动态验证

推荐流程：

```bash
playwright-cli open http://localhost:3000 --persistent
playwright-cli snapshot
playwright-cli screenshot --filename=test-results/initial.png
```

登录/会话类流程：

```bash
playwright-cli fill "data-testid=login-input-email" "test@example.com"
playwright-cli fill "data-testid=login-input-password" "password"
playwright-cli click "data-testid=login-btn-submit"
playwright-cli goto http://localhost:3000/dashboard
```

若元素缺失：

1. 先 `snapshot` 或 Python Playwright 侦察。
2. 确认是 testid 缺失还是 UI 未渲染。
3. testid 缺失可补最小 testid 后复验；UI bug 则记录失败。

## API / Route Handler

- 关键 Route Handler 可用 `curl` 直接测状态、错误态和响应结构。
- 无 API Key 时，只验未配置提示、错误态、空态；真实远程调用标跳过。
- console / 服务端日志不得包含 Key、Token、用户隐私原文。

## TODO 回写建议

- `lint/test/typecheck` 通过只能勾 §8 或静态验证项。
- §2 用户流程必须有浏览器证据或明确半自动证据。
- 缺 testid 导致无法机器验收时，§2 不打勾；补 testid 任务写回 TODO。
