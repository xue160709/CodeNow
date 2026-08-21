---
name: project-debug
description: |
  为 TypeScript/Node.js 项目提供系统性 debug 能力。当用户明确要求 debug 或遇到问题时触发：
  - 用户说"debug"、"bug"、"出问题了"、"帮我看看"、"不对"、"报错"
  - 用户说"为什么不行"、"页面空白"、"数据不对"、"登录失败"
  - 用户说"帮我检查"、"帮我测试"、"帮我验证"，且重点是定位失败原因

  不要在以下场景触发：
  - 用户只是在问代码是做什么的（没有出问题）
  - 用户在写新代码而不是调试
  - 用户要求优化性能但没有报错或异常现象

  本 skill 强调 AI Agent 主动寻找报错信息的能力：复现问题、读取 console/network/server 日志、植入临时探针、编写 TypeScript 调试脚本、最小修复、复验并回写 TODO.md。
---

# Project Debug：TypeScript/Node.js Debug 流程

## 核心目标

Debug 的目标不是猜原因，而是把问题从“感觉不对”收束成可验证证据：

```text
用户现象
  -> 复现步骤
  -> console / network / server / 测试证据
  -> 最小可疑区域
  -> 最小修复
  -> 复验
  -> TODO.md 回写
```

## 渐进式加载

主文件只保留流程。按问题类型读取 reference，不要一次读完。

| 场景 | 读取 |
| --- | --- |
| 用户描述模糊、需要先确认预期和实际行为 | `references/intent-alignment.md` |
| 浏览器页面、console、network、截图、curl/API 检查 | `references/browser-debug.md` |
| 需要植入临时探针或补长期调用日志 | `references/probe-and-logging.md` |
| 页面空白、数据不变、启动失败、登录失败、扩展异常等常见症状 | `references/symptom-playbooks.md` |
| 需要独立验证 API、模块或数据处理链路 | `references/debug-script-template.md` |
| 收尾自检、常用命令速查 | `references/debug-checklist.md` |
| Playwright CLI 安装、降级、截图目录规范 | `../project-verify/references/browser-playwright.md` |
| UI 交互选择器缺失或不稳定 | `../project-verify/references/selector-and-testid.md` |
| API / IPC / 第三方请求的长期日志规范 | `../03-project-develop/references/logging-and-debugging.md` |

## 硬约束

1. **先对齐再深挖**：如果用户现象不足以复现，先用 1-3 个问题确认触发条件、预期行为、实际行为和关键证据。
2. **证据优先**：优先读取 console、network、server 输出、构建/测试错误和关键 API 响应；不要只靠代码直觉下结论。
3. **一次只改一个变量**：定位阶段尽量控制变量，避免同时改多个可疑点导致根因变模糊。
4. **TypeScript 优先**：TypeScript/Node.js 项目中的临时验证脚本优先用 TypeScript；沿用项目已有 `tsx`、Vitest 或 Playwright 测试栈。
5. **日志脱敏**：不得输出 API Key、Token、用户隐私原文。必要时只记录字段是否存在、长度、哈希前缀或业务 ID 摘要。
6. **临时探针要收尾**：修复后删除只为定位而加的噪声日志；如果探针变成长期必要日志，按 `../03-project-develop/references/logging-and-debugging.md` 整理命名、脱敏和成功/失败结果。
7. **验证失败不打勾**：修复后交回 `project-verify` 或按项目验证命令复验；未通过、跳过或阻塞都要写清原因。
8. **每轮结束必须回写 `TODO.md`**：同步本轮修复、未完成项、阻塞、验证结果或后续动作。

## 标准流程

### Phase 0：意图对齐

1. 读取用户描述和 `TODO.md` 中相关条目。
2. 如果问题不清楚，读取 `references/intent-alignment.md`，用简短问题或 ASCII 图确认：
   - 触发条件是什么？
   - 预期应该发生什么？
   - 实际发生了什么？
   - 有哪些截图、报错、日志或复现步骤？
3. 能合理复现时直接进入 Phase 1，不要为形式感反复追问。

### Phase 1：读取合同与运行环境

1. 读取 `package.json`、相关配置、入口文件和 TODO 验收标准。
2. 确认主框架：Next.js、Electron、vite-web-extension、纯 Node.js 或其它。
3. 确认启动命令、端口、API Key / 外部服务约束和已有测试命令。
4. 涉及浏览器动态排查时，先读取 `../project-verify/references/browser-playwright.md`。

### Phase 2：主动复现与证据采集

1. 运行最小复现路径，记录实际 URL、操作步骤和失败现象。
2. 浏览器问题读取 `references/browser-debug.md`：检查 console、network、snapshot、截图。
3. API / 服务端问题用 curl 或独立脚本验证入口、关键参数摘要、状态码和响应形状。
4. 构建或启动失败先保留完整错误摘要，再定位触发文件。

### Phase 3：缩小可疑区域

1. 用 `rg` 搜索事件处理、API 路由、状态更新、数据转换和错误文案。
2. 必要时读取 `references/probe-and-logging.md`，植入临时探针。
3. 对可疑模块写 TypeScript 调试脚本或小范围测试；模板见 `references/debug-script-template.md`。
4. 若当前环境提供 Explore / Plan SubAgent，可用它们做独立探索或方案评估，但最终仍以本地证据为准。

### Phase 4：最小修复

1. 优先修根因，不用大范围重写掩盖问题。
2. 保留用户已有改动，不回滚无关文件。
3. 复杂逻辑和关键分支补中文注释，解释为什么这样做以及调试观察点。
4. 涉及 API、IPC、第三方服务请求或降级逻辑时，补必要调用日志。

### Phase 5：复验

1. 跑本轮相关静态命令：lint、类型检查、build 或项目已有测试。
2. 对原复现路径做动态验证；浏览器问题保留截图、console/network 摘要。
3. 无 API Key 或外部服务不可用时，验证未配置态、错误态和降级逻辑，并在 TODO 标记跳过条件。
4. 修复后如还需正式验收，交回 `project-verify`。

### Phase 6：TODO 回写与汇报

1. 更新 `TODO.md`：已完成打 `[x]`；部分完成、失败、跳过、阻塞写明原因和下一步。
2. 汇报根因、改动、验证命令和剩余风险。
3. 如果是教学/新手场景，用生活化语言解释报错和修复链路。

## 输出建议

汇报时优先按这个顺序：

```text
问题根因：一句话
修复内容：改了哪里
验证结果：跑了什么，结果如何
TODO 状态：已回写什么
剩余风险：还需要用户提供什么或下轮做什么
```

## 自检

- [ ] 已读取 `TODO.md` 和相关代码事实。
- [ ] 已按场景读取必要 reference，未一次性加载所有细节。
- [ ] 已采集 console/network/server/build/test 中至少一种证据。
- [ ] 临时探针已删除，长期日志已脱敏。
- [ ] 已运行可用验证命令或说明无法运行的原因。
- [ ] 已回写 `TODO.md`。
