from django.contrib import admin

from erp.core.organization.models import CostCode, Firm, Project, Site, Store


@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "status")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "firm", "status")
    list_filter = ("firm",)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "project")


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "site")


@admin.register(CostCode)
class CostCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "project")
