# API Documentation: ⚡AI-Powered YouTube Playlist & Video Summarization and Analysis v2

## Overview
Automated workflow: ⚡AI-Powered YouTube Playlist & Video Summarization and Analysis v2. This workflow integrates 24 different services: stickyNote, vectorStoreQdrant, textSplitterRecursiveCharacterTextSplitter, merge, switch. It contains 89 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 106
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-youtube-transcription-dmr.youtubeTranscripter`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreQdrant`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.embeddingsGoogleGemini`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.redis`
- `n8n-nodes-base.if`
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `qdrantApi`
- `googlePalmApi`
- `redis`

## Environment Variables
- `BASE_URL`
