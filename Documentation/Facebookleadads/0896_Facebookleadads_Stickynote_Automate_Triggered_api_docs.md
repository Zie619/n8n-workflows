# API Documentation: Stickynote Workflow

## Overview
Automated workflow: Stickynote Workflow. This workflow integrates 3 different services: stickyNote, facebookLeadAdsTrigger, klicktipp. It contains 3 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 8
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.facebookLeadAdsTrigger`

## Node Types Used
- `n8n-nodes-klicktipp.klicktipp`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.facebookLeadAdsTrigger`

## Integrations
- No external integrations detected

## Required Credentials
- `facebookLeadAdsOAuth2Api`
- `klickTippApi`

## Environment Variables
- `WEBHOOK_URL`
