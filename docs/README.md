# Backend documentation (living handbook)

This folder is the **working documentation for the Django backend**. Use it alongside the product PRDs in the repo root [`docs/`](../docs/) when implementing modules.

| Document | Purpose |
|----------|---------|
| [IMPLEMENTATION_RECORD.md](./IMPLEMENTATION_RECORD.md) | What has been built so far (foundation, structure, APIs, infra, tests) |
| [MODULE_REGISTRY.md](./MODULE_REGISTRY.md) | Master checklist: every Django app, status, build order, PRD links |
| [MODULE_GAP_AUDIT.md](./MODULE_GAP_AUDIT.md) | Catalog vs backend: what exists, what is PRD-only |
| [ENTITY_COVERAGE.md](./ENTITY_COVERAGE.md) | Master prompt §11 entities → models & APIs |
| [API_REFERENCE.md](./API_REFERENCE.md) | **Module-wise HTTP API** (paths, auth, conventions) |
| [modules/](./modules/) | **Per-module notes** — update these as you implement (models, endpoints, migrations, decisions) |

## How we maintain these files

1. **Before starting a module** — Read the product PRD (linked from `MODULE_REGISTRY.md`), set status to *In progress*, and copy [modules/_TEMPLATE.md](./modules/_TEMPLATE.md) if the module file is still minimal.
2. **While building** — Record in the module markdown file:
   - Models and migrations (names, key fields, constraints)
   - API routes (method + path + permission codes)
   - Services vs selectors (who owns writes/reads)
   - Integration points (events, other apps, Celery tasks)
   - Deviations from the PRD (with reason)
3. **When a slice is done** — Update `MODULE_REGISTRY.md` status, add test file names, and add a dated bullet under **Changelog** in `IMPLEMENTATION_RECORD.md`.
4. **Product truth stays in `docs/`** — Backend docs describe **what the code does** and **implementation choices**; requirement IDs and business rules remain in PRDs unless you explicitly move a decision here and link back.

## Related repo docs

- Architecture: [docs/01-architecture/django-application-structure.md](../docs/01-architecture/django-application-structure.md)
- Build order: [docs/10-implementation-planning/module-build-order.md](../docs/10-implementation-planning/module-build-order.md)
- Run locally: [backend/README.md](../README.md)
- Package layout: [erp/README.md](../erp/README.md)

**Last updated:** 2026-10-29
