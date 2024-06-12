from django.db import models
from django.contrib.auth.models import User

class MetodoPagoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=50)
    numero_cuenta = models.CharField(max_length=100)
    fecha_expiracion = models.DateField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
