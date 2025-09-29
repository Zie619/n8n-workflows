# API Documentation: MiniBear Webhook

## Overview
Automated workflow: MiniBear Webhook. This workflow integrates 12 different services: webhook, stickyNote, httpRequest, microsoftToDo, agent. It contains 69 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 122
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `minibear`
- **Method**: `POST`
- **Webhook ID**: `4ef1a53c-a1ec-4a63-a7a5-469423502333`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.microsoftToDo`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.microsoftOneDrive`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.microsoftTeams`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft

## Required Credentials
- `microsoftOneDriveOAuth2Api`
- `microsoftTeamsOAuth2Api`
- `httpHeaderAuth`
- `microsoftToDoOAuth2Api`
- `openRouterApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
