#!/bin/bash

echo "🔒 Testing Path Traversal Protection..."
echo "========================================="

# Test various path traversal attempts
declare -a attacks=(
  "../api_server.py"
  "../../etc/passwd"
  "..%2F..%2Fapi_server.py"
  "..%5C..%5Capi_server.py"
  "%2e%2e%2fapi_server.py"
  "../../../../../../../etc/passwd"
  "....//....//api_server.py"
  "..;/api_server.py"
  "..\api_server.py"
  "~/.ssh/id_rsa"
)

for attack in "${attacks[@]}"; do
  response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/api/workflows/$attack/download")
  if [ "$response" == "400" ] || [ "$response" == "404" ]; then
    echo "✅ Blocked: $attack (Response: $response)"
  else
    echo "❌ FAILED TO BLOCK: $attack (Response: $response)"
  fi
done

echo ""
echo "🔍 Testing Valid Downloads..."
echo "========================================="

# Test valid download
response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8000/api/workflows/0720_Schedule_Filter_Create_Scheduled.json/download")
if [ "$response" == "200" ]; then
  echo "✅ Valid download works (Response: $response)"
else
  echo "❌ Valid download failed (Response: $response)"
fi
