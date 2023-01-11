from rest_framework.test import APITestCase
from rest_framework import status
from apps.users.models import User
from faker import Faker

class TestSetUp(APITestCase):
    
    def setUp(self):
        self.login_url = '/login/'
        user = self.generateSuperUser()
        self.user= user
        data ={
            'username':self.user.username,
            'password':'Abc123456'
        }
        
        #Make a login request
        self.response = self.client.post(
            self.login_url,
            data,
            format='json'
        )
                
        self.token = self.response.data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        return super().setUp()
    
    def generateSuperUser(_):
        faker = Faker()
        name,last_name = faker.name().lower().split(" ")
        username = name + last_name
        email = username + "@gmail.com"
        password = "Abc123456"
        
        
        user = User.objects.create_superuser(
            username=username,
            name=name,
            last_name=last_name,
            email=email,
            password=password
        )
        
        return user



