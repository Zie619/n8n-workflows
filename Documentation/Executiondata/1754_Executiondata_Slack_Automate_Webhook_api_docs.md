# API Documentation: ClockifyBlockiaWorkflow

## Overview
Automated workflow: ClockifyBlockiaWorkflow. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 68
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.slackTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.toolCode`
- `n8n-nodes-base.executionData`
- `@n8n/n8n-nodes-langchain.toolHttpRequest`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.slackTrigger`

## Integrations
- Slack
- Slack
- Slack

## Required Credentials
- `slackApi`
- `openAiApi`
- `clockifyApi`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
