# API Documentation: Send Discord message from Webflow form submission

## Overview
Automated workflow: Send Discord message from Webflow form submission. This workflow integrates 7 different services: stickyNote, code, set, discord, stopAndError. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webflowTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.discord`
- `n8n-nodes-base.webflowTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `webflowApi`
- `discordBotApi`

## Environment Variables
- `WEBHOOK_URL`
