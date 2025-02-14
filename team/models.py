from django.conf import settings
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="teams",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
