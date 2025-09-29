#!/bin/bash

# N8N Workflows Documentation - Enhanced Health Check Script
# Usage: ./scripts/health-check.sh [endpoint] [--verbose]

set -euo pipefail

ENDPOINT="${1:-http://localhost:8000}"
VERBOSE=false
MAX_ATTEMPTS=10
TIMEOUT=10
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --verbose|-v)
            VERBOSE=true
            shift
            ;;
        --help|-h)
            echo "N8N Workflows Documentation - Health Check"
            echo "Usage: $0 [endpoint] [--verbose]"
            echo "  endpoint    Base URL to check (default: http://localhost:8000)"
            echo "  --verbose   Show detailed output"
            exit 0
            ;;
        http*)
            ENDPOINT="$1"
            shift
            ;;
        *)
            shift
            ;;
    esac
done

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[$(date '+%H:%M:%S')]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

verbose() {
    if [[ "$VERBOSE" == "true" ]]; then
        echo -e "${PURPLE}[DEBUG]${NC} $1"
    fi
}

print_banner() {
    echo -e "${BLUE}🏥 N8N Workflows Documentation - Health Check${NC}"
    echo -e "${BLUE}Endpoint: $ENDPOINT${NC}"
    echo -e "${BLUE}Timeout: ${TIMEOUT}s${NC}"
    echo ""
}

# Check if curl is available
check_curl() {
    if ! command -v curl &> /dev/null; then
        error "curl is required but not installed"
        return 1
    fi
    verbose "curl is available"
}

# Detect deployment method
detect_deployment() {
    verbose "Detecting deployment method..."
    
    local deployment_method="unknown"
    
    # Check for Docker containers
    if command -v docker &> /dev/null; then
        if docker ps --filter "name=n8n" --format "table {{.Names}}" | grep -q n8n 2>/dev/null; then
            deployment_method="docker"
        fi
    fi
    
    # Check for Python process
    if pgrep -f "python.*run.py" > /dev/null 2>&1; then
        deployment_method="python"
    fi
    
    # Check for Kubernetes
    if command -v kubectl &> /dev/null; then
        if kubectl get pods -n n8n-workflows 2>/dev/null | grep -q workflows-docs; then
            deployment_method="kubernetes"
        fi
    fi
    
    verbose "Detected deployment method: $deployment_method"
    echo "$deployment_method"
}

# Comprehensive health check
perform_health_check() {
    local endpoint="$1"
    local check_name="$2"
    local expected_status="${3:-200}"
    
    verbose "Checking: $check_name at $endpoint"
    
    local response
    local http_code
    
    if response=$(curl -s -w "%{http_code}" -o /tmp/health_response_$$ --connect-timeout $TIMEOUT --max-time $((TIMEOUT * 2)) "$endpoint" 2>/dev/null); then
        http_code=$(echo "$response" | tail -c 4)
        
        if [[ "$http_code" == "$expected_status" ]]; then
            success "$check_name: HTTP $http_code ✅"
            
            if [[ "$VERBOSE" == "true" ]] && [[ -f "/tmp/health_response_$$" ]]; then
                local response_size=$(wc -c < /tmp/health_response_$$ 2>/dev/null || echo "0")
                verbose "Response size: ${response_size} bytes"
                
                # Show response content for API endpoints
                if [[ "$endpoint" == *"/api/"* ]]; then
                    verbose "Response preview:"
                    head -c 200 /tmp/health_response_$$ 2>/dev/null | sed 's/^/    /' || true
                fi
            fi
            
            rm -f /tmp/health_response_$$ 2>/dev/null
            return 0
        else
            error "$check_name: HTTP $http_code ❌"
            rm -f /tmp/health_response_$$ 2>/dev/null
            return 1
        fi
    else
        error "$check_name: Connection failed ❌"
        return 1
    fi
}

# Check application processes
check_processes() {
    verbose "Checking application processes..."
    
    local deployment_method=$(detect_deployment)
    
    case "$deployment_method" in
        python)
            if pgrep -f "python.*run.py" > /dev/null; then
                local pid=$(pgrep -f "python.*run.py" | head -1)
                success "Python process running (PID: $pid)"
                
                if [[ -f "$PROJECT_DIR/logs/app.pid" ]]; then
                    local saved_pid=$(cat "$PROJECT_DIR/logs/app.pid" 2>/dev/null || echo "unknown")
                    verbose "Saved PID: $saved_pid"
                fi
            else
                warn "Python process not found"
                return 1
            fi
            ;;
        docker)
            if command -v docker &> /dev/null; then
                local containers=$(docker ps --filter "name=n8n" --format "{{.Names}}" 2>/dev/null || echo "")
                if [[ -n "$containers" ]]; then
                    success "Docker containers running: $containers"
                else
                    warn "No Docker containers found"
                    return 1
                fi
            else
                warn "Docker not available"
                return 1
            fi
            ;;
        kubernetes)
            if command -v kubectl &> /dev/null; then
                local pods=$(kubectl get pods -n n8n-workflows --no-headers 2>/dev/null | grep workflows-docs | awk '{print $1}' || echo "")
                if [[ -n "$pods" ]]; then
                    success "Kubernetes pods running: $pods"
                else
                    warn "No Kubernetes pods found"
                    return 1
                fi
            else
                warn "kubectl not available"
                return 1
            fi
            ;;
        *)
            warn "Could not detect deployment method"
            return 1
            ;;
    esac
}

