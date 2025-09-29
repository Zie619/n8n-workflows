# API Documentation: Splitout Workflow

## Overview
Automated workflow: Splitout Workflow. This workflow integrates 15 different services: filter, stickyNote, code, toolSerpApi, scheduleTrigger. It contains 44 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 49
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.toolSerpApi`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.code`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.toolWikipedia`

## Integrations
- Slack
- Slack
- Google
- Slack
- Slack
- Google
- Google
- Slack

## Required Credentials
- No credentials required

## Environment Variables
- No environment variables required
