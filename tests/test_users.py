import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
@pytest.mark.parametrize(
    "view, kwargs",
    pytest.param("users:users-list", {}),
    pytest.param("users:users-detail", {"pk": 1}),
)
def test_users_not_logged_in(api_client,users_fixture,view, kwargs):
    response = api_client.get(reverse(view, kwargs=kwargs))
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
