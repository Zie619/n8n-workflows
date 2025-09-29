#!/bin/bash

# N8N Workflows Documentation Platform - Installation Script
# Universal installer for Linux, macOS, and Windows WSL
# Usage: ./install.sh [--help] [--python-only] [--docker-only] [--full]

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_NAME="n8n-workflows-docs"
MIN_PYTHON_VERSION="3.7"
MIN_NODE_VERSION="16"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Installation flags
INSTALL_PYTHON=true
INSTALL_DOCKER=true
INSTALL_NODE=true
SKIP_CONFIRMATION=false

# OS Detection
OS=""
ARCH=""

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
        if grep -q "Microsoft\|WSL" /proc/version 2>/dev/null; then
            OS="wsl"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
        OS="windows"
    else
        OS="unknown"
    fi
    
    ARCH=$(uname -m)
    if [[ "$ARCH" == "x86_64" ]]; then
        ARCH="amd64"
    elif [[ "$ARCH" == "aarch64" ]] || [[ "$ARCH" == "arm64" ]]; then
        ARCH="arm64"
    fi
}

# Logging functions
print_banner() {
    echo -e "${CYAN}╔═══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${NC} ${PURPLE}🚀 N8N Workflows Documentation Platform Installer${NC} ${CYAN}║${NC}"
    echo -e "${CYAN}╚═══════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}Platform:${NC} $OS ($ARCH)"
    echo -e "${BLUE}Project:${NC}  $PROJECT_NAME"
    echo ""
}

log() {
    echo -e "${BLUE}[INFO]${NC} $1"
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

step() {
    echo -e "${PURPLE}[STEP]${NC} $1"
}

# Version comparison function
version_ge() {
    printf '%s\n%s\n' "$2" "$1" | sort -V -C
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# System requirements check
check_system_requirements() {
    step "Checking system requirements..."
    
    # Check OS compatibility
    if [[ "$OS" == "unknown" ]]; then
        error "Unsupported operating system. This installer supports Linux, macOS, and Windows WSL."
    fi
    
    # Check basic tools
    local missing_tools=()
    
    if ! command_exists curl && ! command_exists wget; then
        missing_tools+=("curl or wget")
    fi
    
    if ! command_exists git; then
        missing_tools+=("git")
    fi
    
    if ! command_exists unzip; then
        missing_tools+=("unzip")
    fi
    
    if [[ ${#missing_tools[@]} -gt 0 ]]; then
        error "Missing required system tools: ${missing_tools[*]}. Please install them first."
    fi
    
    success "System requirements check passed"
}

# Python installation and verification
install_python() {
    if [[ "$INSTALL_PYTHON" != "true" ]]; then
        return 0
    fi
    
    step "Checking Python installation..."
    
    local python_cmd=""
    local python_version=""
    
    # Try different Python commands
    for cmd in python3 python; do
        if command_exists "$cmd"; then
            python_version=$($cmd --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
            if version_ge "$python_version" "$MIN_PYTHON_VERSION"; then
                python_cmd="$cmd"
                break
            fi
        fi
    done
    
    if [[ -z "$python_cmd" ]]; then
        warn "Python $MIN_PYTHON_VERSION+ not found. Installing Python..."
        
        case "$OS" in
            "linux"|"wsl")
                if command_exists apt-get; then
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-pip python3-venv
                elif command_exists yum; then
                    sudo yum install -y python3 python3-pip
                elif command_exists dnf; then
                    sudo dnf install -y python3 python3-pip
                elif command_exists pacman; then
                    sudo pacman -S python python-pip
                else
                    error "Could not install Python. Please install Python $MIN_PYTHON_VERSION+ manually."
                fi
                python_cmd="python3"
                ;;
            "macos")
                if command_exists brew; then
                    brew install python@3.11
                    python_cmd="python3"
                else
                    error "Please install Homebrew first or install Python manually."
                fi
                ;;
            *)
                error "Automatic Python installation not supported on $OS. Please install Python $MIN_PYTHON_VERSION+ manually."
                ;;
        esac
    fi
    
    # Verify installation
    python_version=$($python_cmd --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
    success "Python $python_version found at: $(which $python_cmd)"
    
    # Check pip
    if ! $python_cmd -m pip --version >/dev/null 2>&1; then
        warn "pip not found. Installing pip..."
        if command_exists curl; then
            curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
            $python_cmd get-pip.py
            rm get-pip.py
        else
            error "pip installation failed. Please install pip manually."
        fi
    fi
    
    success "Python environment ready"
    export PYTHON_CMD="$python_cmd"
}

# Node.js installation and verification
install_nodejs() {
    if [[ "$INSTALL_NODE" != "true" ]]; then
        return 0
    fi
    
    step "Checking Node.js installation..."
    
    local node_version=""
    
    if command_exists node; then
        node_version=$(node --version | sed 's/v//')
        if version_ge "$node_version" "$MIN_NODE_VERSION"; then
            success "Node.js $node_version found"
            return 0
        fi
    fi
    
    warn "Node.js $MIN_NODE_VERSION+ not found. Installing Node.js..."
    
    case "$OS" in
        "linux"|"wsl")
            # Install using NodeSource repository
            if command_exists curl; then
                curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
                if command_exists apt-get; then
                    sudo apt-get install -y nodejs
                fi
            else
                error "Could not install Node.js. Please install Node.js $MIN_NODE_VERSION+ manually."
            fi
            ;;
        "macos")
            if command_exists brew; then
                brew install node
            else
                error "Please install Homebrew first or install Node.js manually."
            fi
            ;;
        *)
            error "Automatic Node.js installation not supported on $OS. Please install Node.js $MIN_NODE_VERSION+ manually."
            ;;
    esac
    
    # Verify installation
    if command_exists node; then
        node_version=$(node --version | sed 's/v//')
        success "Node.js $node_version installed successfully"
    else
        error "Node.js installation failed"
    fi
}

# Docker installation and verification
install_docker() {
    if [[ "$INSTALL_DOCKER" != "true" ]]; then
        return 0
    fi
    
    step "Checking Docker installation..."
    
    if command_exists docker && command_exists docker-compose; then
        if docker info >/dev/null 2>&1; then
            success "Docker is already installed and running"
            return 0
        fi
    fi
    
    warn "Docker not found or not running. Installing Docker..."
    
    case "$OS" in
        "linux"|"wsl")
            # Install Docker using the official script
            if command_exists curl; then
                curl -fsSL https://get.docker.com -o get-docker.sh
                sudo sh get-docker.sh
                rm get-docker.sh
                
                # Add user to docker group
                sudo usermod -aG docker "$USER" || warn "Could not add user to docker group"
                
                # Install Docker Compose
                local compose_version="2.20.0"
                sudo curl -L "https://github.com/docker/compose/releases/download/v${compose_version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                sudo chmod +x /usr/local/bin/docker-compose
                
            else
                error "Could not install Docker. Please install Docker manually."
            fi
            ;;
        "macos")
            warn "Please install Docker Desktop for Mac manually from https://docker.com/products/docker-desktop"
            return 0
            ;;
        *)
            error "Automatic Docker installation not supported on $OS. Please install Docker manually."
            ;;
    esac
    
    success "Docker installation completed"
    warn "You may need to log out and log back in for Docker group permissions to take effect"
}

