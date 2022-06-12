from rest_framework import permissions

from utils.db_utils import get_user_object


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = get_user_object(request.user)

        return user.is_superuser

    def has_object_permission(self, request, view, obj):
        user = get_user_object(request.user)

        return user.is_superuser
