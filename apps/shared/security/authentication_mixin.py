from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from apps.shared.security.ExpiringTokenAuth import ExpiringTokenAuthentication

class Authentication(object):
    
    def get_user(self, request):
        token = get_authorization_header(request).split()
        try:
            token = token[1].decode()
            token_expire = ExpiringTokenAuthentication()
            user,token = token_expire.authenticate_credentials(token)
            print(user, token)
            return user
            
        except:
            return None
        
    def dispatch(self, request, *args, **kwargs):
       user = self.get_user(request)
       if user is None:
           response =  Response({'error': 'Authentication credentials were not provided or failed.'}, status=status.HTTP_401_UNAUTHORIZED)
           response.accepted_renderer = JSONRenderer()
           response.accepted_media_type = "application/json"
           response.renderer_context = {}
           
           return response
       
       return super().dispatch(request, *args, **kwargs)