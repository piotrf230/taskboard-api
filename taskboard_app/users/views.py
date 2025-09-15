from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from taskboard_app.users.serializers import UserListSerializer, UserDetailSerializer
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        return UserDetailSerializer

    def get_permissions(self):
        if self.action == "register":
            self.permission_classes = (AllowAny,)
        elif self.action == "token":
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsAuthenticated & IsAdminUser,)
        return super(UserViewSet, self).get_permissions()

    @action(
        url_name="register",
        url_path="register",
        detail=False,
        methods=["POST"],
    )
    def register(self, request):
        print("register")
        user = User.objects.create_user(**request.data)
        print(user)
        #User.save()
        print("saved")
        serializer = UserDetailSerializer(user)
        print("serializer")
        resp = Response(serializer.data, 201)
        print(resp)
        return resp

    @action(
        url_name="token",
        url_path="token",
        detail=False,
        methods=["GET"],
    )
    def token(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data | {"is_admin": request.user.is_superuser})
