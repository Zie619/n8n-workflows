# API Documentation: Remote IOT Sensor monitoring via MQTT and InfluxDB

## Overview
Automated workflow: Remote IOT Sensor monitoring via MQTT and InfluxDB. This workflow integrates 5 different services: stickyNote, httpRequest, code, stopAndError, mqttTrigger. It contains 8 nodes and follows best practices for error handling and security.

## Workflow Metadata
- **Total Nodes**: 17
- **Complexity Level**: Complex
- **Estimated Execution Time**: 30+ seconds
- **Error Handling**: ✅ Implemented

## Trigger Information
### Trigger Types
- `n8n-nodes-base.mqttTrigger`

## Node Types Used
- `n8n-nodes-base.stickyNote`
- `n8n-nodes-base.mqttTrigger`
- `n8n-nodes-base.httpRequest`
- `n8n-nodes-base.code`
- `n8n-nodes-base.stopAndError`

## Integrations
- No external integrations detected

## Required Credentials
- `mqtt`

## Environment Variables
- `API_BASE_URL`
