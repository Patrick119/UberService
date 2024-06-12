from django.db import models
from django.contrib.auth.models import User
from .profesional import Profesional

class ProfesionalCercano(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    distancia = models.FloatField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('usuario', 'profesional')
