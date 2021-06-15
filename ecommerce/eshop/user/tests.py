import json
import copy

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"name": "Test",
                "email": "test10@gmail.com",
                "password": "Sompasswd123"}

        response = self.client.post(
            "http://localhost:5555/user_profile/register/", data)

        # global curr_test_token
        # curr_test_token = "Bearer "+response.data.get('token')
        # print(curr_test_token)
        self.assertEqual(response.status_code,
                         (status.HTTP_200_OK or status.HTTP_201_CREATED))


class LoginTestCase(APITestCase):

    def test_login(self):

        RegistrationTestCase.test_registration(self)

        data = {"username": "test10@gmail.com",
                "password": "Sompasswd123"}

        response = self.client.post("http://localhost:5555/api/token/", data)
        # print(response.content)
        self.assertEqual(response.status_code, (status.HTTP_200_OK))


class UserUpdateTestCase(APITestCase):

    def test_user_update(self):
        user = User.objects.create_user(first_name="Test", username="test10@gmail.com",
                                        password="Sompasswd123")
        token = RefreshToken.for_user(user)
        self.token = str(token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + (self.token))

        self.user = User.objects.get(username="test10@gmail.com")
        self.updated_user = copy.deepcopy(self.user)
        self.updated_user.name = "Updated Test"
        self.updated_user.email = "updated_test10@gmail.com"

        data = {"id": self.user.id,
                "name": self.updated_user.name,
                "email": self.updated_user.email,
                "is_admin": self.updated_user.is_staff,
                "is_staff": self.updated_user.is_staff
                }
        response = self.client.put(
            "http://localhost:5555/user_profile/update/"+str(self.user.id)+"/", data=data, format='json')
        # print(response.content)
        print("*******/////////", response.data.get("email"))
        self.assertEqual(response.status_code, (status.HTTP_200_OK))
