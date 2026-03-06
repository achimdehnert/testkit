# tests/plugin/conftest.py
# pytester runs each test in a subprocess — fully isolated from Django.
# The parent pytest session has Django loaded, but pytester subprocesses are clean.
# Declaring pytest_plugins here makes pytester available in this directory.
pytest_plugins = ["pytester"]
