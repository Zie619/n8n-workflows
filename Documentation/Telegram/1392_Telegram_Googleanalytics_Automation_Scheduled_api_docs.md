# API Documentation: Google Analytics: Weekly Report

## Overview
Automated workflow: Google Analytics: Weekly Report. This workflow integrates 11 different services: stickyNote, toolCalculator, telegram, code, scheduleTrigger. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 29
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.summarize`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.set`
- `@n8n/n8n-nodes-langchain.toolCalculator`
- `n8n-nodes-base.code`
- `n8n-nodes-base.emailSend`
- `n8n-nodes-base.googleAnalytics`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `telegramApi`
- `openAiApi`
- `googleAnalyticsOAuth2`
- `smtp`

## Environment Variables
- `WEBHOOK_URL`
