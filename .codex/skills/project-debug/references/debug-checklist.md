# Debug 检查清单

## 开始前

- [ ] 已读取 `TODO.md` 和相关验收标准。
- [ ] 已确认问题入口、触发步骤、预期行为、实际行为。
- [ ] 已确认项目类型、启动命令、端口、测试命令。
- [ ] 涉及浏览器时已读取 `../../project-verify/references/browser-playwright.md`。

## 证据采集

- [ ] console 错误或无错误结论。
- [ ] network 请求状态。
- [ ] server / dev terminal 输出。
- [ ] curl 或 TypeScript 脚本验证关键 API。
- [ ] 截图或 snapshot，能说明用户看到的状态。

## 定位

- [ ] 已用 `rg` 找到事件 handler、API 路由、状态更新或数据转换位置。
- [ ] 必要时已植入临时探针。
- [ ] 每次只改一个主要可疑点。
- [ ] 已确认根因，不只是修了表面现象。

## 修复

- [ ] 改动范围尽量小。
- [ ] 没有回滚用户已有无关改动。
- [ ] API / IPC / 第三方请求已按规范补日志。
- [ ] 临时探针已删除或整理为长期脱敏日志。
- [ ] 复杂逻辑补了中文注释，说明为什么这样做。

## 验证

- [ ] lint / typecheck / build / test 至少执行可用项。
- [ ] 原复现路径已重新执行。
- [ ] 失败、跳过或阻塞有清楚原因。
- [ ] TODO.md 已回写。

## 常用命令

```bash
# 搜索
rg -n "login|auth|handleSubmit|fetch|axios" .

# 浏览器
playwright-cli console
playwright-cli network
playwright-cli snapshot
playwright-cli screenshot --filename=test-results/debug.png

# API
curl -s http://localhost:4000/api/example
curl -s -o /dev/null -w "%{http_code}" http://localhost:4000/api/example

# 端口
lsof -i :4000

# Node 进程
ps aux | grep node
```

## 汇报模板

```text
根因：<一句话>
改动：<文件和行为>
验证：<命令 / 浏览器证据>
TODO：<已回写内容>
剩余风险：<无 / API Key 不可用 / 外部服务待用户本地确认>
```
