# TypeScript 调试脚本模板

用于独立验证服务、API、数据处理模块或外部依赖。优先沿用项目已有工具：`tsx`、Vitest、Playwright 或项目测试入口。

## 什么时候写脚本

- 浏览器现象背后可能是 API 或数据转换问题。
- 需要绕开 UI，直接验证某个模块。
- 问题需要重复执行，手工点击成本高。
- 需要验证多个接口的响应形状。

## fetch 检查脚本

```typescript
// tests/debug-check.ts
type CheckResult = {
  name: string
  passed: boolean
  detail: string | number
}

const BASE_URL = process.env.DEBUG_BASE_URL ?? 'http://localhost:4000'

async function requestJson(path: string, init?: RequestInit): Promise<unknown> {
  const response = await fetch(`${BASE_URL}${path}`, {
    ...init,
    signal: AbortSignal.timeout(5000),
  })

  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`)
  }

  return response.json()
}

async function runChecks(): Promise<boolean> {
  const results: CheckResult[] = []

  try {
    const response = await fetch(BASE_URL, { signal: AbortSignal.timeout(5000) })
    results.push({ name: '服务响应', passed: response.ok, detail: response.status })
  } catch (error) {
    const message = error instanceof Error ? error.message : 'unknown'
    results.push({ name: '服务响应', passed: false, detail: message })
  }

  try {
    await requestJson('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email: 'admin@test.com', password: 'password' }),
    })
    results.push({ name: '登录 API', passed: true, detail: 200 })
  } catch (error) {
    const message = error instanceof Error ? error.message : 'unknown'
    results.push({ name: '登录 API', passed: false, detail: message })
  }

  try {
    const data = await requestJson('/api/books')
    const count = Array.isArray(data) ? data.length : 'not-list'
    results.push({ name: '书籍 API', passed: Array.isArray(data), detail: count })
  } catch (error) {
    const message = error instanceof Error ? error.message : 'unknown'
    results.push({ name: '书籍 API', passed: false, detail: message })
  }

  console.log('\n=== Debug 检查结果 ===')
  for (const result of results) {
    const status = result.passed ? 'PASS' : 'FAIL'
    console.log(`${status} ${result.name}: ${result.detail}`)
  }

  return results.every((result) => result.passed)
}

runChecks().then((passed) => {
  process.exitCode = passed ? 0 : 1
})
```

运行：

```bash
DEBUG_BASE_URL=http://localhost:4000 npx tsx tests/debug-check.ts
```

## 模块级检查

如果项目已有 Vitest：

```typescript
import { describe, expect, it } from 'vitest'
import { normalizeBookList } from '../src/lib/books'

describe('debug normalizeBookList', () => {
  it('keeps valid items and drops invalid items', () => {
    const result = normalizeBookList([
      { id: '1', title: 'A' },
      { id: null, title: '' },
    ])

    expect(result).toEqual([{ id: '1', title: 'A' }])
  })
})
```

## 收尾

- 临时脚本如果只用于本轮定位，修复后可删除。
- 如果脚本变成有价值的回归测试，改成正式测试命名并纳入项目测试命令。
- TODO 写清楚脚本是临时验证还是已保留为回归测试。
