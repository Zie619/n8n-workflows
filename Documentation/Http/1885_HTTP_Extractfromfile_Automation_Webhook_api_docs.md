# API Documentation: Chinese Translator

## Overview
Automated workflow: Chinese Translator. This workflow integrates 6 different services: webhook, stickyNote, httpRequest, switch, stopAndError. It contains 40 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 81
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `cn`
- **Method**: `POST`
- **Webhook ID**: `b2b119e6-6de5-4684-9a51-4706a1c20caf`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpHeaderAuth`

## Environment Variables
- `BASE_URL`
- `API_BASE_URL`
