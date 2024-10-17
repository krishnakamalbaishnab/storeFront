from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product , Collection
from .serializers import ProductSerializers, CollectionSerializer

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
        
    
@api_view(['GET','POST'])
def collection_list(request, id):
     if request.method == 'GET':
          queryset = Collection.objects.annotate(products_count=Count('products')).all()
          serializer = CollectionSerializer(queryset, many=True)
          return Response(serializer.data)
     elif request.method == 'POST':
          serializer = CollectionSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
     

@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(
            products_count=Count('products')), pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

     