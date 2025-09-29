# API Documentation: LINE Assistant with Google Calendar and Gmail Integration

## Overview
Automated workflow: LINE Assistant with Google Calendar and Gmail Integration. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 42
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `linechatbotagent`
- **Method**: `POST`
- **Webhook ID**: `********-****-****-****-************`


## Node Types Used
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.toolWikipedia`

## Integrations
- Google
- Google

## Required Credentials
- `googleCalendarOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`
