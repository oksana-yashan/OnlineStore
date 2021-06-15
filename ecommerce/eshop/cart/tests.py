import json
import copy

from django.contrib.auth.models import User
from products.models import Product
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class CreateCartItem(APITestCase):

    def test_create_cart_item(self):

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

        data = {
            "product": self.product.id,
            "quantity": 2
        }

        response = self.client.post("http://localhost:5555/cart/current/",
                                    data=data, format='json')
        print(response.content)
        self.assertEqual(response.status_code, (status.HTTP_201_CREATED))

