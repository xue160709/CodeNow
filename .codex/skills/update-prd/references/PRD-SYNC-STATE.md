# PRD 同步状态

同步状态用于解决“代码经常 commit，但 PRD 偶尔才更新”的问题。每次 `update-prd` 完成后，记录本次 PRD 对齐到哪个 Git commit；下次从该 commit 到当前 `HEAD` 做 diff。

## 文件位置

全局状态：

```text
prd/.update-prd-state.json
```

模块状态：

```text
prd/<module>/sync.json
```

## 全局状态字段

```json
{
  "lastPrdSyncCommit": "<sha>",
  "lastPrdSyncAt": "YYYY-MM-DD",
  "mode": "migration|incremental|full-resync|todo-archive",
  "modulesUpdated": [
    "<module>"
  ],
  "notes": "<本轮同步摘要>"
}
```

## 模块状态字段

```json
{
  "lastPrdSyncCommit": "<sha>",
  "lastPrdSyncAt": "YYYY-MM-DD",
  "module": "<module>",
  "lastChangedFiles": [
    "<path>"
  ],
  "notes": "<本轮模块同步摘要>"
}
```

## 基本命令

读取当前 commit：

```bash
git rev-parse HEAD
```

查看增量范围：

```bash
git diff <lastPrdSyncCommit>...HEAD --stat
git diff <lastPrdSyncCommit>...HEAD --name-only
```

查看指定文件变化：

```bash
git diff <lastPrdSyncCommit>...HEAD -- <path>
```

确认同步 commit 是否仍在历史中：

```bash
git cat-file -e <lastPrdSyncCommit>^{commit}
git merge-base --is-ancestor <lastPrdSyncCommit> HEAD
```

## 同步流程

1. 读取 `prd/.update-prd-state.json`。
2. 如果 `lastPrdSyncCommit` 存在且可用，使用 `<lastPrdSyncCommit>...HEAD` 作为增量范围。
3. 如果状态不存在、commit 不存在、commit 不在当前分支历史中，改走全量扫描，并在新状态的 `notes` 中记录原因。
4. 使用 diff 发现影响模块，但最终 PRD 内容以当前代码事实为准。
5. 更新 PRD 和 TODO 后，把 `lastPrdSyncCommit` 更新为当前 `HEAD`。

## 脏工作区

PRD 更新本身会让工作区变脏。记录同步 commit 时使用更新 PRD 前或更新过程中读取到的当前 `HEAD`，表示“PRD 已经对齐到这一版代码”。

如果代码本身存在未提交变更：

- 仍可更新 PRD，但要在 `notes` 中写明“包含未提交代码观察”。
- 不要把未提交代码当成稳定已实现事实，除非用户明确要求。
- 未提交代码造成的不确定项写入 TODO 或技术文档的待确认区。

## 异常处理

### 首次同步

没有 `prd/.update-prd-state.json` 时：

1. 执行全量扫描。
2. 创建全局状态。
3. 为本轮更新过的模块创建 `sync.json`。

### rebase 或历史重写

如果 `lastPrdSyncCommit` 不再是当前 `HEAD` 的祖先：

1. 不强行使用该 diff。
2. 执行全量扫描或让用户确认基线。
3. 在 `notes` 中记录“同步 commit 不在当前历史中”。

### 删除或重命名模块

如果 diff 显示模块文件大量删除或重命名：

1. 先确认当前代码是否仍有对应用户能力。
2. 如果能力存在但路径变化，只更新技术文档和 sync。
3. 如果能力删除或降级，更新产品 README，并把后续处理写回 TODO。

### 无 Git 仓库

如果项目不是 Git 仓库：

1. 跳过 commit 同步状态。
2. 执行全量扫描。
3. 在 PRD 或 TODO 中说明无法使用增量 diff。
