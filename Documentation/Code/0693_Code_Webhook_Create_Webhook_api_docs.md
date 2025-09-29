# API Documentation: Agent Workflow

## Overview
Automated workflow: Agent Workflow. This workflow integrates 12 different services: webhook, microsoftOutlook, stickyNote, httpRequest, code. It contains 36 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 49
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `new-lead-generated-in-erpnext`
- **Method**: `POST`
- **Webhook ID**: `a39ea4e2-99b7-4ae1-baff-9fb370333e2a`


## Node Types Used
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.googleSheetsTool`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.googleDocsTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Microsoft
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `googleDocsOAuth2Api`
- `microsoftOutlookOAuth2Api`
- `erpNextApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
