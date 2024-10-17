from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializers

# Create your views here.
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all()
        # queryset= Product.objects.all()
        serializer = ProductSerializers(queryset, many=True, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  //don't need it if we are using raiseException


@api_view(['GET','PUT','DELETE'])
def product_details(request, id):
        product = get_object_or_404(Product,pk=id)
        if request.method == 'GET':
             serializer = ProductSerializers(product)
             return Response(serializer.data)
        elif request.method == 'PUT':
             serializer = ProductSerializers(product, data = request.data)
             serializer.is_valid(raise_exception=True)
             serializer.save()
             return Response(serializer.data)
        elif request.method == 'DELETE':
            if product.orderitem.count() > 0:
                return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    