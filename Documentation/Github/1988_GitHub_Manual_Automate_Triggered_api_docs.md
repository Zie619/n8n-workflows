# API Documentation: [OPS] Restore workflows from GitHub to n8n

## Overview
Automated workflow: [OPS] Restore workflows from GitHub to n8n. This workflow integrates 8 different services: stickyNote, n8n, merge, set, manualTrigger. It contains 17 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 22
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-base.github`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.n8n`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`

## Integrations
- Github
- Github

## Required Credentials
- `githubApi`
- `n8nApi`

## Environment Variables
- No environment variables required
