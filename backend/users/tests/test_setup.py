from django.urls import reverse

from rest_framework.test import APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from ..models import User


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.logout_url = reverse('logout')
        self.get_user_url = reverse('user')
        self.delete_user_url = reverse('delete')

        self.user_data = {
            "email": "example@test.com",
            "password": "very_strong_password"
        }

        self.user_invalid_email = {
            "email": "invalidemail.com",
            "password": "very_strong_password"
        }

        self.user_short_password = {
            "email": "example@test.com",
            "password": "1"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def authenticate(self):
        user = User.objects.create_user(
            email=self.user_data["email"],
            password=self.user_data["password"]
        )
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {access}'
        )

        return user, refresh