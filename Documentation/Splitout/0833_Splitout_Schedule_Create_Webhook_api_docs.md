# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 17 different services: microsoftOutlook, httpRequest, stickyNote, microsoftExcel, scheduleTrigger. It contains 36 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 45
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.microsoftExcel`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.html`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- Microsoft
- Microsoft

## Required Credentials
- `openAiApi`
- `microsoftExcelOAuth2Api`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- `BASE_URL`
