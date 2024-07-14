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
