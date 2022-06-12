import factory

from django.contrib.auth.hashers import make_password

from src.accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("name")
    password = make_password('123')


class SuperUserFactory(UserFactory):
    is_superuser = True
