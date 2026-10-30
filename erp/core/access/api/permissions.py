from rest_framework.permissions import BasePermission

from erp.core.access.services.access import user_has_permission


class HasERPPermission(BasePermission):
    """Set view.required_permission = 'organisation.firm.view' etc."""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        code = getattr(view, "required_permission", None)
        if not code:
            return True
        return user_has_permission(request.user, code)
