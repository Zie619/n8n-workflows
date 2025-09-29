# API Documentation: Receive messages from a queue via RabbitMQ and send an SMS

## Overview
Automated workflow: Receive messages from a queue via RabbitMQ and send an SMS. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 10
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.rabbitmqTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.rabbitmqTrigger`
- `n8n-nodes-base.vonage`
- `n8n-nodes-base.if`

## Integrations
- No external integrations detected

## Required Credentials
- `vonageApi`
- `rabbitmq`

## Environment Variables
- No environment variables required
