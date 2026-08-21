---
name: project-verify
description: |
  项目测试规范与验收执行 Skill。用于生成/更新 TESTING_CHECKLIST、规划 data-testid、准备 Playwright 验证流程、规划非 UI 测试证据，以及按 TODO.md 验收标准执行 lint/test/typecheck/动态验证、回写 checkbox 和验证记录。支持 Next.js、Electron、vite-web-extension；测试规范统一维护在本 Skill references 中。
---

# Project Verify：测试指南 + TODO 验收执行

本 Skill 同时负责两件事：

| 模式 | 触发 | 行为 |
| --- | --- | --- |
| **Guide 模式** | 用户要测试规范、`data-testid`、`TESTING_CHECKLIST`、Playwright 步骤 | 只生成/更新测试资料与建议；不默认执行全量验收，不随意打勾 TODO |
| **Verify 模式** | 用户要求验收、打勾、跑验证，或 `project-iterate` / `03-project-develop` 完成后 | 读取 `TODO.md`，执行静态与动态验证，按证据回写 checkbox 与验证记录 |

边界：本 Skill 管“怎么测、测什么、证据如何落地”。验证失败后的根因排查和修代码交给 `project-debug` / `project-iterate`；修完后回到本 Skill 复验。

## 渐进式加载

主文档只保留通用流程；按场景读取 reference，不要一次读完。

| 场景 | 读取 |
| --- | --- |
| 浏览器自动化、Playwright CLI/Python、截图、console 日志 | `references/browser-playwright.md` |
| 规划或补交互元素选择器、`data-testid` | `references/selector-and-testid.md` |
| 非 UI 逻辑、API/IPC/background、脚本、数据转换验收 | `references/non-ui-verification.md` |
| 生成或更新 `TESTING_CHECKLIST.md` | `references/checklist-template.md` |
| 主框架 Next.js | `references/nextjs.md` |
| 主框架 Electron | `references/electron.md` |
| 主框架 vite-web-extension / Chrome Extension | `references/vite-web-extension.md` |

## Guide 模式流程

1. 识别项目主框架；若不清楚，读 `TODO.md`、`package.json`、构建配置。
2. 需要清单时读 `references/checklist-template.md`，生成/更新根目录 `TESTING_CHECKLIST.md`。
3. 需要稳定选择器时读 `references/selector-and-testid.md`，只给本轮触及的交互元素补/规划 `data-testid`。
4. 需要非 UI 验收时读 `references/non-ui-verification.md`，为本轮逻辑/API/IPC/background/脚本规划单测、集成测试、fixture、curl/CLI smoke 或日志证据。
5. 需要动态测试步骤时读 `references/browser-playwright.md` 和对应框架 reference。
6. 只在用户明确要求或本轮确实修改仓库时，按 `.codex/rules/todo-writeback.md` 回写 `TODO.md` 开发进度。

## Verify 模式流程

### 1. 读合同

- 读取 `TODO.md`：主框架、§2 验收标准、§8 验证、§3 入口、API Key / 外部服务约束。
- 读取 `package.json` scripts 和锁文件，确认包管理器与命令。
- 确认验证范围：默认验证本轮相关 §2.x；用户要求“全部验收/打勾”或里程碑时再全量 §2。
- 无 `TESTING_CHECKLIST.md` 时，按本轮范围读取 `references/checklist-template.md` 生成；全量验证时覆盖全部 §2。

若 §2 缺失或不可执行，先让 `qa-acceptance-planner` 补验收标准，再继续验证。

### 2. 静态验证（必做，默认不跑 build）

按项目 scripts 依次跑可用命令：

1. `lint`
2. `test`
3. 类型检查（script 或 `tsc --noEmit`）

若脚本不存在，记录 `⚠️ 未提供该 script`，并在 TODO 后续项建议补齐。失败要写入验证记录；UI 动态项和非 UI 功能项不得无证据打勾。

