from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.stock.models import Producto


class Venta(models.Model):
    documentos = (
        ('0', 'Cedula'),
        ('1', 'Cedula Extrangeria'),
        ('2', 'Pasaporte'),

    )

    fecha = models.DateField()
    numero_factura = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    tipodocumento = models.CharField('tipo documento', max_length=1, choices=documentos)
    numerodocumento = models.CharField(max_length=15)
    nombrecliente = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Ventas"
        verbose_name = "Venta"
        ordering = ['id']


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Detalles de ventas"
        verbose_name = "Detalle de venta"
        ordering = ['id']
