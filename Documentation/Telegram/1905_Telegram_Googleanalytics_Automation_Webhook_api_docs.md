# API Documentation: Online Marketing Weekly Report

## Overview
Automated workflow: Online Marketing Weekly Report. This workflow integrates 17 different services: stickyNote, httpRequest, facebookGraphApi, telegram, code. It contains 68 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 93
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.executeWorkflowTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.facebookGraphApi`
- `n8n-nodes-base.googleAnalytics`
- `@n8n/n8n-nodes-langchain.agent`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.toolWorkflow`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `n8n-nodes-base.code`
- `n8n-nodes-base.emailSend`
- `@n8n/n8n-nodes-langchain.lmChatOpenAi`
- `n8n-nodes-base.executeWorkflowTrigger`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `openAiApi`
- `googleAnalyticsOAuth2`
- `googleOAuth2Api`
- `facebookGraphApi`
- `googleAdsOAuth2Api`
- `smtp`
- `telegramApi`

## Environment Variables
- `WEBHOOK_URL`
- `API_BASE_URL`
