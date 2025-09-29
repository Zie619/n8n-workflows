# API Documentation: AirQuality Scheduler

## Overview
Automated workflow: AirQuality Scheduler. This workflow integrates 9 different services: stickyNote, httpRequest, gmailTool, agent, scheduleTrigger. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.toolThink`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.gmailTool`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`
