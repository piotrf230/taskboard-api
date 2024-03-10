from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from . import serializer


class ListUserAPI(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserMinimalSerializer


class GetUserIdAPI(ListAPIView):
    serializer_class = serializer.UserMinimalSerializer

    def get_queryset(self):
        username = self.kwargs.get("un", None)
        return User.objects.filter(username=username)


class CreateUserAPI(CreateAPIView):
    serializer_class = serializer.UserSerializer
    permission_classes = [
        AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                "message": "User {username} created with id {id}!".format(
                    **serializer.data
                )
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )
