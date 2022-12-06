from apps.shared.views.GenericViews import GenericListApiView, GenericCreateApiView, GenericRetrieveApiView, GenericUpdateApiView, GenericDestroyApiView
from apps.shared.views.GenericViewSets import GenericViewSet
from apps.products.api.serializers.product_serializers import ProductListSerializer, ProductCreateSerializer
from rest_framework.response import Response
from rest_framework import status

#CRUD Product

#CRUD PRODUCT USING VIEWSETS
class ProductViewSet(GenericViewSet):
    serializer_class = ProductListSerializer
    
    def create(self, request, *args, **kwargs):
        #The serializer is different to create a new object
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#CRUD PRODUCT USING API VIEWS
#READ
class ProductListApiView(GenericListApiView):
    serializer_class = ProductListSerializer

#CREATE
class ProductCreateApiView(GenericCreateApiView):
    serializer_class = ProductCreateSerializer
    
#READ AND CREATE COULD BE IN A SINGLE CLASS: LISTCREATEAPIVIEW

#RETRIEVE
class ProductRetrieveApiView(GenericRetrieveApiView):
    serializer_class = ProductListSerializer

#DELETE
class ProductDestroyApiView(GenericDestroyApiView):
    serializer_class = ProductListSerializer

#UPDATE
class ProductUpdateApiView(GenericUpdateApiView):
    serializer_class = ProductCreateSerializer

#RETRIEVE, UPDATE AND DELETE COULD BE IN A SINGLE CLASS: RETRIEVEUPDATEDESTROYAPIVIEW