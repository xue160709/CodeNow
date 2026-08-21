# LLM / VLM 对话生成（Chat Completions）

SiliconFlow Chat Completions 接口，兼容 OpenAI Chat Completions 调用方式。LLM 文本对话和 VLM 图片理解共用同一个端点，区别在于 `messages[].content` 的结构。

官方文档：https://api-docs.siliconflow.cn/docs/api/chat-completions-post

## 接入信息

| 项 | 值 |
| :--- | :--- |
| Base URL | `https://api.siliconflow.cn/v1` |
| Endpoint | `POST https://api.siliconflow.cn/v1/chat/completions` |
| 鉴权 | `Authorization: Bearer <SILICONFLOW_API_KEY>` |
| `Content-Type` | `application/json` |
| LLM 示例模型 | `Pro/zai-org/GLM-4.7` |
| VLM 示例模型 | `zai-org/GLM-4.6V` |

模型列表会随平台调整，实际可用模型以 SiliconFlow 控制台 Models 页面为准。

## 请求体（常用字段）

| 字段 | 类型 | 场景 | 说明 |
| :--- | :--- | :--- | :--- |
| `model` | string | LLM / VLM | 必填，模型名称 |
| `messages` | array | LLM / VLM | 必填，对话消息列表 |
| `stream` | boolean | LLM / VLM | 可选，`true` 时使用 SSE 流式返回，结束事件为 `data: [DONE]` |
| `max_tokens` | integer | LLM / VLM | 可选，最大输出 token 数；需要给输入和系统开销预留余量 |
| `temperature` | number | LLM / VLM | 可选，控制随机性，最大值 `2` |
| `top_p` | number | LLM / VLM | 可选，核采样参数，建议不要和 `temperature` 同时大幅调整 |
| `top_k` | number | LLM / VLM | 可选，最大值 `100` |
| `frequency_penalty` | number | LLM / VLM | 可选，范围 `-2` 到 `2` |
| `stop` | string / array | LLM / VLM | 可选，最多 4 个停止序列 |
| `n` | integer | LLM / VLM | 可选，生成候选数量 |
| `response_format` | object | LLM / VLM | 可选，支持 `text`、`json_object`、`json_schema` |
| `tools` | array | LLM | 可选，函数调用工具列表 |
| `tool_choice` | string / object | LLM | 可选，工具选择策略 |
| `enable_thinking` | boolean | 部分推理模型 | 可选，开启 / 关闭 thinking 模式 |
| `thinking_budget` | integer | 部分推理模型 | 可选，推理 token 预算 |
| `reasoning_effort` | string | 部分推理模型 | 可选，如 `high`、`max` |

## messages 写法

LLM 文本对话可以直接把 `content` 写成字符串：

```json
[
  {"role": "system", "content": "你是一个有用的助手"},
  {"role": "user", "content": "你好，请介绍一下你自己"}
]
```

VLM 图片理解需要使用 content blocks 数组，把文字和图片都放进同一条 user 消息：

```json
[
  {
    "role": "user",
    "content": [
      {"type": "text", "text": "请描述这张图片里的内容"},
      {
        "type": "image_url",
        "image_url": {
          "url": "https://example.com/image.jpg"
        }
      }
    ]
  }
]
```

VLM 注意点：

- `model` 必须选择支持视觉输入的模型。
- 图片 URL 需要能被 SiliconFlow 服务端访问；本地文件通常需要先上传到可访问地址。
- 同一条用户消息中可以组合文字说明和图片输入，便于模型理解任务意图。

## 文本对话示例

### cURL

```bash
curl --request POST \
  --url https://api.siliconflow.cn/v1/chat/completions \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${SILICONFLOW_API_KEY}" \
  --data '{
    "model": "Pro/zai-org/GLM-4.7",
    "messages": [
      {"role": "system", "content": "你是一个有用的助手"},
      {"role": "user", "content": "你好，请介绍一下你自己"}
    ]
  }'
```

### Python

```python
# pip install openai
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)

response = client.chat.completions.create(
    model="Pro/zai-org/GLM-4.7",
    messages=[
        {"role": "system", "content": "你是一个有用的助手"},
        {"role": "user", "content": "你好，请介绍一下你自己"},
    ],
)

print(response.choices[0].message.content)
```

### JavaScript

```javascript
const response = await fetch("https://api.siliconflow.cn/v1/chat/completions", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${process.env.SILICONFLOW_API_KEY}`,
  },
  body: JSON.stringify({
    model: "Pro/zai-org/GLM-4.7",
    messages: [
      { role: "system", content: "你是一个有用的助手" },
      { role: "user", content: "你好，请介绍一下你自己" },
    ],
  }),
});

console.log(await response.json());
```

## 流式输出示例

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)

stream = client.chat.completions.create(
    model="Pro/zai-org/GLM-4.7",
    messages=[{"role": "user", "content": "用三句话解释什么是流式输出"}],
    stream=True,
)

for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)
```

## VLM 图片理解示例

### cURL

```bash
curl --request POST \
  --url https://api.siliconflow.cn/v1/chat/completions \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer ${SILICONFLOW_API_KEY}" \
  --data '{
    "model": "zai-org/GLM-4.6V",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "请描述这张图片里的内容"},
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/image.jpg"
            }
          }
        ]
      }
    ],
    "temperature": 0.7,
    "max_tokens": 1000
  }'
```

### Python

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["SILICONFLOW_API_KEY"],
    base_url="https://api.siliconflow.cn/v1",
)

response = client.chat.completions.create(
    model="zai-org/GLM-4.6V",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "请描述这张图片里的内容"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=1000,
)

print(response.choices[0].message.content)
```

## 响应与调试

成功响应的正文包含 `choices`、`usage`、`created`、`model` 等字段；常用读取路径是：

```python
response.choices[0].message.content
```

排查问题时建议记录响应头中的 `x-siliconcloud-trace-id`。日志只记录请求入口、模型名、是否流式、图片数量或图片 URL 域名、成功 / 失败结果和错误摘要，不要输出 API Key、完整用户隐私文本或完整图片地址。
