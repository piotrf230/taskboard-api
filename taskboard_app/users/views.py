from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from taskboard_app.users.serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated & IsAdminUser,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        return UserListSerializer
