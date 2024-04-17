from django.contrib.auth.models import User
from pytest import fixture

from taskboard_app.tasks.choices import TaskState
from taskboard_app.tasks.models import Task

TASKS_LIST = []


@fixture
def user_fixture():
    return User.objects.create(
        first_name="John",
        last_name="Smith",
        username="john.smith",
        email="test.user@email.com",
    )


@fixture
def users_fixture():
    return User.objects.bulk_create(
        (
            User(
                first_name="John",
                last_name="Smith",
                username="john.smith",
                email="js1@email.com",
            ),
            User(
                first_name="Jonathan",
                last_name="Blacksmith",
                username="jo",
                email="js2@email.com",
            ),
            User(
                first_name="Jerry",
                last_name="Smooth",
                username="js",
                email="js3@email.com",
            ),
        )
    )


@fixture
def client_logged(client, user_fixture):
    client.force_login(user_fixture)
    return client


@fixture
def task_fixture(user_fixture):
    return Task.objects.bulk_create(
        (
            Task(
                id=30001,
                name="task1",
                description="task description",
                user=user_fixture,
            ),
            Task(
                id=30002,
                name="task2",
                description="description",
                user=user_fixture,
            ),
            Task(
                id=30003,
                name="task3",
                user=user_fixture,
                state=TaskState.IN_PROGRESS,
            ),
        )
    )
