from django.contrib.auth.models import User
from pytest import fixture

from apps.tasks.choices import TaskState
from apps.tasks.models import Task

TASKS_LIST = [
]


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
def task_fixture(user_fixture):
    return Task.objects.bulk_create(
        (
            Task(
                name="task1",
                description="task description",
                user=user_fixture,
            ),
            Task(
                name="task2",
                description="description",
                user=user_fixture,
            ),
            Task(
                name="task3",
                user=user_fixture,
                state=TaskState.IN_PROGRESS,
            ),
        )
    )
