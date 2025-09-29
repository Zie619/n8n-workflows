# API Documentation: Dynamically create tables in Airtable for your Webflow form submissions

## Overview
Automated workflow: Dynamically create tables in Airtable for your Webflow form submissions. This workflow integrates 8 different services: stickyNote, httpRequest, airtable, code, set. It contains 21 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 34
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webflowTrigger`

## Node Types Used
- `n8n-nodes-base.airtable`
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.webflowTrigger`
- `n8n-nodes-base.code`
- `n8n-nodes-base.set`
- `n8n-nodes-base.if`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `webflowApi`
- `airtableOAuth2Api`
- `airtableTokenApi`

## Environment Variables
- `WEBHOOK_URL`
- `BASE_URL`
