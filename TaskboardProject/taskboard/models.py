from django.db import models
from django.contrib.auth.models import User
from . import constants


class TimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(TimestampModel):
    name = models.CharField(120)
    description = models.CharField(512, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(20, choices=constants.TASK_STATES, default=constants.TASK_STATES[0])

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name
