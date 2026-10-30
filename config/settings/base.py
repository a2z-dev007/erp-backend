"""Shared Django settings. See docs/01-architecture/django-application-structure.md."""

from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ERP_MODULES=(str, "inventory,procurement,finance,crm,sales,hr,assets,construction"),
)

environ.Env.read_env(BASE_DIR / ".env")

SECRET_KEY = env("SECRET_KEY", default="dev-insecure-change-me")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

import sys  # noqa: E402

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# --- ERP package layout: erp/core, erp/modules, erp/extensions, erp/common ---

CORE_APPS = [
    "erp.core.identity",
    "erp.core.access",
    "erp.core.organization",
    "erp.core.approvals",
    "erp.core.audit",
    "erp.core.documents",
    "erp.core.sequences",
    "erp.core.imports",
    "erp.core.notifications",
]

OPTIONAL_MODULE_APPS = {
    "inventory": ["erp.modules.inventory"],
    "procurement": ["erp.modules.procurement"],
    "finance": ["erp.modules.finance"],
    "crm": ["erp.modules.crm"],
    "sales": ["erp.modules.sales"],
    "hr": ["erp.modules.hr"],
    "assets": ["erp.modules.assets"],
    "construction": [
        "erp.extensions.construction.requests",
        "erp.extensions.construction.contractors",
        "erp.extensions.construction.evidence",
        "erp.extensions.construction.boq",
        "erp.extensions.construction.measurement",
        "erp.extensions.construction.client_billing",
        "erp.extensions.construction.costing",
        "erp.extensions.construction.consumption",
        "erp.extensions.construction.equipment",
        "erp.extensions.construction.attendance",
        "erp.extensions.construction.quality",
        "erp.extensions.construction.variations",
    ],
}


def _enabled_module_apps() -> list[str]:
    raw = env("ERP_MODULES")
    keys = [k.strip() for k in raw.split(",") if k.strip()]
    apps: list[str] = []
    for key in keys:
        apps.extend(OPTIONAL_MODULE_APPS.get(key, []))
    return apps


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    *CORE_APPS,
    *_enabled_module_apps(),
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "erp.common.middleware.RequestIDMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}

AUTH_USER_MODEL = "core_identity.User"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=["http://localhost:3000", "http://127.0.0.1:3000"],
)
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=["http://localhost:3000", "http://127.0.0.1:3000"],
)

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SAMESITE = "Lax"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "erp.common.pagination.ERPPageNumberPagination",
    "PAGE_SIZE": 25,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "erp.common.api.exceptions.erp_exception_handler",
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Prince ERP API",
    "DESCRIPTION": "Modular construction ERP — docs/MASTER_ERP_PRD.md",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

CELERY_BROKER_URL = env("REDIS_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND = env("REDIS_URL", default="redis://localhost:6379/0")

ERP_INDUSTRY = env("ERP_INDUSTRY", default="construction")
