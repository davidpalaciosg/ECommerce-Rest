from apps.shared.api import GeneralListApiView, GeneralCreateApiView, GeneralUpdateApiView, GeneralDestroyApiView
from apps.products.api.serializers.general_serializers import *

#Measure Unit CRUD
class MeasureUnitListApiView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitCreateApiView(GeneralCreateApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitUpdateApiView(GeneralUpdateApiView):
    serializer_class = MeasureUnitSerializer
class MeasureUnitDestroyApiView(GeneralDestroyApiView):
    serializer_class = MeasureUnitSerializer

#Category Product CRUD
class CategoryProductListApiView(GeneralListApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductCreateApiView(GeneralCreateApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductUpdateApiView(GeneralUpdateApiView):
    serializer_class = CategoryProductSerializer
class CategoryProductDestroyApiView(GeneralDestroyApiView):
    serializer_class = CategoryProductSerializer

#Indicator CRUD
class IndicatorListApiView(GeneralListApiView):
    serializer_class = IndicatorSerializer
class IndicatorCreateApiView(GeneralCreateApiView):
    serializer_class = IndicatorSerializer
class IndicatorUpdateApiView(GeneralUpdateApiView):
    serializer_class = IndicatorSerializer
class IndicatorDestroyApiView(GeneralDestroyApiView):
    serializer_class = IndicatorSerializer