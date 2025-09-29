#!/bin/bash

# N8N Workflows Documentation - Health Check Script
# Usage: ./scripts/health-check.sh [endpoint]

set -euo pipefail

ENDPOINT="${1:-http://localhost:8000}"
MAX_ATTEMPTS=5
TIMEOUT=10

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
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

# Check if curl is available
if ! command -v curl &> /dev/null; then
    error "curl is required but not installed"
    exit 1
fi

log "Starting health check for $ENDPOINT"

# Test basic connectivity
for attempt in $(seq 1 $MAX_ATTEMPTS); do
    log "Health check attempt $attempt/$MAX_ATTEMPTS"
    
    # Test API stats endpoint
    if response=$(curl -s -w "%{http_code}" -o /tmp/health_response --connect-timeout $TIMEOUT "$ENDPOINT/api/stats" 2>/dev/null); then
        http_code=$(echo "$response" | tail -c 4 | head -c 3)
        
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