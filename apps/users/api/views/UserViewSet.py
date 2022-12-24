from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.shared.views.GenericModelViewSets import GenericModelViewSet

from apps.users.api.serializers import UserSerializer

#CRUD User
class UserViewSet(GenericModelViewSet):
    serializer_class = UserSerializer
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)
    
    def destroy(self, request, *args, **kwargs):
        '''
        Delete an user by id (logical delete)
        
        
        params
            -id (int): id of the object
        '''
        instance = self.get_object()
        if instance:
            instance.is_active = False
            instance.save()
            return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)
        return Response({'error': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    #Permissions
    #permission_classes = [IsAuthenticated]