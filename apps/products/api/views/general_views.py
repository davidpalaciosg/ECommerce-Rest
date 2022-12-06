from apps.shared.views.GenericViews import GeneralListApiView, GeneralCreateApiView, GeneralUpdateApiView, GeneralDestroyApiView
from apps.shared.views.GenericViewSets import GeneralViewSet
from apps.products.api.serializers.general_serializers import *

#Measure Unit CRUD

#Mesaure Unit ViewSet
class MeasureUnitViewSet(GeneralViewSet):
    serializer_class = MeasureUnitSerializer

#Measure Unit API Views
class MeasureUnitListApiView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitCreateApiView(GeneralCreateApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitUpdateApiView(GeneralUpdateApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitDestroyApiView(GeneralDestroyApiView):
    serializer_class = MeasureUnitSerializer

#Category Product CRUD

#Category Product ViewSet
class CategoryProductViewSet(GeneralViewSet):
    serializer_class = CategoryProductSerializer
    
#Category Product API Views
class CategoryProductListApiView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductCreateApiView(GeneralCreateApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductUpdateApiView(GeneralUpdateApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductDestroyApiView(GeneralDestroyApiView):
    serializer_class = CategoryProductSerializer

#Indicator CRUD

#Indicator ViewSet
class IndicatorViewSet(GeneralViewSet):
    serializer_class = IndicatorSerializer

#Indicator API Views
class IndicatorListApiView(GeneralListApiView):
    serializer_class = IndicatorSerializer
class IndicatorCreateApiView(GeneralCreateApiView):
    serializer_class = IndicatorSerializer
class IndicatorUpdateApiView(GeneralUpdateApiView):
    serializer_class = IndicatorSerializer
class IndicatorDestroyApiView(GeneralDestroyApiView):
    serializer_class = IndicatorSerializer