from rest_framework.routers import SimpleRouter

from taskboard_app.users.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

app_name = "users"

router = SimpleRouter()

router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path("users/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("users/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
