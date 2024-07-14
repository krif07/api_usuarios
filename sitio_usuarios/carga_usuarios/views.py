from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import csv
import io
import requests


class CargaMasivaView(View):
    def get(self, request):
        return render(request, 'carga_usuarios/carga_masiva.html')

    def post(self, request):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Formato de archivo inválido", status=400)

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # Saltar la fila de encabezado

        api_url = "http://apiusuarios:8000/api/v1/usuarios/"

        for row in csv.reader(io_string, delimiter=','):
            payload = {
                "nombre": row[0],
                "apellido_paterno": row[1],
                "apellido_materno": row[2],
                "edad": int(row[3]),
                "nombre_cuenta": row[4],
                "contrasena": row[5],
            }
            response = requests.post(api_url, json=payload)
            if response.status_code > 300:
                return HttpResponse(f"Error en la fila: {row} - {response.text}", status=response.status_code)

        return HttpResponse("Carga masiva completada con éxito")
