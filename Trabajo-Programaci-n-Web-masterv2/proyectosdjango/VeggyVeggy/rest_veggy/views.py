from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from productos.models import Productos
from rest_veggy.serializers import ProductosSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        lista_productos =  Productos.objects.all()
        serializer = ProductosSerializer(lista_productos, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = ProductosSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto(request, id):
    try:
        producto = Productos.objects.get(idProducto=id)
    except Productos.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        seriaz =  ProductosSerializer(producto)
        return Response(seriaz.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        seriaz =  ProductosSerializer(producto, data=dataP)
        if seriaz.is_valid():
            seriaz.save()
            return Response(seriaz.data)
        else:
            return Response(seriaz.errors, status = status.HTTP_400_BAD_REQUEST)            
    elif request.method == "DELETE":
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

