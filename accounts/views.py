from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSetMixin

from accounts.models import User
from accounts.serializers import UserSerializer, RegisterSerializer
from accounts.permissions import IsAdmin


class RegisterView(ViewSetMixin, generics.CreateAPIView):
    """View for register users. It has ViewSetMixin parent to add CreateApiView into router"""

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for users, allowed only for superusers"""

    permission_classes = [IsAuthenticated & IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()
