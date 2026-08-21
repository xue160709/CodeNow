# 调用日志与调试探针（03-project-develop）

**本文件与主 Skill 中的「调用日志（必做）」章节配套；写 API / IPC / 第三方请求代码时必须遵守。**

规则来源与仓库根目录 `AGENTS.md` 一致；仅跑 `/03-project-develop` 时也要执行，不能假设 Agent 已读过 AGENTS.md。

## 何时必须加日志

以下路径**每新增或修改一处，都必须有日志**：

| 场景 | 示例位置 |
| --- | --- |
| 远程 API | Next.js Route Handler、Server Action、fetch 封装 |
| 第三方 AI / 模型 | `lib/services/llm.ts`、`app/api/generate/route.ts` |
| Electron IPC | preload `contextBridge` 暴露的方法、main 里 `ipcMain.handle` |
| Electron main 调 API | main 进程 HTTP 客户端 |
| 插件 background 请求 | service worker 里 fetch |
| 降级 / 重试 / 缓存 miss | 分支入口与最终结果 |

纯 UI 组件（无 I/O）可不 log；**只要有网络、IPC、storage 读写失败风险就必须 log**。

## 每条日志至少包含

1. **调用入口**（模块/函数名，统一前缀如 `[闪写/API]`）
2. **关键参数摘要**（mode、模板 id、输入长度、路径；**不是**全文）
3. **成功或失败结果**（status、耗时 ms、结果条数）
4. **失败时错误原因**（`error.message` 或脱敏 code）

## 禁止输出

- API Key、Token、Bearer 全文
- 用户输入原文、隐私字段
- 完整 request/response body

## 推荐写法

### Next.js Route Handler / Node

```ts
export async function POST(req: Request) {
  const tag = '[api/generate]'
  const body = await req.json()
  const inputLen = typeof body.topic === 'string' ? body.topic.length : 0
  console.log(tag, 'enter', { mode: body.mode, templateId: body.templateId, inputLen })

  try {
    const t0 = Date.now()
    const results = await callLlm(body)
    console.log(tag, 'success', { count: results.length, ms: Date.now() - t0 })
    return Response.json({ results })
  } catch (err) {
    const message = err instanceof Error ? err.message : 'unknown'
    console.error(tag, 'fail', { inputLen, message })
    return Response.json({ error: '生成失败' }, { status: 500 })
  }
}
```

### Electron main

```ts
ipcMain.handle('app:generate', async (_e, payload) => {
  console.log('[main/generate] enter', { mode: payload.mode, inputLen: payload.text?.length ?? 0 })
  // ...
})
```

### Chrome Extension background

```ts
console.log('[bg/fetch] enter', { url: redactUrl(url), inputLen })
```

### 前端调用封装（可选 debug）

```ts
console.log('[client/generate] request', { mode, inputLen })
// 失败时 console.error，成功时 console.log 结果条数即可
```

## 自检（写代码后立即核对）

- [ ] 每个新建/修改的 API Route、LLM 封装、IPC handler、background fetch 都有 enter + success/fail 日志
- [ ] 日志里没有 Key、Token、用户原文
- [ ] 错误分支有 `console.error`，不是静默 `catch {}`
- [ ] 重试/降级分支有单独 log 说明走了哪条路径

## 与 project-debug 的关系

用户报告 bug 时用 `project-debug` Skill；开发阶段按本文件预埋日志，便于 `playwright-cli console` 或终端输出定位。
