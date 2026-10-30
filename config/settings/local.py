from .base import *  # noqa: F403

DEBUG = True

# Default to SQLite for local dev and manual API testing (no Docker Postgres required).
# Set USE_SQLITE=false and DATABASE_URL=postgres://... when using Docker Postgres.
if env.bool("USE_SQLITE", default=True):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
