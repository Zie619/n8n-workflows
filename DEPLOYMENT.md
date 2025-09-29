# N8N Workflows Documentation - Deployment Guide

This guide provides comprehensive instructions for deploying the N8N Workflows Documentation system in various environments.

## 🚀 Quick Start

### Prerequisites
- **Docker** (for containerized deployment)
- **Python 3.11+** (for direct deployment)
- **Node.js 16+** (for Node.js alternative)
- **kubectl** (for Kubernetes deployment)

### 1-Minute Docker Deployment
```bash
# Clone the repository
git clone <repository-url>
cd n8n-workflows-1

# Start with Docker Compose
docker-compose up -d

# Access the application
open http://localhost:8000
```

## 📋 Deployment Methods

### Method 1: Direct Python Deployment (Development)

**Best for:** Development, testing, and local usage

```bash
# Install dependencies
pip install -r requirements.txt

# Start development server
./scripts/deploy-dev.sh
# or manually:
python run.py --host 127.0.0.1 --port 8000 --dev
```

**Features:**
- ✅ Auto-reload on code changes
- ✅ Debug mode enabled
- ✅ Local access only
- ✅ Fast startup

### Method 2: Docker Deployment (Recommended)

**Best for:** Production, staging, and consistent environments

#### Simple Docker Run
```bash
docker build -t workflows-doc:latest .
docker run -p 8000:8000 -v $(pwd)/database:/app/database workflows-doc:latest
```

#### Docker Compose (Recommended)
```bash
# Basic deployment
docker-compose up -d

# Production deployment with nginx
docker-compose --profile production up -d
```

**Features:**
- ✅ Production-ready
- ✅ Persistent data storage
- ✅ Health checks
- ✅ Auto-restart
- ✅ Nginx reverse proxy (optional)

### Method 3: Kubernetes Deployment (Enterprise)

**Best for:** High availability, scalability, and enterprise environments

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml

# Check deployment status
kubectl rollout status deployment/n8n-workflows-doc

# Get service URL
kubectl get ingress n8n-workflows-ingress
```

**Features:**
- ✅ High availability (2+ replicas)
- ✅ Auto-scaling
- ✅ Load balancing
- ✅ Rolling updates
- ✅ Persistent storage

### Method 4: Cloud Deployment

#### Heroku
```bash
# Install Heroku CLI and login
heroku create your-app-name
heroku config:set ENVIRONMENT=production
git push heroku main
```

#### Railway
```bash
# Connect to Railway
railway login
railway init
railway up
```

#### DigitalOcean App Platform
Deploy directly from GitHub repository with these settings:
- **Runtime:** Docker
- **Port:** 8000
- **Health Check:** /health

## 🔧 Configuration

### Environment Variables

Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```

Key configurations:
```env
ENVIRONMENT=production
HOST=0.0.0.0
PORT=8000
DATABASE_PATH=database/workflows.db
LOG_LEVEL=INFO
```

### Production Settings
```env
ENVIRONMENT=production
HOST=0.0.0.0
PORT=8000
UVICORN_WORKERS=4
UVICORN_RELOAD=false
RATE_LIMIT_ENABLED=true
```

## 🚦 Health Checks & Monitoring

### Health Check Endpoint
```bash
curl http://localhost:8000/health
```

Response:
```json
{
  "status": "healthy",
  "message": "N8N Workflow API is running"
}
```

### Monitoring Endpoints
- **Health:** `/health`
- **Metrics:** `/api/stats`
- **API Docs:** `/docs`
- **OpenAPI:** `/openapi.json`

### Logging
Logs are available via:
```bash
# Docker
docker-compose logs -f

# Kubernetes
kubectl logs -f deployment/n8n-workflows-doc

# Direct deployment
tail -f application.log
```

## 🔒 Security Considerations

### Production Security Checklist
- [ ] **SSL/TLS enabled** (use nginx or load balancer)
- [ ] **Rate limiting configured**
- [ ] **CORS settings restricted**
- [ ] **Security headers enabled**
- [ ] **Regular security updates**
- [ ] **Backup strategy implemented**

### SSL/TLS Setup
For production deployments, enable SSL/TLS:

1. **With Nginx (Recommended)**
```nginx
server {
    listen 443 ssl http2;
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

2. **With Let's Encrypt**
```bash
certbot --nginx -d yourdomain.com
```

## 📊 Performance Optimization

### Recommended Production Settings

#### Docker Compose
```yaml
services:
  workflows-doc:
    deploy:
      replicas: 2
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M
```

#### Kubernetes
```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

### Database Optimization
- Enable SQLite WAL mode for better concurrent access
- Regular database vacuum for performance
- Consider read replicas for high load

## 🔄 CI/CD Pipeline

### GitHub Actions
The repository includes a complete CI/CD pipeline:

```yaml
# .github/workflows/deploy.yml
- Build and test on pull requests
- Docker image building and pushing
- Automated deployments to staging/production
- Security scanning with Trivy
```

### Manual Deployment Commands
```bash
# Development
./scripts/deploy-dev.sh

# Production (Docker)
./scripts/deploy-prod.sh docker

# Production (Kubernetes)
./scripts/deploy-prod.sh kubernetes
```

## 🆘 Troubleshooting

### Common Issues

#### 1. Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000
# Kill the process
kill -9 <PID>
```

#### 2. Docker Build Failures
```bash
# Clean Docker cache
docker system prune -a
# Rebuild with no cache
docker build --no-cache -t workflows-doc:latest .
```

#### 3. Database Issues
```bash
# Reindex workflows
python run.py --reindex
# Check database integrity
sqlite3 database/workflows.db "PRAGMA integrity_check;"
```

#### 4. SSL Certificate Issues in Docker
If you encounter SSL certificate verification errors:
```dockerfile
# Add to Dockerfile
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### Performance Issues
1. **Slow startup:** Increase `--reindex` timeout
2. **High memory usage:** Reduce batch size in indexing
3. **Slow queries:** Add database indexes

### Getting Help
1. **Check logs:** Application logs contain detailed error information
2. **Health endpoint:** Use `/health` to verify service status
3. **API documentation:** Access `/docs` for API reference
4. **Database stats:** Use `/api/stats` for database information

## 📋 Deployment Checklist

### Pre-deployment
- [ ] Requirements installed
- [ ] Configuration files prepared
- [ ] Database directory exists
- [ ] Port 8000 available
- [ ] SSL certificates (production)

### Post-deployment
- [ ] Health check passes
- [ ] API documentation accessible
- [ ] Workflows indexed successfully
- [ ] Performance monitoring enabled
- [ ] Backup strategy configured
- [ ] Security scan completed

## 🔗 Additional Resources

- **API Documentation:** Available at `/docs` when running
- **Workflow Templates:** Located in `workflows/` directory
- **Configuration Guide:** See `.env.example`
- **Security Guide:** Check `k8s/` directory for security policies
- **Performance Tuning:** Review Docker and Kubernetes resource limits

---

For more specific deployment scenarios or issues, please check the documentation in the `Documentation/` directory or create an issue in the repository.