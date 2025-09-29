# API Documentation: YouTube to X Post- AlexK1919

## Overview
Automated workflow: YouTube to X Post- AlexK1919. This workflow integrates 16 different services: stickyNote, youTube, scheduleTrigger, set, discord. It contains 34 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 39
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.gmail`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.youTube`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.removeDuplicates`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-base.twitter`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.if`
- `@n8n/n8n-nodes-langchain.toolWikipedia`

## Integrations
- Google
- Google
- Slack

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `gmailOAuth2`
- `twitterOAuth2Api`
- `youTubeOAuth2Api`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
