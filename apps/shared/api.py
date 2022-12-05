from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

#CRUD GENERIC API
#READ LIST
class GeneralListApiView(generics.ListAPIView):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
    
#CREATE
class GeneralCreateApiView(generics.CreateAPIView):
    serializer_class = None
    #Override method to create a new object
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        if instance: 
                instance.state = False
                instance.save()
                return Response({'message': 'Object deleted'}, status=status.HTTP_200_OK)
        return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
#DETAIL RETRIEVE
class GeneralRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
    