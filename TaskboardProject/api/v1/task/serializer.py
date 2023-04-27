from rest_framework import serializers
from taskboard.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['created', 'updated', 'name', 'description', 'user', 'state']
