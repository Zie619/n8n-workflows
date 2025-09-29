# API Documentation: Chat with local LLMs using n8n and Ollama

## Overview
Automated workflow: Chat with local LLMs using n8n and Ollama. This workflow integrates 4 different services: stickyNote, chainLlm, lmChatOllama, chatTrigger. It contains 5 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 10
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmChatOllama`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `@n8n/n8n-nodes-langchain.chainLlm`

## Integrations
- No external integrations detected

## Required Credentials
- `ollamaApi`

## Environment Variables
- No environment variables required
