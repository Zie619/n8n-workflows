# API Documentation: xSend and check TTS (Text-to-speech) voice calls end email verification

## Overview
Automated workflow: xSend and check TTS (Text-to-speech) voice calls end email verification. This workflow integrates 9 different services: stickyNote, httpRequest, formTrigger, code, set. It contains 22 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 35
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.form`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.formTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `httpBasicAuth`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
