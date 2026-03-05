# Changelog — iil-testkit

All notable changes to this project will be documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Breaking Change Policy

A **breaking change** is any modification that requires consumers to update their code:
- Removing or renaming a public symbol from `__all__`
- Changing a factory field default that affects test data expectations
- Changing `UserFactory.username` sequence format (`user_N`)
- Removing a fixture from `iil_testkit.fixtures`
- Changing plugin behavior from `warn` to `error` (or vice versa) as the **default**

**Pin recommendation for all repos:**
```
iil-testkit>=0.1.0,<0.2.0
```
Bump the upper bound only after reviewing the CHANGELOG for breaking changes.

---

## [Unreleased]

## [0.1.0] — 2026-03-05

### Added
- `UserFactory`, `StaffUserFactory`, `AdminUserFactory` in `iil_testkit.factories`
- `TenantFactory` in `iil_testkit.contrib.tenants` (explicit import, no implicit coupling)
- pytest plugin (`iil_testkit.plugin`) enforcing `test_should_*` naming (ADR-057)
  - Mode: `error` (default) or `warn` via `iil_naming_mode` ini option
  - Opt-out per test: `@pytest.mark.no_naming_convention`
  - Opt-out globally: `--relax-naming`
- `iil_testkit.assertions`: `assert_redirects_to_login`, `assert_htmx_response`,
  `assert_no_n_plus_one`, `assert_form_error`
- `iil_testkit.fixtures`: `db_user`, `staff_user`, `admin_user`, `api_client`,
  `auth_client`, `staff_client`
- `py.typed` marker for mypy/pyright compatibility (PEP 561)
- Auto-registration via `pytest11` entry point (no manual `conftest.py` needed)

### Notes
- Requires `factory-boy>=3.3.0` for `skip_postgeneration_save` support
- `TenantFactory` requires explicit import from `iil_testkit.contrib.tenants`
- Tested on Python 3.11 and 3.12, Django 4.2+
