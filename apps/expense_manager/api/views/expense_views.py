from apps.shared.views.GenericModelViewSets import GenericModelViewSet
from apps.expense_manager.api.serializers.expense_serializers import *

#Expense CRUD

class ExpenseViewSet(GenericModelViewSet):
    serializer_class = ExpenseSerializer
    serializerCreation = ExpenseCreateSerializer
    serializerUpdate = ExpenseCreateSerializer