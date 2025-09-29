#!/bin/bash
set -e

# N8N Workflows Documentation - Production Deployment Script
echo "🚀 Starting N8N Workflows Documentation - Production Environment"

# Configuration
export ENVIRONMENT=production
export HOST=0.0.0.0
export PORT=8000
export COMPOSE_PROJECT_NAME=n8n-workflows

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
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
    
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed"
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        print_error "Docker Compose is not installed"
        exit 1
    fi
    
    print_status "Dependencies check passed"
}

# Build Docker image
build_image() {
    print_status "Building Docker image..."
    docker build -t workflows-doc:latest .
}

# Deploy with Docker Compose
deploy_docker() {
    print_status "Deploying with Docker Compose..."
    
    # Stop existing containers
    docker-compose down 2>/dev/null || true
    
    # Start services
    docker-compose up -d
    
    print_status "Waiting for services to be ready..."
    sleep 10
    
    # Health check
    if curl -f http://localhost:8000/health > /dev/null 2>&1; then
        print_status "Application is healthy and running"
    else
        print_error "Application health check failed"
        docker-compose logs
        exit 1
    fi
}

# Deploy to Kubernetes
deploy_kubernetes() {
    print_status "Deploying to Kubernetes..."
    
    if ! command -v kubectl &> /dev/null; then
        print_warning "kubectl not found, skipping Kubernetes deployment"
        return
    fi
    
    # Apply Kubernetes manifests
    kubectl apply -f k8s/deployment.yaml
    
    # Wait for rollout
    kubectl rollout status deployment/n8n-workflows-doc
    
    print_status "Kubernetes deployment completed"
}

# Show deployment info
show_info() {
    echo "=========================================="
    print_status "Deployment completed successfully!"
    echo "=========================================="
    print_info "🌐 Application URL: http://localhost:8000"
    print_info "📊 API Documentation: http://localhost:8000/docs"
    print_info "🔍 Health Check: http://localhost:8000/health"
    echo
    print_info "📋 Container Status:"
    docker-compose ps
    echo
    print_info "💡 Useful Commands:"
    echo "  View logs:    docker-compose logs -f"
    echo "  Stop:         docker-compose down"
    echo "  Restart:      docker-compose restart"
    echo "  Update:       ./scripts/deploy-prod.sh"
}

# Backup existing data
backup_data() {
    if [ -d "database" ]; then
        print_status "Backing up existing data..."
        timestamp=$(date +%Y%m%d_%H%M%S)
        cp -r database "database_backup_$timestamp"
        print_status "Data backed up to database_backup_$timestamp"
    fi
}

# Main execution
main() {
    local deployment_type=${1:-docker}
    
    echo "=========================================="
    echo "N8N Workflows Documentation - Production"
    echo "=========================================="
    
    check_dependencies
    backup_data
    build_image
    
    case $deployment_type in
        docker)
            deploy_docker
            show_info
            ;;
        kubernetes|k8s)
            deploy_kubernetes
            ;;
        *)
            print_error "Unknown deployment type: $deployment_type"
            echo "Usage: $0 [docker|kubernetes]"
            exit 1
            ;;
    esac
}

# Handle interrupts
trap 'print_warning "Deployment interrupted"; exit 1' INT TERM

main "$@"