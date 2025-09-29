# API Documentation: Telegram Chat with Buffering

## Overview
Automated workflow: Telegram Chat with Buffering. This workflow integrates 13 different services: telegramTrigger, stickyNote, wait, telegram, agent. It contains 25 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 30
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.telegramTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.supabase`
- `n8n-nodes-base.sort`
- `@n8n/n8n-nodes-langchain.memoryPostgresChat`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.telegramTrigger`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `telegramApi`
- `postgres`
- `supabaseApi`

## Environment Variables
- No environment variables required
