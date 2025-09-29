# API Documentation: Generate SQL queries from schema only - AI-powered

## Overview
Automated workflow: Generate SQL queries from schema only - AI-powered. This workflow integrates 15 different services: convertToFile, stickyNote, mySql, agent, readWriteFile. It contains 34 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 39
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.mySql`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.readWriteFile`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `mySql`

## Environment Variables
- No environment variables required
