from django.db import models

class Desafio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos_recompensa = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
