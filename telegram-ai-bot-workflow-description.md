# Telegram AI Bot 工作流逻辑描述

## 工作流概览

这个 Telegram AI Bot 工作流由四个主要阶段组成，每个阶段位于独立的玻璃平台上，通过发光管道顺序连接。工作流的核心功能是接收 Telegram 消息，通过 AI 处理生成响应，并将响应发送回用户。

## 阶段描述

### 阶段1：触发与输入 (Trigger & Input)
**颜色：黄色**
**标记：触发(Trigger)**

位于左侧的黄色玻璃平台上，包含：
- **Telegram Trigger** 节点：监听 Telegram 聊天中的新消息，作为工作流的起点。

该阶段负责捕获用户输入，当有新消息到达时，通过发光管道将数据传递到下一阶段。

### 阶段2：消息预处理 (Message Preprocessing)
**颜色：绿色**
**标记：预处理(Preprocessing)**

位于中央偏左的绿色玻璃平台上，包含：
- **Preprocess Message** 节点：从 Telegram 消息中提取关键信息（消息文本、用户ID、用户名）。
- **Bot Settings** 节点：配置 AI 模型参数（系统提示、温度、最大令牌数）。

该阶段将原始消息数据转换为结构化格式，并准备好 AI 模型所需的配置参数，然后通过发光管道传递到下一阶段。

### 阶段3：AI 处理 (AI Processing)
**颜色：蓝色**
**标记：AI处理(AI Processing)**

位于中央偏右的蓝色玻璃平台上，包含：
- **OpenAI Chat** 节点：调用 GPT-3.5-turbo 模型，基于系统提示和用户消息生成智能响应。

该阶段是工作流的核心，负责将用户请求转换为 AI 生成的响应，然后通过发光管道传递到最后阶段。

### 阶段4：响应与交互 (Response & Interaction)
**颜色：紫色**
**标记：响应(Response)**

位于右侧的紫色玻璃平台上，包含：
- **Send Typing Action** 节点：向用户发送"正在输入"状态，提升用户体验。
- **Send Response** 节点：将 AI 生成的响应发送回 Telegram 聊天。

该阶段负责将 AI 生成的响应以友好的方式呈现给用户，完成整个交互流程。

## 数据流与连接

所有节点通过发光的白色管道顺序连接，形成完整的数据流：

```
Telegram Trigger → Preprocess Message → Bot Settings → Send Typing Action → OpenAI Chat → Send Response
```

工作流执行顺序：
1. 用户在 Telegram 发送消息
2. Telegram Trigger 捕获消息并触发工作流
3. Preprocess Message 提取消息和用户信息
4. Bot Settings 配置 AI 模型参数
5. Send Typing Action 显示"正在输入"状态
6. OpenAI Chat 生成 AI 响应
7. Send Response 将响应发送回用户

## 核心功能

- **实时响应**：通过 Telegram Trigger 实时监听消息，确保快速响应
- **智能处理**：利用 OpenAI GPT-3.5-turbo 模型生成高质量响应
- **用户体验优化**：添加"正在输入"状态，提升交互体验
- **可配置性**：通过 Bot Settings 节点可灵活调整 AI 模型参数

## 技术栈

- **触发层**：n8n-nodes-base.telegramTrigger
- **处理层**：n8n-nodes-base.set
- **AI层**：n8n-nodes-base.openAi (GPT-3.5-turbo)
- **响应层**：n8n-nodes-base.telegram

这个工作流提供了一个完整的 Telegram AI 机器人框架，可以根据实际需求进行扩展和定制，例如添加更复杂的对话管理、多轮对话支持或集成其他服务。