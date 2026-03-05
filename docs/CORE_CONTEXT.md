# CORE_CONTEXT — testkit (iil-testkit)
> Pflichtlektüre für jeden Coding Agent, Contributor und Reviewer.

## 1. Projekt-Identität
| Attribut | Wert |
|---|---|
| Repo | achimdehnert/testkit |
| PyPI-Package | iil-testkit |
| Zweck | Shared Test Factories, Fixtures, Naming-Convention-Plugin für alle Platform-Django-Repos |
| ADR | ADR-100 |

## 2. Package-Struktur
```
iil_testkit/
├── factories.py    # UserFactory, StaffUserFactory, AdminUserFactory, TenantFactory
├── fixtures.py     # pytest fixtures: db_user, staff_user, admin_user, api_client, auth_client
├── plugin.py       # pytest-Plugin: test_should_* naming enforcer (ADR-057)
└── assertions.py   # assert_redirects_to_login, assert_htmx_response, assert_no_n_plus_one
```

## 3. Architektur-Regeln (NON-NEGOTIABLE)
```
- Keine Django-Models im Package selbst
- TenantFactory nur wenn tenants-App installiert (conditional import)
- skip_postgeneration_save = True immer bei DjangoModelFactory
- Tests: test_should_* Naming (eigenes Plugin)
- Version: semantic versioning, CHANGELOG.md pflegen
```

## 4. Konsumenten
Alle Django-Hub-Repos: bfagent, travel-beat, weltenhub, risk-hub, coach-hub, dev-hub,
pptx-hub, trading-hub, billing-hub, illustration-hub, odoo-hub, cad-hub, mcp-hub,
nl2cad, wedding-hub, 137-hub

## 5. Release
```bash
# Version in iil_testkit/__init__.py erhöhen
git tag v0.x.0 && git push --tags
# GitHub Actions publish.yml deployed automatisch zu PyPI
```
