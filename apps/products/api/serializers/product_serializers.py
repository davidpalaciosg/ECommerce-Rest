from rest_framework import serializers
from apps.products.models import Product

#Import the serializers of the related models
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

class ProductSerializer(serializers.ModelSerializer):
    #Define the fields of the related models
    measure_unit = MeasureUnitSerializer()
    category_product = CategoryProductSerializer()
    
    class Meta:
        model = Product
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']