from apps.shared.views.GenericViews import GenericListApiView, GenericCreateApiView, GenericRetrieveApiView, GenericUpdateApiView, GenericDestroyApiView
from apps.shared.views.GenericViewSets import GenericViewSet
from apps.products.api.serializers.product_serializers import ProductSerializer, ProductCreateSerializer
from rest_framework.response import Response
from rest_framework import status

#CRUD Product

#CRUD PRODUCT USING VIEWSETS
class ProductViewSet(GenericViewSet):
    serializer_class = ProductSerializer
    serializerCreation = ProductCreateSerializer
    serializerUpdate = ProductCreateSerializer

#CRUD PRODUCT USING API VIEWS
#READ
class ProductListApiView(GenericListApiView):
    serializer_class = ProductSerializer
#READ ALL PRODUCTS BY CATEGORY DESCRIPTION 
class ProductByCategoryListApiView(GenericListApiView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        #Return all products with state True and category_product description
        return model.objects.filter(state=True, category_product__description=self.kwargs['category_product_description'])
    
#CREATE
class ProductCreateApiView(GenericCreateApiView):
    serializer_class = ProductCreateSerializer
    
#READ AND CREATE COULD BE IN A SINGLE CLASS: LISTCREATEAPIVIEW

#RETRIEVE
class ProductRetrieveApiView(GenericRetrieveApiView):
    serializer_class = ProductSerializer

#DELETE
class ProductDestroyApiView(GenericDestroyApiView):
    serializer_class = ProductSerializer

#UPDATE
class ProductUpdateApiView(GenericUpdateApiView):
    serializer_class = ProductCreateSerializer

#RETRIEVE, UPDATE AND DELETE COULD BE IN A SINGLE CLASS: RETRIEVEUPDATEDESTROYAPIVIEW