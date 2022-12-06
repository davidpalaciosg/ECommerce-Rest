from rest_framework import serializers
from apps.products.models import Product

#Import serializers from related models
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer

#Serializer for list a Product
class ProductSerializer(serializers.ModelSerializer):
    measure_unit = MeasureUnitSerializer()
    category_product = CategoryProductSerializer()
    
    class Meta:
        model = Product
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']

#Serializer for create a Product
class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']
    
    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url if instance.image else "",
            'measure_unit': instance.measure_unit.description if instance.measure_unit else "",
            'category_product': instance.category_product.description if instance.category_product else "",
        }