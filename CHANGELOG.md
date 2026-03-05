# Changelog — iil-testkit

All notable changes to this project will be documented in this file.

## [0.1.0] — 2026-03-05

### Added
- `UserFactory`, `StaffUserFactory`, `AdminUserFactory` (ADR-100)
- `TenantFactory` (conditional, when `tenants` app installed)
- pytest fixtures: `db_user`, `staff_user`, `admin_user`, `api_client`, `auth_client`, `staff_client`
- pytest plugin: `test_should_*` naming convention enforcer (ADR-057)
- Assertion helpers: `assert_redirects_to_login`, `assert_htmx_response`, `assert_no_n_plus_one`
