# Guía Completa de Deployment con Heroku CLI

Esta guía te llevará paso a paso para desplegar el workflow de automatización de memes usando únicamente la línea de comandos de Heroku.

## 📋 Prerequisitos

### 1. Instalar Heroku CLI

**macOS:**
```bash
brew tap heroku/brew && brew install heroku
```

**Ubuntu/Debian:**
```bash
curl https://cli-assets.heroku.com/install-ubuntu.sh | sh
```

**Windows:**
Descarga e instala desde: https://devcenter.heroku.com/articles/heroku-cli

**Verificar instalación:**
```bash
heroku --version
# Debe mostrar: heroku/8.x.x
```

### 2. Login a Heroku

```bash
# Abrir login en navegador
heroku login

# O usar token (para CI/CD)
heroku login -i
# Ingresa: email y password
```

### 3. Verificar Login

```bash
heroku auth:whoami
# Debe mostrar tu email
```

## 🚀 Deployment Paso a Paso

### Paso 1: Crear Aplicación en Heroku

```bash
# Crear app con nombre único
heroku create your-meme-bot-n8n

# O dejar que Heroku genere un nombre
heroku create

# Verificar creación
heroku apps:info -a your-meme-bot-n8n
```

**Resultado esperado:**
```
=== your-meme-bot-n8n
Addons:        
Auto Cert Mgmt: false
Dynos:         
Git URL:       https://git.heroku.com/your-meme-bot-n8n.git
Owner:         your-email@example.com
Region:        us
Repo Size:     0 B
Slug Size:     0 B
Stack:         heroku-22
Web URL:       https://your-meme-bot-n8n.herokuapp.com/
```

### Paso 2: Agregar PostgreSQL

```bash
# Para Eco Dyno, agregar Mini plan (incluido gratis)
heroku addons:create heroku-postgresql:mini -a your-meme-bot-n8n

# Verificar que se agregó
heroku addons -a your-meme-bot-n8n

# Ver información de la base de datos
heroku pg:info -a your-meme-bot-n8n
```

**Resultado esperado:**
```
=== postgresql-xxxxx-xxxxx
Plan:        Mini
Status:      Available
Connections: 0/20
PG Version:  15.x
Created:     2024-10-30 17:00 UTC
Data Size:   8.6 MB/1 GB
Tables:      0
Fork/Follow: Unsupported
```

### Paso 3: Configurar Variables de Entorno

```bash
# ImgFlip API (obligatorio)
heroku config:set IMGFLIP_USERNAME=tu_usuario_imgflip -a your-meme-bot-n8n
heroku config:set IMGFLIP_PASSWORD=tu_password_imgflip -a your-meme-bot-n8n

# Instagram API (obligatorio)
heroku config:set INSTAGRAM_USER_ID=tu_instagram_business_id -a your-meme-bot-n8n
heroku config:set INSTAGRAM_ACCESS_TOKEN=tu_token_largo_instagram -a your-meme-bot-n8n

# n8n Configuración (obligatorio)
heroku config:set N8N_BASIC_AUTH_ACTIVE=true -a your-meme-bot-n8n
heroku config:set N8N_BASIC_AUTH_USER=admin -a your-meme-bot-n8n
heroku config:set N8N_BASIC_AUTH_PASSWORD=tu_password_seguro -a your-meme-bot-n8n

# n8n URLs (obligatorio - reemplaza con tu app name)
heroku config:set N8N_HOST=your-meme-bot-n8n.herokuapp.com -a your-meme-bot-n8n
heroku config:set N8N_PORT=443 -a your-meme-bot-n8n
heroku config:set N8N_PROTOCOL=https -a your-meme-bot-n8n
heroku config:set WEBHOOK_URL=https://your-meme-bot-n8n.herokuapp.com/ -a your-meme-bot-n8n

# Optimizaciones para Eco Dyno (recomendado)
heroku config:set N8N_PAYLOAD_SIZE_MAX=16 -a your-meme-bot-n8n
heroku config:set EXECUTIONS_DATA_SAVE_ON_ERROR=none -a your-meme-bot-n8n
heroku config:set EXECUTIONS_DATA_SAVE_ON_SUCCESS=none -a your-meme-bot-n8n
heroku config:set EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false -a your-meme-bot-n8n

# Timezone (opcional)
heroku config:set GENERIC_TIMEZONE=America/New_York -a your-meme-bot-n8n

# Verificar todas las variables
heroku config -a your-meme-bot-n8n
```

