from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello),  # Root URL will point to 'say_hello' view
    path('hello/', views.say_hello),
    path('calculate/', views.calculate),
    path('templates/', views.usingTemplates)
]

