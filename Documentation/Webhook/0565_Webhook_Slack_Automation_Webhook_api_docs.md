# API Documentation: Respondtowebhook Workflow

## Overview
Automated workflow: Respondtowebhook Workflow. This workflow integrates 11 different services: webhook, stickyNote, agent, respondToWebhook, stopAndError. It contains 28 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `44c26a10-d54a-46ce-a522-5d83e8a854be`
- **Method**: `POST`
- **Webhook ID**: `44c26a10-d54a-46ce-a522-5d83e8a854be`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`

## Environment Variables
- `WEBHOOK_URL`
