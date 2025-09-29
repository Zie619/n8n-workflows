# API Documentation: Textclassifier Workflow

## Overview
Automated workflow: Textclassifier Workflow. This workflow integrates 18 different services: textClassifier, filter, stickyNote, code, scheduleTrigger. It contains 36 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 41
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `discordBotApi`

## Environment Variables
- `WEBHOOK_URL`
