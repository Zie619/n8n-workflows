# API Documentation: Formtrigger Workflow

## Overview
Automated workflow: Formtrigger Workflow. This workflow integrates 8 different services: stickyNote, httpRequest, formTrigger, set, discord. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.bannerbear`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `httpQueryAuth`
- `discordBotApi`
- `bannerbearApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
