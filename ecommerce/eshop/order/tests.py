import json
import copy

from django.contrib.auth.models import User
from products.models import Product
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class CreateOrder(APITestCase):

    def test_create_order(self):

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

        cart = self.client.post("http://localhost:5555/cart/current/",
                                data=data, format='json').data
        print(cart)

        order = {
            "orderItems": [{"product": data['product'],
                            "quantity": data['quantity'],
                            "total_price": data['quantity']*self.product.price}],
            "shippingAddress": {"address": "Vynnychenka, 1",
                                "city": "Kyiv",
                                "postalCode": "02056",
                                "country": "Ukraine"},
            "paymentMethod": "PayPal",
            "price": 1.2,
        }

        response = self.client.post("http://localhost:5555/order/add/",
                                    data=order, format='json')
        print(response.content)
        self.assertEqual(response.status_code, (status.HTTP_200_OK))
