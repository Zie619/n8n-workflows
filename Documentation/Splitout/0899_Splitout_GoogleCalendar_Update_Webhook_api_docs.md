# API Documentation: Httprequest Workflow

## Overview
Automated workflow: Httprequest Workflow. This workflow integrates 12 different services: filter, httpRequest, stickyNote, markdown, splitOut. It contains 23 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 36
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.googleCalendarTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.googleCalendarTrigger`

## Integrations
- Google

## Required Credentials
- `googleCalendarOAuth2Api`
- `httpHeaderAuth`
- `gmailOAuth2`

## Environment Variables
- `API_BASE_URL`
