from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum
from django.db.models.functions import ExtractYear
from .models import Recaudacion,Asistencia,Consumo

def recaudacion_by_anio(request):
        datos = (Recaudacion.objects
                .annotate(anio=ExtractYear('fecha_creacion_rec'))
                .values('anio')
                .annotate(total=Count('id_rec'))
                .order_by('anio'))
        anio = [str(item['anio']) for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'anio': anio, 'total':total})

def asistencia_by_tipo(request):
        #los valores de asistencia agrupados por el tipo de asistencia.
        datos = (Asistencia.objects
                .values('tipo_asi')
                .annotate(total=Sum('valor_asi'))
                .order_by('tipo_asi'))
        tipo = [item['tipo_asi'] for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'tipo': tipo, 'total': total})

def asistencia_anual(request):
        # Consulta que obtiene el valor total de asistencia agrupado por año de creación
        datos = (Asistencia.objects
                .annotate(anio=ExtractYear('creacion_asi'))
                .values('anio')
                .annotate(total=Sum('valor_asi'))
                .order_by('anio'))
        anios = [str(item['anio']) for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'anios': anios, 'total': total})

def consumo_by_estado(request):
    # Consulta que obtiene el total de consumo agrupado por estado
    datos = (Consumo.objects
             .values('estado_consumo')
             .annotate(total=Count('id_consumo'))
             .order_by('estado_consumo'))
    estados = [item['estado_consumo'] for item in datos]
    total = [item['total'] for item in datos]
    return JsonResponse({'estados': estados, 'total': total})

# Comentario:
# Esta consulta obtiene el total de consumo agrupado por estado.
# Se puede utilizar una gráfica de pastel para visualizar los datos, donde cada porción representa un estado y su tamaño el total de consumo.