# API Documentation: Manualtrigger Workflow

## Overview
Automated workflow: Manualtrigger Workflow. This workflow integrates 10 different services: stickyNote, hubspot, lmChatGoogleGemini, informationExtractor, set. It contains 19 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 24
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.noOp`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `@n8n/n8n-nodes-langchain.informationExtractor`

## Integrations
- Google
- Google
- Hubspot

## Required Credentials
- `hubspotAppToken`
- `googlePalmApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
