# Paso 1: Crear un proyecto Django
# Primero, asegúrate de tener Django y django-ninja instalados en tu entorno. Puedes hacerlo con:

pip install django django-ninja

# Luego, crea los proyectos y las aplicaciones necesarias.

django-admin startproject api_usuarios
django-admin startproject sitio_usuarios
cd api_usuarios
django-admin startapp usuarios
cd ../sitio_usuarios
django-admin startapp carga_usuarios

