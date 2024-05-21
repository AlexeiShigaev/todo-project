# from django.shortcuts import render
from rest_framework import permissions, viewsets
from django_filters import rest_framework as filters

from todos.models import Tag, ToDoTask
from todos.serializers import TagSerializer, ToDoTaskSerializer


class TagFilterSet(filters.FilterSet):
    """Фильтрация для модели Тэгов. Частичное совпадение строки при поиске."""
    class Meta:
        model = Tag
        fields = {
            'name': ['contains', ],
        }


class TagViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Тэгов.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    filterset_class = TagFilterSet
    search_fields = ['name', ]
    ordering_fields = ['name', ]


class ToDoTaskFilterSet(filters.FilterSet):
    class Meta:
        model = ToDoTask
        fields = {
            'title': ['contains', ],
            'description': ['contains', ],
            'finished': ['exact', ],
            'tags': ['exact', ],
            'created_at': ['lt', 'gt'],
        }


class ToDoTaskViewSet(viewsets.ModelViewSet):
    """
    CRUD Для модели Списка дел, в том числе вложенные в модель теги.
    Примеры использования с поиском:
    * поиск незавершенных дел GET /api/todos/tasks/?finished=false
    * поиск подстроки в заголовке GET /api/todos/tasks/?title__contains=333
    * поиск подстроки в описании дела (задачи) GET /api/todos/tasks/?title__contains=333
    Примеры использования с сортировкий:
    * алфавитный порядок по заголовкам GET /api/todos/tasks/?ordering=title
    * последние по дате создания GET /api/todos/tasks/?ordering=-created_at
    """
    queryset = ToDoTask.objects.all()
    serializer_class = ToDoTaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filterset_class = ToDoTaskFilterSet
    search_fields = ['title', 'tags', 'finished']
    ordering_fields = ['title', 'created_at', 'finished', 'deadline']
