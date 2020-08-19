from django.db import models


# Create your models here.


class Categorias(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['id']


class Producto(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='Producto', blank=True, null=True)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['id']
