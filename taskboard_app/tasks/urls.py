from rest_framework.routers import SimpleRouter

from taskboard_app.tasks.views import TaskViewSet

app_name = "tasks"

router = SimpleRouter()

router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = router.urls
