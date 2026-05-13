---
name: git-commit
description: '使用约定式提交（Conventional Commits）分析变更、智能暂存并生成提交说明后执行 git commit。在用户要求提交变更、创建 git 提交或提到「/commit」时使用。支持：(1) 从变更自动推断 type 与 scope；(2) 根据 diff 生成约定式提交信息；(3) 可交互提交并可选覆盖 type/scope/描述；(4) 按逻辑分组智能暂存文件'
license: MIT
allowed-tools: Bash
---

# 基于约定式提交的 Git 提交

## 概述

依据 Conventional Commits 规范创建标准化、语义化的 git 提交。通过分析实际 diff 确定合适的 type、scope 与说明。

## 约定式提交格式

```
<type>[可选 scope]: <description>

[可选正文]

[可选脚注]
```

## 提交类型（Type）

| Type       | 用途                           |
| ---------- | ------------------------------ |
| `feat`     | 新功能                         |
| `fix`      | 缺陷修复                       |
| `docs`     | 仅文档                         |
| `style`    | 格式/样式（无逻辑变更）        |
| `refactor` | 重构（非新功能/非修复）        |
| `perf`     | 性能优化                       |
| `test`     | 新增/更新测试                  |
| `build`    | 构建系统或依赖                 |
| `ci`       | CI 或配置变更                  |
| `chore`    | 杂项/维护                      |
| `revert`   | 回滚某次提交                   |

## 破坏性变更（Breaking Changes）

```
# 在 type/scope 后加感叹号
feat!: remove deprecated endpoint

# 或使用 BREAKING CHANGE 脚注
feat: allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed
```

## 工作流

### 1. 分析 Diff

```bash
# 若已有暂存，使用已暂存的 diff
git diff --staged

# 若未暂存任何内容，使用工作区 diff
git diff

# 同时查看状态
git status --porcelain
```

### 2. 暂存文件（如需要）

若当前没有暂存，或希望按不同方式分组变更：

```bash
# 暂存指定文件
git add path/to/file1 path/to/file2

# 按模式暂存
git add *.test.*
git add src/components/*

# 交互式暂存（按块挑选）
git add -p
```

**切勿提交密钥**（如 .env、credentials.json、私钥等）。

### 3. 生成提交说明

分析 diff 后确定：

- **Type**：属于哪一类变更？
- **Scope**：影响哪个区域/模块？
- **Description**：一行概括改了什么（现在时、祈使语气，少于 72 字符）

### 4. 执行提交

```bash
# 单行
git commit -m "<type>[scope]: <description>"

# 多行（含正文/脚注）
git commit -m "$(cat <<'EOF'
<type>[scope]: <description>

<可选正文>

<可选脚注>
EOF
)"
```

## 最佳实践

- 每次提交只包含一个逻辑上的变更
- 现在时：写「add」而非「added」
- 祈使语气：写「fix bug」而非「fixes bug」
- 关联工单：`Closes #123`、`Refs #456`
- 标题行尽量控制在 72 字符以内

## Git 安全约定

- 禁止修改 git config
- 未经用户明确要求，禁止执行破坏性命令（如 `--force`、hard reset）
- 除非用户要求，禁止使用 `--no-verify` 跳过钩子
- 禁止向 main/master 强推
- 若因钩子导致提交失败，应修复问题后**新建提交**（不要用 amend 掩盖）
