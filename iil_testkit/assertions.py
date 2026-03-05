# iil_testkit/assertions.py — ADR-100
"""Common assertion helpers for platform Django repos."""


def assert_redirects_to_login(response, next_url=None):
    """Assert response redirects to login page."""
    assert response.status_code in (301, 302), (
        f"Expected redirect, got {response.status_code}"
    )
    location = response.get("Location", "")
    assert "/login" in location or "/accounts/login" in location, (
        f"Expected redirect to login, got: {location}"
    )


def assert_htmx_response(response, status_code=200):
    """Assert response is a valid HTMX partial (not full page)."""
    assert response.status_code == status_code, (
        f"Expected {status_code}, got {response.status_code}"
    )
    content = response.content.decode()
    assert "<html" not in content, "HTMX response should not contain full <html> tag"


def assert_no_n_plus_one(queries, threshold=5):
    """Assert query count is within acceptable threshold."""
    assert len(queries) <= threshold, (
        f"Possible N+1: {len(queries)} queries (threshold: {threshold})"
    )
