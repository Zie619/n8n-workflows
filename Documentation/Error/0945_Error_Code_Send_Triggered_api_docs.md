# API Documentation: Error Alert and Summarizer

## Overview
Automated workflow: Error Alert and Summarizer. This workflow integrates 11 different services: stickyNote, code, agent, outputParserStructured, errorTrigger. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.errorTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.errorTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `n8nApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
