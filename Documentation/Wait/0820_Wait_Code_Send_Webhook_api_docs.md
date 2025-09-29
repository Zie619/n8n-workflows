# API Documentation: Code Workflow

## Overview
Automated workflow: Code Workflow. This workflow integrates 17 different services: textClassifier, microsoftOutlook, markdown, filter, wait. It contains 30 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 43
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.splitInBatches`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.microsoftExcel`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.if`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.wait`

## Integrations
- Microsoft
- Microsoft
- Google
- Microsoft

## Required Credentials
- `googlePalmApi`
- `microsoftExcelOAuth2Api`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- `API_BASE_URL`
