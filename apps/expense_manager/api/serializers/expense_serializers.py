from rest_framework import serializers
from apps.expense_manager.models import *

#Import serializers from related models
from apps.expense_manager.api.serializers.general_serializers import *

#Serializer for list a Expense
class ExpenseSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    payment_method = PaymentMethodSerializer()
    voucher = VoucherSerializer()
    expense_category = ExpenseCategorySerializer()
    
    class Meta:
        model = Expense
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']
        
#Serializer for create a Expense
class ExpenseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ['state', 'created_date', 'modified_date', 'deleted_date']