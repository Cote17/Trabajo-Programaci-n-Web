from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from .views import eliminar_producto, home, contactanos, inisiarsesion, articulos, trabajaconnosotros, cerrar_sesion, registro, agregar_producto, modificar_producto
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inisiarsesion, name="home"),
    path('index/',home, name='home'),
    path('Contactanos/',contactanos, name='contactanos'),
    path('Iniciarsesion/',inisiarsesion, name='iniciosesion'),
    path('Productos/',articulos,name='articulos'),
    path('Registro/',registro,name='registro'),
    path('Trabajaconnosotros/',trabajaconnosotros,name='trabajaconnosotros'),
    path('cerrar-sesion/',cerrar_sesion,name='cerrar_sesion'),
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('modificar_producto/<id>', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>', eliminar_producto, name="eliminar_producto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

