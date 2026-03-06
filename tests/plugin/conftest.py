# tests/plugin/conftest.py
# Isolated conftest WITHOUT Django — required for pytester fixture to work.
# pytester cannot run inside a Django-enabled pytest session.
import os

os.environ.pop("DJANGO_SETTINGS_MODULE", None)
