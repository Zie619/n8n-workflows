# API Documentation: Convert Parquet, Avro, ORC & Feather via ParquetReader to JSON

## Overview
Automated workflow: Convert Parquet, Avro, ORC & Feather via ParquetReader to JSON. This workflow integrates 5 different services: webhook, stickyNote, httpRequest, code, stopAndError. It contains 8 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 15
- **Complexity Level**: Moderate
- **Estimated Execution Time**: 5-30 seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.webhook`

### Webhook Endpoints
- **Path**: `convert`
- **Method**: `POST`
- **Webhook ID**: `0b1223c9-c117-45f9-9931-909f2db28955`


## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.webhook`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- No credentials required

## Environment Variables
- `API_BASE_URL`
