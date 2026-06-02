from django.urls import reverse

from rest_framework.test import APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from ..models import Project
from users.models import User


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.create_url = reverse('create_project')
        self.list_url = reverse('projects')

        self.user_data = {
            "email": "example@test.com",
            "password": "very_strong_password"
        }

        self.project_data = {
            "name": "exampleProject",
            "description": "description for an amazing project"
        }

        self.project_invalid_name = {
            "name": "no",
            "description": "description for an amazing project"
        }

        self.project_with_no_description = {
            "name": "exampleProject",
            "description": ""
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