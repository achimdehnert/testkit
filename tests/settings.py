SECRET_KEY = "test-secret-key-not-for-production"
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
]
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]
SESSION_ENGINE = "django.contrib.sessions.backends.db"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
