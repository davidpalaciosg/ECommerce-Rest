from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.api.views.UserViewSet import UserViewSet
from apps.users.api.views.api_views import user_api_view, user_detail_id_api_view, user_detail_username_api_view

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('all/', user_api_view, name='usuario_api'),
    path('all/<int:pk>/', user_detail_id_api_view, name='usuario_detail_api'), 
    path('all/<str:username>/', user_detail_username_api_view, name='usuario_detail_api'),   
]

#Include router urls
urlpatterns += router.urls
