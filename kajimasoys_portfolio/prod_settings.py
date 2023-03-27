import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = (os.environ.get('KAJIMASOYS_PORTFOLIO_DEBUG') == 'True')
ALLOWED_HOSTS = os.environ.get('KAJIMASOYS_PORTFOLIO_ALLOWED_HOSTS', '127.0.0.1').split(',')
SECRET_KEY = os.environ.get('KAJIMASOYS_PORTFOLIO_SECRET_KEY')

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",# from nginx in prod
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('KAJIMASOYS_PORTFOLIO_POSTGRES_NAME'),
        'USER': os.environ.get('KAJIMASOYS_PORTFOLIO_POSTGRES_USER'),
        'PASSWORD': os.environ.get('KAJIMASOYS_PORTFOLIO_POSTGRES_PASSWORD'),
        'HOST': os.environ.get('KAJIMASOYS_PORTFOLIO_POSTGRES_HOST'),
        'PORT': os.environ.get('KAJIMASOYS_PORTFOLIO_POSTGRES_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

CSRF_COOKIE_SECURE = (os.environ.get('KAJIMASOYS_PORTFOLIO_CSRF_COOKIE_SECURE', False) == 'True')
SESSION_COOKIE_SECURE = (os.environ.get('KAJIMASOYS_PORTFOLIO_SESSION_COOKIE_SECURE', False) == 'True')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'home/kajimasoys/kajimasoys_portfolio/kajimasoys_portfolio/cache'
    }
}
