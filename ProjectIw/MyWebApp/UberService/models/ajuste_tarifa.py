from django.db import models
from .profesion import Profesion

class AjusteTarifa(models.Model):
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    tarifa_minima = models.DecimalField(max_digits=8, decimal_places=2)
    tarifa_maxima = models.DecimalField(max_digits=8, decimal_places=2)
    incremento_urgencia = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
