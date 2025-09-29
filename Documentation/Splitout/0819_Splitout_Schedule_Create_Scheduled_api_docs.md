# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 19 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, scheduleTrigger, lmChatOpenAi, if. It contains 40 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 45
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.removeDuplicates`
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.jira`
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.sort`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `jiraSoftwareCloudApi`
- `openAiApi`
- `supabaseApi`

## Environment Variables
- No environment variables required
