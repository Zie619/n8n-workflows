# API Documentation: Lmchatopenai Workflow

## Overview
Automated workflow: Lmchatopenai Workflow. This workflow integrates 11 different services: webhook, stickyNote, agent, respondToWebhook, set. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `c63b08ce-360d-4185-aae1-294afef5cf2b`
- **Method**: `POST`
- **Webhook ID**: `c63b08ce-360d-4185-aae1-294afef5cf2b`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.microsoftOutlookTool`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Microsoft
- Microsoft
- Microsoft
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- No environment variables required
