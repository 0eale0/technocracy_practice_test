import os

from src.tests.test_accounts.factories import UserFactory, SuperUserFactory

import pytest

from rest_framework.test import APITestCase, APIClient

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class InitUsers(APITestCase):
    def init_users(self) -> None:
        self.user = UserFactory()
        self.super_user = SuperUserFactory()

    def auth_users(self) -> None:
        self.user_authorized = APIClient()

        response_for_user = self.user_authorized.post(
            "/api/auth/token/", {'email': self.user.email,
                                 'password': self.user.password}
        )

        user_access_token = response_for_user.json()['access']
        self.user_authorized.credentials(HTTP_AUTHORIZATION='Bearer ' + user_access_token)

    def setUp(self) -> None:
        self.init_users()
        self.auth_users()

