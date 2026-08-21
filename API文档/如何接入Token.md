# SiliconFlow API Key 接入

本文说明如何注册 SiliconFlow、完成实名认证领取代金券、创建 API 密钥，并把密钥配置到本地项目中。

## 注册与代金券

1. 打开注册链接：[https://cloud.siliconflow.cn/i/2ty8He4Z](https://cloud.siliconflow.cn/i/2ty8He4Z)
2. 按页面提示注册或登录 SiliconFlow 账号。
3. 完成实名认证后，可以领取 **16 元代金券**。

代金券活动、领取入口、有效期和使用范围可能随平台调整，最终以 SiliconFlow 页面和账户内展示为准。

## 创建 API 密钥

1. 登录后进入 API 密钥页面：[https://cloud.siliconflow.cn/me/account/ak](https://cloud.siliconflow.cn/me/account/ak)
2. 点击「新建 API 密钥」。
3. 复制生成的 Key，并只保存到本地安全位置。

API Key 就像调用接口时的“通行证”。后续访问 LLM、VLM、图片生成、ASR 等接口时，都需要在请求头里带上它。

```http
Authorization: Bearer <SILICONFLOW_API_KEY>
```

## 写入本地环境变量

推荐在项目根目录创建 `.env` 文件，把 Key 写成环境变量：

```env
SILICONFLOW_API_KEY=这里粘贴你的_SiliconFlow_API_Key
```

注意：

- 不要加引号，不要在等号两边加多余空格。
- 将 `.env` 加入 `.gitignore`，避免把 API Key 提交到公开仓库。
- 不要把 API Key 写进前端页面、浏览器插件页面或公开代码中；生产环境建议由服务端代理调用 SiliconFlow。

## 接口接入参数

| 项 | 值 |
| :--- | :--- |
| Base URL | `https://api.siliconflow.cn/v1` |
| API Key 环境变量 | `SILICONFLOW_API_KEY` |
| 鉴权请求头 | `Authorization: Bearer <SILICONFLOW_API_KEY>` |
| Chat Completions | `POST https://api.siliconflow.cn/v1/chat/completions` |
| Images Generations | `POST https://api.siliconflow.cn/v1/images/generations` |
| Audio Transcriptions | `POST https://api.siliconflow.cn/v1/audio/transcriptions` |

## Python 读取示例

```python
import os

api_key = os.environ["SILICONFLOW_API_KEY"]
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
```

## JavaScript 读取示例

```javascript
const apiKey = process.env.SILICONFLOW_API_KEY;

const headers = {
  "Content-Type": "application/json",
  Authorization: `Bearer ${apiKey}`,
};
```

## 在 AI 编程工具中配置

如果工具支持 OpenAI Compatible Provider，可按下面方式配置：

| 配置项 | 值 |
| :--- | :--- |
| Provider / API 类型 | OpenAI Compatible |
| Base URL | `https://api.siliconflow.cn/v1` |
| API Key | 从 [API 密钥页面](https://cloud.siliconflow.cn/me/account/ak) 新建并复制的 Key |
| Model | 选择 SiliconFlow 控制台中可用的模型名 |

## 用量与安全提醒

- 代金券余额、计费规则、模型价格和活动权益以 SiliconFlow 控制台展示为准。
- 调用失败时，可记录模型名、接口路径、响应状态码、错误摘要和响应头里的 trace id，方便排查。
- 日志里不要输出 API Key、Token、完整用户输入、音频原文、私有图片 URL 等敏感信息。
- 如果怀疑 Key 泄露，立即到 [API 密钥页面](https://cloud.siliconflow.cn/me/account/ak) 删除旧 Key，并新建一个新的 API Key。
