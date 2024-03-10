from django.urls import path, include

urlpatterns = [
    path("task/", include("api.v1.task.urls")),
    path("user/", include("api.v1.user.urls")),
]
