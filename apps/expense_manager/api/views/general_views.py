from apps.shared.views.GenericModelViewSets import GenericModelViewSet
from apps.expense_manager.api.serializers.general_serializers import *

#Import action decorator
from rest_framework.decorators import action
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

#Supplier CRUD
class SupplierViewSet(GenericModelViewSet):
    serializer_class = SupplierSerializer
    
    @action(detail=False, methods=['get'])
    def search_supplier(self, request):
        '''
        Search a supplier by ruc or business name
        '''
        ruc_or_business_name = request.GET.get('ruc_or_business_name')
        if ruc_or_business_name:
            suppliers = Supplier.objects.filter(Q(ruc__icontains=ruc_or_business_name) | Q(business_name__icontains=ruc_or_business_name))
            serializer = self.get_serializer(suppliers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'Ruc or Business Name is required or not found'}, status=status.HTTP_400_BAD_REQUEST)
    
#Payment Method CRUD
class PaymentMethodViewSet(GenericModelViewSet):
    serializer_class = PaymentMethodSerializer

#Voucher CRUD
class VoucherViewSet(GenericModelViewSet):
    serializer_class = VoucherSerializer

#Expense Category CRUD
class ExpenseCategoryViewSet(GenericModelViewSet):
    serializer_class = ExpenseCategorySerializer

#Merma CRUD
class MermaViewSet(GenericModelViewSet):
    serializer_class = MermaSerializer