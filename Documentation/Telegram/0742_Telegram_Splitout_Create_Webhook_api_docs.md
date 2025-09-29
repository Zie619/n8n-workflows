# API Documentation: YT AI News Playlist Creator/AI News Form Updater

## Overview
Automated workflow: YT AI News Playlist Creator/AI News Form Updater. This workflow integrates 10 different services: stickyNote, httpRequest, youTube, filter, telegram. It contains 33 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 46
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.youTube`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `telegramApi`
- `youTubeOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
