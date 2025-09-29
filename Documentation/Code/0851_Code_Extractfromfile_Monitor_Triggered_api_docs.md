# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 12 different services: textClassifier, stickyNote, microsoftOutlook, code, microsoftOutlookTrigger. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.microsoftOutlookTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.microsoftOutlookTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Microsoft
- Microsoft
- Microsoft
- Microsoft

## Required Credentials
- `openAiApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- No environment variables required
