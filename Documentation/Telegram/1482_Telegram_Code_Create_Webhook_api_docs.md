# API Documentation: Generate Instagram Content from Top Trends with AI Image Generation

## Overview
Automated workflow: Generate Instagram Content from Top Trends with AI Image Generation. This workflow integrates 13 different services: stickyNote, httpRequest, facebookGraphApi, telegram, code. It contains 64 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 97
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.postgres`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.facebookGraphApi`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `telegramApi`
- `postgres`
- `facebookGraphApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
