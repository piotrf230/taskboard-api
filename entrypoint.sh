#!/bin/sh

./manage.py collectstatic
./manage.py migrate
gunicorn taskboard_app.wsgi:application --bind 0.0.0.0:5000