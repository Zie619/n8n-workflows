# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 10 different services: stickyNote, markdown, scheduleTrigger, chainLlm, outputParserStructured. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.linear`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `linearApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
