from apps.shared.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import *

class MeasureUnitListApiView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer

class CategoryProductListApiView(GeneralListApiView):
    serializer_class = CategoryProductSerializer

class IndicatorListApiView(GeneralListApiView):
    serializer_class = IndicatorSerializer