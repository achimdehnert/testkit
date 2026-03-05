# iil_testkit/plugin.py — ADR-100
"""pytest plugin: enforce test_should_* naming convention (ADR-057)."""
import pytest


def pytest_collection_modifyitems(config, items):
    """Warn if test functions do not follow test_should_* convention."""
    if config.getoption("--no-naming-check", default=False):
        return
    for item in items:
        if isinstance(item, pytest.Function):
            name = item.originalname or item.name
            if name.startswith("test_") and not name.startswith("test_should_"):
                item.warn(
                    pytest.PytestWarning(
                        f"Naming convention: '{name}' should start with "
                        f"'test_should_' (ADR-057 §2.3). "
                        f"Use --no-naming-check to suppress."
                    )
                )


def pytest_addoption(parser):
    parser.addoption(
        "--no-naming-check",
        action="store_true",
        default=False,
        help="Disable test_should_* naming convention check (ADR-057)",
    )
