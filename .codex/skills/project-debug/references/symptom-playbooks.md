# 症状排查手册

按用户看到的现象选择一个入口。不要一次照单全跑，先取最短证据链。

## 页面空白或加载不出

```text
页面空白
  -> console 是否有运行时异常？
  -> network 是否有 failed / pending？
  -> DOM snapshot 是否有内容但被 CSS 隐藏？
  -> 组件是否正确导出和挂载？
  -> 数据初始态是否导致提前 return null？
```

优先顺序：

1. `playwright-cli console`
2. `playwright-cli network`
3. `playwright-cli snapshot`
4. 搜索页面入口和最近改动文件

常见根因：

- React 运行时异常。
- API pending 导致 loading 不结束。
- CSS 容器高度为 0 或文字颜色与背景相同。
- 客户端组件缺少必要 provider。
- Next.js server/client 边界使用错误。

## 操作后数据不变

```text
用户操作
  -> handler 是否触发？
  -> API 是否发出？
  -> API 返回数据形状是否符合前端预期？
  -> state 是否更新？
  -> 组件是否读取了新的 state/props？
```

优先在 handler、API 响应处理、状态更新处加临时探针。只改一个位置后验证一次。

常见根因：

- 按钮没有绑定事件或被 disabled。
- 使用了错误的 `data-testid` / selector，测试点没点到真实按钮。
- `setState` 后又被旧数据覆盖。
- 缓存没有刷新或 query key 不一致。
- API 成功但返回字段名与前端读取字段不一致。

## 登录失败

```text
点击登录
  -> 表单校验是否通过？
  -> POST /login 是否发出？
  -> 返回 200 / 401 / 500 / CORS？
  -> token/session 是否保存？
  -> 路由跳转或用户状态是否更新？
```

注意不要记录密码、验证码、Token、Cookie。只记录字段是否存在和响应状态。

常见根因：

- 表单校验提前拦截。
- API 地址或环境变量错误。
- 401 没有 catch，loading 一直不恢复。
- session 写入成功但前端读取位置不一致。
- 登录成功后跳转到不存在页面。

## 服务启动失败

```text
启动失败
  -> 端口是否占用？
  -> node_modules 是否存在？
  -> 环境变量是否缺失？
  -> 构建配置是否报错？
  -> 最近改动是否破坏 import/export？
```

命令：

```bash
lsof -i :4000
npm run dev
npm run build
```

保留完整错误摘要，重点看第一处真实错误，后面的连锁报错不要抢先修。

## API 返回错误

```text
API 错误
  -> curl 是否能复现？
  -> 请求方法和路径是否正确？
  -> 参数摘要是否符合 schema？
  -> handler 是否进入？
  -> 第三方服务是否失败？
  -> 是否有降级逻辑？
```

需要长期日志时读取 `../../03-project-develop/references/logging-and-debugging.md`。

## Electron 或扩展异常

Electron：

- main / preload / renderer 分别看日志。
- IPC 调用要记录 channel、参数摘要、成功/失败。
- 确认 preload 暴露 API 与 renderer 调用名一致。

vite-web-extension：

- 区分 popup、content script、background。
- background 请求看 service worker 日志。
- content script 问题先确认脚本是否注入到目标页面。
- storage 相关问题检查 chrome.storage/localStorage 读写位置是否一致。
