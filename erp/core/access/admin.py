from django.contrib import admin

from erp.core.access.models import Permission, Role, UserRoleAssignment


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    search_fields = ("code",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    search_fields = ("code", "name")


@admin.register(UserRoleAssignment)
class UserRoleAssignmentAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    raw_id_fields = ("user", "role")
