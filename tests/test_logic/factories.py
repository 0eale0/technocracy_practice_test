import factory
from faker import Faker

from logic.models import Note, Category
from tests.test_accounts.factories import UserFactory

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    header = factory.Faker("name")


class NoteFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Note

    header = factory.Faker("first_name")
    text = factory.Faker("first_name")
    slug = factory.Faker("last_name")

    user = factory.SubFactory(UserFactory)
