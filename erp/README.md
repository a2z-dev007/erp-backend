# ERP Python Package Layout

Production-style layout: **one top-level `erp` package**, grouped by product layer.

```text
erp/
├── common/                 # Cross-cutting (not a Django app)
│   ├── models.py           # UUIDModel, TimestampedModel, ScopedModel
│   ├── middleware.py
│   └── api/                # Envelope, exceptions, health view
├── core/                   # L1 — always installed
│   ├── identity/           # label: core_identity
│   ├── access/
│   ├── organization/
│   ├── approvals/
│   ├── audit/
│   ├── documents/
│   ├── sequences/
│   ├── imports/
│   └── notifications/
├── modules/                # L2 — toggle via ERP_MODULES
│   ├── inventory/          # label: mod_inventory
│   ├── procurement/
│   └── finance/
└── extensions/             # L3 — industry packs
    └── construction/
        ├── requests/       # label: ext_construction_requests
        ├── contractors/
        └── evidence/
```

## Django app labels

Each subfolder is a Django app. The **Python path** is dotted (`erp.core.identity`); the **app label** stays short (`core_identity`) so database tables and migrations remain stable (`core_identity_user`, etc.).

```python
class IdentityConfig(AppConfig):
    name = "erp.core.identity"
    label = "core_identity"
```

## Per-app internal structure

```text
erp/core/organization/
├── apps.py
├── admin.py
├── models/
├── services/
├── selectors/
├── api/
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── migrations/
└── management/commands/
```

## Import rules

- **Within the same app:** prefer relative imports or `erp.core.organization...`
- **Across apps:** import from the owning app’s public layer (`services`, `selectors`, `api.permissions`) — never reach into another app’s `models` for writes
- **Common utilities:** `from erp.common.models import UUIDModel`

## Adding a new module

1. Create `erp/modules/<name>/` or `erp/extensions/<industry>/<name>/`
2. Set `AppConfig.name` and `label` in `apps.py`
3. Register in `config/settings/base.py` (`CORE_APPS`, `OPTIONAL_MODULE_APPS`, or `ERP_MODULES`)
4. Include `api.urls` in `config/urls.py`
