# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 16 different services: filter, httpRequest, stickyNote, code, scheduleTrigger. It contains 43 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 52
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatAnthropic`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.spotify`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google

## Required Credentials
- `anthropicApi`
- `googleSheetsOAuth2Api`
- `spotifyOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
