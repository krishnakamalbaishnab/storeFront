from django.contrib import admin
from django.db.models.aggregates import Count
# from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.

#another way iof registering models and customising list items
#using decorators


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price' ,'inventoryStatus', 'collection_title']
    list_editable = ['price']
    list_per_page = 10
    ordering = ['title']
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventoryStatus(self, product):
        if product.inventory<10:
            return 'Low'
        return 'OK'



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =['firstName', 'lastName', 'membership','order_count']
    list_editable = ['membership']
    # ordering = ['firstName' , 'lastName']
    list_per_page =10
    search_fields = ['firstName__istartswith', 'lastName__istartswith']
    @admin.display(ordering='order_count')
    def order_count(self, order):
        return order.order_count

    def get_queryset(self,request):
        return super().get_queryset(request).annotate(
            order_count = Count('order')
        )


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display =['title', 'products_count']
    ordering = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{} Products</a>', url, collection.products_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id','placed_at','customer']

    



# admin.site.register(models.Collection)

# admin.site.register(models.Product)