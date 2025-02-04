from django.contrib import admin
from .models import Asistencia, Comunicado, Configuracion, Consumo, Detalle, Evento, Excedente, HistorialPropietario, Impuesto, Lectura, Medidor, Perfil, Recaudacion, Ruta, Socio, Tarifa, TipoEvento, Usuario

# Registra tus modelos aquí

class RecaudacionAdmin(admin.ModelAdmin):
    list_display = ('id_rec', 'numero_factura_rec', 'numero_autorizacion_rec', 'fecha_hora_autorizacion_rec', 'ambiente_rec', 'emision_rev', 'clave_acceso_rec', 'email_rec', 'observacion_rec', 'fk_id_soc', 'nombre_rec', 'identificacion_rec', 'direccion_rec', 'estado_rec', 'fecha_emision_rec', 'fecha_creacion_rec', 'fecha_actualizacion_rec')
    list_filter = ('estado_rec', 'fecha_emision_rec', 'fecha_creacion_rec', 'fecha_actualizacion_rec')
    search_fields = ('id_rec', 'numero_factura_rec', 'numero_autorizacion_rec', 'fecha_hora_autorizacion_rec', 'ambiente_rec', 'emision_rev', 'clave_acceso_rec', 'email_rec', 'observacion_rec', 'fk_id_soc__identificacion_soc', 'nombre_rec', 'identificacion_rec', 'direccion_rec', 'estado_rec', 'fecha_emision_rec', 'fecha_creacion_rec', 'fecha_actualizacion_rec')

class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id_asi', 'fk_id_eve', 'fk_id_soc', 'tipo_asi', 'valor_asi', 'atraso_asi', 'valor_atraso_asi', 'creacion_asi', 'actualizacion_asi')
    list_filter = ('tipo_asi', 'creacion_asi', 'actualizacion_asi')
    search_fields = ('id_asi', 'fk_id_eve__descripcion_eve', 'fk_id_soc__identificacion_soc', 'tipo_asi', 'valor_asi', 'atraso_asi', 'valor_atraso_asi', 'creacion_asi', 'actualizacion_asi')

class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('id_com', 'fecha_com', 'mensaje_com', 'actualizacion_com', 'creacion_com')
    list_filter = ('fecha_com', 'actualizacion_com', 'creacion_com')
    search_fields = ('id_com', 'fecha_com', 'mensaje_com', 'actualizacion_com', 'creacion_com')

class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ('id_con', 'nombre_con', 'ruc_con', 'logo_con', 'telefono_con', 'direccion_con', 'email_con', 'servidor_con', 'puerto_con', 'password_con', 'creacion_con', 'actualizacion_con', 'anio_inicial_con', 'mes_inicial_con')
    list_filter = ('nombre_con', 'ruc_con', 'telefono_con', 'direccion_con', 'email_con', 'servidor_con', 'puerto_con', 'creacion_con', 'actualizacion_con')
    search_fields = ('id_con', 'nombre_con', 'ruc_con', 'logo_con', 'telefono_con', 'direccion_con', 'email_con', 'servidor_con', 'puerto_con', 'password_con', 'creacion_con', 'actualizacion_con', 'anio_inicial_con', 'mes_inicial_con')

class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('id_consumo', 'anio_consumo', 'mes_consumo', 'estado_consumo', 'fecha_creacion_consumo', 'fecha_actualizacion_consumo', 'numero_mes_consumo', 'fecha_vencimiento_consumo')
    list_filter = ('anio_consumo', 'mes_consumo', 'estado_consumo', 'fecha_creacion_consumo', 'fecha_actualizacion_consumo', 'numero_mes_consumo', 'fecha_vencimiento_consumo')
    search_fields = ('id_consumo', 'anio_consumo', 'mes_consumo', 'estado_consumo', 'fecha_creacion_consumo', 'fecha_actualizacion_consumo', 'numero_mes_consumo', 'fecha_vencimiento_consumo')

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('id_det', 'fk_id_lec', 'fk_id_rec', 'cantidad_det', 'detalle_det', 'valor_unitario_det', 'subtotal_det', 'iva_det')
    list_filter = ('fk_id_lec', 'fk_id_rec', 'cantidad_det', 'detalle_det', 'valor_unitario_det', 'subtotal_det', 'iva_det')
    search_fields = ('id_det', 'fk_id_lec__id_lec', 'fk_id_rec__id_rec', 'cantidad_det', 'detalle_det', 'valor_unitario_det', 'subtotal_det', 'iva_det')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id_eve', 'descripcion_eve', 'fecha_hora_eve', 'lugar_eve', 'fk_id_te')
    list_filter = ('descripcion_eve', 'fecha_hora_eve', 'lugar_eve', 'fk_id_te')
    search_fields = ('id_eve', 'descripcion_eve', 'fecha_hora_eve', 'lugar_eve', 'fk_id_te__nombre_te')

class ExcedenteAdmin(admin.ModelAdmin):
    list_display = ('id_ex', 'id_tar', 'limite_minimo_ex', 'limite_maximo_ex', 'tarifa_ex', 'fecha_actualizacion_ex', 'fecha_creacion_ex')
    list_filter = ('id_tar', 'limite_minimo_ex', 'limite_maximo_ex', 'tarifa_ex', 'fecha_actualizacion_ex', 'fecha_creacion_ex')
    search_fields = ('id_ex', 'id_tar__nombre_tar', 'limite_minimo_ex', 'limite_maximo_ex', 'tarifa_ex', 'fecha_actualizacion_ex', 'fecha_creacion_ex')

class HistorialPropietarioAdmin(admin.ModelAdmin):
    list_display = ('id_his', 'fk_id_med', 'fk_id_soc', 'actualizacion_his', 'estado_his', 'observacion_his', 'fecha_cambio_his', 'creacion_his', 'propietario_actual_his')
    list_filter = ('fk_id_med', 'fk_id_soc', 'actualizacion_his', 'estado_his', 'fecha_cambio_his', 'creacion_his', 'propietario_actual_his')
    search_fields = ('id_his', 'fk_id_med__numero_med', 'fk_id_soc__identificacion_soc', 'actualizacion_his', 'estado_his', 'observacion_his', 'fecha_cambio_his', 'creacion_his', 'propietario_actual_his')

class ImpuestoAdmin(admin.ModelAdmin):
    list_display = ('id_imp', 'nombre_imp', 'descripcion_imp', 'porcentaje_imp')
    list_filter = ('nombre_imp', 'porcentaje_imp')
    search_fields = ('id_imp', 'nombre_imp', 'descripcion_imp', 'porcentaje_imp')

class LecturaAdmin(admin.ModelAdmin):
    list_display = ('id_lec', 'anio_lec', 'mes_lec', 'estado_lec', 'fecha_creacion_lec', 'fecha_actualizacion_lec')
    list_filter = ('anio_lec', 'mes_lec', 'estado_lec', 'fecha_creacion_lec', 'fecha_actualizacion_lec')
    search_fields = ('id_lec', 'anio_lec', 'mes_lec', 'estado_lec', 'fecha_creacion_lec', 'fecha_actualizacion_lec')

class MedidorAdmin(admin.ModelAdmin):
    list_display = ('id_med', 'numero_med', 'estado_med')
    list_filter = ('numero_med', 'estado_med')
    search_fields = ('id_med', 'numero_med', 'estado_med')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id_per', 'nombre_per', 'descripcion_per', 'estado_per', 'creacion_per', 'actualizacion_per')
    list_filter = ('nombre_per', 'estado_per', 'creacion_per', 'actualizacion_per')
    search_fields = ('id_per', 'nombre_per', 'descripcion_per', 'estado_per', 'creacion_per', 'actualizacion_per')

class RutaAdmin(admin.ModelAdmin):
    list_display = ('id_rut', 'nombre_rut', 'descripcion_rut', 'estado_rut')
    list_filter = ('nombre_rut', 'estado_rut')
    search_fields = ('id_rut', 'nombre_rut', 'descripcion_rut', 'estado_rut')

class SocioAdmin(admin.ModelAdmin):
    list_display = ('id_soc', 'identificacion_soc', 'direccion_soc', 'telefono_soc', 'email_soc', 'estado_soc')
    list_filter = ('identificacion_soc', 'estado_soc')
    search_fields = ('id_soc', 'identificacion_soc', 'nombre_soc', 'apellido_soc', 'direccion_soc', 'telefono_soc', 'email_soc', 'estado_soc')

class TarifaAdmin(admin.ModelAdmin):
    list_display = ('id_tar', 'nombre_tar', 'descripcion_tar')
    list_filter = ('nombre_tar',)
    search_fields = ('id_tar', 'nombre_tar', 'descripcion_tar', 'valor_tar')

class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ('id_te', 'nombre_te')
    list_filter = ('nombre_te',)
    search_fields = ('id_te', 'nombre_te', 'descripcion_te')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usu', 'nombre_usu', 'apellido_usu', 'email_usu', 'estado_usu')
    list_filter = ('nombre_usu', 'estado_usu')
    search_fields = ('id_usu', 'nombre_usu', 'apellido_usu', 'email_usu', 'estado_usu')

admin.site.register(Recaudacion, RecaudacionAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Comunicado, ComunicadoAdmin)
admin.site.register(Configuracion, ConfiguracionAdmin)
admin.site.register(Consumo, ConsumoAdmin)
admin.site.register(Detalle, DetalleAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Excedente, ExcedenteAdmin)
admin.site.register(HistorialPropietario, HistorialPropietarioAdmin)
admin.site.register(Impuesto, ImpuestoAdmin)
admin.site.register(Lectura, LecturaAdmin)
admin.site.register(Medidor, MedidorAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Ruta, RutaAdmin)
admin.site.register(Socio, SocioAdmin)
admin.site.register(Tarifa, TarifaAdmin)
admin.site.register(TipoEvento, TipoEventoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
