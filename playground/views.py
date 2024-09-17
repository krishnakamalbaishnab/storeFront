from django.shortcuts import render
#from django.http import HttpResponse
#from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer

# Create your views here.

def say_hello(request):
    # exists = Product.objects.filter(pk=0).exists()

    # return HttpResponse("Hello World, Django -Testing")
    # context ={}
    return render(request,'index.html')


def filtering(request):
    
    productList = Product.objects.filter(price__range=(20,30))

    emailList = Customer.objects.filter(email__icontains= '.com')
#TODO: testing
    # collectionList = Collection.objects.filter(featuredProduct__isnull = True)

    # inventory = Product.objects.filter(inventory__lt=10)



    return render(request , 'hello.html', {'product': list(productList),'customer':list(emailList)})

