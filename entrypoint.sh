#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn kajimasoys_portfolio.wsgi:application --bind 0.0.0.0:8000