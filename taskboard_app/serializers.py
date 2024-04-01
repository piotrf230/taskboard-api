from rest_framework import serializers
from taskboard_app.models import Task


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
