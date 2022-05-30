from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "productos/index.html")

def contactanos(request):
    return render(request, "productos/Contactanos.html")

def iniciosesion(request):
    return render(request, "productos/Iniciarsesion.html")

def articulos(request):
    return render(request, "productos/Productos.html")

def registro(request):
    return render(request, "productos/Registro.html")

def trabajaconnosotros(request):
    return render(request, "productos/Trabajaconnosotros.html")
