#!/bin/bash
# Quick validation script for Meme workflow
# Run this before deploying to Heroku

echo "🔍 Validating Meme Automation Workflow..."
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if workflow files exist
echo "📁 Checking workflow files..."
if [ -f "workflows/Meme/2055_Meme_Instagram_Automation_Scheduled.json" ]; then
    echo -e "${GREEN}✓${NC} Main workflow file exists"
else
    echo -e "${RED}✗${NC} Main workflow file missing"
    exit 1
fi

if [ -f "workflows/Meme/2056_Meme_Instagram_Minimal_Scheduled.json" ]; then
    echo -e "${GREEN}✓${NC} Minimal workflow file exists"
else
    echo -e "${YELLOW}⚠${NC} Minimal workflow file missing (optional)"
fi

# Check if documentation exists
echo ""
echo "📚 Checking documentation..."
for doc in "README.md" "HEROKU_DEPLOYMENT.md" ".env.example"; do
    if [ -f "workflows/Meme/$doc" ]; then
        echo -e "${GREEN}✓${NC} $doc exists"
    else
        echo -e "${RED}✗${NC} $doc missing"
    fi
done

# Validate JSON structure
echo ""
echo "🔧 Validating JSON structure..."
if command -v python3 &> /dev/null; then
    if python3 -m json.tool workflows/Meme/2055_Meme_Instagram_Automation_Scheduled.json > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} Main workflow JSON is valid"
    else
        echo -e "${RED}✗${NC} Main workflow JSON is invalid"
        exit 1
    fi
    
    if [ -f "workflows/Meme/2056_Meme_Instagram_Minimal_Scheduled.json" ]; then
        if python3 -m json.tool workflows/Meme/2056_Meme_Instagram_Minimal_Scheduled.json > /dev/null 2>&1; then
            echo -e "${GREEN}✓${NC} Minimal workflow JSON is valid"
        else
            echo -e "${RED}✗${NC} Minimal workflow JSON is invalid"
            exit 1
        fi
    fi
else
    echo -e "${YELLOW}⚠${NC} Python3 not found, skipping JSON validation"
fi

# Check for required environment variables in example
echo ""
echo "🔑 Checking environment variable template..."
required_vars=("IMGFLIP_USERNAME" "IMGFLIP_PASSWORD" "INSTAGRAM_USER_ID" "INSTAGRAM_ACCESS_TOKEN")
missing_vars=0

for var in "${required_vars[@]}"; do
    if grep -q "$var" workflows/Meme/.env.example; then
        echo -e "${GREEN}✓${NC} $var found in .env.example"
    else
        echo -e "${RED}✗${NC} $var missing from .env.example"
        missing_vars=$((missing_vars + 1))
    fi
done

if [ $missing_vars -gt 0 ]; then
    echo -e "${RED}Missing $missing_vars required environment variables${NC}"
    exit 1
fi

# Check workflow structure
echo ""
echo "🏗️ Checking workflow structure..."
workflow_file="workflows/Meme/2055_Meme_Instagram_Automation_Scheduled.json"

# Check for required nodes
required_nodes=("scheduleTrigger" "code" "httpRequest" "set")
for node in "${required_nodes[@]}"; do
    if grep -q "\"type\":.*\"$node\"" "$workflow_file"; then
        echo -e "${GREEN}✓${NC} Contains $node node"
    else
        echo -e "${RED}✗${NC} Missing $node node"
    fi
done

# Check for connections
if grep -q '"connections"' "$workflow_file"; then
    echo -e "${GREEN}✓${NC} Workflow has connections defined"
else
    echo -e "${RED}✗${NC} Workflow missing connections"
    exit 1
fi

# Performance checks
echo ""
echo "⚡ Checking Heroku optimization..."
file_size=$(stat -f%z "$workflow_file" 2>/dev/null || stat -c%s "$workflow_file" 2>/dev/null)
if [ $file_size -lt 50000 ]; then
    echo -e "${GREEN}✓${NC} Workflow size is optimal (${file_size} bytes)"
else
    echo -e "${YELLOW}⚠${NC} Workflow is large (${file_size} bytes)"
fi

# Count nodes
node_count=$(grep -o '"type":' "$workflow_file" | wc -l)
if [ $node_count -lt 20 ]; then
    echo -e "${GREEN}✓${NC} Node count is optimal ($node_count nodes)"
else
    echo -e "${YELLOW}⚠${NC} High node count ($node_count nodes)"
fi

# Check for memory-intensive operations
echo ""
echo "💾 Checking for memory optimization..."
if grep -q '"download"' "$workflow_file"; then
    echo -e "${RED}✗${NC} Contains file download operations (memory-intensive)"
else
    echo -e "${GREEN}✓${NC} No file download operations"
fi

if grep -q '"writeFile"' "$workflow_file"; then
    echo -e "${RED}✗${NC} Contains file write operations (not recommended)"
else
    echo -e "${GREEN}✓${NC} No file write operations"
fi

# Summary
echo ""
echo "═══════════════════════════════════════════"
echo -e "${GREEN}✅ Validation Complete!${NC}"
echo "═══════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "1. Set up accounts: ImgFlip, Cloudinary, Instagram"
echo "2. Configure Heroku environment variables"
echo "3. Deploy n8n to Heroku"
echo "4. Import workflow to n8n"
echo "5. Activate workflow"
echo ""
echo "See HEROKU_DEPLOYMENT.md for detailed instructions"
