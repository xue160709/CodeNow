# 浏览器与 API 排查

用于页面空白、按钮无响应、请求失败、数据没有刷新等浏览器相关问题。

## 前置

使用 `playwright-cli` 前，必须先读取并遵守：

```text
../../project-verify/references/browser-playwright.md
```

重点是安装检测、`npx --yes playwright-cli` 降级、`test-results/` 截图目录和不要反复执行失败命令。

## 主动扫描

```bash
# 打开页面
playwright-cli open http://localhost:4000 --persistent

# 读取浏览器 console
playwright-cli console

# 查看 network 请求
playwright-cli network

# 保存当前状态
playwright-cli screenshot --filename=test-results/debug-initial.png
```

如果 CLI 不可用，按 `browser-playwright.md` 使用 `npx --yes playwright-cli`，或退回 curl、服务端日志、项目测试和人工截图。

## 服务检查

```bash
# 确认服务响应状态码
curl -s -o /dev/null -w "%{http_code}" http://localhost:4000

# 检查健康接口
curl -s http://localhost:4000/api/health

# 检查端口占用
lsof -i :4000
```

## API 检查

```bash
# GET
curl -s -w "\n%{http_code}" http://localhost:4000/api/example

# POST
curl -s -X POST http://localhost:4000/api/example \
  -H "Content-Type: application/json" \
  -d '{"key":"value"}'

# 响应时间
curl -s -w "%{time_total}" -o /dev/null http://localhost:4000/api/example
```

记录时只保留关键摘要：路径、方法、状态码、响应形状、耗时、错误原因。不要记录 Token、Cookie、完整隐私文本。

## 操作后读取证据

```bash
# 清理旧 console，避免误判
playwright-cli eval "console.clear()"

# 执行用户操作
playwright-cli fill "data-testid=login-input-email" "admin@test.com"
playwright-cli click "data-testid=login-btn-submit"

# 再读取 console 和 network
playwright-cli console
playwright-cli network
```

若选择器不稳定，读取 `../../project-verify/references/selector-and-testid.md`，优先补稳定 `data-testid` 后再验证。

## 证据摘要格式

```text
页面：/login
操作：填写邮箱 -> 点击登录
console：无运行时错误 / 有 <错误摘要>
network：POST /api/login -> 401 / pending / failed
截图：test-results/login-failure.png
初步判断：请求已发出，失败在 API 返回或前端错误处理
```
