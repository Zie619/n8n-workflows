# API Documentation: AI Automated TikTok/Youtube Shorts/Reels Generator

## Overview
Automated workflow: AI Automated TikTok/Youtube Shorts/Reels Generator. This workflow integrates 13 different services: stickyNote, httpRequest, wait, code, scheduleTrigger. It contains 67 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 104
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.googleDrive`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.wait`

## Integrations
- Google
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleDriveOAuth2Api`
- `googleSheetsOAuth2Api`
- `openAiApi`
- `discordWebhookApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
- `API_BASE_URL`
