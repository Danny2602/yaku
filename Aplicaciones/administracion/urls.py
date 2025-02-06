from django.urls import path
from . import views

urlpatterns = [
    path('recaudacion/orecaudacion_by_anio/', views.recaudacion_by_anio, name='recaudacion_by_anio'),
    path('asistencia/asistencia_by_tipo/', views.asistencia_by_tipo, name='asistencia_by_tipo'),
    path('asistencia/asistencia_anual/', views.asistencia_anual, name='asistencia_anual'),
    path('consumo/consumo_by_estado/', views.consumo_by_estado, name='consumo_by_estado'),

]