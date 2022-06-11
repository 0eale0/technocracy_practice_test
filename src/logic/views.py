from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin

from logic.models import User
from logic.serializers import UserSerializer, RegisterSerializer


class RegisterView(ViewSetMixin, generics.CreateAPIView):
    """View for register users. It has ViewSetMixin parent to add CreateApiView into router"""

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD users, allowed only for superusers"""

    serializer_class = UserSerializer
    queryset = User.objects.all()



