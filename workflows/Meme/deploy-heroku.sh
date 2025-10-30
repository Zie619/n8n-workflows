#!/bin/bash
# Heroku Deployment Helper Script
# Quick setup for meme automation workflow

set -e  # Exit on error

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# Check if heroku CLI is installed
check_heroku_cli() {
    if ! command -v heroku &> /dev/null; then
        print_error "Heroku CLI no está instalado"
        echo ""
        echo "Instala Heroku CLI:"
        echo "  macOS:   brew tap heroku/brew && brew install heroku"
        echo "  Ubuntu:  curl https://cli-assets.heroku.com/install-ubuntu.sh | sh"
        echo "  Windows: https://devcenter.heroku.com/articles/heroku-cli"
        exit 1
    fi
    print_success "Heroku CLI instalado: $(heroku --version | head -n 1)"
}

# Check if logged in
check_heroku_auth() {
    if ! heroku auth:whoami &> /dev/null; then
        print_error "No has iniciado sesión en Heroku"
        echo ""
        read -p "¿Quieres iniciar sesión ahora? (y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            heroku login
        else
            exit 1
        fi
    fi
    print_success "Sesión activa: $(heroku auth:whoami)"
}

# Main script
print_header "Heroku Deployment Helper - Meme Automation"

echo "Este script te ayudará a configurar tu app en Heroku"
echo ""

# Step 1: Check prerequisites
print_header "Paso 1: Verificando prerequisitos"
check_heroku_cli
check_heroku_auth

# Step 2: App name
print_header "Paso 2: Nombre de la aplicación"
echo "Ingresa un nombre único para tu app (solo letras minúsculas, números y guiones)"
echo "Ejemplo: mi-bot-memes-n8n"
read -p "Nombre de la app: " APP_NAME

if [ -z "$APP_NAME" ]; then
    print_error "El nombre no puede estar vacío"
    exit 1
fi

# Step 3: Create app
print_header "Paso 3: Creando aplicación en Heroku"
if heroku apps:info -a "$APP_NAME" &> /dev/null; then
    print_warning "La app '$APP_NAME' ya existe"
    read -p "¿Quieres usar esta app existente? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo "Creando app..."
    heroku create "$APP_NAME"
    print_success "App creada: $APP_NAME"
fi

# Step 4: Add PostgreSQL
print_header "Paso 4: Agregando PostgreSQL"
if heroku addons -a "$APP_NAME" | grep -q "heroku-postgresql"; then
    print_warning "PostgreSQL ya está agregado"
else
    echo "Agregando PostgreSQL Mini..."
    heroku addons:create heroku-postgresql:mini -a "$APP_NAME"
    print_success "PostgreSQL agregado"
    echo "Esperando a que PostgreSQL esté disponible..."
    sleep 5
fi

# Step 5: Configure environment variables
print_header "Paso 5: Configurando variables de entorno"

echo ""
echo "Necesitamos configurar las credenciales de las APIs"
echo ""

# ImgFlip
print_info "ImgFlip API (https://imgflip.com)"
read -p "ImgFlip Username: " IMGFLIP_USER
read -sp "ImgFlip Password: " IMGFLIP_PASS
echo ""

# Instagram
print_info "Instagram Graph API"
read -p "Instagram User ID: " IG_USER_ID
read -sp "Instagram Access Token: " IG_TOKEN
echo ""

# n8n Auth
print_info "n8n Authentication"
read -p "n8n Admin Username [admin]: " N8N_USER
N8N_USER=${N8N_USER:-admin}
read -sp "n8n Admin Password: " N8N_PASS
echo ""

# Set all variables
echo ""
echo "Configurando variables en Heroku..."

heroku config:set \
  IMGFLIP_USERNAME="$IMGFLIP_USER" \
  IMGFLIP_PASSWORD="$IMGFLIP_PASS" \
  INSTAGRAM_USER_ID="$IG_USER_ID" \
  INSTAGRAM_ACCESS_TOKEN="$IG_TOKEN" \
  N8N_BASIC_AUTH_ACTIVE=true \
  N8N_BASIC_AUTH_USER="$N8N_USER" \
  N8N_BASIC_AUTH_PASSWORD="$N8N_PASS" \
  N8N_HOST="${APP_NAME}.herokuapp.com" \
  N8N_PORT=443 \
  N8N_PROTOCOL=https \
  WEBHOOK_URL="https://${APP_NAME}.herokuapp.com/" \
  N8N_PAYLOAD_SIZE_MAX=16 \
  EXECUTIONS_DATA_SAVE_ON_ERROR=none \
  EXECUTIONS_DATA_SAVE_ON_SUCCESS=none \
  EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS=false \
  GENERIC_TIMEZONE=America/New_York \
  -a "$APP_NAME"

# Clear sensitive variables from memory
unset IMGFLIP_PASS
unset IG_TOKEN
unset N8N_PASS

print_success "Variables de entorno configuradas"

# Step 6: Deploy n8n
print_header "Paso 6: Desplegando n8n"

echo "Opciones de deployment:"
echo "  1) Usar template oficial de n8n (recomendado)"
echo "  2) Omitir deployment (lo haré manualmente)"
echo ""
read -p "Selecciona una opción [1]: " DEPLOY_OPTION
DEPLOY_OPTION=${DEPLOY_OPTION:-1}

