from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskAPI.as_view()),
    path('id/<int:pk>', views.TaskRetrieveUpdateDestroyAPI.as_view()),
    path('user/<int:us>', views.TaskListByUserIDAPI.as_view()),
    path('unassigned/', views.TaskListByNoneUserAPI.as_view()),
    path('keyword/<str:kw>', views.TaskListByKeywordAPI.as_view()),
    path('history/<int:id>', views.TaskHistoryAPI.as_view()),
]
