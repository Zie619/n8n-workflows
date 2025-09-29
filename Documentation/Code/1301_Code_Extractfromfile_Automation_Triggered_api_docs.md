# API Documentation: Amazon Ads AI Optimization

## Overview
Automated workflow: Amazon Ads AI Optimization. This workflow integrates 12 different services: stickyNote, code, chainLlm, googleDrive, merge. It contains 27 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 32
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.extractFromFile`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.code`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
