# API Documentation: Daily AI News Translation & Summary with GPT-4 and Telegram Delivery

## Overview
Automated workflow: Daily AI News Translation & Summary with GPT-4 and Telegram Delivery. This workflow integrates 9 different services: stickyNote, httpRequest, telegram, scheduleTrigger, agent. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 31
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `openAiApi`

## Environment Variables
- `API_BASE_URL`
