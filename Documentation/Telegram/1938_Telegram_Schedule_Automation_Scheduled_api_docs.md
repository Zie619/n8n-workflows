# API Documentation: #️⃣Nostr #damus AI Powered Reporting + Gmail + Telegram

## Overview
Automated workflow: #️⃣Nostr #damus AI Powered Reporting + Gmail + Telegram. This workflow integrates 12 different services: stickyNote, markdown, telegram, lmChatGoogleGemini, scheduleTrigger. It contains 29 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.merge`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.stopAndError`
- `n8n-nodes-nostrobots.nostrobotsread`
- `n8n-nodes-base.aggregate`
- `@n8n/n8n-nodes-langchain.lmChatGoogleGemini`
- `n8n-nodes-base.markdown`
- `n8n-nodes-base.gmail`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `telegramApi`
- `googlePalmApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
