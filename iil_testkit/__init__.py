"""iil-testkit — Shared Test Factory Package for all Platform Django repos.

See ADR-100 for architecture decisions.
"""
__version__ = "0.2.0"

from iil_testkit.tenant_mixins import TenantTestMixin

__all__ = [
    "__version__",
    "TenantTestMixin",
]
