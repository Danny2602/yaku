from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import ExtractYear
from .models import Recaudacion

def recaudacion_modal(request):
    datos = (Recaudacion.objects
             .annotate(anio=ExtractYear('fecha_creacion_rec'))
             .values('anio')
             .annotate(total=Count('id_rec'))
             .order_by('anio'))
    labels = [str(item['anio']) for item in datos]
    counts = [item['total'] for item in datos]
    return JsonResponse({'labels': labels, 'counts': counts})

def asistencia_modal(request):
    return render(request, 'admin/asistencia_modal.html')