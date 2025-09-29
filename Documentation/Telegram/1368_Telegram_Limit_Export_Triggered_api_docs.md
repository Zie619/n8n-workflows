# API Documentation: 🦜✨Use OpenAI to Transcribe Audio + Summarize with AI + Save to Google Drive

## Overview
Automated workflow: 🦜✨Use OpenAI to Transcribe Audio + Summarize with AI + Save to Google Drive. This workflow integrates 12 different services: filter, stickyNote, googleDriveTrigger, telegram, googleDrive. It contains 47 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 52
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.googleDriveTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.limit`
- `n8n-nodes-base.googleDriveTrigger`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `openAiApi`
- `gmailOAuth2`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
