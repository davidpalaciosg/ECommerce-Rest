from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet

from django.urls import path
from apps.products.api.views import general_views as gv
from apps.products.api.views import product_views as pv

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

#Include previous views
urlpatterns = [
    #Measure Unit CRUD
    path('measureUnit/all', gv.MeasureUnitListApiView.as_view(), name='measure_unit_api'),
    path('measureUnit/create', gv.MeasureUnitCreateApiView.as_view(), name='measure_unit_create_api'),
    path('measureUnit/update/<int:pk>', gv.MeasureUnitUpdateApiView.as_view(), name='measure_unit_update_api'),
    path('measureUnit/delete/<int:pk>', gv.MeasureUnitDestroyApiView.as_view(), name='measure_unit_delete_api'),
    
    #Category Product CRUD
    path('categoryProduct/all', gv.CategoryProductListApiView.as_view(), name='category_product_api'),
    path('categoryProduct/create', gv.CategoryProductCreateApiView.as_view(), name='category_product_create_api'),
    path('categoryProduct/update/<int:pk>', gv.CategoryProductUpdateApiView.as_view(), name='category_product_update_api'),
    path('categoryProduct/delete/<int:pk>', gv.CategoryProductDestroyApiView.as_view(), name='category_product_delete_api'),
    
    #Indicator CRUD
    path('indicator/all', gv.IndicatorListApiView.as_view(), name='indicator_api'),
    path('indicator/create', gv.IndicatorCreateApiView.as_view(), name='indicator_create_api'),
    path('indicator/update/<int:pk>', gv.IndicatorUpdateApiView.as_view(), name='indicator_update_api'),
    path('indicator/delete/<int:pk>', gv.IndicatorDestroyApiView.as_view(), name='indicator_delete_api'),
]
urlpatterns += router.urls