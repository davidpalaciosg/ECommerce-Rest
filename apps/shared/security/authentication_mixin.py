from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from apps.shared.security.ExpiringTokenAuth import ExpiringTokenAuthentication

class Authentication(object):
    user = None
    
    def get_user(self, request):
        token = get_authorization_header(request).split()
        try:
            token = token[1].decode()
            token_expire = ExpiringTokenAuthentication()
            user,token, is_expired = token_expire.authenticate_credentials(token)
            return user,token, is_expired 
        except:
            return None, None, None
        
    def dispatch(self, request, *args, **kwargs):
       user, token, is_expired = self.get_user(request)
       
       response = Response()
       response.accepted_renderer = JSONRenderer()
       response.accepted_media_type = "application/json"
       response.renderer_context = {}
       
       if user is None:
           message = {'error': 'Authentication credentials were not provided or failed.'}
           response.data = message
           return response
       
       if is_expired:
           message = {'error': 'Token has expired, refresh it to continue.',
                      'token': token.key,
                      'expired': is_expired}
           response.data = message
           return response
       
       self.user = user
       return super().dispatch(request, *args, **kwargs)