# API Documentation: Get the price of BTC in EUR and send an SMS when the price is larger than EUR 9000

## Overview
Automated workflow: Get the price of BTC in EUR and send an SMS when the price is larger than EUR 9000. This workflow processes data and performs automated tasks.

## Workflow Metadata
- **Total Nodes**: 11
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ❌ Not implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.cron`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.cron`
- `n8n-nodes-base.noOp`
- `n8n-nodes-base.coinGecko`
- `n8n-nodes-base.twilio`
- `n8n-nodes-base.if`

## Integrations
- No external integrations detected

## Required Credentials
- `twilioApi`

## Environment Variables
- No environment variables required
