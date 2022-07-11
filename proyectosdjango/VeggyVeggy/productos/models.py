from email.policy import default
from itertools import product
from django import forms
from django.db import models
from pyexpat import model
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User

# Model de Categoría
class TipoCategoria(models.Model):
    idTipoCategoria = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreTipoCategoria = models.CharField(max_length=100,verbose_name='Tipo de Categoría')

    def __str__(self):
        return self.nombreTipoCategoria

#Model de los Productos
class Productos(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='Id Producto')
    stock = models.IntegerField(verbose_name='Stock') 
    nombre = models.CharField(max_length=100, verbose_name='Nombre producto')
    precio = models.IntegerField(verbose_name='Precio')
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
    correo= models.CharField(max_length=15,verbose_name="Correo")
    telefono= models.CharField(max_length=11, verbose_name="Telefono",blank = True, null = True)
    terminos= models.BooleanField(verbose_name="Terminos y Condiciones")

#Models para el carrito
#Model para clientes
class Clientes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.name

#Orden 
class Order(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_order = models.DateTimeField(auto_now_add=True)
    pagoRealizado= models.BooleanField(default=False)
    enPreparacion= models.BooleanField(default=False)
    enCamino= models.BooleanField(default=False)
    entregado= models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.cantidad for item in orderitems])
        return total

#Model para order item
class OrderItem(models.Model):
    product = models.ForeignKey(Productos, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_add = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.precio * self.cantidad
        return total
    