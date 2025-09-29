# API Documentation: Openaiassistant Workflow

## Overview
Automated workflow: Openaiassistant Workflow. This workflow integrates 10 different services: stickyNote, set, stopAndError, memoryManager, memoryBufferWindow. It contains 15 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.limit`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `@n8n/n8n-nodes-langchain.memoryManager`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.openAiAssistant`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required
