from django.db import models
from .servicio import Servicio

class Recompensa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos_requeridos = models.IntegerField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    servicio_gratuito = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
