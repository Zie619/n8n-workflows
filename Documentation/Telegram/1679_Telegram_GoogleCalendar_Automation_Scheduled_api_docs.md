# API Documentation: Google Calendar Event Reminder

## Overview
Automated workflow: Google Calendar Event Reminder. This workflow integrates 8 different services: stickyNote, telegram, scheduleTrigger, agent, stopAndError. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.removeDuplicates`

## Integrations
- Google

## Required Credentials
- `telegramApi`
- `openAiApi`
- `googleCalendarOAuth2Api`

## Environment Variables
- No environment variables required
