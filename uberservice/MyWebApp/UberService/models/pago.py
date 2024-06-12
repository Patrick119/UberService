from django.db import models
from .orden_servicio import OrdenServicio

class Pago(models.Model):
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20)
    metodo_pago = models.CharField(max_length=50)
    id_transaccion = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
