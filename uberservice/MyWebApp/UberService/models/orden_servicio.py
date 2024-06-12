from django.db import models
from .solicitud_servicio import SolicitudServicio
from .oferta import Oferta

class OrdenServicio(models.Model):
    solicitud_servicio = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    estado = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
