# N8N Workflows Documentation Platform - Deployment Guide

This guide covers deploying the N8N Workflows Documentation Platform in various environments.

## Quick Start (Docker)

### Development Environment
```bash
# Clone repository
git clone <repository-url>
cd n8n-workflows-1

# Start development environment
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

### Production Environment
```bash
# Production deployment
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

# With monitoring
docker compose --profile monitoring up -d
```

## Deployment Options

### 1. Docker Compose (Recommended)

#### Development
```bash
# Start development environment with auto-reload
docker compose -f docker-compose.yml -f docker-compose.dev.yml up

# With additional dev tools (DB admin, file watcher)
docker compose --profile dev-tools up
```

#### Production
```bash
# Basic production deployment
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# With reverse proxy and SSL
docker compose --profile production up -d

# With monitoring stack
docker compose --profile monitoring up -d
```

### 2. Standalone Docker

```bash
# Build image
docker build -t workflows-doc:latest .

# Run container
docker run -d \
  --name n8n-workflows-docs \
  -p 8000:8000 \
  -v $(pwd)/database:/app/database \
  -v $(pwd)/logs:/app/logs \
  -e ENVIRONMENT=production \
  workflows-doc:latest
```

### 3. Python Direct Deployment

#### Prerequisites
- Python 3.11+
- pip

#### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Development mode
python run.py --dev

# Production mode
python run.py --host 0.0.0.0 --port 8000
```

#### Production with Gunicorn
```bash
# Install gunicorn
pip install gunicorn

# Start with gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 api_server:app
```

### 4. Kubernetes Deployment

#### Basic Deployment
```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/ingress.yaml
```

#### Helm Chart
```bash
# Install with Helm
helm install n8n-workflows-docs ./helm/workflows-docs
```

## Environment Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `ENVIRONMENT` | Deployment environment | `development` | No |
| `LOG_LEVEL` | Logging level | `info` | No |
| `HOST` | Bind host | `127.0.0.1` | No |
| `PORT` | Bind port | `8000` | No |
| `DATABASE_PATH` | SQLite database path | `database/workflows.db` | No |
| `WORKFLOWS_PATH` | Workflows directory | `workflows` | No |
| `ENABLE_METRICS` | Enable Prometheus metrics | `false` | No |
| `MAX_WORKERS` | Max worker processes | `1` | No |
| `DEBUG` | Enable debug mode | `false` | No |
| `RELOAD` | Enable auto-reload | `false` | No |

### Configuration Files

Create environment-specific configuration:

#### `.env` (Development)
```bash
ENVIRONMENT=development
LOG_LEVEL=debug
DEBUG=true
RELOAD=true
```

#### `.env.production` (Production)
```bash
ENVIRONMENT=production
LOG_LEVEL=warning
ENABLE_METRICS=true
MAX_WORKERS=4
```

## Security Configuration

### 1. Reverse Proxy Setup (Traefik)

```yaml
# traefik/config/dynamic.yml
http:
  middlewares:
    auth:
      basicAuth:
        users:
          - "admin:$2y$10$..."  # Generate with htpasswd
    security-headers:
      headers:
        customRequestHeaders:
          X-Forwarded-Proto: "https"
        customResponseHeaders:
          X-Frame-Options: "DENY"
          X-Content-Type-Options: "nosniff"
        sslRedirect: true
```

### 2. SSL/TLS Configuration

#### Let's Encrypt (Automatic)
```yaml
# In docker-compose.prod.yml
command:
  - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
  - "--certificatesresolvers.myresolver.acme.email=admin@yourdomain.com"
```

#### Custom SSL Certificate
```yaml
volumes:
  - ./ssl:/ssl:ro
```

### 3. Basic Authentication

```bash
# Generate htpasswd entry
htpasswd -nb admin yourpassword

# Add to Traefik labels
- "traefik.http.middlewares.auth.basicauth.users=admin:$$2y$$10$$..."
```

## Performance Optimization

### 1. Resource Limits

```yaml
# docker-compose.prod.yml
deploy:
  resources:
    limits:
      memory: 512M
      cpus: '0.5'
    reservations:
      memory: 256M
      cpus: '0.25'
```

### 2. Database Optimization

```bash
# Force reindex for better performance
python run.py --reindex

# Or via API
curl -X POST http://localhost:8000/api/reindex
```

### 3. Caching Headers

```yaml
# Traefik middleware for static files
http:
  middlewares:
    cache-headers:
      headers:
        customResponseHeaders:
          Cache-Control: "public, max-age=31536000"
```

## Monitoring & Logging

### 1. Health Checks

```bash
# Docker health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/stats || exit 1

# Manual health check
curl http://localhost:8000/api/stats
```

### 2. Logs

```bash
# View application logs
docker compose logs -f workflows-docs

# View specific service logs
docker logs n8n-workflows-docs

# Log location in container
/app/logs/app.log
```

### 3. Metrics (Prometheus)

```bash
# Start monitoring stack
docker compose --profile monitoring up -d

# Access Prometheus
http://localhost:9090
```

## Backup & Recovery

### 1. Database Backup

```bash
# Backup SQLite database
cp database/workflows.db database/workflows.db.backup

# Or using docker
docker exec n8n-workflows-docs cp /app/database/workflows.db /app/database/workflows.db.backup
```

### 2. Configuration Backup

```bash
# Backup entire configuration
tar -czf n8n-workflows-backup-$(date +%Y%m%d).tar.gz \
  database/ \
  logs/ \
  docker-compose*.yml \
  .env*
```

### 3. Restore

```bash
# Stop services
docker compose down

# Restore database
cp database/workflows.db.backup database/workflows.db

# Start services
docker compose up -d
```

## Scaling & Load Balancing

### 1. Multiple Instances

```yaml
# docker-compose.scale.yml
services:
  workflows-docs:
    deploy:
      replicas: 3
```

```bash
# Scale up
docker compose up --scale workflows-docs=3
```

### 2. Load Balancer Configuration

```yaml
# Traefik load balancing
labels:
  - "traefik.http.services.workflows-docs.loadbalancer.server.port=8000"
  - "traefik.http.services.workflows-docs.loadbalancer.sticky=true"
```

## Troubleshooting

### Common Issues

1. **Database locked error**
   ```bash
   # Check file permissions
   ls -la database/
   
   # Fix permissions
   chmod 664 database/workflows.db
   ```

2. **Port already in use**
   ```bash
   # Check what's using the port
   lsof -i :8000
   
   # Use different port
   docker compose up -d -p 8001:8000
   ```

3. **Out of memory**
   ```bash
   # Check memory usage
   docker stats
   
   # Increase memory limit
   # Edit docker-compose.prod.yml resources
   ```

### Logs & Debugging

```bash
# Application logs
docker compose logs -f workflows-docs

# System logs
docker exec workflows-docs tail -f /app/logs/app.log

# Database logs
docker exec workflows-docs sqlite3 /app/database/workflows.db ".tables"
```

## Migration & Updates

### 1. Update Application

```bash
# Pull latest changes
git pull origin main

# Rebuild and restart
docker compose down
docker compose up -d --build
```

### 2. Database Migration

```bash
# Backup current database
cp database/workflows.db database/workflows.db.backup

# Force reindex with new schema
python run.py --reindex
```

### 3. Zero-downtime Updates

```bash
# Blue-green deployment
docker compose -p n8n-workflows-green up -d --build

# Switch traffic (update load balancer)
# Verify new deployment
# Shut down old deployment
docker compose -p n8n-workflows-blue down
```

## Security Checklist

- [ ] Use non-root user in Docker container
- [ ] Enable HTTPS/SSL in production
- [ ] Configure proper firewall rules
- [ ] Use strong authentication credentials
- [ ] Regular security updates
- [ ] Enable access logs and monitoring
- [ ] Backup sensitive data securely
- [ ] Review and audit configurations regularly

## Support & Maintenance

### Regular Tasks

1. **Daily**
   - Monitor application health
   - Check error logs
   - Verify backup completion

2. **Weekly**
   - Review performance metrics
   - Update dependencies if needed
   - Test disaster recovery procedures

3. **Monthly**
   - Security audit
   - Database optimization
   - Update documentation