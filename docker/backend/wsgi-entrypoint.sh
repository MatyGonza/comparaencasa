#!/bin/ash
set -eo pipefail

export PYTHONPATH="/app:${PYTHONPATH}"
wait_for_db() {
    echo "⌛ Esperando a PostgreSQL..."
    until pg_isready -h db -p 5432 -U postgres; do
        sleep 2
        echo "Reintentando conexión..."
    done
    echo "✅ ¡Conexión exitosa!"
}
main() {
    cd /app
    
    wait_for_db
    # Ejecutar migraciones
    echo "🔄 Aplicando migraciones..."
    python manage.py collectstatic --noinput

    python manage.py migrate --noinput
    python manage.py createsuperuser
    python manage.py loaddata miapp/fixtures/*.json

    # Iniciar Gunicorn con exec
    echo "🚀 Iniciando Gunicorn..."
    exec gunicorn api.wsgi:application \
        --bind 0.0.0.0:8001 \
        --workers ${GUNICORN_WORKERS:-2} \
        --threads ${GUNICORN_THREADS:-2} \
        --log-level ${LOG_LEVEL:-info} \
        --access-logfile - \
        --error-logfile -
        
}

main "$@"