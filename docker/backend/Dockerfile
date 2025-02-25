FROM python:3.8.3-alpine

WORKDIR /app

# Instalar dependencias esenciales
RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    netcat-openbsd \
    libffi-dev
# Instalar clientes esenciales
RUN apk update && apk add --no-cache \
    postgresql-client \
    netcat-openbsd

# Instalar dependencias de Python
COPY ./backend/requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar aplicación
COPY ./backend /app
COPY ./docker /app/docker

# Permisos de ejecución
RUN chmod +x /app/docker/backend/wsgi-entrypoint.sh

# Puerto necesario
EXPOSE 8001

# Entrypoint mejorado
ENTRYPOINT ["/app/docker/backend/wsgi-entrypoint.sh"]