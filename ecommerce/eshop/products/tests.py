import json
import copy

from django.contrib.auth.models import User
from .models import Product
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class CreateReview(APITestCase):

    def test_create_review(self):

        self.user = User.objects.create_user(first_name="Test", username="test10@gmail.com",
                                             password="Sompasswd123")
        token = RefreshToken.for_user(self.user)
        self.token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + (self.token))

        self.product = Product.objects.create(
            name='Sample Name',
            price=0.8,
            quantity=12,
            descriptions='Sample Description',
            sku="0000024"
        )

        data = {"rating": 5,
                "comment": "Awesome test review!"
                }
        response = self.client.post("http://localhost:5555/products/{}/reviews/".format(
            str(self.product.id)), data=data, format='json')
        # print(response.content)
        self.assertEqual(response.status_code, (status.HTTP_200_OK))


class CheckGetProduct(APITestCase):

    def test_get_product(self):

        self.user = User.objects.create_user(first_name="Test", username="test10@gmail.com",
                                             password="Sompasswd123")
        token = RefreshToken.for_user(self.user)
        self.token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + (self.token))

        self.product = Product.objects.create(
            name='Test Name',
            price=1.2,
            quantity=10,
            descriptions='Test Description',
            sku="025000024"
        )

        response = self.client.get("http://localhost:5555/products/{}/".format(
            str(self.product.id)))
        # print(response.content)
        self.assertEqual(response.status_code, (status.HTTP_200_OK))
