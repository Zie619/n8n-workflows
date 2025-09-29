#!/bin/bash

# N8N Workflows Documentation - One-Click Install & Deploy
# Usage: ./quick-start.sh [environment]

set -euo pipefail

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

ENVIRONMENT="${1:-development}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo -e "${BLUE}🚀 N8N Workflows Documentation - Quick Start${NC}"
echo -e "${BLUE}Environment: ${ENVIRONMENT}${NC}"
echo ""

# Step 1: Install dependencies
echo -e "${YELLOW}📦 Step 1: Installing dependencies...${NC}"
if [[ -f "$SCRIPT_DIR/install.sh" ]]; then
    "$SCRIPT_DIR/install.sh" --yes
else
    echo "Install script not found, attempting manual installation..."
    
    # Basic dependency check
    if ! command -v python3 &> /dev/null; then
        echo "❌ Python3 not found. Please install Python 3.7+ and try again."
        exit 1
    fi
    
    # Install Python dependencies
    pip3 install --user -r "$SCRIPT_DIR/requirements.txt"
fi

echo ""

# Step 2: Deploy application
echo -e "${YELLOW}🚀 Step 2: Deploying application...${NC}"
if [[ -f "$SCRIPT_DIR/scripts/deploy.sh" ]]; then
    "$SCRIPT_DIR/scripts/deploy.sh" "$ENVIRONMENT"
else
    echo "Deploy script not found, starting manually..."
    cd "$SCRIPT_DIR"
    python3 run.py --host 0.0.0.0 --port 8000 &
    echo "Application started in background"
fi

echo ""
echo -e "${GREEN}✅ Quick start completed!${NC}"
echo -e "${GREEN}🌐 Access your application at: http://localhost:8000${NC}"
echo -e "${GREEN}📚 API docs available at: http://localhost:8000/docs${NC}"
echo ""
echo -e "${BLUE}💡 Next steps:${NC}"
echo "   • Open http://localhost:8000 in your browser"
echo "   • Explore the 2000+ n8n workflows"
echo "   • Use the search and filtering features"
echo "   • Check the API documentation"
echo ""
echo -e "${BLUE}🛠  Management commands:${NC}"
echo "   • Health check: ./scripts/health-check.sh"
echo "   • View logs: tail -f logs/app.log"
echo "   • Restart: ./scripts/deploy.sh $ENVIRONMENT"
echo "   • Stop: pkill -f 'python.*run.py'"