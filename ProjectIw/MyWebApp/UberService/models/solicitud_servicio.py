from django.db import models
from django.contrib.auth.models import User
from .profesion import Profesion

class SolicitudServicio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    fecha_hora_solicitada = models.DateTimeField()
    presupuesto_ofrecido = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
