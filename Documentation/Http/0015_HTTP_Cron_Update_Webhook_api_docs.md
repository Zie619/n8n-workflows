# API Documentation: Send updates about the position of the ISS every minute to a topic in ActiveMQ

## Overview
Automated workflow for data processing and integration.

## Workflow Metadata
- **Total Nodes**: 4
- **Complexity Level**: Simple
- **Estimated Execution Time**: 1-5 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.cron`

## Node Types Used
- `n8n-nodes-base.cron`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.set`
- `n8n-nodes-base.amqp`

## Integrations
- No external integrations detected

## Required Credentials
- `amqp`

## Environment Variables
- `BASE_URL`
