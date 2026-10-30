import pytest

from django.core.management import call_command

from tests.seed_endpoints import SEED_LIST_ENDPOINTS


@pytest.mark.django_db
def test_module_list_apis_return_ten_rows(client):
    call_command("seed_rbac")
    call_command("seed_all", skip_rbac=True)
    login = client.post(
        "/api/v1/auth/login/",
        {"email": "owner@demo.local", "password": "demo1234"},
        content_type="application/json",
    )
    assert login.status_code == 200

    for path in SEED_LIST_ENDPOINTS:
        response = client.get(path)
        assert response.status_code == 200, path
        data = response.json()["data"]
        if isinstance(data, dict) and "results" in data:
            rows = data["results"]
        else:
            rows = data
        assert len(rows) >= 10, f"{path} returned {len(rows)} rows"
