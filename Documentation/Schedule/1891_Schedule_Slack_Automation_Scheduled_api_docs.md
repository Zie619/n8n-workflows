# API Documentation: Daily meetings summarization with Gemini AI

## Overview
Automated workflow: Daily meetings summarization with Gemini AI. This workflow integrates 7 different services: stickyNote, scheduleTrigger, agent, lmChatGoogleGemini, stopAndError. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.scheduleTrigger`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.googleCalendarTool`
- `n8n-nodes-base.stopAndError`

## Integrations
- Slack
- Google
- Google

## Required Credentials
- `slackApi`
- `googleCalendarOAuth2Api`
- `googlePalmApi`

## Environment Variables
- No environment variables required
