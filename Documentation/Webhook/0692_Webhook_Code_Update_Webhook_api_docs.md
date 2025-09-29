# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 15 different services: webhook, stickyNote, httpRequest, microsoftOutlook, code. It contains 52 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 77
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `syncbricks-com-tutorial-candidate-shortlist`
- **Method**: `POST`
- **Webhook ID**: `f003f8ea-1f24-457c-8f28-762bd7942023`


## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.microsoftOutlook`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.erpNext`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.switch`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.whatsApp`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Microsoft

## Required Credentials
- `whatsAppApi`
- `googlePalmApi`
- `erpNextApi`
- `microsoftOutlookOAuth2Api`

## Environment Variables
- `BASE_URL`
