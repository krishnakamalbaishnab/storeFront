from django.contrib import admin
from . import models
# Register your models here.

#another way iof registering models and customising list items
#using decorators


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    list_editable = ['price']
    list_per_page = 10
    ordering = ['title']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =['firstName', 'lastName', 'membership']
    list_editable = ['membership']
    ordering = ['firstName' , 'lastName']
    list_per_page =10


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display =['title']
    ordering = ['title']



# admin.site.register(models.Collection)

# admin.site.register(models.Product) 
