# Module: `core_documents` (`erp.core.documents`)

**Status:** 📋 Scaffold only  
**Product PRD:** [document-management](../../../docs/04-erp-core/document-management/PRD.md)  
**Last updated:** 2026-10-29

---

## Purpose

File metadata, storage backend (MinIO), linking documents to business entities.

---

## Models

_None yet._

---

## Infrastructure

MinIO available via `docker-compose.yml` (ports 9000/9001). Wire settings in `.env` when implementing.

---

## Open items

- [ ] Storage adapter + presigned upload/download
- [ ] Document version model
- [ ] Link table pattern (entity_type, entity_id)
