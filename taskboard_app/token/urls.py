from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from taskboard_app.token.views import TokenView

app_name = "token"

urlpatterns = [
    path("token/", TokenView.as_view(), name="token_validate"),
    path("token/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
