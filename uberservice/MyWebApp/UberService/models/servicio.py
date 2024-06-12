from django.db import models
from .profesional import Profesional

class Servicio(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
