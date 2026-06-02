#!/bin/bash

# N8N Workflows Documentation - Backup Script
# Usage: ./scripts/backup.sh [backup-name]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
BACKUP_NAME="${1:-$(date +%Y%m%d_%H%M%S)}"
BACKUP_DIR="$PROJECT_DIR/backups"
BACKUP_PATH="$BACKUP_DIR/backup_$BACKUP_NAME"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

log() {
    echo -e "${BLUE}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Create backup directory
mkdir -p "$BACKUP_PATH"

log "Creating backup: $BACKUP_NAME"

# Backup database
if [[ -f "$PROJECT_DIR/database/workflows.db" ]]; then
    log "Backing up database..."
    cp "$PROJECT_DIR/database/workflows.db" "$BACKUP_PATH/workflows.db"
    success "Database backed up"
fi

# Backup configuration files
log "Backing up configuration..."
cp -r "$PROJECT_DIR"/*.yml "$BACKUP_PATH/" 2>/dev/null || true
cp "$PROJECT_DIR"/.env* "$BACKUP_PATH/" 2>/dev/null || true
cp -r "$PROJECT_DIR"/k8s "$BACKUP_PATH/" 2>/dev/null || true
cp -r "$PROJECT_DIR"/helm "$BACKUP_PATH/" 2>/dev/null || true

# Backup logs (last 7 days only)
if [[ -d "$PROJECT_DIR/logs" ]]; then
    log "Backing up recent logs..."
    find "$PROJECT_DIR/logs" -name "*.log" -mtime -7 -exec cp {} "$BACKUP_PATH/" \; 2>/dev/null || true
fi

# Create archive
log "Creating backup archive..."
cd "$BACKUP_DIR"
tar -czf "backup_$BACKUP_NAME.tar.gz" "backup_$BACKUP_NAME"
rm -rf "backup_$BACKUP_NAME"

# Cleanup old backups (keep last 10)
find "$BACKUP_DIR" -name "backup_*.tar.gz" -type f -printf '%T@ %p\n' | \
    sort -rn | tail -n +11 | cut -d' ' -f2- | xargs rm -f

success "Backup created: $BACKUP_DIR/backup_$BACKUP_NAME.tar.gz"