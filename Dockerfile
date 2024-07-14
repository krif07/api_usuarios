# Dockerfile
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos y instalar dependencias
COPY requirements.txt requirements_api.txt
COPY requirements.txt requirements_sitio.txt

RUN pip install --no-cache-dir -r requirements_api.txt
RUN pip install --no-cache-dir -r requirements_sitio.txt

# Copiar los archivos del proyecto
COPY api_usuarios /app/api_usuarios
COPY sitio_usuarios /app/sitio_usuarios

# Ejecutar las migraciones para ambas aplicaciones
WORKDIR /app/api_usuarios
RUN python manage.py migrate

WORKDIR /app/sitio_usuarios
RUN python manage.py migrate

# Exponer los puertos 8000 y 8003
EXPOSE 8000
EXPOSE 8003

# Comando para ejecutar ambas aplicaciones con gunicorn
CMD ["sh", "-c", "gunicorn api_usuarios.wsgi:application --bind 0.0.0.0:8004 & gunicorn sitio_usuarios.wsgi:application --bind 0.0.0.0:8001"]
