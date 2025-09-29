# API Documentation: Prevent concurrent workflow runs using Redis

## Overview
Automated workflow: Prevent concurrent workflow runs using Redis. This workflow integrates 11 different services: stickyNote, wait, switch, redis, set. It contains 43 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 48
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.set`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.switch`
- `n8n-nodes-base.wait`
- `n8n-nodes-base.executeWorkflowTrigger`
- `n8n-nodes-base.redis`
- `n8n-nodes-base.if`
- `n8n-nodes-base.executeWorkflow`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `redis`

## Environment Variables
- No environment variables required
