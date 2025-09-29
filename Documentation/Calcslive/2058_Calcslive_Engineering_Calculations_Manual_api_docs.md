# API Documentation: CalcsLive Demo Workflow Template

## Overview
Demonstrates @calcslive/n8n-nodes-calcslive custom node ({{ $env.WEBHOOK_URL }} that brings unit-aware physical quantities (PQ) and calculations to the n8n ecosystem in a composable manner. Example workflow with cylinder mass calculations.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.manualTrigger`

## Node Types Used
- `n8n-nodes-base.manualTrigger`
- `n8n-nodes-base.stickyNote`
- `@calcslive/n8n-nodes-calcslive.calcsLive`
- `n8n-nodes-base.set`
- `n8n-nodes-base.gmail`

## Integrations
- No external integrations detected

## Required Credentials
- `calcsLiveApi`
- `gmailOAuth2`

## Environment Variables
- No environment variables required
