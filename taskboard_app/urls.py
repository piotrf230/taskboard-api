from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


def schema_generation(namespace):
    schema_name = f"{namespace}_schema"
    schema_url = f"api/{namespace}-schema/"
    return (
        path(
            "api/",
            include(
                ("taskboard_app.{}.urls".format(namespace), namespace),
                namespace=namespace,
            ),
        ),
        path(
            schema_url,
            SpectacularAPIView.as_view(api_version=namespace),
            name=schema_name,
        ),
        path(
            f"{schema_url}swagger-ui/",
            SpectacularSwaggerView.as_view(url_name=schema_name),
            name="swagger-ui",
        ),
        path(
            f"{schema_url}redoc/",
            SpectacularRedocView.as_view(url_name=schema_name),
            name="redoc",
        ),
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    *schema_generation("tasks"),
    *schema_generation("users"),
    *schema_generation("token"),
]
