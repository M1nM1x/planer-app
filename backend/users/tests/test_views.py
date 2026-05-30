from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

from .test_setup import BaseAPITestCase
from ..models import User

class RegistrationViewsBaseAPITestCases(BaseAPITestCase):

    def test_user_cannot_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_user_can_register(self):
        res = self.client.post(
            self.register_url, self.user_data, format='json'
        )

        user = User.objects.get(email=self.user_data["email"])

        self.assertEqual(res.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(user.check_password(self.user_data["password"]))

    def test_user_provided_invalid_email(self):
        res = self.client.post(
            self.register_url, self.user_invalid_email, format='json'
        )
        self.assertEqual(res.status_code, 400)

    def test_user_provided_short_password(self):
        res = self.client.post(
            self.register_url, self.user_short_password, format='json'
        )
        self.assertEqual(res.status_code, 400)


class LoginUserViewBaseAPITestCases(BaseAPITestCase):
    def test_user_can_login(self):
        User.objects.create_user(
            email=self.user_data["email"],
            password=self.user_data["password"]
        )
        res = self.client.post(
            self.login_url, self.user_data, format='json'
        )

        self.assertEqual(res.status_code, 200)
        self.assertIn("access", res.data)
        self.assertIn("refresh", res.data)

    def test_user_cannot_login_with_invalid_password(self):
        User.objects.create_user(
            email=self.user_data["email"],
            password=self.user_data["password"]
        )
        res = self.client.post(
            self.login_url,
            {
                "email": self.user_data["email"],
                "password": "wrong_password"
            },
            format='json'
        )

        self.assertEqual(res.status_code, 401)


class CurrentUserViewBaseAPITestCases(BaseAPITestCase):

    def test_user_is_authorized(self):
        user, refresh = self.authenticate()
        res = self.client.get(self.get_user_url)

        self.assertEqual(res.status_code, 200)
        self.assertIn("email", res.data)

    def test_user_is_not_authorized(self):
        res = self.client.get(self.get_user_url)

        self.assertEqual(res.status_code, 401)


class LogoutUserViewBaseAPITestCases(BaseAPITestCase):

    def test_user_provided_valid_refresh_token(self):
        user, refresh = self.authenticate()

        res = self.client.post(
            self.logout_url, {"refresh": str(refresh)}, format='json'
        )

        self.assertEqual(res.status_code, 205)
        self.assertTrue(BlacklistedToken.objects.filter(token__jti=refresh["jti"]).exists())

    def test_user_provided_invalid_refresh_token(self):
        user, refresh = self.authenticate()

        res = self.client.post(
            self.logout_url, {"refresh": "123"}, format='json'
        )

        self.assertEqual(res.status_code, 400)


class DeleteUserViewBaseAPITestCases(BaseAPITestCase):
    def test_account_deleted_successfully(self):
        user, refresh = self.authenticate()

        res = self.client.delete(self.delete_user_url)

        self.assertEqual(res.status_code, 204)
        self.assertFalse(User.objects.filter(email=self.user_data["email"]).exists())

    def test_deleting_attempt_without_authorization(self):
        res = self.client.delete(self.delete_user_url)
        self.assertEqual(res.status_code, 401)