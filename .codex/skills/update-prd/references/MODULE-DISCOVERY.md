# 模块发现与影响范围判断

`update-prd` 面向多种项目形态，包括但不限于 Next.js、Electron、Vite Chrome Extension；不能写死任何单一框架的路径映射。本文件提供通用判断方法：从项目事实和变更线索中发现模块。

## 目标

把“最近代码变化”转成一份可执行的 PRD 更新范围：

- 哪些已有模块需要更新
- 是否出现新模块
- 哪些变化只影响技术文档
- 哪些变化无法确认，需要写入待确认项或询问用户

## 判断顺序

### 1. 识别项目形态

优先查看这些文件：

- `package.json`
- 框架配置文件，如 `next.config.*`、`vite.config.*`、`electron-builder.*`、`manifest.json`
- 入口目录，如 `app/`、`pages/`、`src/`、`main/`、`renderer/`、`preload/`、`background/`、`content/`、`popup/`
- README、已有 `prd/README.md`、`TODO.md`

项目形态只用于理解结构，不用于硬编码映射。

### 2. 读取已有模块

已有 PRD 是第一优先级：

- `prd/README.md`
- `prd/<module>/README.md`
- `prd/<module>/technical.md`
- `TODO.md` 中的功能章节和未完成目标

如果代码 diff 中出现的词与已有模块名、入口名、功能名高度相关，优先映射到已有模块。

### 3. 读取 Git diff

有同步状态时使用：

```bash
git diff <lastPrdSyncCommit>...HEAD --stat
git diff <lastPrdSyncCommit>...HEAD --name-only
```

没有同步状态时，使用全量扫描：

```bash
find . -maxdepth 3 -type f
rg -n "TODO|fetch|ipc|api|route|schema|type|testid|data-testid"
```

实际执行时优先使用 `rg` 和仓库已有脚本；跳过依赖、构建产物、缓存、日志和密钥文件。

### 4. 按功能聚类

将变化文件按以下线索聚类：

- 文件名、目录名和模块名是否相同或相近
- 页面入口、弹窗入口、菜单入口、浏览器扩展入口是否指向同一用户流程
- 组件是否被某个页面或功能模块主要使用
- API、IPC、后台任务是否服务同一个用户动作
- 数据结构、schema、store、hook 是否被同一组文件引用
- 测试文件是否描述了某个模块行为
- TODO 或 PRD 中是否已有同名功能项

聚类结论必须能用代码路径或 TODO/PRD 条目支撑。

## 框架线索示例

以下只是启发式线索，不是固定映射。

### Next.js

- `app/**/page.*`、`pages/**` 可能代表页面或用户流程
- `app/api/**`、`pages/api/**` 可能代表服务能力、第三方调用或降级逻辑
- `components/**` 可能代表交互组件或跨模块 UI
- `lib/**`、`hooks/**`、`types/**` 可能影响业务规则、状态和数据结构

### Electron

- `main/**` 可能涉及主进程能力、系统集成、窗口管理
- `preload/**` 可能涉及 IPC 桥接和安全边界
- `renderer/**` 可能涉及用户界面与交互模块
- IPC channel 变化通常要同步技术文档的调用入口、参数摘要、成功/失败日志要求

### Vite Chrome Extension

- `manifest.json` 可能影响权限、入口、内容脚本和后台能力
- `background/**` 可能影响后台任务、事件监听和长期状态
- `content/**` 可能影响页面注入能力
- `popup/**`、`options/**` 可能影响用户入口和配置流程

### 通用 Web / 工具项目

- `src/routes/**`、`src/pages/**`、`src/views/**` 可能是用户流程
- `src/components/**` 可能是复用交互模块
- `src/services/**`、`src/api/**` 可能是服务调用与降级逻辑
- `src/store/**`、`src/state/**`、`src/models/**` 可能是数据状态
- `tests/**`、`*.spec.*`、`*.test.*` 可能提供验收事实

## 影响范围报告模板

每次增量同步前先形成简短报告：

```markdown
## PRD 影响范围

- 同步范围：`<lastPrdSyncCommit>...HEAD` / 全量扫描
- 项目形态：Next.js / Electron / Chrome Extension / 其他（基于哪些文件判断）
- 受影响模块：
  - `<module>`：变化文件 `<path>`；原因 `<用户流程/API/数据结构/测试变化>`
- 可能新增模块：
  - `<module>`：依据 `<path 或 TODO 条目>`
- 仅需更新技术文档：
  - `<module>`：例如日志、测试、IPC 参数、数据字段变化
- 待确认：
  - `<path>`：无法稳定归入现有模块，建议用户确认或暂列 TODO
```

## 处理不确定性

- 不能确认模块时，不要强行归类；写入“待确认影响范围”。
- 代码只做内部重命名但用户行为不变时，产品 README 可不改，只更新技术文档的路径。
- 依赖、配置、测试变化如果影响用户可见行为，要更新产品 README；否则只更新技术文档。
- 发现 PRD 与代码冲突时，以当前代码事实为准，并把文档差距写回 TODO 或待确认项。
