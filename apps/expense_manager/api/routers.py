from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.expense_manager.api.views import general_views as gv
from apps.expense_manager.api.views import expense_views as ev

router = DefaultRouter()

router.register(r'expenses', ev.ExpenseViewSet, basename='expenses')
router.register(r'suppliers', gv.SupplierViewSet, basename='suppliers')
router.register(r'paymentmethods', gv.PaymentMethodViewSet, basename='payment-methods')
router.register(r'vouchers', gv.VoucherViewSet, basename='vouchers')
router.register(r'expensecategories', gv.ExpenseCategoryViewSet, basename='expense-categories')
router.register(r'mermas', gv.MermaViewSet, basename='mermas')

#Include Aditional views
urlpatterns = []

#Include router urls
urlpatterns += router.urls