import factory

from django.contrib.auth.hashers import make_password

from accounts.models import User


USER_PASSWORD = "123"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("first_name")
    is_superuser = True
    password = make_password(USER_PASSWORD)
