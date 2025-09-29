# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 14 different services: stickyNote, httpRequest, filter, code, scheduleTrigger. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.html`
- `n8n-nodes-base.googleCalendar`
- `n8n-nodes-base.clearbit`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`
