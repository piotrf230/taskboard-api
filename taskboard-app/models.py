from django.db import models
from django.contrib.auth.models import User
from . import constants
from . import validators


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
        20,
        default=constants.TASK_STATES[0],
        validators=[validators.task_state_validator],
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name


class TaskHistory(CreatedTimestampModel):
    # task could be a foreign key, but tasks can be deleted, and on_delete=DO_NOTHING could create issues
    task_id = models.IntegerField(default=0)
    action = models.CharField(20, validators=[validators.task_action_validator])

    name = models.CharField(120)
    description = models.CharField(512, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(
        20,
        default=constants.TASK_STATES[0],
        validators=[validators.task_state_validator],
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name + " (" + str(self.created) + ")"
