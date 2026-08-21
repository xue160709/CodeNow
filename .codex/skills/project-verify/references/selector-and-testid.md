# 稳定选择器与 data-testid 规范

用于可机器验收的 Web UI：Next.js 页面、Electron renderer、插件 popup/options/side panel/new tab。

## 原则

- 所有可交互元素都应有稳定选择器，优先 `data-testid`。
- 选择器服务于验收，不表达样式，不依赖文案、顺序或 CSS hash。
- testid 全项目唯一，命名稳定，改 UI 文案时不需要改测试。

## 覆盖范围

必须覆盖：

- `<button>`
- `<a>` / 路由链接
- `<input>` / `<textarea>` / `<select>`
- 对话框、模态框、抽屉、折叠面板、菜单项
- 关键开关、上传、复制、保存、删除、提交、刷新等控件

非交互但需要断言时，可给关键状态容器加 testid，例如错误提示、结果列表、空态。

## 命名规则

```text
{页面或区域}-{元素类型}-{动作或语义}
```

常用元素类型：

| 类型 | 缩写 |
| --- | --- |
| button | `btn` |
| link | `link` |
| input | `input` |
| select | `select` |
| tab | `tab` |
| dialog | `dialog` |
| menu item | `menuitem` |
| status / message | `status` |
| list / item | `list` / `item` |

示例：

| 元素 | testid |
| --- | --- |
| 登录提交按钮 | `login-btn-submit` |
| 邮箱输入框 | `login-input-email` |
| 登出按钮 | `layout-btn-logout` |
| 结果列表 | `generate-list-results` |
| 错误提示 | `generate-status-error` |
| 插件 options 保存 Key | `options-btn-save-key` |

## 代码示例

```tsx
<button data-testid="login-btn-submit" onClick={handleSubmit}>
  登录
</button>

<input
  data-testid="login-input-email"
  type="email"
  value={email}
  onChange={(event) => setEmail(event.target.value)}
/>
```

## 验收步骤写法

TODO 或 `TESTING_CHECKLIST.md` 中建议写成：

```markdown
1. 打开 `/login`
2. 填写 `data-testid=login-input-email`
3. 填写 `data-testid=login-input-password`
4. 点击 `data-testid=login-btn-submit`
5. 预期跳转首页，并出现 `data-testid=layout-btn-logout`
```

## 缺失时怎么处理

- 开发阶段：由 `03-project-develop` / `project-iterate` 为本轮触及元素补齐。
- 验收阶段：若缺 testid 但可用 role/text 稳定定位，可先记录“临时定位”；同时把补 testid 写回 TODO 后续项。
- 不得因缺 testid 就无证据打勾。
