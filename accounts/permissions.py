from rest_framework import permissions

from utils.db_utils import get_user_object


class IsAdmin(permissions.BasePermission):
    """Permission only for admin"""

    def has_permission(self, request, view) -> bool:
        user = get_user_object(request.user)

        return user.is_superuser


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Object-level permission to only allow owners or admins to object
    """

    def has_object_permission(self, request, view, obj) -> bool:
        user = get_user_object(request.user)

        if user.is_superuser:
            return True

        return obj.user == request.user


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """Object-level permission, anyone who auth can read,
     but edit can only owner or admin"""

    def has_object_permission(self, request, view, obj) -> bool:
        user = get_user_object(request.user)

        if request.method in permissions.SAFE_METHODS:
            return True

        if user.is_superuser:
            return True

        return obj.user == request.user

