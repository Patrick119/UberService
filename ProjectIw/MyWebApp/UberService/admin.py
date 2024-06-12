from django.contrib import admin
from .models.profesion import Profesion
from .models.profesional import Profesional
from .models.servicio import Servicio
from .models.imagen_servicio import ImagenServicio
from .models.solicitud_servicio import SolicitudServicio
from .models.oferta import Oferta
from .models.orden_servicio import OrdenServicio
from .models.reseña import Reseña
from .models.pago import Pago
from .models.direccion import Direccion
from .models.disponibilidad_profesional import DisponibilidadProfesional
from .models.metodo_pago_usuario import MetodoPagoUsuario
from .models.resumen_reseñas_profesional import ResumenReseñasProfesional
from .models.ajuste_tarifa import AjusteTarifa
from .models.puntos import Puntos
from .models.recompensa import Recompensa
from .models.desafio import Desafio

admin.site.register(Profesion)
admin.site.register(Profesional)
admin.site.register(Servicio)
admin.site.register(ImagenServicio)
admin.site.register(SolicitudServicio)
admin.site.register(Oferta)
admin.site.register(OrdenServicio)
admin.site.register(Reseña)
admin.site.register(Pago)
admin.site.register(Direccion)
admin.site.register(DisponibilidadProfesional)
admin.site.register(MetodoPagoUsuario)
admin.site.register(ResumenReseñasProfesional)
admin.site.register(AjusteTarifa)
admin.site.register(Puntos)
admin.site.register(Recompensa)
admin.site.register(Desafio)
