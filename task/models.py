from django.conf import settings
from django.db import models


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="type_tasks",
    )
    assignee = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="assigned_tasks",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_tasks",
    )
    PRIORITY_CHOICES = (
        (1, "High"),
        (2, "Medium"),
        (3, "Low"),
    )
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    project = models.ForeignKey(
        "project.Project",
        on_delete=models.CASCADE,
        related_name="tasks",
        null=True,
        blank=True,
    )
