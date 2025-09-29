# API Documentation: Summarize Google Drive Documents with Mistral AI and Send via Gmail

## Overview
Automated workflow: Summarize Google Drive Documents with Mistral AI and Send via Gmail. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 12
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `@n8n/n8n-nodes-langchain.lmChatMistralCloud`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleDrive`
- `@n8n/n8n-nodes-langchain.chainSummarization`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `mistralCloudApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
