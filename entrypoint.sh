#!/bin/sh

# echo "Esperando a que la base de datos esté lista..."
# while ! nc -z db 5432; do
#   sleep 1
# done

echo "Aplicando migraciones..."
python src/manage.py migrate

# TODO: Descomentar si se necesitan archivos estáticos
# echo "Recolectando archivos estáticos..."
# python src/manage.py collectstatic --noinput

echo "Levantando servidor..."
python src/manage.py runserver 0.0.0.0:8000
