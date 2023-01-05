from apps.shared.views.GenericModelViewSets import GenericModelViewSet
from apps.expense_manager.api.serializers.general_serializers import *

#Supplier CRUD
class SupplierViewSet(GenericModelViewSet):
    serializer_class = SupplierSerializer
    
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