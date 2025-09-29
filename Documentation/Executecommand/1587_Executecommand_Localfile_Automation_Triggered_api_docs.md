# API Documentation: Localfiletrigger Workflow

## Overview
Automated workflow: Localfiletrigger Workflow. This workflow integrates 10 different services: stickyNote, lmChatMistralCloud, splitOut, chainLlm, outputParserStructured. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.localFileTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.lmChatMistralCloud`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.localFileTrigger`
- `n8n-nodes-base.splitOut`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeCommand`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `mistralCloudApi`

## Environment Variables
- No environment variables required
