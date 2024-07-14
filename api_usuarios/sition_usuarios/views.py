from django.shortcuts import render
import csv
from django.http import HttpResponse
from django.views import View
from usuarios.models import Usuario


class CargaMasivaView(View):
    def get(self, request):
        return render(request, 'carga_usuarios/carga_masiva.html')

    def post(self, request):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Invalid file format", status=400)

        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # Skip the header row

        for row in csv.reader(io_string, delimiter=','):
            Usuario.objects.create(
                nombre=row[0],
                apellido_paterno=row[1],
                apellido_materno=row[2],
                edad=row[3],
                nombre_cuenta=row[4],
                contrasena=row[5],
            )

        return HttpResponse("Carga masiva completada con éxito")
