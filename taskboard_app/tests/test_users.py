from unittest.mock import ANY

import pytest
from django.urls import reverse
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
def test_users_list(client, users_fixture):
    client.force_login(user=users_fixture[0])
    response = client.get(reverse("users:users-list"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "count": 3,
        "next": None,
        "previous": None,
        "results": [
            {"id": ANY, "username": "jo"},
            {"id": ANY, "username": "js"},
            {"id": ANY, "username": "john.smith"},
        ],
    }


@pytest.mark.django_db
def test_users_detail(client, user_fixture):
    client.force_login(user=user_fixture)
    response = client.get(reverse("users:users-detail", kwargs={"pk": user_fixture.id}))
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": ANY,
        "first_name": "John",
        "last_name": "Smith",
        "username": "john.smith",
        "email": "test.user@email.com",
    }
