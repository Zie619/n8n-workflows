# API Documentation: Extract & Summarize Yelp Business Review with Bright Data and Google Gemini

## Overview
Automated workflow: Extract & Summarize Yelp Business Review with Bright Data and Google Gemini. This workflow integrates 10 different services: stickyNote, httpRequest, lmChatGoogleGemini, chainLlm, outputParserStructured. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 31
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `httpHeaderAuth`
- `googlePalmApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
