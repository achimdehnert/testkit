# Changelog

## [0.1.0] — 2026-03-06

### Added
- `UserFactory`, `StaffUserFactory`, `AdminUserFactory` (ADR-100)
- `TenantFactory` in `iil_testkit.contrib.tenants` (optional, no implicit coupling)
- pytest plugin enforcing `test_should_*` naming convention (ADR-057)
- `iil_naming_mode` ini option: `"error"` (default) or `"warn"`
- `--relax-naming` global flag for opt-out
- `@pytest.mark.no_naming_convention` per-test opt-out marker
- `assert_redirects_to_login`, `assert_htmx_response`, `assert_no_n_plus_one`, `assert_form_error`
- pytest fixtures: `db_user`, `staff_user`, `admin_user`, `api_client`, `auth_client`, `staff_client`
- `py.typed` marker (PEP 561)
- Full test suite with ≥80% coverage

### Breaking Changes
- None (initial release)

### Pin Strategy
```
iil-testkit>=0.1.0,<0.2.0
```
