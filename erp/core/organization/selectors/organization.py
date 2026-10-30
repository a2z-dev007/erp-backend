from django.db.models import Q, QuerySet

from erp.core.access.services.access import user_firm_scope_ids
from erp.core.organization.models import CostCode, Firm, Project, Site, Store


def _firm_qs(user) -> QuerySet[Firm]:
    qs = Firm.objects.all().order_by("code")
    firm_ids = user_firm_scope_ids(user)
    if firm_ids is not None:
        qs = qs.filter(id__in=firm_ids)
    return qs


def firms_for_user(user, q: str | None = None) -> QuerySet[Firm]:
    qs = _firm_qs(user)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
    return qs


def projects_for_user(user, firm_id=None, q: str | None = None) -> QuerySet[Project]:
    qs = Project.objects.select_related("firm").filter(firm__in=_firm_qs(user))
    if firm_id:
        qs = qs.filter(firm_id=firm_id)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
    return qs.order_by("code")


def sites_for_user(user, project_id=None, q: str | None = None) -> QuerySet[Site]:
    qs = Site.objects.select_related("project", "project__firm").filter(
        project__firm__in=_firm_qs(user)
    )
    if project_id:
        qs = qs.filter(project_id=project_id)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
    return qs.order_by("code")


def stores_for_user(user, site_id=None, q: str | None = None) -> QuerySet[Store]:
    qs = Store.objects.select_related("site", "site__project").filter(
        site__project__firm__in=_firm_qs(user)
    )
    if site_id:
        qs = qs.filter(site_id=site_id)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
    return qs.order_by("code")


def cost_codes_for_user(user, project_id=None, q: str | None = None) -> QuerySet[CostCode]:
    qs = CostCode.objects.select_related("project").filter(project__firm__in=_firm_qs(user))
    if project_id:
        qs = qs.filter(project_id=project_id)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(code__icontains=q))
    return qs.order_by("code")
