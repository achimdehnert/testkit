# iil_testkit/factories.py — ADR-100
"""Platform-standard factories for all Django-Hub repos."""
import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    """Standard UserFactory — identical across all platform repos."""

    class Meta:
        model = get_user_model()
        skip_postgeneration_save = True

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "testpass123")
    is_active = True


class StaffUserFactory(UserFactory):
    """Staff user with is_staff=True."""

    is_staff = True


class AdminUserFactory(StaffUserFactory):
    """Superuser factory."""

    is_superuser = True


try:
    from django.apps import apps

    if apps.is_installed("apps.tenants") or apps.is_installed("tenants"):

        class TenantFactory(factory.django.DjangoModelFactory):
            """TenantFactory — only available if tenants app is installed."""

            class Meta:
                model = "tenants.Tenant"

            name = factory.Sequence(lambda n: f"Tenant {n}")
            slug = factory.Sequence(lambda n: f"tenant-{n}")
            is_active = True

except Exception:
    pass
