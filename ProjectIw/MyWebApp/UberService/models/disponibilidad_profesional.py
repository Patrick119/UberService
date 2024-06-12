from django.db import models
from .profesional import Profesional

class DisponibilidadProfesional(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
