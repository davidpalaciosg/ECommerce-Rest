from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
#CRUD GENERIC API

#READ
class GeneralListApiView(generics.ListAPIView):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
    
#CREATE
class GeneralCreateApiView(generics.CreateAPIView):
    serializer_class = None
    
#UPDATE
class GeneralUpdateApiView(generics.UpdateAPIView):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
    
#DELETE
class GeneralDestroyApiView(generics.DestroyAPIView):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.state = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)