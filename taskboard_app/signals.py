from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from taskboard_app.models import Task, TaskHistory
from taskboard_app import constants


@receiver(signals.post_save, sender=Task)
def on_create_or_updated_task(instance, **kwargs):
    on_task_changed(instance, 0 if kwargs["created"] else 1)


@receiver(signals.pre_delete, sender=Task)
def on_delete_task(instance, **kwargs):
    on_task_changed(instance, 2)


def on_task_changed(instance, action_index):
    TaskHistory.objects.create(
        action=constants.TASK_ACTION[action_index],
        task_id=instance.id,
        name=instance.name,
        description=instance.description,
        state=instance.state,
        user_id=instance.user_id,
    )
