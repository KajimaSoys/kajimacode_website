import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = (os.environ.get('DEBUG') == 'True')
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get("ALLOWED_HOSTS", "").split(","),
    )
)

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080"  # from nginx in prod
]
CORS_ALLOWED_ORIGINS.extend(
    filter(
        None,
        os.environ.get("CORS_ALLOWED_ORIGINS", "").split(","),
    )
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

CSRF_COOKIE_SECURE = (os.environ.get('CSRF_COOKIE_SECURE', False) == 'True')
SESSION_COOKIE_SECURE = (os.environ.get('SESSION_COOKIE_SECURE', False) == 'True')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/app/kajimasoys_portfolio/cache'
    }
}

# KajimaPush setup
RECIPIENT_TOKEN = os.environ.get("RECIPIENT_TOKEN")
TELEPUSH_URL = os.environ.get("TELEPUSH_URL")
