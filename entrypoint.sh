#!/bin/sh
set -e

mkdir -p /app/db

python3 manage.py migrate

echo "Starting nginx $(nginx -v 2>&1 | awk -F/ '{print $2}')"
nginx
echo "Listening at: http://0.0.0.0:8080"

exec gunicorn config.wsgi:application --bind 0.0.0.0:8081 --workers 4
