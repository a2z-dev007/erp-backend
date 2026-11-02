#!/usr/bin/env bash
set -e

PROJECT_DIR="/var/www/prince_erp/backend"
VENV_DIR="$PROJECT_DIR/.venv"

echo "🚀 Starting Prince ERP Backend Deployment..."

cd "$PROJECT_DIR"

# 1. Fetch latest changes from main branch
echo "📥 Pulling latest git changes..."
git fetch origin main
git reset --hard origin/main

# 2. Activate Python Virtual Environment
echo "🐍 Activating Python virtualenv..."
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtualenv..."
    python3 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"

# 3. Upgrade pip and install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Run database migrations
echo "🗄️ Running database migrations..."
export DJANGO_SETTINGS_MODULE=config.settings.production
python manage.py migrate --noinput

# 5. Collect static files for Nginx
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# 6. Restart backend service
echo "🔄 Restarting application service..."
if systemctl is-active --quiet prince-erp-backend; then
    sudo systemctl restart prince-erp-backend
elif command -v pm2 &> /dev/null && pm2 list | grep -q "prince-erp-backend"; then
    pm2 restart prince-erp-backend
else
    echo "⚠️ Neither systemd service nor PM2 process named 'prince-erp-backend' found running."
    echo "Please ensure the service is configured and started."
fi

# 7. Restart Celery worker if configured
if systemctl is-active --quiet prince-erp-celery; then
    echo "🔄 Restarting Celery worker..."
    sudo systemctl restart prince-erp-celery
fi

echo "✅ Prince ERP Backend successfully deployed!"

