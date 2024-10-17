from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/',views.product_details),
    path('collection',views.collection_list),
    path('collection/<int:id>/',views.collection_list)
]

