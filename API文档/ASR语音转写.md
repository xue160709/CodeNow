# ASR 语音转写（Audio Transcriptions）

SiliconFlow ASR 接口，用于把音频文件转写成文本。接口使用 `multipart/form-data` 上传音频文件。

官方文档：https://api-docs.siliconflow.cn/docs/api/audio-transcriptions-post

## 接入信息

| 项 | 值 |
| :--- | :--- |
| Endpoint | `POST https://api.siliconflow.cn/v1/audio/transcriptions` |
| 鉴权 | `Authorization: Bearer <SILICONFLOW_API_KEY>` |
| `Content-Type` | `multipart/form-data` |
| 示例模型 | `FunAudioLLM/SenseVoiceSmall` |
| 可选模型 | `FunAudioLLM/SenseVoiceSmall`、`TeleAI/TeleSpeechASR` |

## 请求体

| 字段 | 类型 | 必填 | 说明 |
| :--- | :--- | :---: | :--- |
| `file` | file | 是 | 音频文件对象，不是文件名字符串；时长不超过 1 小时，文件大小不超过 50MB |
| `model` | string | 是 | ASR 模型名称 |

## cURL 示例

```bash
curl --request POST \
  --url https://api.siliconflow.cn/v1/audio/transcriptions \
  --header "Authorization: Bearer ${SILICONFLOW_API_KEY}" \
  --form "file=@path/to/your/audio.mp3" \
  --form "model=FunAudioLLM/SenseVoiceSmall"
```

## Python 示例

```python
import os
import requests

url = "https://api.siliconflow.cn/v1/audio/transcriptions"
headers = {
    "Authorization": f"Bearer {os.environ['SILICONFLOW_API_KEY']}",
}
file_path = "path/to/your/audio.mp3"

with open(file_path, "rb") as audio_file:
    files = {
        "file": ("audio.mp3", audio_file, "audio/mpeg"),
        "model": (None, "FunAudioLLM/SenseVoiceSmall"),
    }
    response = requests.post(url, headers=headers, files=files, timeout=120)

response.raise_for_status()
print(response.json()["text"])
```

## JavaScript 示例

浏览器环境可直接把用户选择的 `File` 放进 `FormData`；Node.js 环境需要使用运行时支持的 `File` / `Blob` 或读取文件后构造表单。生产环境建议由服务端代理调用，避免在浏览器暴露 API Key。

```javascript
const apiKey = "<SILICONFLOW_API_KEY>";
const form = new FormData();
form.append("file", audioFile);
form.append("model", "FunAudioLLM/SenseVoiceSmall");

const response = await fetch("https://api.siliconflow.cn/v1/audio/transcriptions", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
  },
  body: form,
});

const data = await response.json();
console.log(data.text);
```

## 响应与调试

成功响应：

```json
{
  "text": "转写后的文本"
}
```

排查问题时建议记录响应头中的 `x-siliconcloud-trace-id`、模型名、文件大小、音频时长、成功 / 失败结果和错误摘要。不要记录 API Key、完整音频原文或用户隐私内容。
