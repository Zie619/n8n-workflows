# API Documentation: Slack Workflow

## Overview
Automated workflow: Slack Workflow. This workflow integrates 17 different services: filter, stickyNote, code, lmChatGoogleGemini, scheduleTrigger. It contains 55 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 60
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Slack
- Slack
- Slack
- Google
- Google
- Google
- Slack

## Required Credentials
- `slackApi`
- `googlePalmApi`

## Environment Variables
- No environment variables required
