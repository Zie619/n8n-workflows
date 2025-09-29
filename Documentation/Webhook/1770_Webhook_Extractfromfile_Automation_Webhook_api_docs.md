# API Documentation: Image-Based Data Extraction API using Gemini AI

## Overview
Automated workflow: Image-Based Data Extraction API using Gemini AI. This workflow integrates 7 different services: webhook, stickyNote, httpRequest, set, respondToWebhook. It contains 18 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 39
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`

### Webhook Endpoints
- **Path**: `data-extractor`
- **Method**: `POST`
- **Webhook ID**: `18118afb-7fd2-47a5-a474-50813c5b20c8`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `googlePalmApi`

## Environment Variables
- `BASE_URL`
