from rest_framework import serializers
from rest_framework.fields import ReadOnlyField

from logic.models import Category,Note


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NoteSerializerView(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Note
        fields = "__all__"
        lookup_field = 'slug'


class NoteSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        lookup_field = 'slug'
