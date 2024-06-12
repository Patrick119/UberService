from django.db import models
from django.contrib.auth.models import User
from .orden_servicio import OrdenServicio
from .profesional import Profesional

class Reseña(models.Model):
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
