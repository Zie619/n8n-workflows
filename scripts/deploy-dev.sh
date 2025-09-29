#!/bin/bash
set -e

# N8N Workflows Documentation - Development Deployment Script
echo "🚀 Starting N8N Workflows Documentation - Development Environment"

# Configuration
export ENVIRONMENT=development
export HOST=127.0.0.1
export PORT=8000

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check dependencies
check_dependencies() {
    print_status "Checking dependencies..."
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed"
        exit 1
    fi
    
    if ! command -v pip3 &> /dev/null; then
        print_error "pip3 is not installed"
        exit 1
    fi
    
    print_status "Dependencies check passed"
}

# Install Python dependencies
install_dependencies() {
    print_status "Installing Python dependencies..."
    pip3 install -r requirements.txt
}

# Setup directories
setup_directories() {
    print_status "Setting up directories..."
    mkdir -p database static workflows
}

# Run database indexing
index_workflows() {
    print_status "Indexing workflows..."
    python3 run.py --reindex &
    SERVER_PID=$!
    sleep 5
    kill $SERVER_PID 2>/dev/null || true
}

# Start the application
start_application() {
    print_status "Starting application on http://${HOST}:${PORT}"
    print_warning "Press Ctrl+C to stop the server"
    python3 run.py --host $HOST --port $PORT --dev
}

# Main execution
main() {
    echo "=========================================="
    echo "N8N Workflows Documentation - Development"
    echo "=========================================="
    
    check_dependencies
    install_dependencies
    setup_directories
    start_application
}

# Handle interrupts
trap 'print_warning "Shutting down..."; exit 0' INT TERM

main "$@"