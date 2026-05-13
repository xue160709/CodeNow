# 文本生成（Chat / Messages）

MiniMax 文本模型，兼容 Anthropic Messages 与 OpenAI Chat Completions。

## 模型

| 模型 | 上下文窗口 | 说明 |
| :--- | :---: | :--- |
| MiniMax-M2.7 | 204,800 | 通用；约 60 TPS |
| MiniMax-M2.7-highspeed | 204,800 | M2.7 高速版；约 100 TPS |
| MiniMax-M2.5 | 204,800 | 通用；约 60 TPS |
| MiniMax-M2.5-highspeed | 204,800 | M2.5 高速版；约 100 TPS |
| MiniMax-M2.1 | 204,800 | 通用；约 60 TPS |
| MiniMax-M2.1-highspeed | 204,800 | M2.1 高速版；约 100 TPS |
| MiniMax-M2 | 204,800 | 编码与 Agent 场景 |

## 接入信息

| 项 | 值 |
| :--- | :--- |
| Base URL（Anthropic 协议，推荐） | `https://api.minimaxi.com/anthropic` |
| Base URL（OpenAI 协议） | `https://api.minimaxi.com/v1` |
| API Key | [Token Plan API Key](https://platform.minimaxi.com/user-center/payment/token-plan) |
| `model` | 见上表 |

流式：在请求体中设置 `stream: true`。

## Anthropic 协议（推荐）

支持 thinking 等块类型。端点：`POST https://api.minimaxi.com/anthropic/v1/messages`

```bash
curl https://api.minimaxi.com/anthropic/v1/messages \
  -H "Authorization: Bearer <MINIMAX_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.7",
    "max_tokens": 1000,
    "messages": [
      {"role": "user", "content": "Hi, how are you?"}
    ]
  }'
```

```python
# pip install anthropic
import anthropic

client = anthropic.Anthropic(
    base_url="https://api.minimaxi.com/anthropic",
    api_key="<MINIMAX_API_KEY>",
)

message = client.messages.create(
    model="MiniMax-M2.7",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Hi, how are you?"}],
)

for block in message.content:
    if block.type == "thinking":
        print(block.thinking)
    elif block.type == "text":
        print(block.text)
```

```javascript
// npm install @anthropic-ai/sdk
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://api.minimaxi.com/anthropic",
  apiKey: "<MINIMAX_API_KEY>",
});

const message = await client.messages.create({
  model: "MiniMax-M2.7",
  max_tokens: 1000,
  messages: [{ role: "user", content: "Hi, how are you?" }],
});

for (const block of message.content) {
  if (block.type === "thinking") console.log(block.thinking);
  else if (block.type === "text") console.log(block.text);
}
```

## OpenAI 协议

端点：`POST https://api.minimaxi.com/v1/chat/completions`

```bash
curl https://api.minimaxi.com/v1/chat/completions \
  -H "Authorization: Bearer <MINIMAX_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MiniMax-M2.7",
    "messages": [
      {"role": "user", "content": "Hi, how are you?"}
    ]
  }'
```

```python
# pip install openai
from openai import OpenAI

client = OpenAI(
    base_url="https://api.minimaxi.com/v1",
    api_key="<MINIMAX_API_KEY>",
)

response = client.chat.completions.create(
    model="MiniMax-M2.7",
    messages=[{"role": "user", "content": "Hi, how are you?"}],
)
print(response.choices[0].message.content)
```

```javascript
// npm install openai
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.minimaxi.com/v1",
  apiKey: "<MINIMAX_API_KEY>",
});

const response = await client.chat.completions.create({
  model: "MiniMax-M2.7",
  messages: [{ role: "user", content: "Hi, how are you?" }],
});

console.log(response.choices[0].message.content);
```
