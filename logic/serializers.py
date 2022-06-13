from rest_framework import serializers
from rest_framework.serializers import raise_errors_on_nested_writes
from rest_framework.utils import model_meta

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
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        """There is smallest rewrited function from drf code for saving user, who created the note"""

        user = self.context['request'].user

        raise_errors_on_nested_writes('create', self, validated_data)

        ModelClass = self.Meta.model

        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        try:
            # Save user who created the note
            instance = ModelClass._default_manager.create(user=user,
                                                          **validated_data)
        except TypeError:
            raise TypeError

        # Save many-to-many relationships after the instance is created.
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance

    class Meta:
        model = Note
        fields = ["header", "text", "slug", "categories", "user", "id"]
        lookup_field = 'slug'
