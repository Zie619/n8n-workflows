# Security Policy

## Reporting Security Vulnerabilities

If you discover a security vulnerability in this project, please report it responsibly by emailing the maintainers directly. Do not create public issues for security vulnerabilities.

## Security Fixes Applied (November 2025)

### 1. Path Traversal Vulnerability (Fixed)
**Issue #48**: Previously, the API server was vulnerable to path traversal attacks on Windows systems.

**Fix Applied**:
- Added comprehensive filename validation with `validate_filename()` function
- Blocks all path traversal patterns including:
  - Parent directory references (`..`, `../`, `..\\`)
  - URL-encoded traversal attempts (`..%5c`, `..%2f`)
  - Absolute paths and drive letters
  - Shell special characters and wildcards
- Uses `Path.resolve()` and `relative_to()` for defense in depth
- Applied to all file-access endpoints:
  - `/api/workflows/{filename}`
  - `/api/workflows/{filename}/download`
  - `/api/workflows/{filename}/diagram`

### 2. CORS Misconfiguration (Fixed)
**Previously**: CORS was configured with `allow_origins=["*"]`, allowing any website to access the API.

**Fix Applied**:
- Restricted CORS origins to specific allowed domains:
  - Local development ports (3000, 8000, 8080)
  - GitHub Pages (`https://zie619.github.io`)
  - Community deployment (`https://n8n-workflows-1-xxgm.onrender.com`)
- Restricted allowed methods to only `GET` and `POST`
- Restricted allowed headers to `Content-Type` and `Authorization`

### 3. Unauthenticated Reindex Endpoint (Fixed)
**Previously**: The `/api/reindex` endpoint could be called by anyone, potentially causing DoS.

**Fix Applied**:
- Added authentication requirement via `admin_token` query parameter
- Token must match `ADMIN_TOKEN` environment variable
- If no token is configured, the endpoint is disabled
- Added rate limiting to prevent abuse
- Logs all reindex attempts with client IP

### 4. Rate Limiting (Added)
**New Security Feature**:
- Implemented rate limiting (60 requests per minute per IP)
- Applied to all sensitive endpoints
- Prevents brute force and DoS attacks
- Returns HTTP 429 when limit exceeded

## Security Configuration

### Environment Variables
```bash
# Required for reindex endpoint
export ADMIN_TOKEN="your-secure-random-token"

# Optional: Configure rate limiting (default: 60)
# MAX_REQUESTS_PER_MINUTE=60
```

### CORS Configuration
To add additional allowed origins, modify the `ALLOWED_ORIGINS` list in `api_server.py`:

```python
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "https://your-domain.com",  # Add your production domain
]
```

## Security Best Practices

1. **Environment Variables**: Never commit sensitive tokens or credentials to the repository
2. **HTTPS Only**: Always use HTTPS in production (HTTP is only for local development)
3. **Regular Updates**: Keep all dependencies updated to patch known vulnerabilities
4. **Monitoring**: Monitor logs for suspicious activity patterns
5. **Backup**: Regular backups of the workflows database

## Security Checklist for Deployment

- [ ] Set strong `ADMIN_TOKEN` environment variable
- [ ] Configure CORS origins for your specific domain
- [ ] Use HTTPS with valid SSL certificate
- [ ] Enable firewall rules to restrict access
- [ ] Set up monitoring and alerting
- [ ] Review and rotate admin tokens regularly
- [ ] Keep Python and all dependencies updated
- [ ] Use a reverse proxy (nginx/Apache) with additional security headers

## Additional Security Headers (Recommended)

When deploying behind a reverse proxy, add these headers:

```nginx
add_header X-Frame-Options "SAMEORIGIN";
add_header X-Content-Type-Options "nosniff";
add_header X-XSS-Protection "1; mode=block";
add_header Content-Security-Policy "default-src 'self'";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
```

## Vulnerability Disclosure Timeline

| Date | Issue | Status | Fixed Version |
|------|-------|--------|---------------|
| Oct 2025 | Path Traversal (#48) | Fixed | 2.0.1 |
| Nov 2025 | CORS Misconfiguration | Fixed | 2.0.1 |
| Nov 2025 | Unauthenticated Reindex | Fixed | 2.0.1 |

## Credits

Security issues reported by:
- Path Traversal: Community contributor via Issue #48

## Contact

For security concerns, please contact the maintainers privately.