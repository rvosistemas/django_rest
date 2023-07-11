from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase, APIRequestFactory, force_authenticate
from rest_framework.renderers import JSONRenderer
from rest_framework_simplejwt.tokens import RefreshToken

from rest_postgres.views import UserViewSet


class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(username="testuser")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_user_list(self):
        url = "/users/"
        request = self.factory.get(url)
        force_authenticate(request, user=self.user, token=self.access_token)
        view = UserViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserLoginViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")

    def test_user_login(self):
        url = reverse("user-login")
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "access")
        self.assertContains(response, "refresh")

    def test_user_login_invalid_credentials(self):
        url = reverse("user-login")
        data = {"username": "testuser", "password": "wrongpassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertDictEqual(response.json(), {"error": "Invalid credentials"})


class UserLogoutViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_user_logout(self):
        url = reverse("user-logout")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"success": "Logout successful"})


class UserRegistrationViewTestCase(APITestCase):
    def test_user_registration(self):
        url = reverse("user-registration")
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testuser").exists())


class UserDeactivateViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_user_deactivate(self):
        url = reverse("user-deactivate", kwargs={"pk": self.user.id})
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.json()["is_active"])

        updated_user = User.objects.get(id=self.user.id)
        self.assertFalse(updated_user.is_active)
