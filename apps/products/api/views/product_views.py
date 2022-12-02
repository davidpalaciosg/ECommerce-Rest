from apps.shared.api import GeneralListApiView, GeneralCreateApiView, GeneralUpdateApiView, GeneralDestroyApiView
from apps.products.api.serializers.product_serializers import ProductListSerializer, ProductCreateSerializer

#CRUD Product
#READ
class ProductListApiView(GeneralListApiView):
    serializer_class = ProductListSerializer

#CREATE
class ProductCreateApiView(GeneralCreateApiView):
    serializer_class = ProductCreateSerializer