# Install project dependencies
install_dependencies() {
    step "Installing project dependencies..."
    
    cd "$SCRIPT_DIR"
    
    # Install Python dependencies
    if [[ -f "requirements.txt" ]] && [[ -n "${PYTHON_CMD:-}" ]]; then
        log "Installing Python dependencies..."
        $PYTHON_CMD -m pip install --user -r requirements.txt
        success "Python dependencies installed"
    fi
    
    # Install Node.js dependencies
    if [[ -f "package.json" ]] && command_exists npm; then
        log "Installing Node.js dependencies..."
        npm install
        success "Node.js dependencies installed"
    fi
    
    # Make scripts executable
    if [[ -d "scripts" ]]; then
        chmod +x scripts/*.sh 2>/dev/null || true
        success "Scripts made executable"
    fi
}

# Verify installation
verify_installation() {
    step "Verifying installation..."
    
    cd "$SCRIPT_DIR"
    
    # Test Python application
    if [[ -f "run.py" ]] && [[ -n "${PYTHON_CMD:-}" ]]; then
        log "Testing Python application..."
        if $PYTHON_CMD run.py --help >/dev/null 2>&1; then
            success "Python application is working"
        else
            warn "Python application test failed"
        fi
    fi
    
    # Test Docker setup
    if [[ -f "docker-compose.yml" ]] && command_exists docker-compose; then
        log "Testing Docker configuration..."
        if docker-compose config >/dev/null 2>&1; then
            success "Docker configuration is valid"
        else
            warn "Docker configuration test failed"
        fi
    fi
    
    # Create necessary directories
    mkdir -p database logs static 2>/dev/null || true
    
    success "Installation verification completed"
}

# Show usage information
show_usage() {
    echo "N8N Workflows Documentation Platform - Installer"
    echo ""
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "OPTIONS:"
    echo "  --help           Show this help message"
    echo "  --python-only    Install only Python environment"
    echo "  --docker-only    Install only Docker environment"  
    echo "  --nodejs-only    Install only Node.js environment"
    echo "  --full           Install all components (default)"
    echo "  --yes            Skip confirmation prompts"
    echo ""
    echo "EXAMPLES:"
    echo "  $0                    # Full installation with prompts"
    echo "  $0 --python-only      # Install only Python components"
    echo "  $0 --yes              # Full installation without prompts"
    echo ""
}

# Show post-installation instructions
show_next_steps() {
    echo ""
    echo -e "${CYAN}╔═══════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║${NC} ${GREEN}🎉 Installation Complete!${NC}                           ${CYAN}║${NC}"
    echo -e "${CYAN}╚═══════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${YELLOW}📋 Next Steps:${NC}"
    echo ""
    echo -e "${BLUE}1. Quick Start (Python):${NC}"
    echo "   python3 run.py"
    echo "   # Then open: http://localhost:8000"
    echo ""
    echo -e "${BLUE}2. Docker Deployment:${NC}"
    echo "   ./scripts/deploy.sh development"
    echo "   # Or use: docker-compose up -d"
    echo ""
    echo -e "${BLUE}3. Production Deployment:${NC}"
    echo "   ./scripts/deploy.sh production"
    echo ""
    echo -e "${BLUE}4. Health Check:${NC}"
    echo "   ./scripts/health-check.sh"
    echo ""
    echo -e "${YELLOW}📚 Documentation:${NC}"
    echo "   - README.md           - Project overview"
    echo "   - DEPLOYMENT.md       - Comprehensive deployment guide"  
    echo "   - DEPLOY_QUICKSTART.md - Quick deployment instructions"
    echo ""
    echo -e "${YELLOW}🆘 Need Help?${NC}"
    echo "   - Run: python3 run.py --help"
    echo "   - Run: ./scripts/deploy.sh --help"
    echo "   - Check: logs/ directory for troubleshooting"
    echo ""
}

# Parse command line arguments
parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            --help|-h)
                show_usage
                exit 0
                ;;
            --python-only)
                INSTALL_PYTHON=true
                INSTALL_DOCKER=false
                INSTALL_NODE=false
                ;;
            --docker-only)
                INSTALL_PYTHON=false
                INSTALL_DOCKER=true
                INSTALL_NODE=false
                ;;
            --nodejs-only)
                INSTALL_PYTHON=false
                INSTALL_DOCKER=false
                INSTALL_NODE=true
                ;;
            --full)
                INSTALL_PYTHON=true
                INSTALL_DOCKER=true
                INSTALL_NODE=true
                ;;
            --yes|-y)
                SKIP_CONFIRMATION=true
                ;;
            *)
                error "Unknown option: $1. Use --help for usage information."
                ;;
        esac
        shift
    done
}

# Confirmation prompt
confirm_installation() {
    if [[ "$SKIP_CONFIRMATION" == "true" ]]; then
        return 0
    fi
    
    echo -e "${YELLOW}Installation Configuration:${NC}"
    echo -e "  Python:  $([ "$INSTALL_PYTHON" == "true" ] && echo "✅" || echo "❌")"
    echo -e "  Node.js: $([ "$INSTALL_NODE" == "true" ] && echo "✅" || echo "❌")"  
    echo -e "  Docker:  $([ "$INSTALL_DOCKER" == "true" ] && echo "✅" || echo "❌")"
    echo ""
    
    read -p "Continue with installation? [y/N]: " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log "Installation cancelled by user"
        exit 0
    fi
}

# Main installation function
main() {
    parse_arguments "$@"
    
    detect_os
    print_banner
    confirm_installation
    
    check_system_requirements
    
    if [[ "$INSTALL_PYTHON" == "true" ]]; then
        install_python
    fi
    
    if [[ "$INSTALL_NODE" == "true" ]]; then
        install_nodejs
    fi
    
    if [[ "$INSTALL_DOCKER" == "true" ]]; then
        install_docker
    fi
    
    install_dependencies
    verify_installation
    
    show_next_steps
    
    success "🚀 Installation completed successfully!"
}

# Run main function with all arguments
main "$@"