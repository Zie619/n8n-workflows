# API Documentation: Splitinbatches Workflow

## Overview
Automated workflow: Splitinbatches Workflow. This workflow integrates 15 different services: stickyNote, httpRequest, filter, formTrigger, code. It contains 31 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 48
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.respondToWebhook`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.linear`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.graphql`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpHeaderAuth`
- `notionApi`
- `linearApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
