# 安全策略

## 报告安全漏洞

如果您在本项目中发现安全漏洞，请负责任地直接通过电子邮件向维护者报告。不要为安全漏洞创建公共问题。

## 已应用的安全修复（2025年11月）

### 1. 路径遍历漏洞（已修复）
**问题 #48**：以前，API服务器在Windows系统上容易受到路径遍历攻击。

**已应用的修复**：
- 添加了带有`validate_filename()`函数的全面文件名验证
- 阻止所有路径遍历模式，包括：
  - 父目录引用 (`..`, `../`, `..\`)
  - URL编码的遍历尝试 (`..%5c`, `..%2f`)
  - 绝对路径和驱动器号
  - Shell特殊字符和通配符
- 使用`Path.resolve()`和`relative_to()`进行深度防御
- 应用于所有文件访问端点：
  - `/api/workflows/{filename}`
  - `/api/workflows/{filename}/download`
  - `/api/workflows/{filename}/diagram`

### 2. CORS配置错误（已修复）
**以前**：CORS配置为`allow_origins=["*"]`，允许任何网站访问API。

**已应用的修复**：
- 将CORS源限制为特定允许的域名：
  - 本地开发端口（3000、8000、8080）
  - GitHub Pages (`https://zie619.github.io`)
  - 社区部署 (`https://n8n-workflows-1-xxgm.onrender.com`)
- 将允许的方法限制为仅`GET`和`POST`
- 将允许的头限制为`Content-Type`和`Authorization`

### 3. 未认证的重新索引端点（已修复）
**以前**：任何人都可以调用`/api/reindex`端点，可能导致拒绝服务攻击（DoS）。

**已应用的修复**：
- 通过`admin_token`查询参数添加了认证要求
- 令牌必须与`ADMIN_TOKEN`环境变量匹配
- 如果未配置令牌，端点将被禁用
- 添加了速率限制以防止滥用
- 记录所有带有客户端IP的重新索引尝试

### 4. 速率限制（已添加）
**新安全功能**：
- 实现了速率限制（每分钟每IP 60个请求）
- 应用于所有敏感端点
- 防止暴力破解和拒绝服务攻击
- 当超过限制时返回HTTP 429

## 安全配置

### 环境变量
```bash
# 重新索引端点必需
export ADMIN_TOKEN="your-secure-random-token"

# 可选：配置速率限制（默认：60）
# MAX_REQUESTS_PER_MINUTE=60
```

### CORS配置
要添加额外的允许源，请修改`api_server.py`中的`ALLOWED_ORIGINS`列表：

```python
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://your-domain.com",  # 添加您的生产域名
]
```

## 安全最佳实践

1. **环境变量**：永远不要将敏感令牌或凭据提交到仓库
2. **仅使用 HTTPS**：在生产环境中始终使用 HTTPS（HTTP 仅用于本地开发）
3. **定期更新**：保持所有依赖项更新以修补已知漏洞
4. **监控**：监控日志中的可疑活动模式
5. **备份**：定期备份工作流数据库

## 部署安全检查清单

- [ ] 设置强大的`ADMIN_TOKEN`环境变量
- [ ] 为您的特定域配置CORS源
- [ ] 使用有效的SSL证书启用HTTPS
- [ ] 启用防火墙规则以限制访问
- [ ] 设置监控和告警
- [ ] 定期审查和轮换管理员令牌
- [ ] 保持Python和所有依赖项更新
- [ ] 使用反向代理（nginx/Apache）并添加额外的安全头

## 推荐的额外安全头

在反向代理后面部署时，请添加以下头信息：

```nginx
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
add_header X-XSS-Protection "1; mode=block";
add_header Content-Security-Policy "default-src 'self'";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
```

## 漏洞披露时间线

| Date | Issue | Status | Fixed Version |
|------|-------|--------|---------------|
| Oct 2025 | Path Traversal (#48) | Fixed | 2.0.1 |
| Nov 2025 | CORS Misconfiguration | Fixed | 2.0.1 |
| Nov 2025 | Unauthenticated Reindex | Fixed | 2.0.1 |

## 致谢

安全问题报告者：
- Path Traversal: 社区贡献者通过Issue #48

## 联系信息

如有安全问题，请私下联系维护者。