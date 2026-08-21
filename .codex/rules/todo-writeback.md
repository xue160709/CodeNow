# TODO.md 回写规范

本规则由仓库根目录 `AGENTS.md` 显式要求读取；它不是 Cursor Rule，也不依赖 `alwaysApply` 或 `globs` 前置字段。

开发过程中 **`TODO.md` 必须与代码同步**。只改代码、不回写 TODO，等于下一 session 丢失进度。

适用：主会话、`product-discovery`（确认后写 TODO）、`03-project-develop`、`project-iterate`、`project-verify`、`project-debug` 修复后。

## 何时必须回写

| 时机 | 要求 |
| --- | --- |
| **每轮开发结束前** | 必须写回 TODO，再结束回复 |
| 完成一项 checkbox | 打 `[x]` |
| **只做了一部分** | 保持 `[ ]`，在条目下或旁注进度 |
| **被阻塞** | 保持 `[ ]`，写清阻塞原因与解除条件 |
| project-verify 验证失败 / 跳过 | 保持 `[ ]`，在验证记录或条目旁注明 |
| 发现新任务或规格差距 | 追加到对应章节或 §10 |
| 用户中断、上下文将满 | **优先**写 TODO 进度摘要，再停 |

**禁止**：代码已改、TODO 仍全是旧状态；口头说「还没做完」但不写进文件。

## 完成状态怎么写

### 已完成

```markdown
- [x] 实现模板写作 Tab 与主题校验
```

### 部分完成（重要）

拆子项或在同条目下追加进度块：

```markdown
- [ ] 实现历史记录页（进行中）
  - [x] 列表渲染与倒序
  - [ ] 复用跳转预填 — 缺 query 解析
  - 进度：2026-05-29，本轮完成列表；下轮做复用
```

或：

```markdown
- [ ] 接入 MiniMax Route Handler
  - 进度：route 已建，流式未接；下步接 SSE 与前端 loading
```

### 阻塞

```markdown
- [ ] 跑通生成主流程
  - ⚠️ 阻塞：无 MINIMAX_API_KEY，已验空态；有 Key 后继续
```

### 验证未过（project-verify / 自测）

```markdown
- [ ] §2.3 验收：复制到剪贴板
  - ❌ 2026-05-29：非 HTTPS 下 clipboard 失败；待加 fallback 或文档说明 localhost
```

### 主动延后

写入 **§10 未完成目标 / 后续功能**，或条目旁标注：

```markdown
- [ ] 流式输出 — 延后：MVP 先用非流式，见 §10
```

## 写到哪里

| 内容 | 位置 |
| --- | --- |
| 阶段任务、子功能 checkbox | 对应章节 §2–§8 |
| 与 prd 原始目标的差距 | **§10 未完成目标 / 后续功能** |
| 本轮摘要、验证结论 | 文末 **## 开发进度** 或 **## 验证记录**（可追加，不覆盖历史） |
| 临时发现的小 fix | 对应功能章节下追加 `- [ ]` |
| product-discovery 会话摘要 | 文末 **## 产品发现记录**（见 `product-discovery` Skill） |

若 TODO 尚无「开发进度」节，可在首次部分完成时追加：

```markdown
## 开发进度

### 2026-05-29
- 本轮：历史列表完成；生成 API 阻塞无 Key
- 下轮建议：配置 Key 后接 `/api/generate` 流式
```

## 与 project-verify 验证记录的关系

- **project-verify** 写 **验证记录**（命令结果、§2 通过/失败/跳过）
- **开发 Skill** 把结论同步到 **§2 checkbox** 和 **开发进度**
- 验证失败项：**不得**打 `[x]`；在 TODO 保留失败原因

## TODO 过长 → 卸货到 prd/

已完成且验证闭环的功能块，不应长期占满 TODO。见 **`.codex/rules/todo-prd-archive.md`**：

- `prd/` 增量写入「已实现」摘要、验收与代码路径
- TODO 折叠为一行「已归档 → prd/xxx.md」或删除并留索引
- 与 `update-prd` 全量重建互补，日常用卸货即可

## 自检（每轮开发结束前）

- [ ] 本轮动过的任务在 TODO 中有对应更新
- [ ] 未完成项有「进度 / 阻塞 / 下步」之一
- [ ] 无 silent drift（代码与 TODO 状态一致）
- [ ] 用户看 TODO 能接着做，不需翻聊天记录
