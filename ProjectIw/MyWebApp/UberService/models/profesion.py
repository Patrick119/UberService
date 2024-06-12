from django.db import models

class Profesion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
