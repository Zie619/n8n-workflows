#!/bin/bash

# N8N Workflows Documentation - Production Deployment Script
# Usage: ./scripts/deploy.sh [environment]
# Environment: development, staging, production

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ENVIRONMENT="${1:-production}"
DOCKER_IMAGE="workflows-doc:${ENVIRONMENT}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    log "Checking prerequisites..."
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        error "Docker is not installed"
    fi
    
    # Check Docker Compose
    if ! docker compose version &> /dev/null; then
        error "Docker Compose is not installed"
    fi
    
    # Check if Docker daemon is running
    if ! docker info &> /dev/null; then
        error "Docker daemon is not running"
    fi
    
    success "Prerequisites check passed"
}

# Validate environment
validate_environment() {
    log "Validating environment: $ENVIRONMENT"
    
    case $ENVIRONMENT in
        development|staging|production)
            log "Environment '$ENVIRONMENT' is valid"
            ;;
        *)
            error "Invalid environment: $ENVIRONMENT. Use: development, staging, or production"
            ;;
    esac
}

# Build Docker image
build_image() {
    log "Building Docker image for $ENVIRONMENT environment..."
    
    cd "$PROJECT_DIR"
    
    if [[ "$ENVIRONMENT" == "development" ]]; then
        docker build -t "$DOCKER_IMAGE" .
    else
        docker build -t "$DOCKER_IMAGE" --target production .
    fi
    
    success "Docker image built successfully: $DOCKER_IMAGE"
}

# Deploy with Docker Compose
deploy_docker_compose() {
    log "Deploying with Docker Compose..."
    
    cd "$PROJECT_DIR"
    
    # Stop existing containers
    if [[ "$ENVIRONMENT" == "development" ]]; then
        docker compose -f docker-compose.yml -f docker-compose.dev.yml down --remove-orphans
        docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
    else
        docker compose -f docker-compose.yml -f docker-compose.prod.yml down --remove-orphans
        docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
    fi
    
    success "Docker Compose deployment completed"
}

# Deploy to Kubernetes
deploy_kubernetes() {
    log "Deploying to Kubernetes..."
    
    if ! command -v kubectl &> /dev/null; then
        error "kubectl is not installed"
    fi
    
    cd "$PROJECT_DIR"
    
    # Apply Kubernetes manifests
    kubectl apply -f k8s/namespace.yaml
    kubectl apply -f k8s/configmap.yaml
    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml
    
    if [[ "$ENVIRONMENT" == "production" ]]; then
        kubectl apply -f k8s/ingress.yaml
    fi
    
    # Wait for deployment to be ready
    kubectl rollout status deployment/workflows-docs -n n8n-workflows --timeout=300s
    
    success "Kubernetes deployment completed"
}

# Deploy with Helm
deploy_helm() {
    log "Deploying with Helm..."
    
    if ! command -v helm &> /dev/null; then
        error "Helm is not installed"
    fi
    
    cd "$PROJECT_DIR"
    
    local release_name="workflows-docs-$ENVIRONMENT"
    local values_file="helm/workflows-docs/values-$ENVIRONMENT.yaml"
    
    if [[ -f "$values_file" ]]; then
        helm upgrade --install "$release_name" ./helm/workflows-docs \
            --namespace n8n-workflows \
            --create-namespace \
            --values "$values_file" \
            --wait --timeout=300s
    else
        warn "Values file $values_file not found, using default values"
        helm upgrade --install "$release_name" ./helm/workflows-docs \
            --namespace n8n-workflows \
            --create-namespace \
            --wait --timeout=300s
    fi
    
    success "Helm deployment completed"
}

# Health check
health_check() {
    log "Performing health check..."
    
    local max_attempts=30
    local attempt=1
    local url="http://localhost:8000/api/stats"
    
    if [[ "$ENVIRONMENT" == "production" ]]; then
        url="https://workflows.yourdomain.com/api/stats"  # Update with your domain
    fi
    
    while [[ $attempt -le $max_attempts ]]; do
        log "Health check attempt $attempt/$max_attempts..."
        
        if curl -f -s "$url" &> /dev/null; then
            success "Application is healthy!"
            return 0
        fi
        
        sleep 10
        ((attempt++))
    done
    
    error "Health check failed after $max_attempts attempts"
}

# Cleanup old resources
cleanup() {
    log "Cleaning up old resources..."
    
    # Remove dangling Docker images
    docker image prune -f
    
    # Remove unused Docker volumes
    docker volume prune -f
    
    success "Cleanup completed"
}

# Main deployment function
deploy() {
    log "Starting deployment process for $ENVIRONMENT environment..."
    
    check_prerequisites
    validate_environment
    
    # Choose deployment method based on environment and available tools
    if command -v kubectl &> /dev/null && [[ "$ENVIRONMENT" == "production" ]]; then
        if command -v helm &> /dev/null; then
            deploy_helm
        else
            deploy_kubernetes
        fi
    else
        build_image
        deploy_docker_compose
    fi
    
    health_check
    cleanup
    
    success "Deployment completed successfully!"
    
    # Show deployment information
    case $ENVIRONMENT in
        development)
            log "Application is available at: http://localhost:8000"
            log "API Documentation: http://localhost:8000/docs"
            ;;
        staging)
            log "Application is available at: http://workflows-staging.yourdomain.com"
            ;;
        production)
            log "Application is available at: https://workflows.yourdomain.com"
            ;;
    esac
}

# Rollback function
rollback() {
    log "Rolling back deployment..."
    
    if command -v kubectl &> /dev/null; then
        kubectl rollout undo deployment/workflows-docs -n n8n-workflows
        kubectl rollout status deployment/workflows-docs -n n8n-workflows --timeout=300s
    else
        cd "$PROJECT_DIR"
        docker compose down
        # Restore from backup if available
        if [[ -f "database/workflows.db.backup" ]]; then
            cp database/workflows.db.backup database/workflows.db
        fi
        deploy_docker_compose
    fi
    
    success "Rollback completed"
}

# Show usage information
usage() {
    cat << EOF
N8N Workflows Documentation - Deployment Script

Usage: $0 [OPTIONS] [ENVIRONMENT]

ENVIRONMENTS:
    development    Development environment (default configuration)
    staging        Staging environment (production-like)
    production     Production environment (full security and performance)

OPTIONS:
    --rollback     Rollback to previous deployment
    --cleanup      Cleanup only (remove old resources)
    --health       Health check only
    --help         Show this help message

EXAMPLES:
    $0 development                  # Deploy to development
    $0 production                   # Deploy to production
    $0 --rollback production        # Rollback production deployment
    $0 --health                     # Check application health

EOF
}

# Parse command line arguments
main() {
    case "${1:-}" in
        --help|-h)
            usage
            exit 0
            ;;
        --rollback)
            ENVIRONMENT="${2:-production}"
            rollback
            exit 0
            ;;
        --cleanup)
            cleanup
            exit 0
            ;;
        --health)
            health_check
            exit 0
            ;;
        "")
            deploy
            ;;
        *)
            ENVIRONMENT="$1"
            deploy
            ;;
    esac
}

# Execute main function with all arguments
main "$@"