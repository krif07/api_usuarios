# Dockerfile
# Utiliza una imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /usr/src/app

# Copia los archivos de requerimientos
COPY requirements.txt ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del proyecto
COPY . .

# Expone el puerto de Django (8000 por defecto)
EXPOSE 8000

# Define el comando de inicio
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
