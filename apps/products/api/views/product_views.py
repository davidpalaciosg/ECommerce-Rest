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
class ProductByCategoryDescriptionListApiView(GenericListApiView):
    '''
    List all products by the category_product description
    
    
    params
        -category_product_description (str): name of the category_product
    '''
    serializer_class = ProductSerializer
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        #Return all products with state True and category_product description
        return model.objects.filter(state=True, category_product__description=self.kwargs['category_product_description'])
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.count() == 0:
            return Response({'detail': 'No records found '}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
#READ ALL PRODUCTS BY CATEGORY ID
class ProductByCategoryIdListApiView(GenericListApiView):
    '''
    List all products by the category_product id
    
    
    params
        -id (int): id of the category_product
    '''
    serializer_class = ProductSerializer
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        #Return all products with state True and category_product id
        return model.objects.filter(state=True, category_product_id=self.kwargs['id'])
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.count() == 0:
            return Response({'detail': 'No records found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

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