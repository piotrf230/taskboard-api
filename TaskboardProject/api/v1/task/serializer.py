from rest_framework import serializers
from taskboard.models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['created', 'updated', 'name', 'description', 'user', 'state', ]


class TaskHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskHistory
        fields = ['created', 'action', 'task', 'name', 'description', 'user', 'state', ]
