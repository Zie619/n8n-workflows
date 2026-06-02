#!/bin/bash
# =============================================================================
# AI Stack Startup Script for Linux/macOS
# =============================================================================
# This script checks prerequisites, creates folders, and launches the stack
# Run: chmod +x start.sh && ./start.sh
# =============================================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo ""
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}  $1${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
}

print_step() {
    echo -e "${YELLOW}▶ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Banner
echo ""
echo -e "${MAGENTA}    ╔═══════════════════════════════════════════════════════════╗${NC}"
echo -e "${MAGENTA}    ║                                                           ║${NC}"
echo -e "${MAGENTA}    ║     🤖 AI AUTOMATION STACK                                ║${NC}"
echo -e "${MAGENTA}    ║     n8n + Agent Zero + ComfyUI                            ║${NC}"
echo -e "${MAGENTA}    ║                                                           ║${NC}"
echo -e "${MAGENTA}    ╚═══════════════════════════════════════════════════════════╝${NC}"
echo ""

# Parse arguments
NO_PULL=false
CPU_MODE=false
ACTION="start"

while [[ $# -gt 0 ]]; do
    case $1 in
        --no-pull|-n)
            NO_PULL=true
            shift
            ;;
        --cpu|-c)
            CPU_MODE=true
            shift
            ;;
        --stop|-s)
            ACTION="stop"
            shift
            ;;
        --logs|-l)
            ACTION="logs"
            shift
            ;;
        --status)
            ACTION="status"
            shift
            ;;
        --help|-h)
            echo "Usage: ./start.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --no-pull, -n    Skip pulling Docker images"
            echo "  --cpu, -c        Run ComfyUI in CPU mode (no GPU)"
            echo "  --stop, -s       Stop the stack"
            echo "  --logs, -l       View container logs"
            echo "  --status         Show container status"
            echo "  --help, -h       Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Handle actions
case $ACTION in
    stop)
        print_header "Stopping AI Stack"
        docker compose down
        print_success "Stack stopped"
        exit 0
        ;;
    logs)
        docker compose logs -f
        exit 0
        ;;
    status)
        print_header "Stack Status"
        docker compose ps
        exit 0
        ;;
esac

# =============================================================================
# STEP 1: Check Docker
# =============================================================================
print_header "Checking Prerequisites"

print_step "Checking Docker installation..."
if command -v docker &> /dev/null; then
    DOCKER_VERSION=$(docker --version)
    print_success "Docker found: $DOCKER_VERSION"
else
    print_error "Docker is not installed"
    print_info "Please install Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

print_step "Checking if Docker is running..."
if docker info &> /dev/null; then
    print_success "Docker daemon is running"
else
    print_error "Docker daemon is not running"
    print_info "Please start Docker and try again"
    exit 1
fi

print_step "Checking Docker Compose..."
if docker compose version &> /dev/null; then
    COMPOSE_VERSION=$(docker compose version)
    print_success "Docker Compose found: $COMPOSE_VERSION"
else
    print_error "Docker Compose is not available"
    exit 1
fi

# Check for NVIDIA GPU (optional)
print_step "Checking for NVIDIA GPU support..."
HAS_GPU=false
if command -v nvidia-smi &> /dev/null; then
    GPU_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || echo "")
    if [ -n "$GPU_NAME" ]; then
        print_success "NVIDIA GPU detected: $GPU_NAME"
        HAS_GPU=true
    fi
fi

if [ "$HAS_GPU" = false ]; then
    print_info "No NVIDIA GPU detected (use --cpu flag for CPU mode)"
fi

# =============================================================================
# STEP 2: Create Directory Structure
# =============================================================================
print_header "Setting Up Directory Structure"

DIRECTORIES=(
    "data/n8n"
    "data/agent-zero"
    "shared/comfyui/models/checkpoints"
    "shared/comfyui/models/loras"
    "shared/comfyui/models/vae"
    "shared/comfyui/models/controlnet"
    "shared/comfyui/models/upscale_models"
    "shared/comfyui/models/embeddings"
    "shared/comfyui/models/clip"
    "shared/comfyui/output"
    "shared/comfyui/input"
    "shared/comfyui/custom_nodes"
    "shared/workflows"
)

for dir in "${DIRECTORIES[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        print_success "Created: $dir"
    else
        print_info "Exists: $dir"
    fi
done

# =============================================================================
# STEP 3: Pull Images
# =============================================================================
if [ "$NO_PULL" = false ]; then
    print_header "Pulling Docker Images"
    
    print_step "Pulling n8n..."
    docker pull n8nio/n8n:latest
    
    print_step "Pulling Agent Zero..."
    docker pull frdel/agent-zero-run:latest
    
    print_step "Pulling ComfyUI..."
    docker pull aidockorg/comfyui-cuda:latest
    
    print_success "All images pulled successfully"
else
    print_info "Skipping image pull (--no-pull flag set)"
fi

# =============================================================================
# STEP 4: Start Stack
# =============================================================================
print_header "Starting AI Stack"

if [ "$CPU_MODE" = true ] || [ "$HAS_GPU" = false ]; then
    print_info "Starting in CPU mode (no GPU acceleration for ComfyUI)"
    export COMFYUI_ARGS="--cpu"
fi

print_step "Starting containers..."
docker compose up -d

# Wait for services to be healthy
print_step "Waiting for services to start..."
sleep 10

# =============================================================================
# STEP 5: Display Status
# =============================================================================
print_header "Stack Status"

docker compose ps

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  🎉 AI Stack is running!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${WHITE}  📊 n8n (Workflow Automation):${NC}"
echo -e "${CYAN}     http://localhost:5678${NC}"
echo ""
echo -e "${WHITE}  🤖 Agent Zero (AI Agent):${NC}"
echo -e "${CYAN}     http://localhost:50080${NC}"
echo ""
echo -e "${WHITE}  🎨 ComfyUI (Image Generation):${NC}"
echo -e "${CYAN}     http://localhost:8188${NC}"
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
print_info "Commands:"
echo "  ./start.sh --stop    # Stop the stack"
echo "  ./start.sh --logs    # View logs"
echo "  ./start.sh --status  # Check status"
echo ""
print_info "Shared folder: ./shared (accessible by all services)"
print_info "ComfyUI models: ./shared/comfyui/models"
echo ""