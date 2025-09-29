# API Documentation: Stravatrigger Workflow

## Overview
Automated workflow: Stravatrigger Workflow. This workflow integrates 9 different services: stickyNote, code, lmChatGoogleGemini, agent, stravaTrigger. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 26
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.stravaTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stravaTrigger`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.whatsApp`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `googlePalmApi`
- `stravaOAuth2Api`
- `gmailOAuth2`
- `smtp`
- `whatsAppApi`

## Environment Variables
- No environment variables required
