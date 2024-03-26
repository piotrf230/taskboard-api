from rest_framework import serializers
from taskboard_app.models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "created",
            "updated",
            "name",
            "description",
            "user",
            "state",
        ]


class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = [
            "created",
            "action",
            "task_id",
            "name",
            "description",
            "user",
            "state",
        ]
