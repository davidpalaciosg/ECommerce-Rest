from apps.shared.GenericViews import GeneralListApiView, GeneralCreateApiView, GeneralRetrieveApiView, GeneralUpdateApiView, GeneralDestroyApiView
from apps.products.api.serializers.product_serializers import ProductListSerializer, ProductCreateSerializer

#CRUD Product
#READ
class ProductListApiView(GeneralListApiView):
    serializer_class = ProductListSerializer

#CREATE
class ProductCreateApiView(GeneralCreateApiView):
    serializer_class = ProductCreateSerializer
    
#RETRIEVE
class ProductRetrieveApiView(GeneralRetrieveApiView):
    serializer_class = ProductListSerializer

#DELETE
class ProductDestroyApiView(GeneralDestroyApiView):
    serializer_class = ProductListSerializer

#UPDATE
class ProductUpdateApiView(GeneralUpdateApiView):
    serializer_class = ProductCreateSerializer
    