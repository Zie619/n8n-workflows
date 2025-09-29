# API Documentation: Effortless Email Management with AI

## Overview
Automated workflow: Effortless Email Management with AI. This workflow integrates 19 different services: stickyNote, vectorStoreQdrant, lmChatOpenAi, emailSend, textClassifier. It contains 42 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 63
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.emailSend`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatDeepSeek`
- `n8n-nodes-base.emailReadImap`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google

## Required Credentials
- `deepSeekApi`
- `qdrantApi`
- `openAiApi`
- `httpHeaderAuth`
- `imap`
- `gmailOAuth2`
- `googleDriveOAuth2Api`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
