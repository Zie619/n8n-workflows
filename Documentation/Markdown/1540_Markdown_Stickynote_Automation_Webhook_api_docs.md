# API Documentation: Airtable markdown to html

## Overview
Automated workflow: Airtable markdown to html. This workflow integrates 6 different services: webhook, stickyNote, markdown, airtable, stopAndError. It contains 11 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `848644e5-6b1d-42b3-9259-5828c29780a8`
- **Method**: `POST`
- **Webhook ID**: `848644e5-6b1d-42b3-9259-5828c29780a8`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.if`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
