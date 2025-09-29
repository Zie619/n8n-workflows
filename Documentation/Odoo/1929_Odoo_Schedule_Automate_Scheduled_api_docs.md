# API Documentation: ERP AI chatbot for Odoo sales module

## Overview
Automated workflow: ERP AI chatbot for Odoo sales module. This workflow integrates 16 different services: convertToFile, stickyNote, scheduleTrigger, agent, readWriteFile. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 27
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.lmOpenAi`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.odoo`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.readWriteFile`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.convertToFile`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `odooApi`
- `openAiApi`

## Environment Variables
- No environment variables required
