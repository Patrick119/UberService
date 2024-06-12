from django.db import models
from .profesional import Profesional

class ResumenReseñasProfesional(models.Model):
    profesional = models.OneToOneField(Profesional, on_delete=models.CASCADE)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2)
    total_reseñas = models.IntegerField()
    puntos_acumulados = models.IntegerField(default=0)
    posicion_clasificacion = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
