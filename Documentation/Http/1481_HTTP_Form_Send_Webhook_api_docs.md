# API Documentation: Send TTS (Text-to-speech) voice calls

## Overview
Automated workflow: Send TTS (Text-to-speech) voice calls. This workflow integrates 4 different services: stickyNote, httpRequest, formTrigger, stopAndError. It contains 7 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 16
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.formTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.formTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `httpBasicAuth`

## Environment Variables
- `WEBHOOK_URL`
