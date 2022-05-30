from email.policy import default
from django import forms
from django.db import models

# Create your models here.
class TipoCategoria(models.Model):
    idTipoCategoria = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreTipoCategoria = models.CharField(max_length=50,verbose_name='Tipo de Categoría')

    def __str__(self):
        return self.nombreTipoCategoria


class Productos(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    nombre = models.CharField(max_length=50, verbose_name='Nombre producto')
    img = models.ImageField(upload_to = 'productos/static/productos/img/', default='', verbose_name = 'Imagen Producto')
    descripcion = models.CharField(max_length=200,null=True, blank=True, verbose_name='Descripción producto')
    categoria = models.ForeignKey(TipoCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
