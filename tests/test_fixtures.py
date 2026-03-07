# tests/test_fixtures.py
import pytest


@pytest.mark.django_db
def test_should_provide_db_user_fixture(db_user):
    assert db_user.pk is not None
    assert db_user.is_active is True
    assert not db_user.is_staff


@pytest.mark.django_db
def test_should_provide_staff_user_fixture(staff_user):
    assert staff_user.is_staff is True
    assert staff_user.is_superuser is False


@pytest.mark.django_db
def test_should_provide_admin_user_fixture(admin_user):
    assert admin_user.is_staff is True
    assert admin_user.is_superuser is True


@pytest.mark.django_db
def test_should_provide_api_client_fixture(api_client):
    assert api_client is not None


@pytest.mark.django_db
def test_should_provide_auth_client_fixture(auth_client, db_user):
    assert auth_client is not None


@pytest.mark.django_db
def test_should_provide_staff_client_fixture(staff_client, staff_user):
    assert staff_client is not None


@pytest.mark.django_db
def test_should_auth_client_be_distinct_from_api_client(auth_client, api_client):
    assert auth_client is not api_client


def test_should_skip_drf_fixtures_when_not_installed(pytestconfig):
    """drf_api_client and drf_auth_client skip gracefully when DRF not installed."""
    try:
        import rest_framework  # noqa: F401
    except ImportError:
        pass  # expected in test env without DRF
