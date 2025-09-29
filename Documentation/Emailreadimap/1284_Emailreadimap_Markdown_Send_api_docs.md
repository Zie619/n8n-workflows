# API Documentation: AI Email processing autoresponder with approval (Yes/No)

## Overview
Automated workflow: AI Email processing autoresponder with approval (Yes/No). This workflow integrates 13 different services: stickyNote, markdown, vectorStoreQdrant, agent, set. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- Manual trigger (no automatic triggers configured)

## Node Types Used
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.set`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `qdrantApi`
- `openAiApi`
- `imap`
- `gmailOAuth2`
- `smtp`

## Environment Variables
- No environment variables required
