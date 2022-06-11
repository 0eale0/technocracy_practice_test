from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.utils.db_utils import get_user_by_id
from logic import models
from logic import serializers
from logic.permissions import IsAdmin


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for category, allowed for authenticated users"""

    permission_classes = [IsAuthenticated]

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for note, use different serializers for any action.
       User can see only him notes, admin every note"""

    serializer_classes = {
        'create': serializers.NoteSerializerCreate,
        # ... other actions
    }
    default_serializer_class = serializers.NoteSerializerView

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    # permission_classes = [IsAuthenticated]

    queryset = models.Note.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = get_user_by_id(request.user)
        instance = self.get_object()

        if instance.user != user.pk and not user.is_superuser:
            return Response("You don't have access for this note", status=405)

        serializer = self.get_serializer(instance)

        return Response(serializer.data)



