from django import forms
from django.forms import ModelForm
from .models import Productos 

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = ['idProducto','nombre','img','descripcion','categoria']

'''
class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria']
'''