# 浏览器自动化与 Playwright 参考

用于 Web UI 动态验证、截图取证、console/network 排查。Next.js、Electron renderer、插件 popup/options 静态预览都可复用。

## 工具选择

| 场景 | 优先工具 |
| --- | --- |
| 少量点击、填表、截图、保持登录态 | `playwright-cli` |
| 连续操作、批量截图、捕获交互期间 console、侦察 DOM | Python Playwright |
| 服务没启动或端口不明 | 先启动服务并确认 URL，再自动化 |

## playwright-cli 准备

任何 `playwright-cli` 命令前先执行：

```bash
if command -v playwright-cli >/dev/null 2>&1; then
  playwright-cli --version
else
  npm install -g playwright-cli
  command -v playwright-cli >/dev/null 2>&1 || exit 1
fi

mkdir -p test-results
```

全局安装因权限、沙箱或网络失败时，不要重复空转。该会话统一降级为：

```bash
npx --yes playwright-cli open http://localhost:3000 --persistent
npx --yes playwright-cli click "data-testid=home-btn-submit"
```

若仍不可用，在 `TESTING_CHECKLIST.md` / `TODO.md` 验证记录中标 `⚠️ 阻塞`；UI 项不得打勾。

## 常用命令

```bash
playwright-cli open http://localhost:3000 --persistent
playwright-cli goto http://localhost:3000/dashboard
playwright-cli fill "data-testid=login-input-email" "test@example.com"
playwright-cli click "data-testid=login-btn-submit"
playwright-cli screenshot --filename=test-results/login-success.png
playwright-cli snapshot
playwright-cli console
playwright-cli network
playwright-cli close
```

保持登录态：第一次用 `open --persistent`，后续页面跳转用 `goto`。

## 先侦察再操作

动态应用不要刚 `goto` 就查 DOM。先等待渲染完成，再截图或读取元素：

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto("http://localhost:3000")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="test-results/inspect.png", full_page=True)
    print(page.locator("button").count())
    browser.close()
```

## 捕获 console 日志

交互期间的日志比操作后单次 `console` 更完整：

```python
from playwright.sync_api import sync_playwright

logs = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1440, "height": 900})

    def on_console(msg):
        line = f"[{msg.type}] {msg.text}"
        logs.append(line)
        print(line)

    page.on("console", on_console)
    page.goto("http://localhost:3000")
    page.wait_for_load_state("networkidle")
    page.click("text=Dashboard")
    page.wait_for_timeout(1000)
    browser.close()

with open("test-results/console.log", "w") as f:
    f.write("\n".join(logs))
```

## 静态 HTML / 构建产物

插件 popup/options 或普通静态页可用 `file://` 预览：

```python
from pathlib import Path
from playwright.sync_api import sync_playwright

url = Path("dist_chrome/popup.html").resolve().as_uri()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto(url)
    page.screenshot(path="test-results/popup-static.png", full_page=True)
    browser.close()
```

## 证据要求

- 截图放 `test-results/`。
- console/network 输出只摘要关键错误和状态，不贴密钥、Token、用户隐私原文。
- 失败时记录：操作步骤、实际现象、错误日志、截图路径、下一步。

## 常见失败

| 现象 | 处理 |
| --- | --- |
| `command not found` | 执行准备步骤；失败则用 `npx --yes`；仍失败标阻塞 |
| 元素找不到 | 先 `snapshot` / Python DOM 侦察；优先补 `data-testid` |
| 登录态丢失 | 使用 `open --persistent` + `goto` |
| 页面加载超时 | 检查 dev server、端口、终端日志 |
| 动态 DOM 未出现 | 等 `networkidle` 或具体 `wait_for_selector` |
