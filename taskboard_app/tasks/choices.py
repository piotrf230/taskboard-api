from django.db import models


class TaskState(models.TextChoices):
    NEW = "N", "New task"
    IN_PROGRESS = "P", "In progress"
    COMPLETED = "C", "Completed"
