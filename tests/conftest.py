from tests.test_accounts.factories import UserFactory, USER_PASSWORD

import pytest

from rest_framework.test import APITestCase, APIClient

from tests.test_logic.factories import NoteFactory
from tests.test_logic import test_config

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class InitUsers(APITestCase):
    def init_user(self) -> None:
        self.user = UserFactory()

    def auth_user(self) -> None:
        self.user_authorized = APIClient()

        response_for_user = self.user_authorized.post(
                  "/api/token/", {'username': self.user.username,
                                 'password': USER_PASSWORD}
        )

        user_access_token = response_for_user.json()['access']
        self.user_authorized.credentials(HTTP_AUTHORIZATION='Bearer ' + user_access_token)

    def init_notes(self) -> None:
        notes_count = test_config.NOTES_COUNT
        self.notes = [NoteFactory() for i in range(notes_count)]

    def setUp(self) -> None:
        self.init_user()
        self.auth_user()
        self.init_notes()

