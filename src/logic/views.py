from rest_framework import viewsets

from logic.models import Category
from logic.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet CRUD for category, allowed for authenticated users"""

    serializer_class = CategorySerializer
    queryset = Category.objects.all()



