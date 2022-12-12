from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ExpiringTokenAuthentication(TokenAuthentication):
    '''
    This class is used to expire the token after a certain time
    '''
    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed('Invalid token')
        
        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')
        
        is_expired = self.token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed('The token is expired')
        
        return (token.user, token)
    
    def expires_in(self,token):
        '''
        Calculate the time left for the token to expire
        '''
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time
        
    def is_token_expired(self, token):
        '''
        Check if token is expired
        '''
        return self.expires_in(token) < timedelta(seconds=0)
     
    def token_expire_handler(self,token):
        '''
        Uses the token_expire_handler to check if the token is expired
        '''
        is_expire = self.is_token_expired(token)
        return is_expire