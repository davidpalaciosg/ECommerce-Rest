from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from ...users.api.serializers import UserSerializer

class Login(ObtainAuthToken):
    #Try to login
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            serializer = UserSerializer(user)
            
            #Verify if user is active
            if user.is_active:
                #Generate or obtain token
                token, created = Token.objects.get_or_create(user=user)
                
                #First login    
                if created: 
                    return Response({
                        'token': token.key,
                        'user': serializer.data,
                        'message': 'User logged in successfully'
                        }, status=status.HTTP_201_CREATED
                    )
                #If user has already logged in on another session
                else:
                    #Delete all sessions
                    deleteAllSesions(user)
                        
                    token.delete() #Delete old token
                    #Create new token  
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': serializer.data,
                        'message': 'User logged in successfully, old sessions deleted'
                        }, status=status.HTTP_200_OK
                    )
            else:
                return Response({'error': 'User is not active'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def post(self, request, *args, **kwargs):
        #Get token
        try: 
            token = request.POST.get('token')
            token = Token.objects.filter(key=token).first()
            print(token.user)
            if token:
                user = token.user
                #Delete all sessions
                deleteAllSesions(user)
                token.delete() #Delete token
                
                session_message = 'All sessions deleted'
                token_message = 'Token deleted'
                return Response({'session_message': session_message, 'token_message': token_message},
                                status=status.HTTP_200_OK)
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Token not found'}, status=status.HTTP_409_CONFLICT)
            

def deleteAllSesions(user):
    '''
    Given an user, delete all sessions
    '''
    all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
    if all_sessions.exists():
        #Delete old sessions
        for session in all_sessions:
            session_data = session.get_decoded()
            if user.id == int(session_data.get('_auth_user_id')):
                session.delete()