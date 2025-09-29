# API Documentation: Telegram Workflow

## Overview
Automated workflow: Telegram Workflow. This workflow integrates 16 different services: telegramTrigger, stickyNote, telegram, memoryRedisChat, code. It contains 50 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 55
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.memoryRedisChat`
- `@n8n/n8n-nodes-langchain.agent`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.memoryManager`
- `n8n-nodes-base.redis`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `telegramApi`
- `redis`

## Environment Variables
- No environment variables required
