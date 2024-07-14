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

# Ejecutar la aplicación con docker-compose

# 1. Crear las imágenes 
docker-compose up --build

# 2. Probar en estas urls

api_usuarios debería estar accesible en http://127.0.0.1:8003/api/v1/usuarios/.
sitio_usuarios debería estar accesible en http://127.0.0.1:8004/carga/carga-masiva/.

