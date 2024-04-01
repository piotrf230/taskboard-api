from django.db import models
from django.contrib.auth.models import User
from taskboard_app import validators
from taskboard_app.choices import TaskState


class UpdatedTimestampModel(models.Model):
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedTimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Task(CreatedTimestampModel, UpdatedTimestampModel):
    name = models.CharField(120)
    description = models.CharField(512, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(
        max_length=1,
        choices=TaskState.choices,
        default=TaskState.NEW
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name