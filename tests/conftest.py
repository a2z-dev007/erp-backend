import pytest
from django.conf import settings
from django.core.management import call_command


@pytest.fixture(scope="session", autouse=True)
def _assert_sqlite_test_db():
    engine = settings.DATABASES["default"]["ENGINE"]
    assert "sqlite" in engine, f"Tests must use SQLite, got {engine}"


@pytest.fixture
def seeded_rbac(db):
    call_command("seed_rbac")
