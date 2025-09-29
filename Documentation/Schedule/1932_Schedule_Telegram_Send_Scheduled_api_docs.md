# API Documentation: Automatically Send Daily Meeting List to Telegram

## Overview
Automated workflow: Automatically Send Daily Meeting List to Telegram. This workflow integrates 7 different services: stickyNote, telegram, scheduleTrigger, function, set. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.function`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google

## Required Credentials
- `googleCalendarOAuth2Api`

## Environment Variables
- No environment variables required
