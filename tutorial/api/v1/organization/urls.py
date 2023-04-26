from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.OrganizationAPI.as_view()),
    path('<int:pk>', views.OrganizationRetrieveUpdateDestroyAPI.as_view())
]
