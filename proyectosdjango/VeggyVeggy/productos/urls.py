from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from .views import eliminar_producto, home, contactanos, inisiarsesion, articulos, trabajaconnosotros, cerrar_sesion, registro, agregar_producto, modificar_producto, updateItem, tiendita, carrito, pago, Dpago
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

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
    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('updateItem/', updateItem, name="updateItem"),
    path('tiendita/', tiendita, name="tiendita"),
    path('carrito/', carrito, name="carrito"),
    path('pago/', pago, name="pago"),
    path('Dpago/', Dpago, name="Dpago"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

