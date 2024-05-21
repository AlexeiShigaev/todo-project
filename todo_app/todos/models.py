from django.db import models


class Tag(models.Model):
    """
    Модель для Тегов
    """
    name = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class ToDoTask(models.Model):
    """
    Модель для списка дел
    """
    finished = models.BooleanField(
        default=False, verbose_name='Выполнено'
    )
    title = models.CharField(
        max_length=100, null=False, blank=False, default='Заголовок', verbose_name='Заголовок задачи'
    )
    description = models.TextField(
        default='Постановка задачи', null=False, blank=False, verbose_name='Постановка задачи'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Создан'
    )
    deadline = models.DateTimeField(
        null=True, blank=True, verbose_name='Срок выполения'
    )
    tags = models.ManyToManyField(
        Tag, blank=True, verbose_name="Тэги"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



