# API Documentation: Google Trend Data Extract, Summarization with Bright Data & Google Gemini

## Overview
Automated workflow: Google Trend Data Extract, Summarization with Bright Data & Google Gemini. This workflow integrates 12 different services: stickyNote, httpRequest, lmChatGoogleGemini, readWriteFile, chainLlm. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 43
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.gmail`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.function`
- `n8n-nodes-base.readWriteFile`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
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
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
