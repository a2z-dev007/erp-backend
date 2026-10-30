import pytest

from erp.core.access.models import Role, UserRoleAssignment
from erp.core.identity.models import User
from erp.core.organization.models import Firm


@pytest.mark.django_db
def test_firm_list_requires_permission(client):
    firm = Firm.objects.create(code="F1", name="Firm One")
    user = User.objects.create_user(email="scoped@example.com", password="secret123")
    role = Role.objects.create(code="NoPerm", name="No Perm")
    UserRoleAssignment.objects.create(
        user=user,
        role=role,
        scope_json={"firm_ids": [str(firm.id)]},
    )
    client.post(
        "/api/v1/auth/login/",
        {"email": "scoped@example.com", "password": "secret123"},
        content_type="application/json",
    )
    assert client.get("/api/v1/organisation/firms/").status_code == 403


@pytest.mark.django_db
def test_firm_crud_with_owner_role(client, seeded_rbac):
    firm = Firm.objects.create(code="HQ", name="HQ Firm")
    user = User.objects.create_user(email="owner2@example.com", password="secret123")
    owner_role = Role.objects.get(code="Owner")
    UserRoleAssignment.objects.create(
        user=user,
        role=owner_role,
        scope_json={"firm_ids": [str(firm.id)]},
    )
    client.post(
        "/api/v1/auth/login/",
        {"email": "owner2@example.com", "password": "secret123"},
        content_type="application/json",
    )
    response = client.get("/api/v1/organisation/firms/")
    assert response.status_code == 200
    data = response.json()["data"]
    assert len(data) >= 1
