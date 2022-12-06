from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

#CRUD WITH GENERIC VIEWSET
class GeneralViewSet(viewsets.ModelViewSet):
    serializer_class = None
    
    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)
        return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.state = False
            instance.save()
            return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)
        return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
    