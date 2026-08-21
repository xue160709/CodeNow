# TESTING_CHECKLIST 模板

当项目根目录缺少 `TESTING_CHECKLIST.md`，或验证范围变化时使用。清单是验收工作台；TODO 是最终状态来源，两者要同步。

## 文件位置

- 根目录：`TESTING_CHECKLIST.md`
- 截图与日志：`test-results/`

## 模板

```markdown
# <项目名> 验证清单

最后更新：YYYY-MM-DD
主框架：<Next.js / Electron / vite-web-extension>
验证范围：<§2.x / 全量 §2>

## 环境信息

| 项目 | 值 |
| --- | --- |
| 包管理器 | npm / pnpm / yarn / bun |
| 服务地址 / 输出目录 | http://localhost:3000 / dist_chrome / Electron GUI |
| 测试工具 | lint / test / typecheck / playwright-cli / Python Playwright / curl/CLI smoke / 手动走查 |
| API Key 状态 | 已配置 / 未配置，仅验空态 |

## 静态验证

| 命令 | 预期 | 状态 | 备注 |
| --- | --- | --- | --- |
| npm run lint | exit 0 | ⬜ | |
| npm run test | exit 0 | ⬜ | |
| npm run typecheck / tsc --noEmit | exit 0 | ⬜ | |
| npm run build（按需） | exit 0 | ⬜ | 默认不跑；仅发布/打包/构建产物验证 |

## 功能验证

| TODO 项 | 验证步骤 | 预期结果 | 状态 | 证据 | 备注 |
| --- | --- | --- | --- | --- | --- |
| §2.1 <功能> | 1. ... | ... | ⬜ | `test-results/...png` | |

## 失败 / 跳过 / 阻塞

- [ ] <项> — ❌/⚠️ 原因；下一步

## 证据索引

- `test-results/...png`
- `test-results/console.log`
- 关键命令输出摘要：...
```

## 状态写法

| 状态 | 含义 |
| --- | --- |
| ✅ | 已通过，有证据，可同步 TODO `[x]` |
| ❌ | 已执行但失败，TODO 保持 `[ ]` |
| ⚠️ | 跳过或半自动，TODO 保持 `[ ]` 并写条件 |
| ⬜ | 未执行 |

## 维护规则

- 每个 TODO §2 验收项至少对应一行功能验证。
- 截图、console log、测试 / smoke 输出摘要要能追溯到具体条目。
- 清单通过不等于自动完成；最终必须同步写回 `TODO.md`。
