# API Documentation: Set Workflow

## Overview
Automated workflow: Set Workflow. This workflow integrates 14 different services: stickyNote, httpRequest, filter, scheduleTrigger, clearbit. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 40
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.html`
- `n8n-nodes-base.openAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.clearbit`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `openAiApi`
- `clearbitApi`
- `googleCalendarOAuth2Api`
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`
