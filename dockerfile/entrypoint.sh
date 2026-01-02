#!/bin/sh

echo "Running migrations"
python manage.py migrate --noinput

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Starting app"
exec daphne -b 0.0.0.0 -p 8000 first_step_app.asgi:application