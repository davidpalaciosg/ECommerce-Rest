from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.api.serializers import UserSerializer

from apps.users.models import User

class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
           login_serializer = self.get_serializer(data=request.data)
           if login_serializer.is_valid():
               user_serializer = UserSerializer(user)
               data_response = {
                   'user': user_serializer.data,
                   'access_token': login_serializer.validated_data['access'],
                   'refresh_token': login_serializer.validated_data['refresh'],
                   'message': 'Login successfully',
               }
               
               return Response(data_response, status=status.HTTP_200_OK)
           else:
                return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                   
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED) 

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        
        user = request.user
        if user:
            print(user.id)
            #Refresh the access token
            RefreshToken.for_user(user)
            return Response({'message': 'Logout successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)