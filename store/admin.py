from django.contrib import admin , messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.

#another way iof registering models and customising list items
#using decorators


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    list_display = ['title','price' ,'inventoryStatus', 'collection_title']
    list_editable = ['price']
    list_per_page = 10
    ordering = ['title']
    list_select_related = ['collection']
    list_filter = ['collection','last_update', InventoryFilter]
    search_fields = ['title']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventoryStatus(self, product):
        if product.inventory<10:
            return 'Low'
        return 'OK'
    
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.'
            # messages.ERROR
        )



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
    search_fields = ['title']

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
            products_count = Count('products')
        )


class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display =['id','placed_at','customer']

    



# admin.site.register(models.Collection)

# admin.site.register(models.Product)