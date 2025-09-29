# API Documentation: Send Daily Birthday Reminders from Google Contacts to Slack

## Overview
Automated workflow: Send Daily Birthday Reminders from Google Contacts to Slack. This workflow integrates 7 different services: filter, stickyNote, scheduleTrigger, stopAndError, slack. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.googleContacts`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Slack

## Required Credentials
- `slackOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
