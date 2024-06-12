from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gis_models

class Profesion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

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

class Servicio(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class ImagenServicio(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    url_imagen = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

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

class Oferta(models.Model):
    solicitud_servicio = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    precio_ofrecido = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class OrdenServicio(models.Model):
    solicitud_servicio = models.ForeignKey(SolicitudServicio, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    fecha_hora_inicio = models.DateTimeField()
    fecha_hora_fin = models.DateTimeField()
    estado = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Reseña(models.Model):
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    comentario = models.TextField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Pago(models.Model):
    orden_servicio = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20)
    metodo_pago = models.CharField(max_length=50)
    id_transaccion = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

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

class DisponibilidadProfesional(models.Model):
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class MetodoPagoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_pago = models.CharField(max_length=50)
    numero_cuenta = models.CharField(max_length=100)
    fecha_expiracion = models.DateField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class ResumenReseñasProfesional(models.Model):
    profesional = models.OneToOneField(Profesional, on_delete=models.CASCADE)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2)
    total_reseñas = models.IntegerField()
    puntos_acumulados = models.IntegerField(default=0)
    posicion_clasificacion = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class AjusteTarifa(models.Model):
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    tarifa_minima = models.DecimalField(max_digits=8, decimal_places=2)
    tarifa_maxima = models.DecimalField(max_digits=8, decimal_places=2)
    incremento_urgencia = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Puntos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Recompensa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos_requeridos = models.IntegerField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    servicio_gratuito = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Desafio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    puntos_recompensa = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class ProfesionalCercano(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    distancia = models.FloatField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('usuario', 'profesional')
