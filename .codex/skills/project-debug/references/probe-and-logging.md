# 探针与日志

用于证据不足、需要确认某段代码是否被执行、某个变量在哪一步变坏时。

## 临时探针

临时探针用于定位，修复后应删除，除非它被整理成长期必要日志。

```typescript
console.log('[debug:auth] submit entered', {
  hasEmail: Boolean(email),
  passwordLength: password.length,
})

console.log('[debug:auth] request result', {
  status: response.status,
  ok: response.ok,
})

console.log('[debug:state] before update', {
  previousUserId: user?.id ?? null,
  nextUserId: nextUser?.id ?? null,
})
```

不要输出密码、Token、Cookie、API Key、完整用户输入。

## 结构化探针

跨前后端排查时，用统一字段方便搜索：

```typescript
console.log(JSON.stringify({
  scope: 'debug',
  feature: 'login',
  stage: 'route-handler',
  timestamp: new Date().toISOString(),
  requestId,
  method,
  path,
  status,
}))
```

## 长期调用日志

涉及 API、IPC、第三方服务请求或降级逻辑时，长期日志必须覆盖：

- 调用入口：功能名、路径或 handler 名。
- 参数摘要：字段是否存在、数量、长度、枚举值；不得记录敏感原文。
- 成功结果：状态码、耗时、返回数据形状。
- 失败结果：错误类型、错误原因摘要、是否进入降级。

长期日志的详细规范见：

```text
../../03-project-develop/references/logging-and-debugging.md
```

## 前端读取探针

```bash
playwright-cli eval "console.clear()"
# 执行操作
playwright-cli console
```

如果 console 里探针没有出现，优先判断：

```text
用户操作
  -> 事件是否绑定？
  -> handler 是否执行？
  -> 条件分支是否提前 return？
  -> 请求是否发出？
```

## 后端读取探针

优先看 dev server 终端输出。如果服务由后台 session 运行，读取对应终端或重启服务并保留输出摘要。

## 收尾

- 修复完成后删除 `[debug:*]` 临时探针。
- 如果保留日志，改成项目统一命名，补成功/失败和耗时。
- TODO 或汇报里写清楚哪些日志是新增长期日志。
