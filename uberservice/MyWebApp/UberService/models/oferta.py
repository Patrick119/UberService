from django.db import models
from .solicitud_servicio import SolicitudServicio
from .profesional import Profesional

class Oferta(models.Model):
    solicitud_servicio = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    precio_ofrecido = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
