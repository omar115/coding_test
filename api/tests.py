
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from . import models

# Create your tests here.

class ParentUserTestCase(APITestCase):

    def test_parent_create(self):
        data = {
            "first_name": "Steven",
            "last_name": "king",
            "street": "12/A",
            "city": "Sample",
            "state": "Germany",
            "zip_code": 123
        }
        response = self.client.post(reverse('parent-user-create'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_parent_list(self):
        response = self.client.get(reverse('parent-user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

class ChildUserTestCase(APITestCase):

    def setUp(self):
        self.parent = models.ParentUser.objects.create(
            first_name="Steven",
            last_name="King",
            street = "12/A",
            city="Dhaka",
            state="BD",
            zip_code = 12
        )
    
    def test_child_create(self):
        data = {
            "parent_user":self.parent,
            "child_first_name":"Max",
            "child_last_name":"powell",
        }
    

        response = self.client.post(reverse('child-user-create'), data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_child_list(self):
        response = self.client.get(reverse('child-user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)