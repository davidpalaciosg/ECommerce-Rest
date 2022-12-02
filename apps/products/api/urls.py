from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListApiView, CategoryProductListApiView, IndicatorListApiView

urlpatterns = [
    path('measureUnit/', MeasureUnitListApiView.as_view(), name='measure_unit_api'),
    path('categoryProduct/', CategoryProductListApiView.as_view(), name='category_product_api'),
    path('indicator/', IndicatorListApiView.as_view(), name='indicator_api'),
]
  