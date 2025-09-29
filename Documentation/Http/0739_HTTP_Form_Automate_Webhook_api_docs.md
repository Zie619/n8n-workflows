# API Documentation: Streamline Your Zoom Meetings with Secure, Automated Stripe Payments

## Overview
Automated workflow: Streamline Your Zoom Meetings with Secure, Automated Stripe Payments. This workflow integrates 11 different services: stickyNote, httpRequest, formTrigger, noOp, set. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 40
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.stripeTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.zoom`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.stripeTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Stripe

## Required Credentials
- `googleSheetsOAuth2Api`
- `zoomOAuth2Api`
- `gmailOAuth2`
- `stripeApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
