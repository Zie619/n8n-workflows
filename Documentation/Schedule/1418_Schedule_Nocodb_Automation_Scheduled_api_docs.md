# API Documentation: Noco Kanban Board with AI Prioritization

## Overview
Automated workflow: Noco Kanban Board with AI Prioritization. This workflow integrates 15 different services: stickyNote, formTrigger, scheduleTrigger, agent, outputParserStructured. It contains 33 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 54
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.nocoDb`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack

## Required Credentials
- `slackOAuth2Api`
- `openAiApi`
- `nocoDbApiToken`
- `smtp`

## Environment Variables
- No environment variables required
