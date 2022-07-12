from dataclasses import fields
from django import forms
from django.forms import ModelForm
from productos.models import Productos, Users, NewUser

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = ['idProducto','nombre','precio','img','descripcion','categoria']

class UsersForm(ModelForm):
    pswrdN = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formulario__input','id':'contrasena','name':'contrasena'}))
    usrN = forms.CharField(widget=forms.TextInput(attrs={'class':'formulario__input','id':'nombre','name':'nombre'}))
    class Meta:
        model = Users
        fields= ['usrN','pswrdN']

class NewUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formulario__input','id':'password','name':'password'}),label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'formulario__input','id':'password2','name':'password2'}),label='')
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'formulario__input','id':'nombre','name':'nombre'}),label='')
    correo = forms.CharField(widget=forms.EmailInput(attrs={'class':'formulario__input','id':'correo','name':'correo'}),label='')
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class':'formulario__input','id':'telefono','name':'telefono'}),label='')
    terminos = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'formulario__checkbox','id':'terminos','name':'terminos'}),label='')

    class Meta:
        model = NewUser
        fields = ['nombre','telefono','correo','password','password2','terminos']
        
