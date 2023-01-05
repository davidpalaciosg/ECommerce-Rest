from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from apps.shared.GenericModels import SharedModelHistorical
from apps.products.models import Product
# Create your models here.

class Supplier(SharedModelHistorical):
    ruc = models.CharField(max_length=11, unique=True)
    business_name = models.CharField('Nombre de Empresa (Razón Social)', max_length=150, blank=False, null=False)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        
    def __str__(self):
        return self.business_name

class PaymentMethod(SharedModelHistorical):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Método de pago'
        verbose_name_plural = 'Métodos de pago'
        
    def __str__(self):
        return self.name

class Voucher(SharedModelHistorical):
    name = models.CharField("Nombre de Comprobante de Pago", max_length=100)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Comprobante de Pago'
        verbose_name_plural = 'Comprobantes de Pago'
    
    def __str__(self):
        return self.name
    
class ExpenseCategory(SharedModelHistorical):
    name = models.CharField("Nombre de Categoría de Gasto", max_length=100)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Categoría de Gasto'
        verbose_name_plural = 'Categorías de Gasto'
    
    def __str__(self):
        return self.name
    
class Expense(SharedModelHistorical):
    date = models.DateField("Fecha de Gasto", auto_now=False, auto_now_add=False)
    quantity = models.DecimalField("Cantidad", max_digits=10, decimal_places=2)
    unit_price = models.DecimalField("Precio Unitario", max_digits=10, decimal_places=2)
    voucher_number = models.CharField("Número de Comprobante de Pago", max_length=50)
    total = models.DecimalField("Total", max_digits=10, decimal_places=2, default=0)
    
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE, related_name='voucher')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='payment_method')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE, related_name='category')
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
    
    def __str__(self):
        return self.voucher_number
    
class Merma(SharedModelHistorical):
    date = models.DateField("Fecha de Merma", auto_now=False, auto_now_add=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='merma_product')
    quantity = models.DecimalField("Cantidad", max_digits=7, decimal_places=2)
    lost_money = models.DecimalField("Dinero Perdido", max_digits=7, decimal_places=2)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Merma'
        verbose_name_plural = 'Mermas'
        
    def __str__(self):
        return f'Merma de {self.product.name}'