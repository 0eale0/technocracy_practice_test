from accounts.models import User


def create_user(data) -> User:
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
    )

    user.set_password(data['password'])
    user.save()

    return user


def get_user_by_id(user_id: int) -> User:
    user_id = 1
    user = User.objects.get(id=user_id)

    print(user.username)

    return user
