import datetime
from unittest.mock import ANY

import freezegun
import pytest
from django.urls import reverse
from pytest_unordered import unordered
from rest_framework import status

from taskboard_app.tasks.choices import TaskState
from taskboard_app.tasks.models import Task


@pytest.mark.parametrize(
    "method, view, kwargs",
    (
        pytest.param("get", "tasks:tasks-list", {}),
        pytest.param("get", "tasks:tasks-detail", {"pk": 1}),
        pytest.param("put", "tasks:tasks-detail", {"pk": 1}),
        pytest.param("patch", "tasks:tasks-detail", {"pk": 1}),
        pytest.param("delete", "tasks:tasks-detail", {"pk": 1}),
        pytest.param(
            "get", "tasks:tasks-history", {"pk": 1, "date": "1111-11-11-11-11-11"}
        ),
    ),
)
@pytest.mark.django_db
def test_tasks_not_logged_in(client, task_fixture, method, view, kwargs):
    response = getattr(client, method)(reverse(view, kwargs=kwargs), {})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_tasks_list(client_logged, task_fixture):
    response = client_logged.get(reverse("tasks:tasks-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "count": 3,
        "next": None,
        "previous": None,
        "results": ANY,
    }
    assert [dict(item) for item in response.data["results"]] == unordered(
        [
            {
                "id": ANY,
                "created": ANY,
                "updated": ANY,
                "name": "task1",
                "description": "task description",
                "user": {"id": ANY, "username": "john.smith"},
                "state": TaskState.NEW,
            },
            {
                "id": ANY,
                "created": ANY,
                "updated": ANY,
                "name": "task2",
                "description": "description",
                "user": {"id": ANY, "username": "john.smith"},
                "state": TaskState.NEW,
            },
            {
                "id": ANY,
                "created": ANY,
                "updated": ANY,
                "name": "task3",
                "description": "",
                "user": {"id": ANY, "username": "john.smith"},
                "state": TaskState.IN_PROGRESS,
            },
        ]
    )


@pytest.mark.django_db
def test_tasks_create(client_logged, task_fixture):
    response = client_logged.post(
        reverse("tasks:tasks-list"),
        {"name": "new task", "description": "new description"},
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        "id": ANY,
        "created": ANY,
        "updated": ANY,
        "name": "new task",
        "description": "new description",
        "user": None,
        "state": TaskState.NEW,
    }


@pytest.mark.parametrize(
    "method, body, expected_status, expected_result",
    (
        pytest.param(
            "get",
            {},
            status.HTTP_200_OK,
            {
                "id": ANY,
                "created": ANY,
                "updated": ANY,
                "name": "task1",
                "description": "task description",
                "user": {"id": ANY, "username": "john.smith"},
                "state": TaskState.NEW,
            },
        ),
        pytest.param(
            "put",
            {
                "name": "task update",
                "description": "desc",
                "state": TaskState.IN_PROGRESS,
            },
            status.HTTP_200_OK,
            {
                "id": ANY,
                "created": ANY,
                "updated": ANY,
                "name": "task update",
                "description": "desc",
                "user": {"id": ANY, "username": "john.smith"},
                "state": TaskState.IN_PROGRESS,
            },
        ),
        pytest.param(
            "patch",
            {"state": TaskState.IN_PROGRESS},
            status.HTTP_200_OK,
            {
                "id": ANY,
                "created": ANY,
                "updated": ANY,
                "name": "task1",
                "description": "task description",
                "user": {"id": ANY, "username": "john.smith"},
                "state": TaskState.IN_PROGRESS,
            },
        ),
        pytest.param(
            "delete",
            {},
            status.HTTP_204_NO_CONTENT,
            None,
        ),
    ),
)
@pytest.mark.django_db
def test_tasks_detail(
    client_logged, task_fixture, method, body, expected_status, expected_result
):
    response = getattr(client_logged, method)(
        reverse("tasks:tasks-detail", kwargs={"pk": task_fixture[0].id}),
        body,
        content_type="application/json",
    )
    assert response.status_code == expected_status
    assert response.data == expected_result


@pytest.mark.django_db
@freezegun.freeze_time("2020-01-01", as_kwarg="frozen_time")
def test_tasks_history(client_logged, **kwargs):
    task = Task.objects.create(
        id=30001,
        name="task1",
        description="task description",
        user=None,
    )
    frozen_time = kwargs.get("frozen_time")
    frozen_time.tick(delta=datetime.timedelta(days=300))
    client_logged.patch(
        reverse("tasks:tasks-detail", kwargs={"pk": task.id}),
        {"state": TaskState.IN_PROGRESS},
        content_type="application/json",
    )
    response = client_logged.get(
        reverse(
            "tasks:tasks-history",
            kwargs={"pk": task.id, "date": "2020-01-10-00-00-00"},
        )
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": ANY,
        "created": ANY,
        "updated": ANY,
        "name": "task1",
        "description": "task description",
        "user": None,
        "state": TaskState.NEW,
    }
