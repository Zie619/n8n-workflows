# API Documentation: New Ticket Alerts to Teams

## Overview
Automated workflow: New Ticket Alerts to Teams. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 20
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.microsoftTeams`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.redis`
- `n8n-nodes-base.stopAndError`

## Integrations
- Microsoft

## Required Credentials
- `microsoftTeamsOAuth2Api`
- `httpHeaderAuth`
- `redis`

## Environment Variables
- `API_BASE_URL`
