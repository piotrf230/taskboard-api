from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "detail":
            return UserDetailSerializer
        return UserListSerializer
