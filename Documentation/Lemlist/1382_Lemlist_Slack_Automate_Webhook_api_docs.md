# API Documentation: Markdown Workflow

## Overview
Automated workflow: Markdown Workflow. This workflow integrates 12 different services: stickyNote, markdown, httpRequest, chainLlm, outputParserStructured. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 31
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.lemlistTrigger`

## Node Types Used
- `n8n-nodes-base.lemlistTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.lemlist`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`
