# API Documentation: Linkedin Automation

## Overview
Automated workflow: Linkedin Automation. This workflow integrates 10 different services: filter, stickyNote, httpRequest, telegram, airtable. It contains 24 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 45
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.code`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.linkedIn`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`
- `linkedInOAuth2Api`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
