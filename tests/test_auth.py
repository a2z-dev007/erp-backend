import pytest

from erp.core.identity.models import User


@pytest.mark.django_db
def test_login_and_me(client):
    User.objects.create_user(email="test@example.com", password="secret123")
    login = client.post(
        "/api/v1/auth/login/",
        {"email": "test@example.com", "password": "secret123"},
        content_type="application/json",
    )
    assert login.status_code == 200
    body = login.json()["data"]
    assert body["email"] == "test@example.com"
    assert body.get("token")

    me = client.get("/api/v1/users/me/")
    assert me.status_code == 200
    assert me.json()["data"]["email"] == "test@example.com"


@pytest.mark.django_db
def test_login_token_authorization_header(client):
    User.objects.create_user(email="token@example.com", password="secret123")
    login = client.post(
        "/api/v1/auth/login/",
        {"email": "token@example.com", "password": "secret123"},
        content_type="application/json",
    )
    token = login.json()["data"]["token"]

    me = client.get(
        "/api/v1/users/me/",
        HTTP_AUTHORIZATION=f"Token {token}",
    )
    assert me.status_code == 200
    assert me.json()["data"]["email"] == "token@example.com"
