from django.urls import path
from apps.users.api.views.api import user_api_view, user_detail_id_api_view, user_detail_username_api_view

urlpatterns = [
    path('all/', user_api_view, name='usuario_api'),
    path('all/<int:pk>/', user_detail_id_api_view, name='usuario_detail_api'), 
    path('all/<str:username>/', user_detail_username_api_view, name='usuario_detail_api'),   
]
