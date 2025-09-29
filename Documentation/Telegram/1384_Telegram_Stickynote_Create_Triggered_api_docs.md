# API Documentation: Post new Google Calendar events to Telegram

## Overview
Automated workflow: Post new Google Calendar events to Telegram. This workflow integrates 4 different services: stickyNote, googleCalendarTrigger, telegram, stopAndError. It contains 6 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleCalendarTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.googleCalendarTrigger`

## Integrations
- Google

## Required Credentials
- `googleCalendarOAuth2Api`

## Environment Variables
- No environment variables required
