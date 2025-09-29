# API Documentation: HDW Lead Geländewagen

## Overview
Automated workflow: HDW Lead Geländewagen. This workflow integrates 22 different services: stickyNote, scheduleTrigger, hdwWebParserTool, lmChatOpenAi, if. It contains 118 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 123
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.openAi`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-hdw.hdwLinkedin`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-hdw.hdwLinkedinManagement`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-hdw.hdwWebParserTool`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `hdwLinkedinApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
