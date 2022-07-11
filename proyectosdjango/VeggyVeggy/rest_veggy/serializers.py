from tkinter import Image
from rest_framework import serializers
from productos.models import Productos

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['idProducto','nombre','precio','img','descripcion','categoria']
        
class ImageSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(required=True)
    class Meta:
        model = Productos
        fields = ['idProducto','nombre','precio', 'img', 'descripcion', 'categoria']