from django.urls import path
from apps.users.api.api import UserApiView

urlpatterns = [
    path('all/', UserApiView.as_view(), name='usuario_api')    
]
