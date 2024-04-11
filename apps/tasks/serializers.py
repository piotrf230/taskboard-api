from rest_framework import serializers

from apps.tasks.models import Task
from apps.users.serializers import UserListSerializer


class TaskSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)

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
