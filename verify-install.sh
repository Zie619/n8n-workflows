#!/bin/bash

# N8N Workflows Documentation - Installation & Deployment Verification
# Demonstrates the complete install and deploy workflow

set -euo pipefail

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🧪 N8N Workflows Documentation - Installation & Deployment Verification${NC}"
echo -e "${BLUE}This script demonstrates the complete install and deploy workflow${NC}"
echo ""

# Test 1: Installation Help
echo -e "${YELLOW}📋 Test 1: Installation Help${NC}"
./install.sh --help
echo ""

# Test 2: Deployment Help  
echo -e "${YELLOW}📋 Test 2: Deployment Help${NC}"
./scripts/deploy.sh --help
echo ""

# Test 3: Health Check Help
echo -e "${YELLOW}📋 Test 3: Health Check Help${NC}"
./scripts/health-check.sh --help
echo ""

# Test 4: Python Application Help
echo -e "${YELLOW}📋 Test 4: Python Application Help${NC}"
python3 run.py --help
echo ""

# Test 5: Quick Validation of Components
echo -e "${YELLOW}📋 Test 5: Component Validation${NC}"

# Check if critical files exist
files=("install.sh" "quick-start.sh" "scripts/deploy.sh" "scripts/health-check.sh" "requirements.txt" "run.py" "INSTALL.md" "README.md")
missing_files=()

for file in "${files[@]}"; do
    if [[ -f "$file" ]]; then
        echo -e "${GREEN}✅${NC} $file"
    else
        echo -e "${RED}❌${NC} $file (missing)"
        missing_files+=("$file")
    fi
done

echo ""

if [[ ${#missing_files[@]} -eq 0 ]]; then
    echo -e "${GREEN}✅ All critical components are present${NC}"
else
    echo -e "${RED}❌ Missing components: ${missing_files[*]}${NC}"
    exit 1
fi

# Test 6: Verify Python Dependencies
echo -e "${YELLOW}📋 Test 6: Python Dependencies Check${NC}"
if python3 -c "import fastapi, uvicorn, pydantic" 2>/dev/null; then
    echo -e "${GREEN}✅ Python dependencies are installed${NC}"
else
    echo -e "${RED}❌ Python dependencies missing${NC}"
    echo "Run: pip3 install -r requirements.txt"
    exit 1
fi

echo ""

# Final Summary
echo -e "${GREEN}🎉 Installation & Deployment Verification Complete!${NC}"
echo ""
echo -e "${BLUE}🚀 Ready to Use Commands:${NC}"
echo ""
echo -e "${YELLOW}Quick Start:${NC}"
echo "  ./quick-start.sh development"
echo ""
echo -e "${YELLOW}Manual Installation:${NC}"
echo "  ./install.sh --python-only --yes"
echo ""  
echo -e "${YELLOW}Deploy Application:${NC}"
echo "  ./scripts/deploy.sh development"
echo ""
echo -e "${YELLOW}Run Application Directly:${NC}"
echo "  python3 run.py"
echo ""
echo -e "${YELLOW}Health Check:${NC}"
echo "  ./scripts/health-check.sh http://localhost:8000"
echo ""
echo -e "${BLUE}📚 Documentation:${NC}"
echo "  • INSTALL.md - Comprehensive installation guide"
echo "  • README.md - Application overview and features"
echo "  • DEPLOYMENT.md - Deployment options"
echo ""
echo -e "${GREEN}🌐 After starting the application, access it at:${NC}"
echo "  • Main Interface: http://localhost:8000"
echo "  • API Documentation: http://localhost:8000/docs"
echo "  • Health Stats: http://localhost:8000/api/stats"
echo ""