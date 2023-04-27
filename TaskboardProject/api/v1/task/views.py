from taskboard.models import Task
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
        kw_in_name = Task.objects.filter(name__contains=keyword)
        kw_in_desc = Task.objects.filter(description__contains=keyword)
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
