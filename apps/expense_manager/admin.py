from django.contrib import admin
from apps.expense_manager.models import *

# Register your models here.
admin.site.register(Supplier)
admin.site.register(PaymentMethod)
admin.site.register(Voucher)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(Merma)
