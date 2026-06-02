#!/bin/bash

# N8N Workflows Documentation - Docker Container Runner
# Enhanced version with better cross-platform support and error handling

set -euo pipefail

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# Check prerequisites
if ! command -v docker &> /dev/null; then
    error "Docker is not installed. Please install Docker first."
fi

if ! docker compose version &> /dev/null; then
    error "Docker Compose is not available. Please install Docker Compose."
fi

log "Starting N8N Workflows Documentation Platform..."

# Build and start containers
if ! docker compose up -d --build; then
    error "Failed to start Docker containers"
fi

# Wait for application to be ready
log "Waiting for application to start..."
sleep 10

# Health check
max_attempts=12
attempt=1
while [[ $attempt -le $max_attempts ]]; do
    log "Health check attempt $attempt/$max_attempts"
    
    if curl -s -f http://localhost:8000/api/stats > /dev/null 2>&1; then
        success "Application is ready!"
        break
    fi
    
    if [[ $attempt -eq $max_attempts ]]; then
        warn "Application may not be fully ready yet"
        break
    fi
    
    sleep 5
    ((attempt++))
done

# Display information
success "N8N Workflows Documentation Platform is running!"
echo
echo "🌐 Access URLs:"
echo "   Main Interface: http://localhost:8000"
echo "   API Documentation: http://localhost:8000/docs"
echo "   API Stats: http://localhost:8000/api/stats"
echo
echo "📊 Container Status:"
docker compose ps
echo
echo "📝 To view logs: docker compose logs -f"
echo "🛑 To stop: docker compose down"

# Open browser based on OS
open_browser() {
    local url="http://localhost:8000"
    
    case "$OSTYPE" in
        darwin*)
            # macOS
            if command -v open &> /dev/null; then
                log "Opening browser on macOS..."
                open "$url" 2>/dev/null || warn "Could not open browser automatically"
            fi
            ;;
        msys*|cygwin*|win*)
            # Windows
            log "Opening browser on Windows..."
            start "$url" 2>/dev/null || warn "Could not open browser automatically"
            ;;
        linux*)
            # Linux
            if [[ -n "${DISPLAY:-}" ]] && command -v xdg-open &> /dev/null; then
                log "Opening browser on Linux..."
                xdg-open "$url" 2>/dev/null || warn "Could not open browser automatically"
            else
                log "No display detected or xdg-open not available"
            fi
            ;;
        *)
            warn "Unknown operating system: $OSTYPE"
            ;;
    esac
}

# Attempt to open browser
open_browser

log "Setup complete! The application should now be accessible in your browser."