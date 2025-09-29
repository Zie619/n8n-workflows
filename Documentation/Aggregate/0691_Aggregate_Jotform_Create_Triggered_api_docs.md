# API Documentation: Klicktipp Workflow

## Overview
Automated workflow: Klicktipp Workflow. This workflow integrates 8 different services: stickyNote, splitOut, merge, set, aggregate. It contains 14 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 19
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.jotFormTrigger`

## Node Types Used
- `n8n-nodes-base.jotFormTrigger`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.merge`
- `n8n-nodes-klicktipp.klicktipp`
- `n8n-nodes-base.splitOut`
- `n8n-nodes-base.aggregate`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`

## Integrations
- No external integrations detected

## Required Credentials
- `klickTippApi`
- `jotFormApi`

## Environment Variables
- No environment variables required
