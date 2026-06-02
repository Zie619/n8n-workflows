# =============================================================================
# AI Stack Startup Script for Windows
# =============================================================================
# This script checks prerequisites, creates folders, and launches the stack
# Run: .\start.ps1
# =============================================================================

param(
    [switch]$NoPull,
    [switch]$CPU,
    [switch]$Stop,
    [switch]$Logs,
    [switch]$Status
)

$ErrorActionPreference = "Stop"

# Colors
function Write-Color($Text, $Color) {
    Write-Host $Text -ForegroundColor $Color
}

function Write-Header($Text) {
    Write-Host ""
    Write-Color "═══════════════════════════════════════════════════════════════" "Cyan"
    Write-Color "  $Text" "Cyan"
    Write-Color "═══════════════════════════════════════════════════════════════" "Cyan"
    Write-Host ""
}

function Write-Step($Text) {
    Write-Color "▶ $Text" "Yellow"
}

function Write-Success($Text) {
    Write-Color "✓ $Text" "Green"
}

function Write-Error($Text) {
    Write-Color "✗ $Text" "Red"
}

function Write-Info($Text) {
    Write-Color "ℹ $Text" "Blue"
}

# Banner
Write-Host ""
Write-Color "    ╔═══════════════════════════════════════════════════════════╗" "Magenta"
Write-Color "    ║                                                           ║" "Magenta"
Write-Color "    ║     🤖 AI AUTOMATION STACK                                ║" "Magenta"
Write-Color "    ║     n8n + Agent Zero + ComfyUI                            ║" "Magenta"
Write-Color "    ║                                                           ║" "Magenta"
Write-Color "    ╚═══════════════════════════════════════════════════════════╝" "Magenta"
Write-Host ""

# Handle flags
if ($Stop) {
    Write-Header "Stopping AI Stack"
    docker compose down
    Write-Success "Stack stopped"
    exit 0
}

if ($Logs) {
    docker compose logs -f
    exit 0
}

if ($Status) {
    Write-Header "Stack Status"
    docker compose ps
    exit 0
}

# =============================================================================
# STEP 1: Check Docker
# =============================================================================
Write-Header "Checking Prerequisites"

Write-Step "Checking Docker installation..."
try {
    $dockerVersion = docker --version
    Write-Success "Docker found: $dockerVersion"
} catch {
    Write-Error "Docker is not installed or not in PATH"
    Write-Info "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop"
    exit 1
}

Write-Step "Checking if Docker is running..."
try {
    docker info | Out-Null
    Write-Success "Docker daemon is running"
} catch {
    Write-Error "Docker daemon is not running"
    Write-Info "Please start Docker Desktop and try again"
    exit 1
}

Write-Step "Checking Docker Compose..."
try {
    $composeVersion = docker compose version
    Write-Success "Docker Compose found: $composeVersion"
} catch {
    Write-Error "Docker Compose is not available"
    exit 1
}

# Check for NVIDIA GPU (optional)
Write-Step "Checking for NVIDIA GPU support..."
try {
    $nvidiaSmi = nvidia-smi --query-gpu=name --format=csv,noheader 2>$null
    if ($nvidiaSmi) {
        Write-Success "NVIDIA GPU detected: $nvidiaSmi"
        $hasGPU = $true
    } else {
        $hasGPU = $false
    }
} catch {
    Write-Info "No NVIDIA GPU detected (ComfyUI will use CPU mode if -CPU flag is set)"
    $hasGPU = $false
}

# =============================================================================
# STEP 2: Create Directory Structure
# =============================================================================
Write-Header "Setting Up Directory Structure"

$directories = @(
    "data/n8n",
    "data/agent-zero",
    "shared/comfyui/models/checkpoints",
    "shared/comfyui/models/loras",
    "shared/comfyui/models/vae",
    "shared/comfyui/models/controlnet",
    "shared/comfyui/models/upscale_models",
    "shared/comfyui/models/embeddings",
    "shared/comfyui/models/clip",
    "shared/comfyui/output",
    "shared/comfyui/input",
    "shared/comfyui/custom_nodes",
    "shared/workflows"
)

foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Success "Created: $dir"
    } else {
        Write-Info "Exists: $dir"
    }
}

# =============================================================================
# STEP 3: Pull Images
# =============================================================================
if (-not $NoPull) {
    Write-Header "Pulling Docker Images"
    
    Write-Step "Pulling n8n..."
    docker pull n8nio/n8n:latest
    
    Write-Step "Pulling Agent Zero..."
    docker pull frdel/agent-zero-run:latest
    
    Write-Step "Pulling ComfyUI..."
    docker pull yanwk/comfyui-boot:latest
    
    Write-Success "All images pulled successfully"
} else {
    Write-Info "Skipping image pull (-NoPull flag set)"
}

# =============================================================================
# STEP 4: Start Stack
# =============================================================================
Write-Header "Starting AI Stack"

if ($CPU -or -not $hasGPU) {
    Write-Info "Starting in CPU mode (no GPU acceleration for ComfyUI)"
    # Modify compose to use CPU mode
    $env:COMFYUI_ARGS = "--cpu"
}

Write-Step "Starting containers..."
docker compose up -d

# Wait for services to be healthy
Write-Step "Waiting for services to start..."
Start-Sleep -Seconds 10

# =============================================================================
# STEP 5: Display Status
# =============================================================================
Write-Header "Stack Status"

docker compose ps

Write-Host ""
Write-Color "═══════════════════════════════════════════════════════════════" "Green"
Write-Color "  🎉 AI Stack is running!" "Green"
Write-Color "═══════════════════════════════════════════════════════════════" "Green"
Write-Host ""
Write-Color "  📊 n8n (Workflow Automation):" "White"
Write-Color "     http://localhost:5678" "Cyan"
Write-Host ""
Write-Color "  🤖 Agent Zero (AI Agent):" "White"
Write-Color "     http://localhost:50080" "Cyan"
Write-Host ""
Write-Color "  🎨 ComfyUI (Image Generation):" "White"
Write-Color "     http://localhost:8188" "Cyan"
Write-Host ""
Write-Color "═══════════════════════════════════════════════════════════════" "Green"
Write-Host ""
Write-Info "Commands:"
Write-Host "  .\start.ps1 -Stop    # Stop the stack"
Write-Host "  .\start.ps1 -Logs    # View logs"
Write-Host "  .\start.ps1 -Status  # Check status"
Write-Host ""
Write-Info "Shared folder: ./shared (accessible by all services)"
Write-Info "ComfyUI models: ./shared/comfyui/models"
Write-Host ""