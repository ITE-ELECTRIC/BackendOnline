#!/bin/sh

echo "Esperando a que la base de datos esté lista..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Aplicando migraciones..."
python manage.py migrate

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "Levantando servidor..."
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
