from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from . import serializer


class ListUserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserMinimalSerializer


class GetUserIdAPI(ListAPIView):
    serializer_class = serializer.UserMinimalSerializer

    def get_queryset(self):
        username = self.kwargs.get('un', None)
        return User.objects.filter(username=username)


class CreateUserAPI(CreateAPIView):
    serializer_class = serializer.UserSerializer
    permission_classes = [AllowAny, ]
