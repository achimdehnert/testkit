# tests/test_assertions.py
import pytest

from iil_testkit.assertions import assert_htmx_response, assert_no_n_plus_one


def test_should_assert_no_n_plus_one_passes_within_threshold():
    assert_no_n_plus_one(list(range(3)), threshold=5)


def test_should_assert_no_n_plus_one_fails_above_threshold():
    with pytest.raises(AssertionError, match="Possible N\\+1"):
        assert_no_n_plus_one(list(range(10)), threshold=5)


def test_should_assert_htmx_rejects_full_html():
    class FakeResponse:
        status_code = 200
        content = b"<html><body>Full page</body></html>"

    with pytest.raises(AssertionError, match="full <html>"):
        assert_htmx_response(FakeResponse())
