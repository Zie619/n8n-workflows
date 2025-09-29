# API Documentation: Hubspot Workflow

## Overview
Automated workflow: Hubspot Workflow. This workflow integrates 6 different services: stickyNote, filter, hubspot, scheduleTrigger, stopAndError. It contains 9 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.hubspot`
- `n8n-nodes-base.slack`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.stopAndError`

## Integrations
- Hubspot
- Slack

## Required Credentials
- `slackOAuth2Api`
- `hubspotOAuth2Api`

## Environment Variables
- No environment variables required
