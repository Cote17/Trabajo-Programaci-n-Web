from email.policy import default
from django import forms
from django.db import models
from pyexpat import model
from tabnanny import verbose
from unittest.util import _MAX_LENGTH

# Model de Categoría
class TipoCategoria(models.Model):
    idTipoCategoria = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreTipoCategoria = models.CharField(max_length=100,verbose_name='Tipo de Categoría')

    def __str__(self):
        return self.nombreTipoCategoria

#Model de los Productos
class Productos(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    nombre = models.CharField(max_length=100, verbose_name='Nombre producto')
    img = models.ImageField(null=True,upload_to = 'productos/static/productos/img/', default='', verbose_name = 'Imagen Producto')
    descripcion = models.CharField(max_length=500,null=True, blank=True, verbose_name='Descripción producto')
    categoria = models.ForeignKey(TipoCategoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#Model para Usuarios
class Users(models.Model):
    usrN= models.CharField(max_length=30,verbose_name="Nombre Usuario")
    pswrdN= models.CharField(max_length=15, verbose_name="Contraseña")

class NewUser(models.Model):
    nombre= models.CharField(max_length=30,verbose_name="Nombre Usuario",blank = True, null = True)
    password= models.CharField(max_length=15, verbose_name="Contraseña")
    password2= models.CharField(max_length=15,verbose_name="Confirmar Contraseña")
    #usuario= models.CharField(max_length=30, verbose_name="Ciudad")
    correo= models.CharField(max_length=15,verbose_name="Correo")
    telefono= models.CharField(max_length=8, verbose_name="Telefono")
    terminos= models.BooleanField(verbose_name="Terminos y Condiciones")

    
