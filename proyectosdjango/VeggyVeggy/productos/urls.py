from django.urls import path
from .views import home, contactanos, iniciosesion, articulos, trabajaconnosotros, registro

urlpatterns = [
    path('', home, name="home"),
    path('index/',home, name='home'),
    path('Contactanos/',contactanos, name='contactanos'),
    path('Iniciarsesion/',iniciosesion, name='iniciosesion'),
    path('Productos/',articulos,name='articulos'),
    path('Registro/',registro,name='registro'),
    path('Trabajaconnosotros/',trabajaconnosotros,name='trabajaconnosotros'),
]