**Tip: Configurar múltiples variables a la vez**
```bash
heroku config:set \
  IMGFLIP_USERNAME=tu_usuario \
  IMGFLIP_PASSWORD=tu_password \
  INSTAGRAM_USER_ID=tu_id \
  INSTAGRAM_ACCESS_TOKEN=tu_token \
  -a your-meme-bot-n8n
```

### Paso 4: Desplegar n8n en Heroku

#### Opción A: Usando Buildpack de n8n (Recomendado)

```bash
# Clonar template de n8n para Heroku
git clone https://github.com/n8n-io/n8n-heroku.git
cd n8n-heroku

# Conectar a tu app de Heroku
heroku git:remote -a your-meme-bot-n8n

# Desplegar
git push heroku main

# Escalar dyno a Eco
heroku ps:scale web=1:eco -a your-meme-bot-n8n
```

#### Opción B: Crear desde cero

```bash
# Crear directorio
mkdir n8n-heroku && cd n8n-heroku
git init

# Crear package.json
cat > package.json << 'EOF'
{
  "name": "n8n-heroku",
  "version": "1.0.0",
  "description": "n8n on Heroku",
  "main": "index.js",
  "scripts": {
    "start": "n8n"
  },
  "engines": {
    "node": "18.x"
  },
  "dependencies": {
    "n8n": "^1.0.0"
  }
}
EOF

# Crear Procfile
echo "web: n8n start" > Procfile

# Commit inicial
git add .
git commit -m "Initial n8n setup"

# Conectar con Heroku
heroku git:remote -a your-meme-bot-n8n

# Desplegar
git push heroku main

# Escalar dyno
heroku ps:scale web=1:eco -a your-meme-bot-n8n
```

### Paso 5: Configurar Base de Datos PostgreSQL

```bash
# Conectar a PostgreSQL
heroku pg:psql -a your-meme-bot-n8n

# Copiar y pegar el contenido de setup_postgres.sql
# O ejecutar directamente desde archivo:
```

**Crear tabla manualmente:**
```sql
CREATE TABLE IF NOT EXISTS meme_posts (
  id SERIAL PRIMARY KEY,
  template_id VARCHAR(50) NOT NULL,
  topic VARCHAR(100) NOT NULL,
  text0 VARCHAR(255) NOT NULL,
  text1 VARCHAR(255) NOT NULL,
  meme_url TEXT,
  instagram_id VARCHAR(100),
  posted_at TIMESTAMP DEFAULT NOW(),
  success BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_meme_posts_posted_at ON meme_posts(posted_at DESC);
CREATE INDEX idx_meme_posts_topic ON meme_posts(topic);

-- Verificar
\dt
\d meme_posts
\q
```

**O ejecutar script directamente:**
```bash
# Desde tu máquina local donde tienes setup_postgres.sql
heroku pg:psql -a your-meme-bot-n8n < workflows/Meme/setup_postgres.sql
```

### Paso 6: Verificar Deployment

```bash
# Ver logs en tiempo real
heroku logs --tail -a your-meme-bot-n8n

# Verificar que n8n está corriendo
curl -I https://your-meme-bot-n8n.herokuapp.com

# Debe devolver: HTTP/2 200
```

### Paso 7: Acceder a n8n

```bash
# Abrir en navegador
heroku open -a your-meme-bot-n8n

# O manualmente:
# https://your-meme-bot-n8n.herokuapp.com
# Usuario: admin (o el que configuraste)
# Password: el que configuraste en N8N_BASIC_AUTH_PASSWORD
```

### Paso 8: Importar Workflow

