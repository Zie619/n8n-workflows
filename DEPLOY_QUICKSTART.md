# 🚀 Deployment Quick Start Guide

This guide provides rapid deployment instructions for the N8N Workflows Documentation Platform.

## 🐳 Docker Deployment (Recommended)

### Option 1: One-Click Docker Deployment

```bash
# Quick start - builds and runs everything
./run-as-docker-container.sh
```

**What this does:**
- Builds the Docker image
- Starts the application with Docker Compose
- Performs health checks
- Opens browser automatically
- Accessible at: http://localhost:8000

### Option 2: Manual Docker Compose

```bash
# Development environment
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

# Production environment
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

### Option 3: Using Deployment Script

```bash
# Deploy to development
./scripts/deploy.sh development

# Deploy to production
./scripts/deploy.sh production

# Check health
./scripts/health-check.sh

# Create backup
./scripts/backup.sh
```

## 🖥️ Local Python Deployment

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start development server
python run.py

# Start production server
python run.py --host 0.0.0.0 --port 8000
```

### With Environment Configuration

```bash
# Copy environment template
cp .env.development .env

# Edit configuration as needed
# vim .env

# Start with environment file
python run.py --dev
```

## ☸️ Kubernetes Deployment

### Using kubectl

```bash
# Apply all manifests
kubectl apply -f k8s/

# Check status
kubectl get pods -n n8n-workflows
kubectl get services -n n8n-workflows
```

### Using Helm

```bash
# Install with Helm
helm install workflows-docs ./helm/workflows-docs --namespace n8n-workflows --create-namespace

# Upgrade deployment
helm upgrade workflows-docs ./helm/workflows-docs

# Uninstall
helm uninstall workflows-docs --namespace n8n-workflows
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ENVIRONMENT` | Deployment environment | `development` |
| `HOST` | Server host | `127.0.0.1` |
| `PORT` | Server port | `8000` |
| `LOG_LEVEL` | Logging level | `info` |

### Environment Files

- `.env.development` - Development configuration
- `.env.staging` - Staging configuration  
- `.env.production` - Production configuration

## 📊 Health Checks

```bash
# Quick health check
curl http://localhost:8000/api/stats

# Detailed health check with script
./scripts/health-check.sh http://localhost:8000
```

## 🔍 Access Points

Once deployed, access the application at:

- **Main Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **API Stats**: http://localhost:8000/api/stats
- **Health Check**: http://localhost:8000/api/stats

## 🛠️ Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Use different port
   docker compose up -p 8001:8000
   ```

2. **Database issues**
   ```bash
   # Force reindex
   python run.py --reindex
   ```

3. **Docker build fails**
   ```bash
   # Clean build
   docker system prune -f
   docker compose build --no-cache
   ```

### View Logs

```bash
# Docker logs
docker compose logs -f

# Application logs
tail -f logs/app.log
```

## 📚 Full Documentation

For complete deployment documentation, see:
- [DEPLOYMENT.md](./DEPLOYMENT.md) - Comprehensive deployment guide
- [README.md](./README.md) - Application overview and features

## 🆘 Quick Help

```bash
# Show deployment script help
./scripts/deploy.sh --help

# Show Python application help
python run.py --help

# Show health check help
./scripts/health-check.sh --help
```