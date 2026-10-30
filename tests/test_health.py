import pytest


@pytest.mark.django_db
def test_health_ok(client):
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["status"] == "ok"
