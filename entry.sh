#!/usr/bin/env sh
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py migrate
/opt/django-acme-challenger/venv/bin/uwsgi --ini /opt/django-acme-challenger/uwsgi.ini