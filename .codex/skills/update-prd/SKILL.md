---
name: update-prd
description: 维护 PRD 文档，确保与实际代码实现保持同步；支持从根目录 prd.md 迁移为 prd/ 模块文档体系，按 Git commit 增量同步代码变化，分离产品文档与技术文档，并把未完成差距写回 TODO.md。日常 TODO 卸货见 .codex/rules/todo-prd-archive.md。
---

# PRD 维护专家

你负责维护项目的 `prd/` 文档体系。核心目标不是把所有细节塞进一份大文档，而是让产品信息容易阅读，让技术上下文足够支撑后续开发、调试和验证。

## 核心原则

1. **代码事实优先**：`prd/` 只描述当前代码真实存在或已经验证的能力；未实现、部分实现、降级实现写回 `TODO.md`。
2. **产品文档与技术文档分层**：`prd/<module>/README.md` 写产品相关内容，保持短、清楚、产品化；`prd/<module>/technical.md` 写技术相关内容，保留代码路径、数据结构、测试、日志和边界情况。
3. **模块文件夹强制**：模块文档一律使用 `prd/<module>/` 文件夹，包含 `README.md`、`technical.md` 和必要的同步状态文件。
4. **Git diff 是线索，不是事实**：从上次 PRD 同步 commit 到当前 `HEAD` 的 diff 用于发现变化范围；最终文档必须以当前代码和已验证行为为准。
5. **TODO 是继续开发入口**：任何未完成差距、阻塞和下步动作必须写回 `TODO.md`，不能只写在聊天里或 PRD 里。
6. **支持多项目形态，禁止固定框架映射**：`update-prd` 适用于 Next.js、Electron、Vite Chrome Extension 和其他结构；框架线索只用于理解项目事实，不能把任何单一框架路径硬绑定到固定 PRD 模块。

## 快速开始

1. **选择模式**：判断本轮是根目录 `prd.md` 迁移、增量同步、全量重建，还是 TODO 已完成块卸货。
2. **读取现状**：读取 `TODO.md`、`prd/README.md`、相关模块 PRD、`prd/.update-prd-state.json` 和模块 `sync.json`（如果存在）。
3. **定位变化**：若存在上次同步 commit，运行 `git diff <lastPrdSyncCommit>...HEAD --stat`；若不存在，走全量扫描。
4. **发现模块**：按 `references/MODULE-DISCOVERY.md` 从项目结构、已有 PRD、TODO、文件名、目录名、导入关系和 diff 聚类推断影响模块。
5. **更新文档**：按 `references/PRD-CONVENTIONS.md` 和 `references/PRD-TEMPLATES.md` 更新产品 README 与技术文档。
6. **回写 TODO**：把原目标与当前实现的差距、阻塞、下步动作同步到 `TODO.md`。
7. **记录同步点**：按 `references/PRD-SYNC-STATE.md` 更新全局和模块级 sync 状态。
8. **验收**：检查引用路径存在、TODO 状态一致、PRD 未把未完成项写成已实现。

## 工作流：根目录 `prd.md` 迁移

当仓库根目录满足以下条件时，优先执行本流程：

- 存在 `prd.md`
- 不存在 `prd/` 文件夹

这通常表示项目刚完成 `/03-project-develop`。根目录 `prd.md` 是原始总目标，不等于当前已完成事实。

执行步骤：

1. 完整读取 `prd.md`，把它作为产品总目标和需求上限。
2. 阅读当前项目代码、路由/入口、组件、状态与数据模型、API 封装、配置、构建脚本、README 和现有 `TODO.md`。
3. 跳过 `.git/`、`node_modules/`、`.next/`、`dist/`、`build/`、`out/`、覆盖率产物、日志、缓存和密钥文件。
4. 创建 `prd/` 模块文档体系：`prd/README.md`、`prd/<module>/README.md`、`prd/<module>/technical.md`、必要时创建 `sync.json`。
5. `prd/` 只写当前已实现或代码中真实存在的能力；原 `prd.md` 中未实现、部分实现、实现方式变化或被降级的目标写入 `TODO.md`。
6. 按需更新 `AGENTS.md`，使其继续说明后续任务以 `TODO.md` 为准；不创建或维护平行的工具专属指令文件。
7. 将根目录 `prd.md` 归档为 `prd.original.md`。如果 `prd.original.md` 已存在，先对比内容：相同则删除重复 `prd.md`，不同则保留旧文件并将本次归档为 `prd.original.<YYYYMMDD>.md`。
8. 更新 `prd/.update-prd-state.json`，记录本次迁移时的 `HEAD`。

`AGENTS.md` 建议至少包含：

