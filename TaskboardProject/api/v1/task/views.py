from taskboard.models import Task, TaskHistory
from . import serializer

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TaskAPI(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializer.TaskSerializer


class TaskRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(id=self.kwargs.get('pk', None))


class TaskListByKeywordAPI(ListAPIView):
    serializer_class = serializer.TaskSerializer

    def get_queryset(self):
        keyword = self.kwargs.get('kw', None)
        kw_in_name = Task.objects.filter(name__icontains=keyword)
        kw_in_desc = Task.objects.filter(description__icontains=keyword)
        return kw_in_desc | kw_in_name


class TaskListByUserIDAPI(ListAPIView):
    serializer_class = serializer.TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('us', None)
        return Task.objects.filter(user_id=user_id)


class TaskListByNoneUserAPI(ListAPIView):
    serializer_class = serializer.TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user_id=None)


class TaskListByStateAPI(ListAPIView):
    serializer_class = serializer.TaskSerializer

    def get_queryset(self):
        state = self.kwargs.get('st', None)
        return Task.objects.filter(state__icontains=state)


class TaskHistoryAPI(ListAPIView):
    queryset = TaskHistory.objects.all()
    serializer_class = serializer.TaskHistorySerializer

class TaskHistoryByIdAPI(ListAPIView):
    serializer_class = serializer.TaskHistorySerializer

    def get_queryset(self):
        task_id = self.kwargs.get('id', None)
        return TaskHistory.objects.filter(task_id=task_id)
