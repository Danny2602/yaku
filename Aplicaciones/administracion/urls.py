from django.urls import path
from . import views

urlpatterns = [
    path('recaudacion/open-modal/', views.recaudacion_modal, name='recaudacion_modal'),
    path('asistencia/open-modal/', views.asistencia_modal, name='asistencia_modal'),
]