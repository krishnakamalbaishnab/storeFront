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
        queryset= Product.objects.all()
        serializer = ProductSerializers(queryset, many=True, context={'request':request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
             serializer.validated_data
             return Response('OKAY')
        # else:
        #      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  //don't need it if we are using raiseException


@api_view()
def product_details(request, id):
        product = get_object_or_404(Product,pk=id)
        serializers = ProductSerializers(product)
        return Response(serializers.data)
    