**Opción A: Desde la interfaz web (recomendado)**
1. Accede a tu n8n: `https://your-meme-bot-n8n.herokuapp.com`
2. Login con tus credenciales
3. Click en **Workflows** → **Import from File**
4. Selecciona: `2057_Meme_Instagram_EcoDyno_PostgreSQL_Scheduled.json`
5. Configura credenciales de PostgreSQL
6. Activa el workflow

**Opción B: Usando API de n8n (avanzado)**
```bash
# Obtener workflow JSON
WORKFLOW_JSON=$(cat workflows/Meme/2057_Meme_Instagram_EcoDyno_PostgreSQL_Scheduled.json)

# Importar via API
curl -X POST https://your-meme-bot-n8n.herokuapp.com/rest/workflows \
  -u admin:tu_password \
  -H "Content-Type: application/json" \
  -d "$WORKFLOW_JSON"
```

### Paso 9: Configurar Credenciales PostgreSQL en n8n

```bash
# Obtener DATABASE_URL
heroku config:get DATABASE_URL -a your-meme-bot-n8n

# Formato: postgres://user:password@host:port/database
# Extraer componentes:
# User: parte antes del primer :
# Password: entre primer : y @
# Host: entre @ y :
# Port: después de host:
# Database: después de último /
```

En n8n:
1. **Credentials** → **New**
2. Selecciona **Postgres**
3. Ingresa los datos extraídos de DATABASE_URL
4. ✅ Marca "SSL" como enabled
5. **Save**

### Paso 10: Activar Workflow

```bash
# Ver workflows (via API)
curl -u admin:tu_password https://your-meme-bot-n8n.herokuapp.com/rest/workflows

# Activar workflow (reemplaza WORKFLOW_ID)
curl -X PATCH https://your-meme-bot-n8n.herokuapp.com/rest/workflows/WORKFLOW_ID \
  -u admin:tu_password \
  -H "Content-Type: application/json" \
  -d '{"active": true}'
```

O desde la interfaz:
1. Abre el workflow importado
2. Click en el toggle **Active** (arriba a la derecha)
3. Listo! ✅

## 🔍 Monitoreo y Mantenimiento

### Ver Estado del Dyno

```bash
# Estado actual
heroku ps -a your-meme-bot-n8n

# Información detallada
heroku ps:type -a your-meme-bot-n8n

# Uso de recursos
heroku metrics -a your-meme-bot-n8n
```

### Logs

```bash
# Ver logs en tiempo real
heroku logs --tail -a your-meme-bot-n8n

# Últimas 200 líneas
heroku logs -n 200 -a your-meme-bot-n8n

# Filtrar por fuente
heroku logs --source app --tail -a your-meme-bot-n8n

# Filtrar por dyno
heroku logs --dyno web --tail -a your-meme-bot-n8n
```

### Base de Datos

```bash
# Conectar a psql
heroku pg:psql -a your-meme-bot-n8n

# Backup manual
heroku pg:backups:capture -a your-meme-bot-n8n

# Listar backups
heroku pg:backups -a your-meme-bot-n8n

# Descargar backup
heroku pg:backups:download -a your-meme-bot-n8n

# Ver conexiones activas
heroku pg:psql -a your-meme-bot-n8n -c "SELECT count(*) FROM pg_stat_activity;"

# Ver tamaño de base de datos
heroku pg:psql -a your-meme-bot-n8n -c "SELECT pg_size_pretty(pg_database_size(current_database()));"

# Ver posts recientes
heroku pg:psql -a your-meme-bot-n8n -c "SELECT * FROM meme_posts ORDER BY posted_at DESC LIMIT 5;"
```

### Reiniciar Aplicación

```bash
# Reinicio completo
heroku restart -a your-meme-bot-n8n

# Reiniciar solo web dyno
heroku ps:restart web -a your-meme-bot-n8n

# Reiniciar y ver logs
heroku restart -a your-meme-bot-n8n && heroku logs --tail -a your-meme-bot-n8n
```

## 🔧 Resolución de Problemas

### Problema: No se puede conectar a n8n

