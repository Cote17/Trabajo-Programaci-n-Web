from pickle import NONE
import re
import time
from telnetlib import TM
from turtle import delay
from django.shortcuts import render, redirect
from productos.formulario import ProductosForm, UsersForm
from .models import Productos, Users, NewUser
from .formulario import ProductosForm, UsersForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
import requests

# Create your views here.
toki = None

def is_SU(user):
    return (user.is_authenticated and user.is_superuser)

@login_required
def home(request):
    return render(request, "productos/index.html")

@login_required
def contactanos(request):
    return render(request, "productos/Contactanos.html")

@login_required
def articulos(request):
    productos = Productos.objects.all()
    datos ={
        'productos':productos
    }
    return render(request, "productos/Productos.html",datos)

#Registro de usuario con el token
def registro(request):
    datos={
        'form':NewUserForm(use_required_attribute=False)
    }
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            #Se obtienen los datos del usuario desde formulario
            usernameN = form.cleaned_data.get('nombre')
            passwordN = form.cleaned_data.get('password')
            passwordN2 = form.cleaned_data.get('password2')
            correo = form.cleaned_data.get('correo')
            fono = form.cleaned_data.get('telefono')
            TyC = form.cleaned_data.get('terminos')
            try:
                #vericar que el usuario exista
                user = User.objects.get(username = usernameN)
            except User.DoesNotExist:
                #si no existe se crea un nuevo usuario validando si es que las contraseñas son iguales
                if(passwordN == passwordN2):
                    user = User.objects.create_user(username = usernameN, email=correo, password = passwordN) 
                    user = authenticate(username=usernameN, password=passwordN)
                    my_group = Group.objects.get(name = 'Clientes')
                    user.groups.add(my_group)
                    login(request,user)
                    body= {"username": usernameN ,"password" : passwordN} #Se crea un json con info de usuario que creado
                    r = requests.post('http://localhost:8000/api/loginpagina',data=json.dumps(body)) #Creación del token
                    print(r.text)#Te muestra el token o errores
            return render(request,"productos/Registro.html",datos)
        time.sleep(2)
    return render(request,"productos/Registro.html",datos)

@login_required
def trabajaconnosotros(request):
    return render(request, "productos/Trabajaconnosotros.html")

@user_passes_test(is_SU)
def agregar_producto(request):
    datos = {
        'form': ProductosForm()
    }

    if request.method == 'POST':
        formulario = ProductosForm(request.POST or None, request.FILES or None) #Carga de archivos        
        if formulario.is_valid():
            formulario.save() #inserta la BD
            datos['mensaje'] = 'Se guardó Producto'
        else:
            datos['mensaje'] = 'NO se guardó Producto'
    
    return render(request, "productos/agregar-Producto.html",datos)

@user_passes_test(is_SU)
def modificar_producto(request, id):
    producto = Productos.objects.get(idProducto = id)

    datos = {
        'form': ProductosForm(instance = producto)
    }

    if request.method == 'POST':
        formulario = ProductosForm(request.POST or None, request.FILES or None, instance = producto)

        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'Se modificó producto'
            return redirect(articulos)
        else:
            datos['mensaje'] = 'NO se modificó producto'
            return render(request,'productos/modificar-producto.html',datos)

    return render(request,"productos/agregar-Producto.html", datos)

@user_passes_test(is_SU)
def eliminar_producto(request, id):
    producto = Productos.objects.get(idProducto = id)
    producto.delete() #delete de la BD
    return redirect(to='articulos')

def inisiarsesion(request):
    datos={
        'form':UsersForm()
    }
    if (request.method == 'POST'):
        form=UsersForm(request.POST)
        if form.is_valid():
            username = request.POST['usrN']
            password = request.POST['pswrdN']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,"productos/index.html")
    return render(request,"productos/Iniciarsesion.html",datos)
def recuperar(request):
    return render(request,"productos/recuperarContra.html")
    
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        time.sleep(5)
        return redirect(inisiarsesion)
    
    return render(request, "productos/cerrar-sesion.html")


@user_passes_test(is_SU)
def nuevoProdApi(request):
    global toki
    datos={
        'form':ProductosForm()
    }
    if request.method == 'POST':
        formulario = ProductosForm(request.POST or None, request.FILES or None) #se agrega request file para cargar imágenes
        if formulario.is_valid():
            idProducto=formulario.cleaned_data.get('idProducto')
            nombre=formulario.cleaned_data.get('nombre')
            img=formulario.cleaned_data.get('img')
            descripcion=formulario.cleaned_data.get('descripcion')
            body={"idProducto":idProducto,"nombre":nombre,"img":img,"descripcion":descripcion}
            headers={"authorization": "Token " + toki}
            r = requests.post('http://localhost:8000/api/lista_productos',data=json.dumps(body),header=headers) # se realiza la creacion de token
            print(r.text)
            datos['mensaje']='Guardados correctamente'
        else:
            datos['mensaje']='no se ha guardado uwu'
    return render(request,'productos/nuevoApi.html',datos)