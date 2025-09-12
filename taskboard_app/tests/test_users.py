from unittest.mock import ANY

import pytest
from django.urls import reverse
from pytest_unordered import unordered
from rest_framework import status


@pytest.mark.parametrize(
    "view, kwargs",
    (
        pytest.param("users:users-list", {}),
        pytest.param("users:users-detail", {"pk": 1}),
    ),
)
@pytest.mark.django_db
def test_users_not_logged_in(client, users_fixture, view, kwargs):
    response = client.get(reverse(view, kwargs=kwargs))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_users_list(client_logged_admin, users_fixture):
    response = client_logged_admin.get(reverse("users:users-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "count": 4,
        "next": None,
        "previous": None,
        "results": ANY,
    }
    assert [dict(item) for item in response.data["results"]] == unordered(
        [
            {"id": ANY, "username": "admin"},
            {"id": ANY, "username": "jo"},
            {"id": ANY, "username": "js"},
            {"id": ANY, "username": "john.smith"},
        ]
    )


@pytest.mark.django_db
def test_users_detail(client_logged_admin, user_fixture):
    response = client_logged_admin.get(
        reverse("users:users-detail", kwargs={"pk": user_fixture.id})
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": ANY,
        "first_name": "John",
        "last_name": "Smith",
        "username": "john.smith",
        "email": "test.user@email.com",
    }
