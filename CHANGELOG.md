# Changelog

## v0.2.0 (2026-03-07)

### Added
- `drf_api_client` fixture — unauthenticated DRF `APIClient` (auto-skips if DRF not installed)
- `drf_auth_client` fixture — DRF `APIClient` authenticated as `db_user` via `force_authenticate`
- `[drf]` optional dependency group in `pyproject.toml`
- `CHANGELOG.md`

### Changed
- All Django-Hub repos should now use `iil-testkit>=0.2.0` in `requirements-test.txt`

## v0.1.0 (2026-03-06)

### Added
- Initial release
- `UserFactory`, `StaffUserFactory`, `AdminUserFactory`
- `db_user`, `staff_user`, `admin_user`, `api_client`, `auth_client`, `staff_client` fixtures
- `assert_redirects_to_login`, `assert_htmx_response`, `assert_no_n_plus_one`, `assert_form_error`
- `iil-testkit` pytest plugin enforcing `test_should_*` naming convention (ADR-057)
- `iil_testkit.contrib.tenants.TenantFactory` for multi-tenant repos
