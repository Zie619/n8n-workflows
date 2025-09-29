# API Documentation: Google Search Engine Results Page Extraction with Bright Data

## Overview
Automated workflow: Google Search Engine Results Page Extraction with Bright Data. This workflow integrates 10 different services: stickyNote, httpRequest, toolHttpRequest, lmChatGoogleGemini, agent. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `googlePalmApi`
- `httpHeaderAuth`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
