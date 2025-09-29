# API Documentation: RAG on living data

## Overview
Automated workflow: RAG on living data. This workflow integrates 18 different services: notionTrigger, stickyNote, textSplitterTokenSplitter, vectorStoreSupabase, chainRetrievalQa. It contains 36 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.notionTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.supabase`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.summarize`
- `@n8n/n8n-nodes-langchain.retrieverVectorStore`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.notionTrigger`
- `@n8n/n8n-nodes-langchain.chainRetrievalQa`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `notionApi`
- `supabaseApi`

## Environment Variables
- `WEBHOOK_URL`
