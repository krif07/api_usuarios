# Paso 1: Crear un proyecto Django
# Primero, asegúrate de tener Django y django-ninja instalados en tu entorno. Puedes hacerlo con:

pip install django django-ninja
pip install requests

# Luego, crea los proyectos y las aplicaciones necesarias.

django-admin startproject api_usuarios
django-admin startproject sitio_usuarios
cd api_usuarios
django-admin startapp usuarios
cd ../sitio_usuarios
django-admin startapp carga_usuarios

# Realiza las migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecuta el servidor de desarrollo
python manage.py runserver

# Construir la imagen de Docker
docker build -t my_django_app .

# Ejecutar el contenedor
docker run -p 8000:8000 my_django_app

# Ejecutar la aplicación

# Paso 1: Navegar al Directorio de la Aplicación
cd /path/to/mi_proyecto/api_usuarios

# Paso 2: Construir la Imagen Docker
docker build -t api_usuarios_image .

# Paso 3: Ejecutar el Contenedor
docker run -d -p 8003:8000 --name api_usuarios_container api_usuarios_image

# Paso 4: Verificar que el Contenedor esté Corriendo
docker ps

# Paso 5: Acceder a la Aplicación
La aplicación debería estar accesible en http://127.0.0.1:8003.

# Otros pasos
docker stop api_usuarios_container
docker rm api_usuarios_container
docker logs api_usuarios_container
docker exec -it api_usuarios_container /bin/bash

