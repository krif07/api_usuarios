from django.urls import path
from .views import CargaMasivaView

urlpatterns = [
    path('carga-masiva/', CargaMasivaView.as_view(), name='carga_masiva'),
]