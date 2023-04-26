from rest_framework.permissions import AllowAny

from taskboard.models import Task
from . import serializer

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TaskAPI(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = serializer.TaskSerializer
    permission_classes = (AllowAny,)


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
