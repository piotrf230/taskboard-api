from django.contrib import admin

from apps.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
    list_display = ("id", "user", "name", "state")
