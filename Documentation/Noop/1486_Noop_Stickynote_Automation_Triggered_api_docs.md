# API Documentation: Extract personal data with a self-hosted LLM Mistral NeMo

## Overview
Automated workflow: Extract personal data with a self-hosted LLM Mistral NeMo. This workflow integrates 8 different services: stickyNote, chainLlm, outputParserStructured, set, outputParserAutofixing. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 18
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.lmChatOllama`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.outputParserAutofixing`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`

## Integrations
- No external integrations detected

## Required Credentials
- `ollamaApi`

## Environment Variables
- No environment variables required
