# API Documentation: AI Agent to chat with you Search Console Data, using OpenAI and Postgres

## Overview
Automated workflow: AI Agent to chat with you Search Console Data, using OpenAI and Postgres. This workflow integrates 13 different services: webhook, stickyNote, httpRequest, agent, memoryPostgresChat. It contains 39 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 60
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.executeWorkflowTrigger`

### Webhook Endpoints
- **Path**: `a6820b65-76cf-402b-a934-0f836dee6ba0/chat`
- **Method**: `POST`
- **Webhook ID**: `a6820b65-76cf-402b-a934-0f836dee6ba0`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `oAuth2Api`
- `postgres`
- `httpBasicAuth`

## Environment Variables
- `BASE_URL`
