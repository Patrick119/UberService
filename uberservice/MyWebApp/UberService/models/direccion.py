from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calle = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
