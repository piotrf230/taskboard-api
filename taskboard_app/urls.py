from rest_framework import routers

from taskboard_app.views import TaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls