# N8N 工作流文档平台 - 部署指南

本指南介绍了在各种环境中部署 N8N 工作流文档平台的方法。

## 快速开始（Docker）

### 开发环境
```bash
# 克隆仓库
git clone <repository-url>
cd n8n-workflows-1

# 启动开发环境
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

### 生产环境
```bash
# 生产部署
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

# 带有监控功能
docker compose --profile monitoring up -d
```

## 部署选项

### 1. Docker Compose（推荐）

#### 开发环境
```bash
# 启动带有自动重载功能的开发环境
docker compose -f docker-compose.yml -f docker-compose.dev.yml up

# 使用额外的开发工具（数据库管理、文件监控器）
docker compose --profile dev-tools up
```

#### 生产环境
```bash
# 基础生产部署
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# 带有反向代理和SSL
docker compose --profile production up -d

# 带有监控栈
docker compose --profile monitoring up -d
```

### 2. 独立Docker

```bash
# 构建镜像
docker build -t workflows-doc:latest .

# 运行容器
docker run -d \
  --name n8n-workflows-docs \
  -p 8000:8000 \
  -v $(pwd)/database:/app/database \
  -v $(pwd)/logs:/app/logs \
  -e ENVIRONMENT=production \
  workflows-doc:latest
```

### 3. Python直接部署

#### 先决条件
- Python 3.11+
- pip

#### 安装
```bash
# 安装依赖
pip install -r requirements.txt

# 开发模式
python run.py --dev

# 生产模式
python run.py --host 0.0.0.0 --port 8000
```

#### 使用Gunicorn的生产环境
```bash
# 安装gunicorn
pip install gunicorn

# 使用gunicorn启动
gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 api_server:app
```

### 4. Kubernetes部署

#### 基础部署
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

## 环境配置

### 环境变量

| 变量 | 描述 | 默认值 | 是否必需 |
|----------|-------------|---------|----------|
| `ENVIRONMENT` | 部署环境 | `development` | 否 |
| `LOG_LEVEL` | 日志级别 | `info` | 否 |
| `HOST` | 绑定主机 | `127.0.0.1` | 否 |
| `PORT` | 绑定端口 | `8000` | 否 |
| `DATABASE_PATH` | SQLite数据库路径 | `database/workflows.db` | 否 |
| `WORKFLOWS_PATH` | 工作流目录 | `workflows` | 否 |
| `ENABLE_METRICS` | 启用Prometheus指标 | `false` | 否 |
| `MAX_WORKERS` | 最大工作进程数 | `1` | 否 |
| `DEBUG` | 启用调试模式 | `false` | 否 |
| `RELOAD` | 启用自动重载 | `false` | 否 |

### 配置文件

创建特定环境的配置：

#### `.env`（开发环境）
```bash
ENVIRONMENT=development
LOG_LEVEL=debug
DEBUG=true
RELOAD=true
```

#### `.env.production`（生产环境）
```bash
ENVIRONMENT=production
LOG_LEVEL=warning
ENABLE_METRICS=true
MAX_WORKERS=4
```

## 安全配置

### 1. 反向代理设置（Traefik）

```yaml
# traefik/config/dynamic.yml
http:
  middlewares:
    auth:
      basicAuth:
        users:
          - "admin:$2y$10$..."  # 使用htpasswd生成
    security-headers:
      headers:
        customRequestHeaders:
          X-Forwarded-Proto: "https"
        customResponseHeaders:
          X-Frame-Options: "DENY"
          X-Content-Type-Options: "nosniff"
        sslRedirect: true
```

### 2. SSL/TLS配置

#### Let's Encrypt（自动）
```yaml
# 在docker-compose.prod.yml中
command:
  - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
  - "--certificatesresolvers.myresolver.acme.email=admin@yourdomain.com"
```

#### 自定义SSL证书
```yaml
volumes:
  - ./ssl:/ssl:ro
```

### 3. 基本认证

```bash
# 生成htpasswd条目
htpasswd -nb admin yourpassword

