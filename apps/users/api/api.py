from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from apps.users.models import User
from apps.users.api.serializers import UserSerializer

@api_view(['GET', 'POST'])
def user_api_view(request: Request):
    #GET ALL USERS
    if request.method == 'GET':
        #Queryset
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    #CREATE NEW USER
    elif request.method == 'POST':
        user_serializer:UserSerializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

#GET/UPDATE/DELETE USER BY ID
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_id_api_view(request: Request, pk: int):
    
    user = User.objects.filter(id=pk).first()
    if user:
        #GET USER BY ID
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        #UPDATE USER BY ID
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #DELETE USER BY ID
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message': 'User deleted'})
    return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#GET USER BY USERNAME
@api_view(['GET'])
def user_detail_username_api_view(request: Request, username: str):
    if request.method == 'GET':
        user = User.objects.filter(username=username).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)