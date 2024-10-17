from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):

    #another method of writing the model serializer
    class Meta:
        model = Product
        fields = ['id','title','slug','description','','price','priceWithTax','collection']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # price = serializers.DecimalField(max_digits=6,decimal_places=2)
    # priceWithTax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset = Collection.objects.all()
    # )
    priceWithTax = serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self,product: Product):
        return product.price * Decimal(1.1)

    
