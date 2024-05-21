from django.contrib import admin

from .models import Tag, ToDoTask


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = 'name',


@admin.register(ToDoTask)
class TagAdmin(admin.ModelAdmin):
    model = ToDoTask
    list_display = 'finished', 'title', 'description', 'deadline'
    readonly_fields = 'created_at',
    list_display_links = 'title',
