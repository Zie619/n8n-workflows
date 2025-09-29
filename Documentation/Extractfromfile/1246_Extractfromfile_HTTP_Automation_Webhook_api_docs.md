# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 19 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, merge, switch, lmChatOpenAi. It contains 42 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 55
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.supabase`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.if`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `supabaseApi`

## Environment Variables
- `BASE_URL`
