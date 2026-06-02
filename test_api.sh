#!/bin/bash

echo "🔍 Testing API Functionality..."
echo "========================================="

# Test search
echo "1. Testing search for 'Slack'..."
results=$(curl -s "http://localhost:8000/api/workflows?search=Slack" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['workflows']))")
echo "   Found $results workflows mentioning Slack"

# Test categories
echo ""
echo "2. Testing categories endpoint..."
categories=$(curl -s "http://localhost:8000/api/categories" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['categories']))")
echo "   Found $categories categories"

# Test integrations
echo ""
echo "3. Testing integrations endpoint..."
integrations=$(curl -s "http://localhost:8000/api/integrations" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['integrations']))")
echo "   Found $integrations integrations"

# Test filters
echo ""
echo "4. Testing filter by complexity..."
high_complex=$(curl -s "http://localhost:8000/api/workflows?complexity=high" | python3 -c "import sys, json; data=json.load(sys.stdin); print(len(data['workflows']))")
echo "   Found $high_complex high complexity workflows"

# Test pagination
echo ""
echo "5. Testing pagination..."
page2=$(curl -s "http://localhost:8000/api/workflows?page=2&per_page=10" | python3 -c "import sys, json; data=json.load(sys.stdin); print(f\"Page {data['page']} of {data['pages']}, {len(data['workflows'])} items\")")
echo "   $page2"

# Test specific workflow
echo ""
echo "6. Testing get specific workflow..."
workflow=$(curl -s "http://localhost:8000/api/workflows/1" | python3 -c "import sys, json; data=json.load(sys.stdin); print(data['name'] if 'name' in data else 'NOT FOUND')")
echo "   Workflow: $workflow"
