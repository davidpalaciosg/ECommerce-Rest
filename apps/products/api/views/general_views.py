from apps.shared.views.GenericViews import GenericListApiView, GenericCreateApiView, GenericUpdateApiView, GenericDestroyApiView
from apps.shared.views.GenericViewSets import GenericViewSet
from apps.products.api.serializers.general_serializers import *

#Measure Unit CRUD

#Mesaure Unit ViewSet
class MeasureUnitViewSet(GenericViewSet):
    serializer_class = MeasureUnitSerializer

#Measure Unit API Views
class MeasureUnitListApiView(GenericListApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitCreateApiView(GenericCreateApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitUpdateApiView(GenericUpdateApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitDestroyApiView(GenericDestroyApiView):
    serializer_class = MeasureUnitSerializer

#Category Product CRUD

#Category Product ViewSet
class CategoryProductViewSet(GenericViewSet):
    serializer_class = CategoryProductSerializer
    
#Category Product API Views
class CategoryProductListApiView(GenericListApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductCreateApiView(GenericCreateApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductUpdateApiView(GenericUpdateApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductDestroyApiView(GenericDestroyApiView):
    serializer_class = CategoryProductSerializer

#Indicator CRUD

#Indicator ViewSet
class IndicatorViewSet(GenericViewSet):
    serializer_class = IndicatorSerializer

#Indicator API Views
class IndicatorListApiView(GenericListApiView):
    serializer_class = IndicatorSerializer
class IndicatorCreateApiView(GenericCreateApiView):
    serializer_class = IndicatorSerializer
class IndicatorUpdateApiView(GenericUpdateApiView):
    serializer_class = IndicatorSerializer
class IndicatorDestroyApiView(GenericDestroyApiView):
    serializer_class = IndicatorSerializer