```markdown
# 项目协作说明

后续任务以仓库根目录 `TODO.md` 为准。

开始工作前请先读取：
- `TODO.md`
- `prd/README.md`
- `prd/` 下与当前任务相关的模块文档

**不要**读取 `prd.original.md` 作为开发依据（该文件仅为归档的原始总目标，供人类回顾）。

执行时请优先完成 `TODO.md` 中未勾选的任务；如果实际代码、`prd/` 与 `TODO.md` 冲突，以当前代码事实和 `prd/` 已实现文档为依据，并把新的差距或后续任务更新回 `TODO.md`。
```

## 工作流：增量 PRD 同步

适用于项目已经有 `prd/`，且用户希望根据最近代码变化更新 PRD。

1. 读取 `prd/.update-prd-state.json` 的 `lastPrdSyncCommit`。
2. 若 commit 存在且仍在当前仓库历史中，运行：

```bash
git diff <lastPrdSyncCommit>...HEAD --stat
git diff <lastPrdSyncCommit>...HEAD -- <relevant-path>
```

3. 若没有同步状态、commit 丢失、分支历史被重写或 diff 范围不可信，改走全量扫描，并在同步状态中记录原因。
4. 使用 `references/MODULE-DISCOVERY.md` 生成影响范围：受影响模块、可能新增模块、无法确认的变化。
5. 对每个受影响模块：
   - 更新 `prd/<module>/README.md` 的产品状态。
   - 更新 `prd/<module>/technical.md` 的实现上下文、相关代码路径、测试和日志要求。
   - 更新 `prd/<module>/sync.json` 的同步 commit 和本轮变更文件摘要。
6. 更新 `prd/README.md` 模块索引。
7. 将未完成目标、阻塞项和下步动作写回 `TODO.md`。
8. 更新 `prd/.update-prd-state.json`。

## 工作流：全量重建或里程碑同步

适用于首次整理、多模块大改、历史同步状态不可用、用户要求“全面更新 PRD”的情况。

1. 扫描项目入口、页面、核心组件、API/IPC/第三方调用、状态管理、数据结构、配置、测试和 README。
2. 读取已有 `prd/` 与 `TODO.md`，保留仍与代码一致的内容。
3. 按模块重建或更新 `prd/<module>/README.md` 与 `technical.md`。
4. 不删除不确定内容；将疑似过时或无法验证的内容写入待确认项。
5. 对照原始目标或 TODO，把未完成差距写回 `TODO.md`。
6. 更新全局与模块级 sync 状态。

## 工作流：TODO 卸货

当 `TODO.md` 过长或已有模块验收闭环时，按 `.codex/rules/todo-prd-archive.md` 执行。

关键要求：

1. 只归档已全部 `[x]` 且已验证的功能块。
2. 写入对应模块的 `README.md` 和 `technical.md`。
3. 更新 `prd/README.md` 索引。
4. 精简 TODO：折叠为“已归档 -> prd/<module>/README.md”或删除并保留索引。
5. 在 TODO 追加卸货记录。

## 文档结构

推荐结构：

```text
prd/
  README.md
  .update-prd-state.json
  <module>/
    README.md
    technical.md
    sync.json
    decisions.md        # 可选
```

模块文档必须使用上述文件夹结构，并同步更新 `prd/README.md` 索引。

## 验收清单

提交或结束本轮前逐项检查：

- [ ] 已判断本轮模式：迁移 / 增量同步 / 全量重建 / TODO 卸货。
- [ ] 已读取 `TODO.md`、`prd/README.md` 和相关模块文档。
- [ ] 若存在同步状态，已查看 `<lastPrdSyncCommit>...HEAD` diff；若未使用 diff，已写明原因。
- [ ] 已按模块发现方法识别受影响模块，没有使用固定框架路径强行映射。
- [ ] 产品 README 保持短、清楚、产品化，没有塞入大量代码细节。
- [ ] 技术文档包含必要代码路径、数据结构、调用日志要求、测试点和边界情况。
- [ ] PRD 中引用的代码路径均已核对存在；不存在或不确定的路径已标注待确认。
- [ ] 未把未实现、部分实现或未验证能力写成“已实现”。
- [ ] `prd/README.md` 模块索引已同步。
- [ ] 未完成差距、阻塞项和下步动作已写回 `TODO.md`。
- [ ] 全局 `prd/.update-prd-state.json` 与模块 `sync.json` 已更新或注明跳过原因。

## 参考

- `references/MODULE-DISCOVERY.md` - 通用模块发现与影响范围判断
- `references/PRD-CONVENTIONS.md` - 产品文档与技术文档写作规范
- `references/PRD-TEMPLATES.md` - 模块文件夹、README、technical、TODO 差距与 sync 模板
- `references/PRD-SYNC-STATE.md` - Git commit 同步状态与异常处理
