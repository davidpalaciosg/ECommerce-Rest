from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_views import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls

#Include other views
'''
urlpatterns = [
    # ... 
    url(r'^you_path/', include(router.urls)),
    url(r'^you_path/you_sub_path', views.UpdateTimeView.as_view()),
    # ... 
]
'''