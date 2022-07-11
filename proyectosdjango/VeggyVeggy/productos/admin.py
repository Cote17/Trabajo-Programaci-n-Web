from django.contrib import admin
from .models import TipoCategoria,Productos, Clientes, Order, OrderItem
# Register your models here.
admin.site.register(TipoCategoria)
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Order)
admin.site.register(OrderItem)