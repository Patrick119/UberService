from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from .profesion import Profesion

class Profesional(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    numero_licencia = models.CharField(max_length=100)
    años_experiencia = models.IntegerField()
    bio = models.TextField()
    tarifa_hora = models.DecimalField(max_digits=8, decimal_places=2)
    ubicacion = gis_models.PointField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
