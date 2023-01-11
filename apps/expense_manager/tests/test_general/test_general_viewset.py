from apps.shared.tests.test_setup import TestSetUp
from apps.expense_manager.tests.factories.general_factories import *
from rest_framework import status


class SupplierTestCase(TestSetUp):
    '''
    Class to test supplier viewset
    '''
    url = '/expense-manager/suppliers/'

    def test_search_supplier(self):
        '''
        Method to test search supplier endpoint with ruc
        '''
        url= self.url+'search_supplier/'
        print('SEARCH SUPPLIER: GET ->', url )
                
        supplier = SupplierFactory().create_supplier()
        response = self.client.get(
            url,
            {
                'ruc_or_business_name': supplier.ruc
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['ruc'], supplier.ruc)
        
    def test_create_supplier(self):
        '''
        Method to test create supplier endpoint
        '''
        
        print('CREATE SUPPLIER: POST ->', self.url )
        supplier = SupplierFactory().generate_supplier_JSON()
        response = self.client.post(
            self.url,
            supplier,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['ruc'], supplier['ruc'])
    
    def test_update_supplier(self):
        '''
        Method to test update supplier endpoint
        '''
        url = self.url+'1/'
        print('UPDATE SUPPLIER: PUT ->', url )
        supplier = SupplierFactory().create_supplier()
        supplier.ruc = '12345678901'
        #Generate supplier JSON from supplier object
        updated_supplier = SupplierFactory().generate_JSON_from_supplier(supplier)
        
        response = self.client.put(
            url,
            updated_supplier,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
            