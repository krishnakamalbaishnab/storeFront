from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.

def say_hello(request):
    Product.objects.all()

    return HttpResponse("Hello World, Django -Testing")




