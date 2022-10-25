#!/bin/bash
set -e

# Load base commands
python manage.py migrate --noinput
python manage.py initialize

if [[ $DJANGO_DEBUG -eq 0 ]]; then
  python manage.py collectstatic --noinput
  gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
else
  python manage.py runserver 8000
fi

