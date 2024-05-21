from rest_framework import routers

from todos.views import TagViewSet, ToDoTaskViewSet

router = routers.SimpleRouter()
router.register('todos/tags', TagViewSet)
router.register('todos/tasks', ToDoTaskViewSet)

