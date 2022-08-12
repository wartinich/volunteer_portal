#!/usr/bin/env bash
#!/bin/sh

echo "PostgreSQL started"

echo "Collecting static..."
python manage.py collectstatic --no-input

echo "Static collecting finished"
python manage.py migrate

echo "Start server"
python manage.pt runserver 0.0.0.0:8000