from django.urls import path, include

urlpatterns = [
    path("task/", include("api.task.urls")),
    path("user/", include("api.user.urls")),
]
