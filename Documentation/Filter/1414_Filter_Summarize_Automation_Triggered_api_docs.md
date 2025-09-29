# API Documentation: Store Notion's Pages as Vector Documents into Supabase with OpenAI

## Overview
Automated workflow: Store Notion's Pages as Vector Documents into Supabase with OpenAI. This workflow integrates 10 different services: notionTrigger, stickyNote, filter, textSplitterTokenSplitter, summarize. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.notionTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.notion`
- `n8n-nodes-base.notionTrigger`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `@n8n/n8n-nodes-langchain.textSplitterTokenSplitter`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- No environment variables required
