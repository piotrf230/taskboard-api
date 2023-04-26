from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
from taskboard.models import Task, TaskHistory
from taskboard import constants


@receiver(signals.post_save, sender=Task)
def on_create_or_updated_task(sender, **kwargs):
    on_task_changed(sender, 0 if kwargs['created'] else 1)


@receiver(signals.pre_delete, sender=Task)
def on_delete_task(sender, **kwargs):
    on_task_changed(sender, 2)


def on_task_changed(sender, action_index):
    htask = TaskHistory()
    htask.action = constants.TASK_ACTION[action_index]
    htask.name = sender.name
    htask.description = sender.description
    htask.user = User.objects.get(sender.user)
    htask.state = sender.state

    htask.save()
    print("saved!")
