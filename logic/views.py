from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.permissions import IsOwnerOrAdmin, IsOwnerOrAdminOrReadOnly
from utils.db_utils import get_user_object, get_filtered_notes_by_user_id
from logic import models
from logic import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for category, allowed readonly for authenticated users. Any user can create category,
    and read all categories, but edit can only owner or admin."""

    permission_classes = [IsAuthenticated & IsOwnerOrAdminOrReadOnly]

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for note, use different serializers for any action.
       User can see and edit only him notes, admin every note"""

    serializer_classes = {
        'create': serializers.NoteSerializerCreate,
        # ... other actions
    }
    default_serializer_class = serializers.NoteSerializerView

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]

    queryset = models.Note.objects.all()
    lookup_field = 'slug'

    def list(self, request, *args, **kwargs):
        """Return only users notes or all if it's admin"""

        user = get_user_object(request.user)

        if user.is_superuser:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = get_filtered_notes_by_user_id(user.pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
