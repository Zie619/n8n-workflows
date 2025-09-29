# 📦 Installation Guide - N8N Workflows Documentation Platform

> **Complete installation guide with automated installers and manual setup instructions**

## 🚀 Quick Installation (Recommended)

### One-Command Installation
```bash
# Download and run the automated installer
curl -fsSL https://raw.githubusercontent.com/sahiixx/n8n-workflows-1/main/install.sh | bash

# Or if you have the repository cloned
./install.sh
```

**What the installer does:**
- ✅ Detects your operating system (Linux, macOS, Windows WSL)
- ✅ Installs Python 3.7+ if not available
- ✅ Installs Node.js 16+ if not available
- ✅ Installs Docker if not available
- ✅ Installs all project dependencies
- ✅ Verifies installation and provides next steps

### Installation Options
```bash
# Full installation (default)
./install.sh --full

# Python environment only
./install.sh --python-only

# Docker environment only
./install.sh --docker-only

# Node.js environment only
./install.sh --nodejs-only

# Skip confirmation prompts
./install.sh --yes
```

---

## 🖥️ Manual Installation

### Prerequisites

#### System Requirements
- **Operating System**: Linux, macOS, or Windows WSL
- **RAM**: 2GB minimum, 4GB recommended
- **Disk Space**: 1GB for application + workflows
- **Network**: Internet connection for initial setup

#### Required Software
- **Python 3.7+** - For the API server and workflow processing
- **pip** - Python package manager
- **Git** - For repository management
- **curl/wget** - For downloading dependencies

#### Optional (for specific deployment methods)
- **Node.js 16+** - For Node.js implementation
- **Docker & Docker Compose** - For containerized deployment
- **kubectl** - For Kubernetes deployment
- **Helm** - For Helm chart deployment

---

## 🐧 Linux Installation

### Ubuntu/Debian
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y python3 python3-pip python3-venv git curl unzip

# Clone repository
git clone https://github.com/sahiixx/n8n-workflows-1.git
cd n8n-workflows-1

# Install dependencies
pip3 install --user -r requirements.txt

# Make scripts executable
chmod +x scripts/*.sh install.sh

# Start the application
python3 run.py
```

### CentOS/RHEL/Fedora
```bash
# Update system
sudo yum update -y  # or sudo dnf update -y

# Install required packages
sudo yum install -y python3 python3-pip git curl unzip  # or dnf

# Clone and setup
git clone https://github.com/sahiixx/n8n-workflows-1.git
cd n8n-workflows-1

# Install dependencies
pip3 install --user -r requirements.txt

# Start the application
python3 run.py
```

### Arch Linux
```bash
# Update system
sudo pacman -Syu

# Install required packages
sudo pacman -S python python-pip git curl unzip

# Clone and setup
git clone https://github.com/sahiixx/n8n-workflows-1.git
cd n8n-workflows-1

# Install dependencies
pip install --user -r requirements.txt

# Start the application
python run.py
```

---

## 🍎 macOS Installation

### Using Homebrew (Recommended)
```bash
# Install Homebrew if not installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required packages
brew install python git curl

# Clone repository
git clone https://github.com/sahiixx/n8n-workflows-1.git
cd n8n-workflows-1

# Install dependencies
pip3 install --user -r requirements.txt

# Start the application
python3 run.py
```

### Using Python.org Installer
```bash
# Download and install Python from python.org
# Then:

# Clone repository
git clone https://github.com/sahiixx/n8n-workflows-1.git
cd n8n-workflows-1

# Install dependencies
python3 -m pip install --user -r requirements.txt

# Start the application
python3 run.py
```

---

## 🪟 Windows Installation

### Windows Subsystem for Linux (WSL) - Recommended
```bash
# Install WSL2 with Ubuntu
wsl --install

# Inside WSL, follow the Ubuntu installation steps above
```

### Windows Native (PowerShell)
```powershell
# Install Python from python.org or Microsoft Store
# Install Git from git-scm.com

# Clone repository
git clone https://github.com/sahiixx/n8n-workflows-1.git
cd n8n-workflows-1

# Install dependencies
pip install -r requirements.txt

# Start the application
python run.py
```

---

## 🐳 Docker Installation

### Prerequisites
Install Docker and Docker Compose:

```bash
# Linux (Ubuntu/Debian)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# macOS
brew install --cask docker

# Windows
# Download Docker Desktop from docker.com
```

### Docker Deployment
```bash
# Clone repository
git clone https://github.com/sahiixx/n8n-workflows-1.git
cd n8n-workflows-1

# Quick deployment
./run-as-docker-container.sh

# Or manually
docker-compose up -d --build
```

---

## ☸️ Kubernetes Installation

### Prerequisites
```bash
# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Install Helm (optional)
curl https://get.helm.sh/helm-v3.12.0-linux-amd64.tar.gz | tar -xzO linux-amd64/helm > helm
sudo install helm /usr/local/bin/
```

### Kubernetes Deployment
```bash
# Deploy with kubectl
kubectl apply -f k8s/

# Or deploy with Helm
helm install n8n-workflows ./helm/workflows-docs
```

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```bash
# Application settings
HOST=127.0.0.1
PORT=8000
ENVIRONMENT=development

# Database settings
DATABASE_PATH=database/workflows.db

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# Optional: External services
# WEBHOOK_URL=https://your-domain.com/webhook
```

### Directory Structure
After installation, your directory should look like:
```
n8n-workflows-1/
├── workflows/          # 2000+ n8n workflow JSON files
├── database/          # SQLite database (auto-created)
├── static/           # Static web assets
├── logs/             # Application logs
├── scripts/          # Deployment and utility scripts
├── requirements.txt  # Python dependencies
├── run.py           # Main application launcher
├── install.sh       # Installation script
└── README.md        # Documentation
```

---

## ✅ Verification

### Test Installation
```bash
# Test Python application
python3 run.py --help

# Test deployment scripts
./scripts/deploy.sh --help
./scripts/health-check.sh

# Test Docker (if installed)
docker-compose config
```

### Start Application
```bash
# Start with default settings
python3 run.py

# Start with custom settings
python3 run.py --host 0.0.0.0 --port 3000

# Start in development mode
python3 run.py --dev

# Force database reindex
python3 run.py --reindex
```

### Access Points
- **Main Application**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/api/stats
- **Workflow Search**: http://localhost:8000/api/workflows

---

## 🔍 Troubleshooting

### Common Issues

#### Python Issues
```bash
# Python not found
sudo apt install python3 python3-pip  # Linux
brew install python                   # macOS

# pip not found
python3 -m ensurepip --upgrade

# Permission denied
pip3 install --user -r requirements.txt

# Module not found
python3 -m pip install --user -r requirements.txt
```

#### Docker Issues
```bash
# Docker daemon not running
sudo systemctl start docker

# Permission denied
sudo usermod -aG docker $USER
# Then log out and log back in

# Docker Compose not found
sudo apt install docker-compose-plugin  # Linux
brew install docker-compose             # macOS
```

#### Application Issues
```bash
# Port already in use
python3 run.py --port 3000

# Database issues
python3 run.py --reindex

# Missing directories
mkdir -p database logs static

# Permission issues
chmod +x scripts/*.sh install.sh
```

#### Performance Issues
```bash
# Slow database queries
python3 run.py --reindex

# Memory issues
# Use Docker deployment for better resource management
docker-compose up -d
```

### Getting Help

#### Check Logs
```bash
# Application logs
tail -f logs/app.log

# Docker logs
docker-compose logs -f

# System logs
journalctl -u docker
```

#### Debug Mode
```bash
# Start in development mode with verbose logging
python3 run.py --dev

# Enable debug logging
export LOG_LEVEL=DEBUG
python3 run.py
```

#### Community Support
- **GitHub Issues**: https://github.com/sahiixx/n8n-workflows-1/issues
- **Documentation**: README.md, DEPLOYMENT.md
- **n8n Community**: https://community.n8n.io/

---

## 🚀 Next Steps

After successful installation:

1. **[Quick Start](DEPLOY_QUICKSTART.md)** - Get running in minutes
2. **[Deployment Guide](DEPLOYMENT.md)** - Production deployment
3. **[README](README.md)** - Features and usage
4. **Import Workflows** - Start using the 2000+ workflows

### Quick Commands Reference
```bash
# Install everything
./install.sh --yes

# Quick start
python3 run.py

# Deploy to production
./scripts/deploy.sh production

# Health check
./scripts/health-check.sh

# Update workflows
git pull && python3 run.py --reindex
```

---

## 📊 What's Included

After installation, you'll have access to:
- **2,053 n8n workflows** with intelligent naming
- **365 unique integrations** automatically categorized
- **Lightning-fast search** with SQLite FTS5
- **Modern web interface** with dark/light themes
- **REST API** with automatic documentation
- **Multiple deployment options** (Python, Docker, Kubernetes)
- **Health monitoring** and performance metrics
- **Production-ready** configuration

---

*🎯 Perfect for developers, automation engineers, and anyone looking to explore the world of n8n workflows with professional tooling.*