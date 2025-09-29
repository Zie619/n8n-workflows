# API Documentation: Monitor_security_advisories

## Overview
Automated workflow: Monitor_security_advisories. This workflow integrates 11 different services: filter, stickyNote, scheduleTrigger, noOp, set. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.scheduleTrigger`

## Node Types Used
- `n8n-nodes-base.n8nTrainingCustomerDatastore`
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.jira`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.rssFeedRead`
- `n8n-nodes-base.scheduleTrigger`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.filter`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `jiraSoftwareCloudApi`
- `gmailOAuth2`

## Environment Variables
- `WEBHOOK_URL`
