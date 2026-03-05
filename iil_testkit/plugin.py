# iil_testkit/plugin.py — ADR-100
"""pytest plugin: enforce test_should_* naming convention (ADR-057).

Configuration in pytest.ini / pyproject.toml:
    [tool.pytest.ini_options]
    iil_naming_mode = "error"   # "error" (default) | "warn"

Opt-out per test:
    @pytest.mark.no_naming_convention
    def test_legacy_name(): ...

Opt-out globally:
    pytest --relax-naming
"""
import pytest

__all__ = ["pytest_collection_modifyitems", "pytest_addoption", "pytest_configure"]


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "no_naming_convention: opt out of test_should_* naming check (ADR-057)",
    )


def pytest_addoption(parser):
    parser.addoption(
        "--relax-naming",
        action="store_true",
        default=False,
        help="Disable test_should_* naming convention enforcement (ADR-057)",
    )
    try:
        parser.addini(
            "iil_naming_mode",
            default="error",
            help="Naming convention mode: 'error' (default) or 'warn'",
        )
    except ValueError:
        pass


def pytest_collection_modifyitems(config, items):
    """Enforce test_should_* naming convention (ADR-057)."""
    if config.getoption("--relax-naming", default=False):
        return

    violations = []
    for item in items:
        if not isinstance(item, pytest.Function):
            continue
        if item.get_closest_marker("no_naming_convention"):
            continue
        name = item.originalname or item.name
        if name.startswith("test_") and not name.startswith("test_should_"):
            violations.append(item.nodeid)

    if not violations:
        return

    mode = config.getini("iil_naming_mode") or "error"
    msg = (
        f"Naming convention violations (ADR-057 §2.3) — "
        f"{len(violations)} test(s) must start with 'test_should_':\n"
        + "\n".join(f"  {v}" for v in violations)
        + "\n\nFix: rename to test_should_<what_it_does>(...)"
        + "\nOpt-out: @pytest.mark.no_naming_convention or --relax-naming"
    )

    if mode == "error":
        pytest.fail(msg, pytrace=False)
    else:
        import warnings
        warnings.warn(msg, stacklevel=2)
