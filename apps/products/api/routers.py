from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet

from django.urls import path
from apps.products.api.views import general_views as gv
from apps.products.api.views import product_views as pv

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')
router.register(r'measureunits', gv.MeasureUnitViewSet, basename='measure-units')
router.register(r'categoryproducts', gv.CategoryProductViewSet, basename='category-products')
router.register(r'indicators', gv.IndicatorViewSet, basename='indicators')

#Include Aditional views
urlpatterns = [
    path('products/category/<int:id>', pv.ProductByCategoryIdListApiView.as_view(), name='product_by_category_api'),
    path('products/category/<str:category_product_description>', pv.ProductByCategoryDescriptionListApiView.as_view(), name='product_by_category_api'),
]

#Include router urls
urlpatterns += router.urls