# Check database
check_database() {
    if [[ -f "$PROJECT_DIR/database/workflows.db" ]]; then
        local db_size=$(wc -c < "$PROJECT_DIR/database/workflows.db" 2>/dev/null || echo "0")
        success "Database found (${db_size} bytes)"
        return 0
    else
        warn "Database file not found"
        return 1
    fi
}

# Check logs
check_logs() {
    if [[ -d "$PROJECT_DIR/logs" ]]; then
        local log_files=$(find "$PROJECT_DIR/logs" -name "*.log" 2>/dev/null | wc -l)
        success "Log directory found ($log_files log files)"
        
        if [[ "$VERBOSE" == "true" ]] && [[ -f "$PROJECT_DIR/logs/app.log" ]]; then
            verbose "Recent log entries:"
            tail -n 5 "$PROJECT_DIR/logs/app.log" 2>/dev/null | sed 's/^/    /' || verbose "No recent logs"
        fi
        return 0
    else
        warn "Log directory not found"
        return 1
    fi
}

# Main health check
main() {
    print_banner
    check_curl || exit 1
    
    local checks_passed=0
    local total_checks=0
    
    log "Performing comprehensive health check..."
    
    # Basic connectivity test
    for attempt in $(seq 1 $MAX_ATTEMPTS); do
        verbose "Connectivity attempt $attempt/$MAX_ATTEMPTS"
        
        if perform_health_check "$ENDPOINT" "Basic connectivity"; then
            break
        elif [[ $attempt -eq $MAX_ATTEMPTS ]]; then
            error "Could not establish basic connectivity after $MAX_ATTEMPTS attempts"
            exit 1
        else
            verbose "Waiting 2 seconds before retry..."
            sleep 2
        fi
    done
    
    echo ""
    log "Running detailed health checks..."
    
    # API Health Checks
    local api_checks=(
        "/api/stats:API Statistics"
        "/api/workflows?limit=1:Workflow Search"
        "/api/categories:Categories API"
        "/:Main Interface"
    )
    
    for check in "${api_checks[@]}"; do
        local endpoint_path="${check%%:*}"
        local check_name="${check##*:}"
        total_checks=$((total_checks + 1))
        
        if perform_health_check "$ENDPOINT$endpoint_path" "$check_name"; then
            checks_passed=$((checks_passed + 1))
        fi
    done
    
    echo ""
    
    # System Health Checks
    log "Checking system components..."
    
    total_checks=$((total_checks + 1))
    if check_processes; then
        checks_passed=$((checks_passed + 1))
    fi
    
    total_checks=$((total_checks + 1))
    if check_database; then
        checks_passed=$((checks_passed + 1))
    fi
    
    total_checks=$((total_checks + 1))
    if check_logs; then
        checks_passed=$((checks_passed + 1))
    fi
    
    echo ""
    
    # Summary
    if [[ $checks_passed -eq $total_checks ]]; then
        success "All health checks passed! ($checks_passed/$total_checks) 🎉"
        success "Application is fully operational"
        echo ""
        echo -e "${GREEN}🌐 Application Access Points:${NC}"
        echo "   • Main Interface: $ENDPOINT"
        echo "   • API Documentation: $ENDPOINT/docs"
        echo "   • Health Stats: $ENDPOINT/api/stats"
        echo "   • Workflow Search: $ENDPOINT/api/workflows"
        exit 0
    elif [[ $checks_passed -gt $((total_checks / 2)) ]]; then
        warn "Partial health check passed ($checks_passed/$total_checks) ⚠️"
        warn "Some components may not be functioning correctly"
        exit 1
    else
        error "Health check failed ($checks_passed/$total_checks) ❌"
        error "Application is not functioning correctly"
        echo ""
        echo -e "${RED}🔧 Troubleshooting suggestions:${NC}"
        echo "   • Check if the application is running: ps aux | grep python"
        echo "   • Review logs: tail -f logs/app.log"
        echo "   • Restart application: ./scripts/deploy.sh development"
        echo "   • Check network connectivity: curl -I $ENDPOINT"
        exit 2
    fi
}

# Run main function
main "$@"
        
        if [[ "$http_code" == "200" ]]; then
            success "API is responding (HTTP $http_code)"
            
            # Parse and display stats
            if command -v jq &> /dev/null; then
                stats=$(cat /tmp/health_response)
                total=$(echo "$stats" | jq -r '.total // "N/A"')
                active=$(echo "$stats" | jq -r '.active // "N/A"')
                integrations=$(echo "$stats" | jq -r '.unique_integrations // "N/A"')
                
                log "Database status:"
                log "  - Total workflows: $total"
                log "  - Active workflows: $active"
                log "  - Unique integrations: $integrations"
            fi
            
            # Test main page
            if curl -s -f --connect-timeout $TIMEOUT "$ENDPOINT" > /dev/null; then
                success "Main page is accessible"
            else
                warn "Main page is not accessible"
            fi
            
            # Test API documentation
            if curl -s -f --connect-timeout $TIMEOUT "$ENDPOINT/docs" > /dev/null; then
                success "API documentation is accessible"
            else
                warn "API documentation is not accessible"
            fi
            
            # Clean up
            rm -f /tmp/health_response
            
            success "All health checks passed!"
            exit 0
        else
            warn "API returned HTTP $http_code"
        fi
    else
        warn "Failed to connect to $ENDPOINT"
    fi
    
    if [[ $attempt -lt $MAX_ATTEMPTS ]]; then
        log "Waiting 5 seconds before retry..."
        sleep 5
    fi
done

# Clean up
rm -f /tmp/health_response

error "Health check failed after $MAX_ATTEMPTS attempts"
exit 1