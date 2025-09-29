# API Documentation: Dynamic Form with AI

## Overview
Automated workflow: Dynamic Form with AI. This workflow integrates 11 different services: filter, formTrigger, stickyNote, splitOut, chainLlm. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.form`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required
