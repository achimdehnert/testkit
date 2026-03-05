# iil_testkit/fixtures.py — ADR-100
"""pytest fixtures for platform Django repos."""
import pytest


@pytest.fixture
def db_user(db):
    """A standard authenticated user, saved to DB."""
    from iil_testkit.factories import UserFactory
    return UserFactory()


@pytest.fixture
def staff_user(db):
    """A staff user, saved to DB."""
    from iil_testkit.factories import StaffUserFactory
    return StaffUserFactory()


@pytest.fixture
def admin_user(db):
    """A superuser, saved to DB."""
    from iil_testkit.factories import AdminUserFactory
    return AdminUserFactory()


@pytest.fixture
def api_client():
    """Django test client (unauthenticated)."""
    from django.test import Client
    return Client()


@pytest.fixture
def auth_client(db_user):
    """Django test client authenticated as db_user."""
    from django.test import Client
    client = Client()
    client.force_login(db_user)
    return client


@pytest.fixture
def staff_client(staff_user):
    """Django test client authenticated as staff user."""
    from django.test import Client
    client = Client()
    client.force_login(staff_user)
    return client