```bash
# Verificar que el dyno está corriendo
heroku ps -a your-meme-bot-n8n

# Debe mostrar: web.1: up
# Si muestra "crashed", ver logs:
heroku logs --tail -a your-meme-bot-n8n

# Verificar variables de entorno
heroku config -a your-meme-bot-n8n | grep N8N_
```

### Problema: Error de Base de Datos

```bash
# Verificar que PostgreSQL está activo
heroku pg:info -a your-meme-bot-n8n

# Test de conexión
heroku pg:psql -a your-meme-bot-n8n -c "SELECT 1;"

# Ver logs de PostgreSQL
heroku pg:diagnose -a your-meme-bot-n8n

# Verificar que la tabla existe
heroku pg:psql -a your-meme-bot-n8n -c "\dt"
```

### Problema: Workflow No se Ejecuta

```bash
# Ver logs de n8n
heroku logs --tail -a your-meme-bot-n8n | grep workflow

# Verificar horario del servidor
heroku run date -a your-meme-bot-n8n

# Ver execuciones en n8n UI:
# https://your-meme-bot-n8n.herokuapp.com/executions
```

### Problema: Falta de Memoria

```bash
# Ver uso de memoria
heroku metrics:memory -a your-meme-bot-n8n

# Si es alto, reducir:
heroku config:set EXECUTIONS_DATA_SAVE_ON_SUCCESS=none -a your-meme-bot-n8n
heroku config:set N8N_PAYLOAD_SIZE_MAX=8 -a your-meme-bot-n8n

# Reiniciar
heroku restart -a your-meme-bot-n8n
```

## 📊 Comandos Útiles

### Gestión de Dynos

```bash
# Escalar dyno
heroku ps:scale web=1:eco -a your-meme-bot-n8n

# Detener dyno (parar workflow)
heroku ps:scale web=0 -a your-meme-bot-n8n

# Iniciar de nuevo
heroku ps:scale web=1:eco -a your-meme-bot-n8n

# Cambiar tipo de dyno
heroku ps:type web=hobby -a your-meme-bot-n8n
```

### Variables de Entorno

```bash
# Ver todas
heroku config -a your-meme-bot-n8n

# Ver una específica
heroku config:get IMGFLIP_USERNAME -a your-meme-bot-n8n

# Actualizar
heroku config:set IMGFLIP_PASSWORD=nuevo_password -a your-meme-bot-n8n

# Borrar
heroku config:unset VARIABLE_NAME -a your-meme-bot-n8n

# Exportar a archivo .env local
heroku config -a your-meme-bot-n8n --shell > .env
```

### Addons

```bash
# Listar addons
heroku addons -a your-meme-bot-n8n

# Info de PostgreSQL
heroku addons:info heroku-postgresql -a your-meme-bot-n8n

# Abrir dashboard de addon
heroku addons:open heroku-postgresql -a your-meme-bot-n8n
```

### Mantenimiento

```bash
# Vacuum PostgreSQL
heroku pg:psql -a your-meme-bot-n8n -c "VACUUM ANALYZE meme_posts;"

# Limpiar posts viejos
heroku pg:psql -a your-meme-bot-n8n -c "DELETE FROM meme_posts WHERE posted_at < NOW() - INTERVAL '90 days';"

# Ver estadísticas
heroku pg:psql -a your-meme-bot-n8n -c "SELECT * FROM meme_analytics LIMIT 7;"
```

## 🔄 Actualización del Workflow

```bash
# Descargar workflow actualizado
# En n8n UI: Export workflow → Guardar JSON

# O actualizar directamente en n8n UI:
# 1. Edit workflow
# 2. Make changes
# 3. Save
# 4. No requiere redeploy en Heroku
```

## 🗑️ Eliminar Todo (Cleanup)

```bash
# Ver app
heroku apps:info -a your-meme-bot-n8n

# Eliminar app (esto borra todo: dynos, addons, configs)
heroku apps:destroy -a your-meme-bot-n8n --confirm your-meme-bot-n8n

# Verificar eliminación
heroku apps | grep your-meme-bot-n8n
# No debe aparecer
```

## 📈 Monitoreo Avanzado

