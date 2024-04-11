from rest_framework import routers

from apps.tasks.views import TaskViewSet

app_name = "tasks"

router = routers.SimpleRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = router.urls
