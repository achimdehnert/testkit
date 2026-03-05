# AGENT_HANDOVER — testkit (iil-testkit)
> Lesen vor jeder Session. Aktualisieren nach jeder Session.

## Aktueller Stand
| Attribut | Wert |
|---|---|
| Zuletzt aktualisiert | 2026-03-05 |
| Version | 0.1.0 (noch nicht auf PyPI) |
| Branch | main |

## Was wurde zuletzt getan?
- 2026-03-05 — Repo angelegt, Package-Struktur implementiert, ADR-100 erstellt
- Factories: UserFactory, StaffUserFactory, AdminUserFactory, TenantFactory (conditional)
- pytest-Plugin für test_should_* Naming (ADR-057)
- Fixtures: db_user, staff_user, admin_user, api_client, auth_client, staff_client
- Assertions: assert_redirects_to_login, assert_htmx_response, assert_no_n_plus_one

## Offene Aufgaben (Priorisiert)
- [ ] GitHub Project anlegen + PROJECT_NUMBER setzen
- [ ] Labels bootstrap ausführen
- [ ] v0.1.0 auf PyPI veröffentlichen (/release Workflow)
- [ ] In bfagent, travel-beat, weltenhub: UserFactory auf Import umstellen
- [ ] In dev-hub, risk-hub, pptx-hub, trading-hub, coach-hub: factories.py anlegen

## Migration der bestehenden Repos
```python
# Vorher (copy-paste in jedem Repo):
class UserFactory(factory.django.DjangoModelFactory): ...

# Nachher:
from iil_testkit.factories import UserFactory
```
