from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskAPI.as_view()),
    path('id/<int:pk>', views.TaskRetrieveUpdateDestroyAPI.as_view()),
    path('keyword/<str:kw>', views.TaskListByKeywordAPI.as_view()),
]
