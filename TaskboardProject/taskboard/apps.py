from django.apps import AppConfig
from django.db.models.signals import post_save


class TaskboardAppConfig(AppConfig):
    name = 'taskboard'

    def ready(self):
        from . import signals
