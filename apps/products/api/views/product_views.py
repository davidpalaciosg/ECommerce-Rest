from apps.shared.api import GeneralListApiView, GeneralCreateApiView, GeneralUpdateApiView, GeneralDestroyApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

#CRUD Product
#READ
class ProductListApiView(GeneralListApiView):
    serializer_class = ProductSerializer