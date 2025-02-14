from django.contrib import admin

from task.models import TaskType


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
