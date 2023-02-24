import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = (os.environ.get('TEAM_PORTFOLIO_DEBUG') == 'True')
ALLOWED_HOSTS = os.environ.get('TEAM_PORTFOLIO_ALLOWED_HOSTS', '127.0.0.1').split(',')

SECRET_KEY = os.environ.get('TEAM_PORTFOLIO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('TEAM_PORTFOLIO_POSTGRES_NAME'),
        'USER': os.environ.get('TEAM_PORTFOLIO_POSTGRES_USER'),
        'PASSWORD': os.environ.get('TEAM_PORTFOLIO_POSTGRES_PASSWORD'),
        'HOST': os.environ.get('TEAM_PORTFOLIO_POSTGRES_HOST'),
        'PORT': os.environ.get('TEAM_PORTFOLIO_POSTGRES_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

CSRF_COOKIE_SECURE = (os.environ.get('TEAM_PORTFOLIO_CSRF_COOKIE_SECURE', False) == 'True')
SESSION_COOKIE_SECURE = (os.environ.get('TEAM_PORTFOLIO_SESSION_COOKIE_SECURE', False) == 'True')
