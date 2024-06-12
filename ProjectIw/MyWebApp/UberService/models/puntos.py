from django.db import models
from django.contrib.auth.models import User

class Puntos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
