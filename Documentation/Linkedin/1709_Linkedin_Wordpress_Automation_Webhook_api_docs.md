# API Documentation: AI Social Media Publisher from WordPress

## Overview
Automated workflow: AI Social Media Publisher from WordPress. This workflow integrates 13 different services: stickyNote, wordpress, facebookGraphApi, httpRequest, twitter. It contains 31 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.facebookGraphApi`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.twitter`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.linkedIn`

## Integrations
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `linkedInOAuth2Api`
- `openRouterApi`
- `facebookGraphApi`
- `twitterOAuth2Api`
- `wordpressApi`

## Environment Variables
- `WEBHOOK_URL`
