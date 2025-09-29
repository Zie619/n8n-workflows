# API Documentation: Gmailtrigger Workflow

## Overview
Automated workflow: Gmailtrigger Workflow. This workflow integrates 9 different services: textClassifier, stickyNote, gmailTrigger, lmChatGoogleGemini, stopAndError. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 37
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.gmailTrigger`

## Node Types Used
- `@n8n/n8n-nodes-langchain.textClassifier`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.sendInBlue`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.gmailTrigger`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`
- `sendInBlueApi`
- `smtp`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
