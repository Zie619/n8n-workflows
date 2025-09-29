# API Documentation: AI Document Assistant via Telegram + Supabase

## Overview
Automated workflow: AI Document Assistant via Telegram + Supabase. This workflow integrates 20 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, switch, toolThink, extractFromFile. It contains 39 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 44
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `n8n-nodes-base.openWeatherMapTool`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.telegramTrigger`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `@n8n/n8n-nodes-langchain.toolThink`
- `n8n-nodes-base.set`

## Integrations
- Google
- Google

## Required Credentials
- `openWeatherMapApi`
- `telegramApi`
- `googlePalmApi`
- `supabaseApi`

## Environment Variables
- No environment variables required
