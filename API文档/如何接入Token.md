# Token Plan 与 API Key 接入

本文说明如何开通 **Token Plan**、获取 **Token Plan API Key**，以及与用量、按量计费 Key 的关系。具体配额以 [Token Plan 订阅页](https://platform.minimaxi.com/subscribe/token-plan) 及账户内展示为准。

## 获取 API Key

1. **订阅 Token Plan**  
   打开 [Token Plan](https://platform.minimaxi.com/subscribe/token-plan?code=JBlROVn3gJ&source=link)，选择套餐并完成支付。

2. **复制 Key**  
   订阅生效后，进入 [用户中心 → Token Plan / 支付与套餐](https://platform.minimaxi.com/user-center/payment/token-plan)，在套餐详情中复制 **Token Plan API Key**。

3. **写入本地环境变量（推荐）**  
   在项目根目录新建文件 `.env`（与运行代码的目录一致即可），填入你从控制台复制的 Key，**不要**加引号、不要多空格：

   ```env
   MINIMAX_API_KEY=这里粘贴你的_Token_Plan_API_Key
   ```

   - 将 `.env` 加入 `.gitignore`，避免把 Key 推送到远程仓库。  
   - 代码里从环境变量读取后，再拼到请求头，等价于：

   ```http
   Authorization: Bearer <与 MINIMAX_API_KEY 相同的值>
   ```

   示例（Python）：`api_key = os.environ["MINIMAX_API_KEY"]`，请求头 `{"Authorization": f"Bearer {api_key}"}`。其他语言同理读取 `MINIMAX_API_KEY` 即可。

## 重要说明

- **与按量计费 Key 区分**：Token Plan API Key 仅用于 Token Plan 权益范围内的接口，**不能**与仅适用于按量计费文本等场景的 API Key 互换使用；需切换计费方式时请改用对应类型的 Key（见下文「用量用尽时」）。
- **有效期**：Key 仅在当前 Token Plan **订阅有效期内**可用；过期后需续费或改用其他计费方式。
- **安全**：勿将 Key 写入公开仓库或客户端明文分发，避免盗用导致额度损失。

## 用量规则（摘要）

- **文本（如 M2.7 / M2.7-highspeed）**：多按 **请求次数** 计，在 **约 5 小时滚动窗口** 内重置（以控制台说明为准）。
- **语音、图像、视频、音乐等**：多按 **自然日配额** 计，**每日**重置。

以下为文档整理时的套餐额度参考表；若与官网不一致，**以官网与用户中心为准**。

### 标准版

| 能力 | Starter | Plus | Max |
| :--- | :--- | :--- | :--- |
| M2.7（次 / 5 小时） | 600 | 1,500 | 4,500 |
| Speech 2.8（字符 / 日） | — | 4,000 | 11,000 |
| image-01（张 / 日） | — | 50 | 120 |
| Hailuo-2.3-Fast 768P 6s（个 / 日） | — | — | 2 |
| Hailuo-2.3 768P 6s（个 / 日） | — | — | 2 |
| Music-2.6（首 / 日，限免策略以官网为准） | 100 | 100 | 100 |

### 极速版

| 能力 | Plus-极速版 | Max-极速版 | Ultra-极速版 |
| :--- | :--- | :--- | :--- |
| M2.7-highspeed（次 / 5 小时） | 1,500 | 4,500 | 30,000 |
| Speech 2.8（字符 / 日） | 9,000 | 19,000 | 50,000 |
| image-01（张 / 日） | 100 | 200 | 800 |
| Hailuo-2.3-Fast 768P 6s（个 / 日） | — | 3 | 5 |
| Hailuo-2.3 768P 6s（个 / 日） | — | 3 | 5 |
| Music-2.6（首 / 日） | 100 | 100 | 100 |

非文本模型调用示例与 CLI 说明见：[MiniMax CLI（Token Plan）](https://platform.minimaxi.com/docs/token-plan/minimax-cli)。

## 在 AI 编程工具中配置

在对应工具里将 Base URL / Provider 配为 MiniMax 文档要求的形式，并把 **API Key** 填为上述 Token Plan Key。官方接入说明（链接指向 MiniMax 文档站）：

| 工具 | 文档 |
| :--- | :--- |
| OpenClaw | [接入说明](https://platform.minimaxi.com/docs/token-plan/openclaw) |
| Claude Code | [接入说明](https://platform.minimaxi.com/docs/token-plan/claude-code) |
| Cursor | [接入说明](https://platform.minimaxi.com/docs/token-plan/cursor) |
| TRAE | [接入说明](https://platform.minimaxi.com/docs/token-plan/trae) |
| Cline | [接入说明](https://platform.minimaxi.com/docs/token-plan/cline) |
| Hermes Agent | [接入说明](https://platform.minimaxi.com/docs/token-plan/hermes-agent) |
| 其他工具 | [其他工具](https://platform.minimaxi.com/docs/token-plan/other-tools) |

若上述路径 404，请在 [Token Plan 文档目录](https://platform.minimaxi.com/docs) 内搜索工具名。

## 用量用尽时

**文本（5 小时窗口）**

1. **改用按量计费**：将请求使用的 Key 换为 [按量计费 / 接口密钥](https://platform.minimaxi.com/user-center/basic-information/interface-key) 中申请的 Key，按平台计费规则从账户余额扣费。  
2. **等待窗口恢复**：暂停调用，待当前滚动窗口内额度释放后再用 Token Plan Key 调用。

**非文本（每日配额）**

1. **改用按量计费**：使用支持对应模型的按量计费 Key（若该模型支持）。  
2. **等待次日重置**：每日配额在指定时刻重置，以控制台说明为准。

---

**说明**：文中套餐名、数字与「限免」策略可能随官方调整而变化，接入与排错请以 [MiniMax 开放平台](https://platform.minimaxi.com) 当前页面为准。
