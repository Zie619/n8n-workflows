# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 12 different services: microsoftOutlook, stickyNote, markdown, filter, splitInBatches. It contains 36 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.lmChatOllama`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`

## Integrations
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft
- Microsoft

## Required Credentials
- No credentials required

## Environment Variables
- `WEBHOOK_URL`
