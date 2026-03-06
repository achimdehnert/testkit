# tests/test_plugin.py — Django-context tests only (no pytester)


def test_should_register_no_naming_convention_marker(pytestconfig):
    ini_lines = pytestconfig.getini("markers")
    assert any("no_naming_convention" in line for line in ini_lines)


def test_should_accept_relax_naming_option(pytestconfig):
    val = pytestconfig.getoption("--relax-naming", default=False)
    assert val is False


def test_should_read_iil_naming_mode_ini(pytestconfig):
    mode = pytestconfig.getini("iil_naming_mode")
    assert mode in ("error", "warn")