### Crear Dashboard Simple

```bash
# Instalar watch para monitoreo continuo
# macOS: brew install watch
# Linux: apt-get install watch

# Monitoreo cada 30 segundos
watch -n 30 'heroku ps -a your-meme-bot-n8n && echo "---" && heroku pg:info -a your-meme-bot-n8n'
```

### Script de Monitoreo

```bash
# Crear script monitor.sh
cat > monitor.sh << 'EOF'
#!/bin/bash
APP_NAME="your-meme-bot-n8n"

echo "=== Dyno Status ==="
heroku ps -a $APP_NAME

echo -e "\n=== Recent Logs ==="
heroku logs -n 10 -a $APP_NAME

echo -e "\n=== Database Info ==="
heroku pg:info -a $APP_NAME

echo -e "\n=== Recent Posts ==="
heroku pg:psql -a $APP_NAME -c "SELECT topic, posted_at, success FROM meme_posts ORDER BY posted_at DESC LIMIT 5;"

echo -e "\n=== Success Rate (7 days) ==="
heroku pg:psql -a $APP_NAME -c "SELECT COUNT(*) as total, SUM(CASE WHEN success THEN 1 ELSE 0 END) as successful, ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 2) as success_rate FROM meme_posts WHERE posted_at > NOW() - INTERVAL '7 days';"
EOF

chmod +x monitor.sh

# Ejecutar
./monitor.sh
```

## 🎯 Checklist de Deployment

Usa este checklist para verificar que todo está configurado:

```bash
# 1. Heroku CLI instalado
heroku --version
# ✅ Debe mostrar versión

# 2. Login correcto
heroku auth:whoami
# ✅ Debe mostrar tu email

# 3. App creada
heroku apps:info -a your-meme-bot-n8n
# ✅ Debe mostrar info de la app

# 4. PostgreSQL agregado
heroku addons -a your-meme-bot-n8n
# ✅ Debe mostrar heroku-postgresql

# 5. Variables configuradas
heroku config -a your-meme-bot-n8n
# ✅ Debe mostrar todas las variables

# 6. Dyno corriendo
heroku ps -a your-meme-bot-n8n
# ✅ Debe mostrar "web.1: up"

# 7. n8n accesible
curl -I https://your-meme-bot-n8n.herokuapp.com
# ✅ Debe devolver 200

# 8. Tabla creada
heroku pg:psql -a your-meme-bot-n8n -c "\dt"
# ✅ Debe mostrar meme_posts

# 9. Workflow importado y activo
# ✅ Verificar en UI de n8n

# 10. Primera ejecución exitosa
heroku pg:psql -a your-meme-bot-n8n -c "SELECT COUNT(*) FROM meme_posts;"
# ✅ Debe mostrar count > 0 después de primera ejecución
```

## 📚 Referencias

- [Heroku CLI Commands](https://devcenter.heroku.com/articles/heroku-cli-commands)
- [Heroku PostgreSQL](https://devcenter.heroku.com/articles/heroku-postgresql)
- [n8n Documentation](https://docs.n8n.io/)
- [n8n on Heroku](https://github.com/n8n-io/n8n-heroku)

## 💡 Tips Finales

1. **Guarda tu DATABASE_URL**: Puede que la necesites
2. **Backups automáticos**: Heroku los hace, pero descarga uno manualmente
3. **Monitorea semanalmente**: Revisa logs y success rate
4. **Rota tokens**: Instagram tokens expiran cada 60 días
5. **Usa alias**: Crea alias en tu shell para comandos frecuentes

```bash
# Agregar a ~/.bashrc o ~/.zshrc
alias meme-logs="heroku logs --tail -a your-meme-bot-n8n"
alias meme-status="heroku ps -a your-meme-bot-n8n"
alias meme-db="heroku pg:psql -a your-meme-bot-n8n"
alias meme-restart="heroku restart -a your-meme-bot-n8n"
```

---

¡Tu bot de memes está listo! 🎉🤖

**Siguiente paso**: Monitorea la primera semana y ajusta la frecuencia según necesites.
