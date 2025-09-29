# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 11 different services: stickyNote, code, agent, stopAndError, lmChatOpenAi. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.chatTrigger`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`

## Environment Variables
- No environment variables required
