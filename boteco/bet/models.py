from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Team: {self.name} - Description{self.description}"
