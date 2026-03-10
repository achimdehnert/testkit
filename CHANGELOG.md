# Changelog

## v0.2.0 (2026-03-10)

### Added
- `drf_api_client` fixture — unauthenticated DRF `APIClient` (auto-skips if DRF not installed)
- `drf_auth_client` fixture — DRF `APIClient` authenticated as `db_user` via `force_authenticate`
- `[drf]` optional dependency group in `pyproject.toml`
- `CHANGELOG.md`

### Fixed
- **BREAKING BUG**: `plugin.py` used `pytest.fail()` in `pytest_collection_modifyitems` which
  caused `INTERNALERROR` (not a normal test failure) when naming violations were found
- Changed default `iil_naming_mode` from `"error"` to `"warn"` — naming convention is now
  advisory by default; opt-in to `"error"` mode explicitly when all tests follow `test_should_*`
- `pytest.fail()` replaced with `pytest.UsageError()` in error-mode to produce a proper
  collection error instead of INTERNALERROR

### Changed
- All Django-Hub repos should now use `iil-testkit>=0.2.0` in `requirements-test.txt`
- Repos with legacy `test_*` naming will get a warning, not a hard failure

## v0.1.0 (2026-03-06)

### Added
- Initial release
- `UserFactory`, `StaffUserFactory`, `AdminUserFactory`
- `db_user`, `staff_user`, `admin_user`, `api_client`, `auth_client`, `staff_client` fixtures
- `assert_redirects_to_login`, `assert_htmx_response`, `assert_no_n_plus_one`, `assert_form_error`
- `iil-testkit` pytest plugin enforcing `test_should_*` naming convention (ADR-057)
- `iil_testkit.contrib.tenants.TenantFactory` for multi-tenant repos
