# API Documentation: Openai Workflow

## Overview
Automated workflow: Openai Workflow. This workflow integrates 10 different services: postgresTool, stickyNote, httpRequest, webhook, set. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 43
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `d074ca1e-52f9-47af-8587-8c24d431f9cd`
- **Method**: `POST`
- **Webhook ID**: `7f176935-cb83-4147-ac14-48c8d747863a`


## Node Types Used
- `n8n-nodes-base.supabase`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.if`
- `n8n-nodes-base.postgresTool`
- `n8n-nodes-base.set`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `postgres`
- `supabaseApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
