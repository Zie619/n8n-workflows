# API Documentation: Youtube_Automation

## Overview
Automated workflow: Youtube_Automation. This workflow integrates 15 different services: stickyNote, youTube, httpRequest, wait, code. It contains 38 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 47
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.youTube`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.removeDuplicates`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google

## Required Credentials
- `youTubeOAuth2Api`
- `openAiApi`
- `googlePalmApi`

## Environment Variables
- `BASE_URL`
