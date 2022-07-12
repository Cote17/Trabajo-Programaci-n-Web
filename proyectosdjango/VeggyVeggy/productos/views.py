from pickle import NONE
import re
import time
from telnetlib import TM
from turtle import delay
from django.shortcuts import render, redirect
from productos.formulario import ProductosForm, UsersForm
from .models import Productos, Users, NewUser, Clientes, Order, OrderItem
from .formulario import ProductosForm, UsersForm, NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
import requests
import datetime

# Create your views here.

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
                    cliente, created = Clientes.objects.get_or_create(user=request.user,name=request.user.username,email=request.user.email)
                    login(request,user)
                    body= {"username": usernameN ,"password" : passwordN} #Se crea un json con info de usuario que creado
                    r = requests.post('http://localhost:8000/api/loginpagina',data=json.dumps(body)) #Creación del token
                    print(r.text)#Te muestra el token o errores
            return render(request,"productos/Registro.html",datos)
        time.sleep(1)
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
                if(username ==  "admin"):
                    cliente, created = Clientes.objects.get_or_create(user=request.user,name=request.user.username,email="admin@gmail.com")
                else:
                    cliente, created = Clientes.objects.get_or_create(user=request.user,name=request.user.username,email=request.user.email)
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

def updateItem(request):
    data=json.loads(request.body)
    idProducto= data['idProducto']
    action = data['action']
    
    print('Action: ', action)
    print('idProducto: ', idProducto)

    cliente = request.user.clientes
    product = Productos.objects.get(idProducto=idProducto)
    order, created = Order.objects.get_or_create(cliente = cliente, complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    
    if action == 'add':
        orderItem.cantidad = (orderItem.cantidad + 1)
        product.stock = (product.stock - 1)
    elif action == 'remove':
        orderItem.cantidad = (orderItem.cantidad - 1)
        product.stock = (product.stock + 1)
        
    orderItem.save()
    product.save()
    
    if orderItem.cantidad <= 0:
        orderItem.delete()
        
    return JsonResponse('Producto se añadido', safe=False)

def tiendita(request):
    if request.user.is_authenticated:
        cliente = request.user.clientes
        order, created = Order.objects.get_or_create(cliente = cliente, complete = False )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total' : 0, 'get_cart_items':0}
        cartItems = order['get_cartI_items']


def carrito(request):
    if request.user.is_authenticated:
        #cliente, created = Clientes.objects.get_or_create(user=request.user)
        cliente, created = Clientes.objects.get_or_create(user=request.user,name=request.user.username,email=request.user.email)
        order,created = Order.objects.get_or_create(cliente = cliente, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0 , 'get_cart_items':0}
        cartItems = order ['get_cart_items']
    context = {'items':items, 'order': order, 'cartItems':cartItems}
    return render(request, 'productos/carrito.html',context)

@login_required
def Dpago(request):
    return render(request, "productos/Dpago.html")

@login_required
def pago(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        cliente = request.user.clientes
        order, created = Order.objects.get_or_create(cliente = cliente, complete = False )

        order.transaction_id = transaction_id
        if order.get_cart_total >0:
            order.complete = True
            order.pagoRealizado = True
        else:
            if order.get_cart_items>0:
                order.pagoRealizado = True
                order.complete = True
            else:
                return JsonResponse('No existen productos!', safe=False)
        order.save()
        return redirect(seguimiento)
    return JsonResponse('Pago realizado!', safe=False)

def historialPed(request):
    listaproductos = Order.objects.filter(cliente=request.user.clientes)
    print(listaproductos)
    data={
        'pedido' : listaproductos
    }
    return render(request,'productos/historialPed.html',data)
    
def seguimiento(request):
    if request.user.is_superuser:
        return redirect(cambioestado)
    else:
        #listaproductos = Order.objects.all()
        listaproductos = Order.objects.filter(cliente=request.user.clientes, complete=True, pagoRealizado=True,entregado=False)
        print(listaproductos)
        data={
            'pedido' : listaproductos
        }
    return render(request,'productos/seguimiento.html', data)

@user_passes_test(is_SU)
def cambioestado(request):
    listaproductos = Order.objects.filter(complete=True,entregado=False)
    print(listaproductos)
    data={
        'pedido' : listaproductos
    }
    return render(request,'productos/cambiarEstado.html',data)

@user_passes_test(is_SU)
def cambio(request,id):
    listaproductos = Order.objects.filter(complete=True,entregado=False)
    print(listaproductos)
    data={
        'pedido' : listaproductos
    }
    p=Order.objects.get(id=id)
    if(p.enCamino==True):
        p.entregado = True
    elif (p.enPreparacion ==True):
        p.enCamino = True
    elif(p.pagoRealizado == True):
        p.enPreparacion = True
    p.save()
    return redirect(cambioestado)