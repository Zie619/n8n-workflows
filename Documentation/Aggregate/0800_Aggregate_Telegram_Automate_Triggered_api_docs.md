# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 9 different services: stickyNote, telegramTrigger, telegram, agent, stopAndError. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.memoryBufferWindow`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- No credentials required

## Environment Variables
- `BASE_URL`
