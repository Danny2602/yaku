from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Sum
from django.db.models.functions import ExtractYear, ExtractMonth
from .models import Comunicado, Configuracion, Lectura, Evento, Excedente, HistorialPropietario,Recaudacion, Asistencia, Consumo
from calendar import month_name
meses_espanol = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

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

def comunicados_by_mes(request):
        # Consulta que obtiene el número de comunicados agrupados por mes
        datos = (Comunicado.objects
                .annotate(mes=ExtractMonth('fecha_com'))
                .values('mes')
                .annotate(total=Count('id_com'))
                .order_by('mes'))
        meses = [meses_espanol[item['mes'] - 1] for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'meses': meses, 'total': total})

def configuraciones_by_anio(request):
        # Consulta que obtiene el número de configuraciones agrupadas por año de creación
        datos = (Configuracion.objects
                .annotate(anio=ExtractYear('creacion_con'))
                .values('anio')
                .annotate(total=Count('id_con'))
                .order_by('anio'))
        anios = [item['anio'] for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'anios': anios, 'total': total})

def lectura_by_estado(request):
        # Consulta que obtiene el total de lecturas agrupadas por mes y estado "COBRADA"
        datos = (Lectura.objects
                .filter(estado_lec='COBRADA')
                .annotate(mes=ExtractMonth('fecha_creacion_lec'))
                .values('mes')
                .annotate(total=Count('id_lec'))
                .order_by('mes'))
        meses = [meses_espanol[item['mes'] - 1] for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'meses': meses, 'total': total})

def eventos_by_anio(request):
        # Consulta que obtiene el número de eventos agrupados por año
        datos = (Evento.objects
                .annotate(anio=ExtractYear('fecha_hora_eve'))
                .values('anio')
                .annotate(total=Count('id_eve'))
                .order_by('anio'))
        anios = [item['anio'] for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'anios': anios, 'total': total})

def excedentes_by_tarifa(request):
        # Consulta que obtiene el total de excedentes agrupados por tarifa
        datos = (Excedente.objects
                .values('id_tar')
                .annotate(total=Count('id_ex'))
                .order_by('id_tar'))
        tarifas = [item['id_tar'] for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'tarifas': tarifas, 'total': total})

def historial_by_estado(request):
        # Consulta que obtiene el total de historiales agrupados por estado
        datos = (HistorialPropietario.objects
                .values('estado_his')
                .annotate(total=Count('id_his'))
                .order_by('estado_his'))
        estados = [item['estado_his'] for item in datos]
        total = [item['total'] for item in datos]
        return JsonResponse({'estados': estados, 'total': total})