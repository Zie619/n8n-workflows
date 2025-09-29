# API Documentation: Scheduletrigger Workflow

## Overview
Automated workflow: Scheduletrigger Workflow. This workflow integrates 12 different services: stickyNote, scheduleTrigger, chainLlm, outputParserStructured, set. It contains 30 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- No external integrations detected

## Required Credentials
- `jiraSoftwareCloudApi`
- `openAiApi`

## Environment Variables
- No environment variables required
