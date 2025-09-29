# API Documentation: Generate audio from text using OpenAI - text-to-speech Workflow

## Overview
Automated workflow: Generate audio from text using OpenAI - text-to-speech Workflow. This workflow integrates 5 different services: webhook, stickyNote, respondToWebhook, stopAndError, openAi. It contains 10 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 23
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.respondToWebhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `generate_audio`
- **Method**: `POST`
- **Webhook ID**: `28feeb38-ef2d-4a2e-bd7c-25a524068e25`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.respondToWebhook`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `openAiApi`

## Environment Variables
- No environment variables required
