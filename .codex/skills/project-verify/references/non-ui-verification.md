# 非 UI 代码验收参考

用于纯函数、数据转换、API Route / 服务封装、Electron IPC、浏览器插件 background、CLI / 脚本等无法用 `data-testid` 直接点击的代码。

## 原则

- 非 UI 验收也必须可复现、可观察、可回写 TODO。
- 优先使用项目已有测试框架和 `npm run test`；没有测试框架时，用最小 smoke 脚本、curl、fixture 输入输出或日志证据兜底，并把补测试脚本写回 TODO。
- 外部 API 默认不依赖真实 Key：先验未配置态、错误态、mock 成功态和日志脱敏。
- 不输出 API Key、Token、用户隐私原文；日志和测试快照只保留摘要。

## 验收方式映射

| 代码类型 | 推荐证据 |
| --- | --- |
| 纯函数 / 工具函数 | 单元测试：输入 fixture，断言输出与边界情况 |
| 数据转换 / 校验 | fixture JSON + 单测，覆盖空值、非法值、极值 |
| API Route / 服务封装 | mock fetch / mock SDK 的集成测试；无 Key 时测未配置态 |
| Electron IPC / preload | handler 单测或 smoke，断言参数摘要、返回结构和错误分支 |
| 浏览器插件 background | message handler / storage 读写测试；必要时 mock `chrome.storage` |
| CLI / 脚本 | 执行命令，记录 exit code、stdout 摘要和错误态 |
| 第三方服务降级 | mock 超时、失败响应、空响应，断言 fallback 和日志 |

## 必跑命令

按项目实际 scripts 执行：

```bash
npm run lint
npm run test
npm run typecheck
```

若没有 `typecheck`，可用项目本地 TypeScript：

```bash
npx tsc --noEmit
```

若某个 script 不存在：记录 `⚠️ 未提供该 script`，不要伪造通过；同时在 TODO 追加“补齐测试脚本 / 类型检查脚本”的后续项。

## 证据写法

```markdown
### 非 UI 验收
| 模块 | 验收方式 | 结果 | 证据 |
| --- | --- | --- | --- |
| lib/normalize.ts | npm run test -- normalize | ✅ | 12 tests passed |
| app/api/generate | mock API Key 缺失态 | ✅ | 返回 400 + 脱敏错误日志 |
```

## 失败处理

- 测试失败：TODO 对应项保持 `[ ]`，写明失败用例和下一步。
- 无测试入口：TODO 对应项保持 `[ ]` 或标部分完成，补“增加测试入口”任务。
- 只能人工确认：写 `⚠️ 跳过` 和用户本地验证步骤，不得直接打勾。
