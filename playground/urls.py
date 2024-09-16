from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_hello),  # Root URL will point to 'say_hello' view
    path('home/', views.say_hello),
    path('filter/',views.filtering)
    # path('calculate/', views.calculate),
    # path('templates/', views.usingTemplates)
]

