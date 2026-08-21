# PRD 模板

本文件提供可复用模板。使用时根据项目事实删改，不要机械填充空章节。

## `prd/README.md`

```markdown
# 产品文档

## 项目概览

<用 3-5 句话说明当前产品是什么、服务谁、现在做到什么程度。>

## 模块索引

| 模块 | 状态 | 产品文档 | 技术文档 |
| --- | --- | --- | --- |
| <模块名> | 已实现 / 部分实现 / 规划中 | `<module>/README.md` | `<module>/technical.md` |

## 当前重点

- <本阶段最重要的产品目标或 TODO 入口>

## 文档规则

- `prd/<module>/README.md` 描述产品状态和用户流程。
- `prd/<module>/technical.md` 描述实现细节和调试上下文。
- `TODO.md` 是继续开发入口，未完成目标以 TODO 为准。
```

## 模块 README

````markdown
# <模块名>

## 模块定位

<这个模块解决什么问题，用户为什么需要它。>

## 当前已实现

- <用户可见能力 1>
- <用户可见能力 2>
- 入口：<页面、按钮、菜单或触发方式>

## 用户流程

```text
1. <用户动作>
   ↓
2. <系统反馈>
   ↓
3. <结果>
```

## 还没做什么

- <关键缺口，详细任务见 TODO.md>

## 关键决策

- <为什么这样做，或者为什么暂时不做某方案>

## 关联模块

- `<other-module>`：<关联原因>
````

## 技术文档

````markdown
# <模块名> 技术文档

## 代码入口

| 路径 | 作用 |
| --- | --- |
| `<path>` | <为什么与本模块相关> |

## 数据结构

- `<type/schema/store>`：<字段和用途摘要>

## 调用链路

```text
<入口>
  -> <组件/服务>
  -> <API/IPC/第三方服务>
  -> <成功/失败状态>
```

## 日志与调试

- 调用入口：<应记录什么>
- 关键参数摘要：<脱敏摘要，不记录敏感原文>
- 成功结果：<应记录什么>
- 失败原因：<应记录什么>

## 测试与验收

- 自动测试：`<test-file>`
- 稳定选择器：`data-testid="<id>"`
- 手动验收：<步骤>
- 跳过/阻塞：<原因，没有则写“无”>

## 边界情况

- <空态、错误态、权限、网络失败、降级逻辑>

## TODO 对应项

- `TODO.md`：<相关条目或章节>

## 最近同步

- commit：`<sha>`
- 日期：`YYYY-MM-DD`
- 变化摘要：<本轮 diff 对本模块的影响>
- 待确认：<没有则写“无”>
````

## 模块 `sync.json`

```json
{
  "lastPrdSyncCommit": "<sha>",
  "lastPrdSyncAt": "YYYY-MM-DD",
  "module": "<module>",
  "lastChangedFiles": [
    "<path>"
  ],
  "notes": "<本轮同步摘要>"
}
```

## 全局 `.update-prd-state.json`

```json
{
  "lastPrdSyncCommit": "<sha>",
  "lastPrdSyncAt": "YYYY-MM-DD",
  "mode": "incremental",
  "modulesUpdated": [
    "<module>"
  ],
  "notes": "<本轮同步摘要>"
}
```

## TODO 差距

```markdown
## 未完成目标 / 后续功能

- [ ] <功能名称>：来自 <prd/TODO/代码发现>；当前状态：未实现 / 部分实现 / 已降级；下一步：<具体可执行任务>。
```

## TODO 卸货记录

```markdown
## TODO 卸货记录

### YYYY-MM-DD
- 归档：<TODO 章节或功能块> -> `prd/<module>/README.md`
- 技术文档：`prd/<module>/technical.md`
- TODO 行数：<归档前> -> <归档后>
- 下轮活跃项：<仍需继续的任务>
```
