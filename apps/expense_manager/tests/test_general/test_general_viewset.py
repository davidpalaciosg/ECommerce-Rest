from apps.shared.tests.test_setup import TestSetUp
from apps.expense_manager.tests.factories.general_factories import *
from rest_framework import status


class SupplierTestCase(TestSetUp):
    '''
    Class to test supplier viewset
    '''
    url = '/expense-manager/suppliers/'

    def test_search_supplier(self):
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            self.url+'search_supplier/',
            {
                'ruc_or_business_name': supplier.ruc
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['ruc'], supplier.ruc)
