from rest_framework import serializers
from todos.models import Tag, ToDoTask


class TagSerializer(serializers.ModelSerializer):
    """Сериализация данных для модели Тэгов"""
    class Meta:
        model = Tag
        fields = ('pk', 'name')


class ToDoTaskSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для модели списка задач.
    Поле с тегами Сериализуется инструментом для модели Тэгов, тэги вкладываются вложенным списком.
    """
    tags = TagSerializer(many=True)

    class Meta:
        model = ToDoTask
        fields = ('pk', 'title', 'description', 'finished', 'created_at', 'deadline', 'tags')

