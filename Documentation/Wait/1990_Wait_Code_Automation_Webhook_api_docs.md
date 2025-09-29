# API Documentation: OpenAI Assistant for Hubspot Chat

## Overview
Automated workflow: OpenAI Assistant for Hubspot Chat. This workflow integrates 10 different services: webhook, stickyNote, httpRequest, wait, airtable. It contains 59 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 112
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `hubspot-tinder`
- **Method**: `POST`
- **Webhook ID**: `637d5b46-b35f-4943-92a2-864ddce170f4`


## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- No external integrations detected

## Required Credentials
- `hubspotDeveloperApi`
- `openAiApi`
- `hubspotAppToken`
- `hubspotOAuth2Api`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
