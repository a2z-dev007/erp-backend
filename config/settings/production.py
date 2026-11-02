from .base import *  # noqa: F403

DEBUG = False

# Security settings for production behind Nginx reverse proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Database is configured via DATABASE_URL in .env

