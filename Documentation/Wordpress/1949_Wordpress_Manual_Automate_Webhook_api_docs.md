# API Documentation: Automate Content Generator for WordPress with DeepSeek R1

## Overview
Automated workflow: Automate Content Generator for WordPress with DeepSeek R1. This workflow integrates 8 different services: wordpress, httpRequest, stickyNote, set, stopAndError. It contains 26 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 39
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.wordpress`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `n8n-nodes-base.httpRequest`
- `@n8n/n8n-nodes-langchain.openAi`
- `n8n-nodes-base.set`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google

## Required Credentials
- `googleSheetsOAuth2Api`
- `openAiApi`
- `wordpressApi`
- `wooCommerceApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