if [ "$DEPLOY_OPTION" == "1" ]; then
    echo ""
    print_info "Clonando n8n-heroku template..."
    
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"
    
    git clone https://github.com/n8n-io/n8n-heroku.git
    cd n8n-heroku
    
    heroku git:remote -a "$APP_NAME"
    
    echo "Desplegando a Heroku..."
    git push heroku main
    
    cd - > /dev/null
    rm -rf "$TEMP_DIR"
    
    print_success "n8n desplegado"
else
    print_warning "Deployment omitido - deberás hacerlo manualmente"
    echo ""
    echo "Para desplegar manualmente:"
    echo "  git clone https://github.com/n8n-io/n8n-heroku.git"
    echo "  cd n8n-heroku"
    echo "  heroku git:remote -a $APP_NAME"
    echo "  git push heroku main"
fi

# Step 7: Scale dyno
print_header "Paso 7: Configurando dyno"

echo "¿Qué tipo de dyno quieres usar?"
echo "  1) Eco ($5/mes, 1000 horas, recomendado)"
echo "  2) Hobby ($7/mes, siempre activo)"
echo "  3) Free (deprecado, usar Eco)"
echo ""
read -p "Selecciona una opción [1]: " DYNO_OPTION
DYNO_OPTION=${DYNO_OPTION:-1}

case $DYNO_OPTION in
    1)
        heroku ps:scale web=1:eco -a "$APP_NAME"
        print_success "Dyno escalado a Eco"
        ;;
    2)
        heroku ps:scale web=1:hobby -a "$APP_NAME"
        print_success "Dyno escalado a Hobby"
        ;;
    3)
        heroku ps:scale web=1 -a "$APP_NAME"
        print_success "Dyno escalado (Free/Basic)"
        ;;
esac

# Step 8: Setup database
print_header "Paso 8: Configurando base de datos"

echo "¿Quieres crear la tabla de PostgreSQL ahora?"
read -p "(y/n) [y]: " -n 1 -r
echo
SETUP_DB=${REPLY:-y}

if [[ $SETUP_DB =~ ^[Yy]$ ]]; then
    echo ""
    print_info "Creando tabla meme_posts..."
    
    heroku pg:psql -a "$APP_NAME" << 'EOF'
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

CREATE INDEX IF NOT EXISTS idx_meme_posts_posted_at ON meme_posts(posted_at DESC);
CREATE INDEX IF NOT EXISTS idx_meme_posts_topic ON meme_posts(topic);

\dt
EOF
    
    print_success "Base de datos configurada"
else
    print_warning "Setup de base de datos omitido"
    echo ""
    echo "Para configurar manualmente:"
    echo "  heroku pg:psql -a $APP_NAME < workflows/Meme/setup_postgres.sql"
fi

# Step 9: Final steps
print_header "Paso 9: Pasos finales"

echo ""
print_success "¡Deployment completado!"
echo ""
echo "Tu app está disponible en:"
echo "  ${GREEN}https://${APP_NAME}.herokuapp.com${NC}"
echo ""
echo "Credenciales de n8n:"
echo "  Usuario: ${GREEN}${N8N_USER}${NC}"
echo "  Password: ${GREEN}[el que configuraste]${NC}"
echo ""
print_info "Próximos pasos:"
echo ""
echo "1. Accede a n8n:"
echo "   ${BLUE}heroku open -a $APP_NAME${NC}"
echo ""
echo "2. Importa el workflow:"
echo "   - En n8n: Workflows → Import from File"
echo "   - Selecciona: 2057_Meme_Instagram_EcoDyno_PostgreSQL_Scheduled.json"
echo ""
echo "3. Configura credenciales de PostgreSQL en n8n:"
echo "   - Credentials → New → Postgres"
echo "   - Usa los datos de: ${BLUE}heroku config:get DATABASE_URL -a $APP_NAME${NC}"
echo ""
echo "4. Activa el workflow:"
echo "   - Toggle 'Active' en el workflow"
echo ""
echo "5. Monitorea logs:"
echo "   ${BLUE}heroku logs --tail -a $APP_NAME${NC}"
echo ""
print_info "Comandos útiles:"
echo "  Ver status:    ${BLUE}heroku ps -a $APP_NAME${NC}"
echo "  Ver logs:      ${BLUE}heroku logs --tail -a $APP_NAME${NC}"
echo "  Ver DB:        ${BLUE}heroku pg:psql -a $APP_NAME${NC}"
echo "  Reiniciar:     ${BLUE}heroku restart -a $APP_NAME${NC}"
echo "  Ver config:    ${BLUE}heroku config -a $APP_NAME${NC}"
echo ""
print_success "¡Listo! Tu bot de memes está en la nube 🎉🤖"
echo ""

# Save app info to file (non-sensitive data only)
cat > ".heroku-app-info" << EOF
# WARNING: This file contains app info. Do not commit to git!
APP_NAME=$APP_NAME
N8N_URL=https://${APP_NAME}.herokuapp.com
DEPLOYED_AT=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
# Note: Credentials are stored securely in Heroku config
# View with: heroku config -a $APP_NAME
EOF

print_info "Info guardada en: .heroku-app-info (non-sensitive data only)"
print_warning "Este archivo está en .gitignore - no lo commitees accidentalmente"
echo ""
