"""
Pytest / CI settings — always SQLite (never Postgres from .env).

Run: pytest   (DJANGO_SETTINGS_MODULE is set in pyproject.toml)
"""

import os

# Block .env from pointing tests at Postgres (read_env in base does not override existing keys).
os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ.setdefault("USE_SQLITE", "true")
os.environ.setdefault(
    "ERP_MODULES",
    "inventory,procurement,finance,crm,sales,hr,assets,construction",
)

from .base import *  # noqa: F403

DEBUG = False
TESTING = True

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
