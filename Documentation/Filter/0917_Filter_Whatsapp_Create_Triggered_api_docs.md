# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 7 different services: stickyNote, filter, klicktipp, switch, klicktippTrigger. It contains 12 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.whatsAppTrigger`
- `CUSTOM.klicktippTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `CUSTOM.klicktippTrigger`
- `CUSTOM.klicktipp`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.whatsAppTrigger`
- `n8n-nodes-base.whatsApp`

## Integrations
- No external integrations detected

## Required Credentials
- `whatsAppApi`
- `klickTippApi`
- `whatsAppTriggerApi`

## Environment Variables
- No environment variables required
