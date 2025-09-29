# API Documentation: Email mailbox as Todoist tasks

## Overview
Automated workflow: Email mailbox as Todoist tasks. This workflow integrates 13 different services: stickyNote, scheduleTrigger, agent, outputParserStructured, merge. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 36
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.emailReadImap`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.todoist`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`
- `imap`
- `gmailOAuth2`
- `todoistApi`

## Environment Variables
- No environment variables required
