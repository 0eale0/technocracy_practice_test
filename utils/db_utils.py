from django.db.models import QuerySet

from accounts.models import User
from logic.models import Note


def create_user(data: dict) -> User:
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
    )

    user.set_password(data['password'])
    user.save()

    return user


def get_user_object(user) -> User:
    # pytest send object, simple using id. There is check for it
    user = User.objects.get(id=user) if type(user) == int else user

    return user


def get_filtered_notes_by_user_id(user_id: int) -> QuerySet:
    notes = Note.objects.prefetch_related("categories").filter(user=user_id)

    return notes
