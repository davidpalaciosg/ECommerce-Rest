from rest_framework import serializers
from apps.expense_manager.models import *

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id','ruc','business_name','address','phone','email']
        
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id','name','description']
        
class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ['id','name']
        
class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id','name']
        
class MermaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merma
        fields = ['id','date','product', 'quantity', 'lost_money']
        