# Proyecto App Full Stack
## Descripción del Proyecto

Este proyecto tiene como objetivo evaluar la capacidad de resolución y aprendizaje en el desarrollo de aplicaciones Full Stack. El proyecto consiste en crear una API utilizando Django como backend y React.js como frontend. La aplicación debe permitir buscar películas, actores y series utilizando la base de datos abierta de IMDB.

## Requisitos del Proyecto

- **Backend**: Desarrollado en Python 3.8+ con Django 3+.
- **Frontend**: Desarrollado en React.js.
- **Base de Datos**: PostgreSQL.
- **Servidor**:  Nginx y Gunicorn con Docker.

## Funcionalidades

1. **Interfaz de Búsqueda**: Al estilo de Google, donde se pueden buscar películas, actores y series.
2. **Backend API**: Realiza un GET para obtener películas que contengan la palabra buscada en su nombre.
3. **Frontend**: Renderiza la página con React.js, permite ingresar texto en una caja de búsqueda y mostrar resultados debajo del botón de búsqueda.

## Instalación y Ejecución


1. **Clonar el Repositorio**:
git clone <url-del-repositorio>


2. **Configurar Variables de Entorno**:
Modifica el archivo `.env` con tus credenciales de base de datos y otros parámetros necesarios:**:

        DB_NAME=DB_NAME
        DB_USER=DB_USER
        DB_PASSWORD=DB_PASSWORD
        DB_HOST=db
        DB_PORT=5432
        DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost:8001
        DJANGO_SECRET_KEY=DJANGO_SECRET_KEY
        DJANGO_ALLOWED_HOSTS=localhost


3. **Corra los comandos de docker**:

        docker-compose up --build


## Pruebas

        http://localhost

        http://localhost/mipp/api/search

## Recursos de Ayuda

- [Django](https://www.djangoproject.com/)
- [React](https://reactjs.org/)
- [Material UI](https://mui.com/)
- [Docker](https://www.docker.com/)
- [Tutorial de Docker](https://docs.docker.com/get-started/)

