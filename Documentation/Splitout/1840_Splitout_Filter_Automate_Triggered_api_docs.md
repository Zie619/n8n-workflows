# API Documentation: BambooHR AI-Powered Company Policies and Benefits Chatbot

## Overview
Automated workflow: BambooHR AI-Powered Company Policies and Benefits Chatbot. This workflow integrates 24 different services: stickyNote, textSplitterRecursiveCharacterTextSplitter, outputParserAutofixing, lmChatOpenAi, chatTrigger. It contains 58 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 63
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.documentDefaultDataLoader`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.textSplitterRecursiveCharacterTextSplitter`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.informationExtractor`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.bambooHr`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.toolVectorStore`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.vectorStoreSupabase`
- `n8n-nodes-base.filter`
- `@n8n/n8n-nodes-langchain.embeddingsOpenAi`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `supabaseApi`
- `openAiApi`
- `bambooHrApi`

## Environment Variables
- No environment variables required
