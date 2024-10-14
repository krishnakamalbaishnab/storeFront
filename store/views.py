from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializers

# Create your views here.
@api_view()
def product_list(request):
    queryset= Product.objects.all()
    serializer = ProductSerializers(queryset, many=True)
    return Response(serializer.data)

@api_view()
def product_details(request, id):
        product = get_list_or_404(Product,pk=id)
        serializers = ProductSerializers(product)
        return Response(serializers.data)
    