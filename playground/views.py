from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    return HttpResponse("Hello Django")

def calculate(request):
    x = 5
    y = 6
    return HttpResponse(x+y)

def usingTemplates(request):
    return render(request, 'index.html')

