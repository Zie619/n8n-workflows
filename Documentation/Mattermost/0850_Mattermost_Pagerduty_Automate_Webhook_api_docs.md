# API Documentation: Unnamed Workflow

## Overview
Automated workflow for data processing and integration.

## Workflow Metadata
- **Total Nodes**: 14
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `/ack`
- **Method**: `POST`
- **Webhook ID**: `d3025d6c-5956-439e-9c9a-db3ef524a24f`

- **Path**: `/resolve`
- **Method**: `POST`
- **Webhook ID**: `92d7ddfa-20f9-49bc-976e-4f6c76c0b3b4`

- **Path**: `9888d896-dd23-4e97-9d16-c12055b64133`
- **Method**: `POST`
- **Webhook ID**: `9888d896-dd23-4e97-9d16-c12055b64133`


## Node Types Used
- `n8n-nodes-base.jira`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.pagerDuty`
- `n8n-nodes-base.mattermost`

## Integrations
- No external integrations detected

## Required Credentials
- `jiraSoftwareCloudApi`
- `pagerDutyApi`
- `mattermostApi`

## Environment Variables
- `BASE_URL`
