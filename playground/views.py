from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product
# Create your views here.

def say_hello(request):
    # exists = Product.objects.filter(pk=0).exists()

    # return HttpResponse("Hello World, Django -Testing")
    # context ={}
    return render(request,'index.html')


def filtering(request):
    querySet = Product.objects.filter(price__range=(20,30))

    return render(request , 'hello.html', {'product':list(querySet)})

