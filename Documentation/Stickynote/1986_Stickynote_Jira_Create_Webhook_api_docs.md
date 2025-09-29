# API Documentation: Create_Unique_Jira_tickets_from_Splunk_alerts

## Overview
Automated workflow: Create_Unique_Jira_tickets_from_Splunk_alerts. This workflow integrates 6 different services: webhook, stickyNote, set, stopAndError, jira. It contains 13 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `f2a52578-2fef-40a6-a7ff-e03f6b751a02`
- **Method**: `POST`
- **Webhook ID**: `f2a52578-2fef-40a6-a7ff-e03f6b751a02`


## Node Types Used
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `jiraSoftwareCloudApi`

## Environment Variables
- No environment variables required
