FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/sitio_usuarios
RUN python manage.py migrate

EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
