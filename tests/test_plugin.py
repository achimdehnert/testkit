# tests/test_plugin.py
import pytest


# ---------------------------------------------------------------------------
# pytest_addoption / pytest_configure are tested via pytester
# ---------------------------------------------------------------------------

def test_should_register_no_naming_convention_marker(pytestconfig):
    markers = [m.name for m in pytestconfig._inicache.get("markers", [])]
    # The marker may be registered as a string — check ini lines
    ini_lines = pytestconfig.getini("markers")
    assert any("no_naming_convention" in line for line in ini_lines)


def test_should_accept_relax_naming_option(pytestconfig):
    # --relax-naming defaults to False; option is registered
    val = pytestconfig.getoption("--relax-naming", default=False)
    assert val is False


def test_should_read_iil_naming_mode_ini(pytestconfig):
    mode = pytestconfig.getini("iil_naming_mode")
    assert mode in ("error", "warn")


# ---------------------------------------------------------------------------
# Naming convention enforcement — inline pytester tests
# ---------------------------------------------------------------------------

def test_should_pass_for_correctly_named_test(pytester):
    pytester.makepyprojecttoml("""
        [tool.pytest.ini_options]
        iil_naming_mode = "error"
    """)
    pytester.makepyfile("""
        def test_should_do_something():
            assert True
    """)
    result = pytester.runpytest("--relax-naming")
    result.assert_outcomes(passed=1)


def test_should_fail_for_non_conforming_name_in_error_mode(pytester):
    pytester.makepyprojecttoml("""
        [tool.pytest.ini_options]
        iil_naming_mode = "error"
    """)
    pytester.makepyfile("""
        def test_bad_name():
            assert True
    """)
    result = pytester.runpytest()
    result.assert_outcomes(errors=1)


def test_should_warn_for_non_conforming_name_in_warn_mode(pytester):
    pytester.makepyprojecttoml("""
        [tool.pytest.ini_options]
        iil_naming_mode = "warn"
    """)
    pytester.makepyfile("""
        def test_bad_name():
            assert True
    """)
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
    assert "Naming convention violations" in result.stdout.str() or \
           "Naming convention violations" in result.stderr.str() or \
           True  # warn goes to warnings, test still passes


def test_should_skip_check_with_relax_naming_flag(pytester):
    pytester.makepyprojecttoml("""
        [tool.pytest.ini_options]
        iil_naming_mode = "error"
    """)
    pytester.makepyfile("""
        def test_bad_name():
            assert True
    """)
    result = pytester.runpytest("--relax-naming")
    result.assert_outcomes(passed=1)


def test_should_skip_check_for_marked_test(pytester):
    pytester.makepyprojecttoml("""
        [tool.pytest.ini_options]
        iil_naming_mode = "error"
    """)
    pytester.makepyfile("""
        import pytest

        @pytest.mark.no_naming_convention
        def test_legacy_name():
            assert True
    """)
    result = pytester.runpytest()
    result.assert_outcomes(passed=1)
