from rest_framework import viewsets

from logic import models
from logic import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for category, allowed for authenticated users"""

    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for note, use different serializers for any action. Allowed for anyone"""

    serializer_classes = {
        'create': serializers.NoteSerializerCreate,
        # ... other actions
    }
    default_serializer_class = serializers.NoteSerializerView
    queryset = models.Note.objects.all()

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

