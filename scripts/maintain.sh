#!/bin/bash
set -e

# N8N Workflows Documentation - Maintenance Script
# This script handles deployment, monitoring, and maintenance tasks

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
COMPOSE_PROJECT_NAME="n8n-workflows"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() { echo -e "${GREEN}✅ $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ️  $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }

show_help() {
    cat << EOF
N8N Workflows Documentation - Maintenance Script

USAGE:
    $0 [COMMAND] [OPTIONS]

COMMANDS:
    start               Start the application (Docker Compose)
    stop                Stop the application
    restart             Restart the application
    status              Show application status
    logs                Show application logs
    update              Update and restart the application
    backup              Backup application data
    restore [file]      Restore from backup file
    health              Check application health
    clean               Clean up Docker resources
    reindex             Force workflow reindexing
    dev                 Start in development mode
    prod                Deploy in production mode

OPTIONS:
    -f, --follow        Follow logs output
    -h, --help          Show this help message

EXAMPLES:
    $0 start                    # Start the application
    $0 logs -f                  # Follow logs
    $0 backup                   # Create backup
    $0 restore backup.tar.gz    # Restore from backup
    $0 dev                      # Start in development mode
EOF
}

check_dependencies() {
    local deps_ok=true
    
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed"
        deps_ok=false
    fi
    
    if ! docker compose version &> /dev/null; then
        print_error "Docker Compose is not available"
        deps_ok=false
    fi
    
    if [ "$deps_ok" = false ]; then
        exit 1
    fi
}

start_application() {
    print_status "Starting N8N Workflows Documentation..."
    cd "$PROJECT_ROOT"
    docker compose up -d
    sleep 5
    check_health
}

stop_application() {
    print_status "Stopping N8N Workflows Documentation..."
    cd "$PROJECT_ROOT"
    docker compose down
}

restart_application() {
    print_status "Restarting N8N Workflows Documentation..."
    cd "$PROJECT_ROOT"
    docker compose restart
    sleep 5
    check_health
}

show_status() {
    print_info "Application Status:"
    cd "$PROJECT_ROOT"
    docker compose ps
    echo
    docker compose top 2>/dev/null || true
}

show_logs() {
    local follow_flag=""
    if [[ "$1" == "-f" ]] || [[ "$1" == "--follow" ]]; then
        follow_flag="-f"
    fi
    
    cd "$PROJECT_ROOT"
    docker compose logs $follow_flag
}

update_application() {
    print_status "Updating N8N Workflows Documentation..."
    cd "$PROJECT_ROOT"
    
    # Pull latest changes (if in git repo)
    if [ -d ".git" ]; then
        git pull origin main || print_warning "Could not update from git"
    fi
    
    # Rebuild and restart
    docker compose build --no-cache
    docker compose up -d
    sleep 10
    check_health
    
    print_status "Update completed"
}

backup_data() {
    local backup_dir="$PROJECT_ROOT/backups"
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_file="$backup_dir/n8n-workflows-backup-$timestamp.tar.gz"
    
    print_status "Creating backup..."
    mkdir -p "$backup_dir"
    
    # Create backup of database and configuration
    cd "$PROJECT_ROOT"
    tar -czf "$backup_file" \
        database/ \
        .env 2>/dev/null \
        docker-compose.yml \
        nginx.conf 2>/dev/null \
        || true
    
    print_status "Backup created: $backup_file"
    
    # Cleanup old backups (keep last 10)
    ls -t "$backup_dir"/n8n-workflows-backup-*.tar.gz 2>/dev/null | tail -n +11 | xargs rm -f 2>/dev/null || true
}

restore_data() {
    local backup_file="$1"
    
    if [ -z "$backup_file" ] || [ ! -f "$backup_file" ]; then
        print_error "Backup file not found: $backup_file"
        exit 1
    fi
    
    print_warning "This will restore from backup and restart the application"
    read -p "Continue? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        print_info "Restore cancelled"
        exit 0
    fi
    
    print_status "Stopping application..."
    stop_application
    
    print_status "Restoring from backup: $backup_file"
    cd "$PROJECT_ROOT"
    tar -xzf "$backup_file"
    
    print_status "Starting application..."
    start_application
    
    print_status "Restore completed"
}

check_health() {
    print_info "Checking application health..."
    local max_attempts=10
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        if curl -f http://localhost:8000/health > /dev/null 2>&1; then
            print_status "Application is healthy"
            print_info "🌐 Access at: http://localhost:8000"
            print_info "📊 API Docs: http://localhost:8000/docs"
            return 0
        fi
        
        print_info "Attempt $attempt/$max_attempts - waiting for application..."
        sleep 3
        ((attempt++))
    done
    
    print_error "Application health check failed"
    print_info "Check logs with: $0 logs"
    return 1
}

clean_docker() {
    print_status "Cleaning up Docker resources..."
    cd "$PROJECT_ROOT"
    
    # Stop and remove containers
    docker compose down --remove-orphans
    
    # Remove unused images
    docker image prune -f
    
    # Remove unused volumes (be careful!)
    read -p "Remove unused Docker volumes? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        docker volume prune -f
    fi
    
    print_status "Docker cleanup completed"
}

reindex_workflows() {
    print_status "Reindexing workflows..."
    cd "$PROJECT_ROOT"
    
    # Stop the application
    docker compose stop workflows-doc
    
    # Run reindexing
    docker compose run --rm workflows-doc python run.py --reindex
    
    # Start the application
    docker compose up -d workflows-doc
    sleep 5
    check_health
    
    print_status "Reindexing completed"
}

start_dev() {
    print_status "Starting in development mode..."
    cd "$PROJECT_ROOT"
    
    # Check if Python is available
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is required for development mode"
        exit 1
    fi
    
    # Install dependencies
    pip3 install -r requirements.txt
    
    # Start development server
    python3 run.py --host 127.0.0.1 --port 8000 --dev
}

deploy_prod() {
    print_status "Deploying in production mode..."
    cd "$PROJECT_ROOT"
    
    # Build production image
    docker compose build
    
    # Start with production profile
    docker compose --profile production up -d
    
    sleep 10
    check_health
    
    print_status "Production deployment completed"
    print_info "🌐 HTTP: http://localhost:80"
    print_info "🔒 HTTPS: https://localhost:443 (if SSL configured)"
}

# Main script logic
main() {
    case "${1:-help}" in
        start)
            check_dependencies
            start_application
            ;;
        stop)
            check_dependencies
            stop_application
            ;;
        restart)
            check_dependencies
            restart_application
            ;;
        status)
            check_dependencies
            show_status
            ;;
        logs)
            check_dependencies
            show_logs "${2:-}"
            ;;
        update)
            check_dependencies
            update_application
            ;;
        backup)
            backup_data
            ;;
        restore)
            restore_data "$2"
            ;;
        health)
            check_health
            ;;
        clean)
            check_dependencies
            clean_docker
            ;;
        reindex)
            check_dependencies
            reindex_workflows
            ;;
        dev)
            start_dev
            ;;
        prod)
            check_dependencies
            deploy_prod
            ;;
        help|--help|-h)
            show_help
            ;;
        *)
            print_error "Unknown command: $1"
            echo
            show_help
            exit 1
            ;;
    esac
}

# Handle interrupts
trap 'print_warning "Operation interrupted"; exit 1' INT TERM

main "$@"