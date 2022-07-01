#!/usr/bin/env bash
#!/bin/sh

echo "PostgreSQL started"

echo "Make migrations"
python manage.py makemigrations

echo "Accept migrations"
python manage.py migrate

echo "Start server at port 8000"
python manage.py runserver 0.0.0.0:8000