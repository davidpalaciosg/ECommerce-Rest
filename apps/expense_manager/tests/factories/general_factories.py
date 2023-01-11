from faker import Faker

from apps.expense_manager.models import *

faker = Faker()

class SupplierFactory:
    '''
    Class to create fake suppliers for testing
    '''
    def generate_supplier_JSON(self):
        return{
            'ruc':str(faker.random_number(digits=11)),
            'business_name':faker.company(),
            'address':faker.address(),
            'phone':str(faker.random_number(digits=9)),
            'email':faker.email()
        }
        
    def generate_JSON_from_supplier(self, supplier):
        return{
            'ruc':supplier.ruc,
            'business_name':supplier.business_name,
            'address':supplier.address,
            'phone':supplier.phone,
            'email':supplier.email
        }
        
    def create_supplier(self):
        return Supplier.objects.create(**self.generate_supplier_JSON())

class PaymentMethodFactory:
    '''
    Class to create fake payment methods for testing
    '''
    def generate_payment_method_JSON(self):
        return{
            'name':faker.word(),
            'description':faker.sentence()
        }
    def create_payment_method(self):
        return PaymentMethod.objects.create(**self.generate_payment_method_JSON())
    
class VoucherFactory:
    '''
    Class to create fake vouchers for testing
    '''
    def generate_voucher_JSON(self):
        return{
            'name':faker.word()
        }
    def create_voucher(self):
        return Voucher.objects.create(**self.generate_voucher_JSON())
    
class ExpenseCategoryFactory:
    '''
    Class to create fake expense categories for testing
    '''
    def generate_expense_category_JSON(self):
        return{
            'name':faker.word()
        }
    def create_expense_category(self):
        return ExpenseCategory.objects.create(**self.generate_expense_category_JSON())
    