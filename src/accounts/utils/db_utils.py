from accounts.models import User


def create_user(data):
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
    )

    user.set_password(data['password'])
    user.save()

    return user
