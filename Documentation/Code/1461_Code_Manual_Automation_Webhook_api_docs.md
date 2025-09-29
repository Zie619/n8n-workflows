# API Documentation: YouTube Video Analyzer with AI

## Overview
Automated workflow: YouTube Video Analyzer with AI. This workflow integrates 13 different services: stickyNote, httpRequest, code, chainLlm, outputParserStructured. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 38
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.lmChatDeepSeek`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `deepSeekApi`
- `openAiApi`
- `httpHeaderAuth`
- `openRouterApi`
- `smtp`

## Environment Variables
- `BASE_URL`
