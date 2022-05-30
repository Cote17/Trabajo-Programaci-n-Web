import re
from django.shortcuts import render, redirect

from productos.formulario import ProductosForm
from .models import Productos
from .formulario import ProductosForm

# Create your views here.
def home(request):
    return render(request, "productos/index.html")

def contactanos(request):
    return render(request, "productos/Contactanos.html")

def iniciosesion(request):
    return render(request, "productos/Iniciarsesion.html")

def articulos(request):
    productos = Productos.objects.all()
    datos ={
        'productos':productos
    }
    return render(request, "productos/Productos.html",datos)

def registro(request):
    return render(request, "productos/Registro.html")

def trabajaconnosotros(request):
    return render(request, "productos/Trabajaconnosotros.html")

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
        else:
            datos['mensaje'] = 'NO se modificó producto'

    return render(request,"productos/agregar-Producto.html", datos)

def eliminar_producto(request, id):
    producto = Productos.objects.get(idProducto = id)
    producto.delete() #delete de la BD
    return redirect(to='articulos')
