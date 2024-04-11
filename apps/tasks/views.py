from datetime import datetime

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    @action(
        detail=True,
        methods=["GET"],
        url_name="history",
        url_path="history/(?P<date>\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})",
    )
    def history(self, request, pk=None, date=None):
        if date:
            date = datetime.strptime(date, "%Y-%m-%d-%H-%M-%S")
            task = self.get_object().history.as_of(date)
            serializer = self.get_serializer(task)
            return Response(serializer.data)
        return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
