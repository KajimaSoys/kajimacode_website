"""
Django settings for kajimasoys_portfolio project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# app-model ordering imports
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html


BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    # project apps
    'core.apps.CoreConfig',
    'requests.apps.RequestsConfig',
    'pages.apps.PagesConfig',

    # default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd parties
    'rest_framework',
    'corsheaders',
    'adminsortable2',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CSRF_TRUSTED_ORIGINS = ["https://kajimacode.com"]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ROOT_URLCONF = 'kajimasoys_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kajimasoys_portfolio.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# FILE_PATH_FIELD_DIRECTORY = 'rezal/apps/main/contract_db/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *


# app-model ordering

ADMIN_ORDERING = (
    (
        'core',
        (
            'Group',
            'Project',
            'ProjectImages',
            'Skill',
            'Work'
        )
    ),
    (
        'requests',
        (
            'Order',
            'Rate',
            'Feedback'
        )
    ),
    (
        'pages',
        (
            'Navbar',
            'Footer',
            'CookieElement',
            'RateElement',
            'MainPage',
            'ProjectsPage',
            'SkillsPage',
            'AboutPage',
            'TermsPage',
            'PrivacyPage',
            'CookiesPage'
        )
    ),
    ('auth', ('User', 'Group')),
)

LINKED_MODELS = [

]


def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request, app_label)

    if not app_dict:
        return

    NEW_ADMIN_ORDERING = []
    if app_label:
        for ao in ADMIN_ORDERING:
            if ao[0] == app_label:
                NEW_ADMIN_ORDERING.append(ao)
                break

    if not app_label:
        for app_key in list(app_dict.keys()):
            if not any(app_key in ao_app for ao_app in ADMIN_ORDERING):
                app_dict.pop(app_key)

    app_list = sorted(
        app_dict.values(),
        key=lambda x: [ao[0] for ao in ADMIN_ORDERING].index(x['app_label'])
    )

    # Обработка моделей и моделей-ссылок
    # print(f"target_app:\t{link['target_app']}\tapp_label:\t{app['app_label']}")

    for app in app_list:
        if app['app_label'] in [ao[0] for ao in ADMIN_ORDERING]:
            ao_models = next(ao[1] for ao in ADMIN_ORDERING if ao[0] == app['app_label'])
            updated_models = []

            for model_name in ao_models:
                # Добавляем оригинальные модели
                model = next((m for m in app['models'] if m['object_name'] == model_name), None)
                if model:
                    updated_models.append(model)

                # Добавляем модели-ссылки, если они есть
                link = next((link for link in LINKED_MODELS if
                             link['model_name'] == model_name and link['target_app'] == app['app_label']), None)
                if link:
                    model_url = reverse(f'admin:{link["source_app"].lower()}_{model_name.lower()}_changelist')
                    add_url = reverse(f'admin:{link["source_app"].lower()}_{model_name.lower()}_add')
                    updated_models.append({
                        'name': format_html('<a href="{}">{}</a>', model_url, link['model_name_verbose']),
                        'object_name': f'{model_name}Link',
                        'admin_url': model_url,
                        'add_url': add_url,
                    })

            app['models'] = updated_models

    return app_list


admin.AdminSite.get_app_list = get_app_list
