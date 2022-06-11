from rest_framework import permissions

from accounts.utils.db_utils import get_user_by_id


class IsAdmin(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_object_permission(self, request, view, obj):
        user = get_user_by_id(request.user)

        return user.is_superuser
