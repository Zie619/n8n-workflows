# API Documentation: Extractfromfile Workflow

## Overview
Automated workflow: Extractfromfile Workflow. This workflow integrates 13 different services: webhook, stickyNote, outputParserItemList, splitInBatches, chainLlm. It contains 32 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `35e874df-2904-494e-a9f5-5a3f20f517f8`
- **Method**: `POST`
- **Webhook ID**: `35e874df-2904-494e-a9f5-5a3f20f517f8`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDocs`
- `@n8n/n8n-nodes-langchain.outputParserItemList`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Slack
- Google
- Google

## Required Credentials
- `slackApi`
- `openAiApi`
- `gmailOAuth2`
- `googleDocsOAuth2Api`

## Environment Variables
- `BASE_URL`
