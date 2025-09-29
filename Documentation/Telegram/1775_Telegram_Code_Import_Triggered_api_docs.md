# API Documentation: AI-Driven WooCommerce Product Importer with SEO

## Overview
Automated workflow: AI-Driven WooCommerce Product Importer with SEO. This workflow integrates 11 different services: stickyNote, telegram, code, chainLlm, outputParserStructured. It contains 20 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 25
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.splitInBatches`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.googleSheets`
- `@n8n/n8n-nodes-langchain.chainLlm`
- `@n8n/n8n-nodes-langchain.lmChatOpenRouter`
- `n8n-nodes-base.code`
- `n8n-nodes-base.wooCommerce`
- `@n8n/n8n-nodes-langchain.outputParserStructured`
- `n8n-nodes-base.stopAndError`

## Integrations
- Google
- Google
- Google

## Required Credentials
- `openRouterApi`
- `googleSheetsOAuth2Api`
- `telegramApi`
- `wooCommerceApi`

## Environment Variables
- `WEBHOOK_URL`
