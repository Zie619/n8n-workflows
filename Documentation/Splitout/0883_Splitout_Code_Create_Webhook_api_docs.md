# API Documentation: If Workflow

## Overview
Automated workflow: If Workflow. This workflow integrates 16 different services: stickyNote, httpRequest, code, scheduleTrigger, agent. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.html`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