`build` 不作为默认验证项。只有用户明确要求、发布/打包、验证构建产物、确认浏览器插件加载目录或项目 TODO 明确要求时，才按需执行并记录结果。

### 3. 动态验证

1. 按主框架只读一份框架 reference。
2. 需要浏览器或 Web UI 时，先读 `references/browser-playwright.md`，完成 CLI/降级准备与 `test-results/`。
3. 需要非 UI 验收时，按 `references/non-ui-verification.md` 执行对应测试、curl/CLI smoke 或日志证据采集。
4. 启动 dev / preview / 按需构建产物，记录实际 URL、端口、扩展输出目录或 GUI 限制。
5. 按 `TODO.md` §2 逐条执行；每个通过项要有命令输出、测试结果、截图、console/network 证据或明确的人工/半自动证据。
6. API Key 不可用时，只验未配置态、错误态、localStorage/chrome.storage 保存逻辑；真实远程生成项标跳过。
7. 失败项先记录证据；需要修复时交给 `project-debug` 或开发 Skill，修完再复验。

### 4. 写回 TODO

- 通过：对应 checkbox 改 `[x]`。
- 失败：保持 `[ ]`，写 `❌` 原因。
- 跳过：保持 `[ ]`，写 `⚠️` 条件和用户本地验证步骤。
- 阻塞：保持 `[ ]`，写阻塞原因与解除条件。
- 末尾追加/更新 **验证记录**，并同步 `TESTING_CHECKLIST.md` 状态。

禁止无证据把 §2 全部打勾。

### 5. 汇报

汇报通过/失败/跳过数量、阻塞项、关键命令结果、`TESTING_CHECKLIST.md` 与 `test-results/` 路径。若阻塞会影响 `update-prd`，明确说明先修复再归档。

## 验证记录模板

```markdown
---

## 验证记录

最后验证：YYYY-MM-DD
主框架：<Next.js / Electron / vite-web-extension>
范围：<§2.x / 全量 §2>

### 静态验证
| 命令 | 结果 | 备注 |
| --- | --- | --- |
| npm run lint | ✅/❌/⚠️ | |
| npm run test | ✅/❌/⚠️ | |
| npm run typecheck / tsc --noEmit | ✅/❌/⚠️ | |
| npm run build（按需） | ✅/❌/⚠️ | 默认不跑；仅发布/打包/构建产物验证 |

### §2 摘要
| 功能 | 通过 | 失败 | 跳过 |
| --- | --- | --- | --- |

### 失败 / 跳过 / 阻塞
- [ ] <项> — ❌/⚠️ 原因；下一步

### 证据
- `TESTING_CHECKLIST.md`
- `test-results/<...>.png`
- 关键 test / console / network / smoke 输出摘要
```

## 与其它 Skill 的关系

- `03-project-develop` / `project-iterate`：负责实现与预埋 testid；完成后可调用本 Skill 验收。
- `project-debug`：负责失败项排查、加探针、修复；修完回到本 Skill 复验。
- `qa-acceptance-planner`：负责补可执行验收标准；本 Skill 不凭空扩写产品范围。

## 自检

- [ ] 已区分 Guide / Verify 模式，没有在 Guide 模式误打 TODO 勾。
- [ ] 已确认验证范围（增量或全量）。
- [ ] 已读范围内验收标准和对应框架 reference。
- [ ] UI 动态验证前已读 `browser-playwright.md` 并准备 `test-results/`。
- [ ] 触及交互元素时已按 `selector-and-testid.md` 检查稳定选择器。
- [ ] 触及非 UI 逻辑/API/IPC/background/脚本时已按 `non-ui-verification.md` 检查测试或 smoke 证据。
- [ ] 静态验证已跑并记录。
- [ ] 未把 `build` 当成默认验证项；如已执行，已说明触发原因。
- [ ] §2 项已逐条执行或标注失败/跳过/阻塞，无无证据打勾。
- [ ] `TESTING_CHECKLIST.md` 与 `TODO.md` 验证记录已同步。
