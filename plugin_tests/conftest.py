# plugin_tests/conftest.py
# Top-level conftest for pytester-based plugin tests.
# No Django settings — pytester runs subprocesses in isolation.
pytest_plugins = ["pytester"]