# 添加到Traefik标签
- "traefik.http.middlewares.auth.basicauth.users=admin:$$2y$$10$$..."
```

## 性能优化

### 1. 资源限制

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

### 2. 数据库优化

```bash
# 强制重新索引以提高性能
python run.py --reindex

# 或通过API
curl -X POST http://localhost:8000/api/reindex
```

### 3. 缓存头

```yaml
# Traefik静态文件中间件
http:
  middlewares:
    cache-headers:
      headers:
        customResponseHeaders:
          Cache-Control: "public, max-age=31536000"
```

## 监控与日志

### 1. 健康检查

```bash
# Docker health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/stats || exit 1

# Manual health check
curl http://localhost:8000/api/stats
```

### 2. 日志

```bash
# View application logs
docker compose logs -f workflows-docs

# View specific service logs
docker logs n8n-workflows-docs

# Log location in container
/app/logs/app.log
```

### 3. 指标（Prometheus）

```bash
# Start monitoring stack
docker compose --profile monitoring up -d

# Access Prometheus
http://localhost:9090
```

## 备份与恢复

### 1. 数据库备份

```bash
# Backup SQLite database
cp database/workflows.db database/workflows.db.backup

# Or using docker
docker exec n8n-workflows-docs cp /app/database/workflows.db /app/database/workflows.db.backup
```

### 2. 配置备份

```bash
# Backup entire configuration
tar -czf n8n-workflows-backup-$(date +%Y%m%d).tar.gz \
  database/ \
  logs/ \
  docker-compose*.yml \
  .env*
```

### 3. 恢复

```bash
# Stop services
docker compose down

# Restore database
cp database/workflows.db.backup database/workflows.db

# Start services
docker compose up -d
```

## 扩展与负载均衡

### 1. 多实例部署

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

### 2. 负载均衡器配置

```yaml
# Traefik load balancing
labels:
  - "traefik.http.services.workflows-docs.loadbalancer.server.port=8000"
  - "traefik.http.services.workflows-docs.loadbalancer.sticky=true"
```

## 故障排除

### 常见问题

1. **数据库锁定错误**
   ```bash
   # Check file permissions
   ls -la database/
   
   # Fix permissions
   chmod 664 database/workflows.db
   ```

2. **端口已被占用**
   ```bash
   # Check what's using the port
   lsof -i :8000
   
   # Use different port
   docker compose up -d -p 8001:8000
   ```

3. **内存不足**
   ```bash
   # Check memory usage
   docker stats
   
   # Increase memory limit
   # Edit docker-compose.prod.yml resources
   ```

### 日志与调试

```bash
# Application logs
docker compose logs -f workflows-docs

# System logs
docker exec workflows-docs tail -f /app/logs/app.log

# Database logs
docker exec workflows-docs sqlite3 /app/database/workflows.db ".tables"
```

## 迁移与更新

### 1. 更新应用

```bash
# Pull latest changes
git pull origin main

# Rebuild and restart
docker compose down
docker compose up -d --build
```

### 2. 数据库迁移

```bash
# Backup current database
cp database/workflows.db database/workflows.db.backup

# Force reindex with new schema
python run.py --reindex
```

### 3. 零停机更新

```bash
# Blue-green deployment
docker compose -p n8n-workflows-green up -d --build

# Switch traffic (update load balancer)
# Verify new deployment
# Shut down old deployment
docker compose -p n8n-workflows-blue down
```

## 安全检查清单

- [ ] 在Docker容器中使用非root用户
- [ ] 在生产环境中启用HTTPS/SSL
- [ ] 配置适当的防火墙规则
- [ ] 使用强认证凭据
- [ ] 定期进行安全更新
- [ ] 启用访问日志和监控
- [ ] 安全备份敏感数据
- [ ] 定期审查和审计配置

## 支持与维护

### 常规任务

1. **每日**
   - Monitor application health
   - Check error logs
   - Verify backup completion

2. **每周**
   - Review performance metrics
   - Update dependencies if needed
   - Test disaster recovery procedures

3. **每月**
   - Security audit
   - Database optimization
   - Update documentation