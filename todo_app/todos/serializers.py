from rest_framework import serializers
from todos.models import Tag, ToDoTask


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name')


class ToDoTaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = ToDoTask
        fields = ('pk', 'title', 'description', 'finished', 'created_at', 'deadline', 'tags')

