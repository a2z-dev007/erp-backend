from erp.core.access.models import Permission, Role, UserRoleAssignment


def user_permission_codes(user) -> set[str]:
    if user.is_superuser:
        return {p.code for p in Permission.objects.all()}
    role_ids = UserRoleAssignment.objects.filter(user=user).values_list("role_id", flat=True)
    return set(
        Permission.objects.filter(roles__id__in=role_ids).values_list("code", flat=True).distinct()
    )


def user_has_permission(user, code: str) -> bool:
    if user.is_superuser:
        return True
    return code in user_permission_codes(user)


def user_firm_scope_ids(user) -> list | None:
    """None means unrestricted (superuser). Empty list means no firm access."""
    if user.is_superuser:
        return None
    firm_ids: set = set()
    assignments = UserRoleAssignment.objects.filter(user=user).values_list("scope_json", flat=True)
    for scope in assignments:
        if not scope:
            continue
        for fid in scope.get("firm_ids", []) or []:
            firm_ids.add(str(fid))
    return list(firm_ids)
