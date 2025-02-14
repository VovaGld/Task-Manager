from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    team = models.ForeignKey(
        "team.Team", on_delete=models.CASCADE, related_name="projects"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="projects"
    )
