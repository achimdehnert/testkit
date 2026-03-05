# tests/test_factories.py
import pytest

from iil_testkit.factories import AdminUserFactory, StaffUserFactory, UserFactory


@pytest.mark.django_db
def test_should_create_user_with_factory():
    user = UserFactory()
    assert user.pk is not None
    assert user.username.startswith("user_")
    assert user.is_active is True
    assert user.check_password("testpass123")


@pytest.mark.django_db
def test_should_create_unique_usernames():
    u1 = UserFactory()
    u2 = UserFactory()
    assert u1.username != u2.username


@pytest.mark.django_db
def test_should_create_staff_user():
    user = StaffUserFactory()
    assert user.is_staff is True
    assert user.is_superuser is False


@pytest.mark.django_db
def test_should_create_admin_user():
    user = AdminUserFactory()
    assert user.is_staff is True
    assert user.is_superuser is True
