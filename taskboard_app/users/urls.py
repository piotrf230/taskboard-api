from rest_framework.routers import SimpleRouter

from taskboard_app.users.views import UserViewSet

app_name = "users"

router = SimpleRouter()

router.register(r"users", UserViewSet, basename="users")

urlpatterns = router.urls
