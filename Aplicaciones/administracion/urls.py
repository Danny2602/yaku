from django.urls import path
from . import views

urlpatterns = [
    path('recaudacion/orecaudacion_by_anio/', views.recaudacion_by_anio, name='recaudacion_by_anio'),
    path('asistencia/asistencia_by_tipo/', views.asistencia_by_tipo, name='asistencia_by_tipo'),
    path('asistencia/asistencia_anual/', views.asistencia_anual, name='asistencia_anual'),
    path('consumo/consumo_by_estado/', views.consumo_by_estado, name='consumo_by_estado'),
    path('comunicados/comunicados_by_mes/', views.comunicados_by_mes, name='comunicados_by_mes'),
    path('configuraciones/configuraciones_by_anio/', views.configuraciones_by_anio, name='configuraciones_by_anio'),
    path('lectura/lectura_by_estado/', views.lectura_by_estado, name='lectura_by_estado'),
    path('eventos/eventos_by_anio/', views.eventos_by_anio, name='eventos_by_anio'),
    path('excedentes/excedentes_by_tarifa/', views.excedentes_by_tarifa, name='excedentes_by_tarifa'),
    path('historial/historial_by_estado/', views.historial_by_estado, name='historial_by_estado'),
]