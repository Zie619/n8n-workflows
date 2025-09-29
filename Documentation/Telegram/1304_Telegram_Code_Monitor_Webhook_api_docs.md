# API Documentation: Monitor USDT ERC-20 Wallet Balance with Etherscan and Telegram Notifications

## Overview
Automated workflow: Monitor USDT ERC-20 Wallet Balance with Etherscan and Telegram Notifications. This workflow integrates 8 different services: stickyNote, httpRequest, telegram, code, set. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 21
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.cron`

## Node Types Used
- `n8n-nodes-base.telegram`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.cron`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `telegramApi`

## Environment Variables
- `API_BASE_URL`
