import random

import requests
from authorizer import get_auth_token
from config import user_count

tokens = []


def create_user_data(i):
    num_str = str(i)
    if i < 10:
        num_str = "0" + num_str
    user = {"username": (None, "user" + num_str), "password": (None, "password" + num_str)}
    return user


def test_add_user():
    for i in range(user_count):
        user = create_user_data(i)
        req = requests.post("http://localhost/api/v1/user/register/", files=user)
        assert req.status_code == 201


def test_duplicate_user():
    user = create_user_data(random.randint(1, user_count - 1))
    req = requests.post("http://localhost/api/v1/user/register/", files=user)
    assert req.status_code == 400


def test_login():
    for i in range(user_count):
        user = create_user_data(i)
        req = requests.post("http://localhost/api/v1/user/login/", files=user)
        assert req.status_code == 200
        req_json = req.json()
        tokens.append((i, req_json["refresh"], req_json["access"]))


def test_verify():
    for i, refresh, access in tokens:
        data = {"token": (None, refresh)}
        req = requests.post("http://localhost/api/v1/user/verify-token/", files=data)
        assert req.status_code == 200

        data = {"token": (None, access)}
        req = requests.post("http://localhost/api/v1/user/verify-token/", files=data)
        assert req.status_code == 200


def test_refresh():
    for i, refresh, access in tokens:
        data = {"refresh": (None, refresh)}
        req = requests.post("http://localhost/api/v1/user/refresh-token/", files=data)
        assert req.status_code == 200


def test_list_all():
    header = get_auth_token()
    req = requests.get("http://localhost/api/v1/user/all/", headers=header)
    assert req.status_code == 200


def test_username():
    header = get_auth_token()
    for i in range(user_count):
        name = create_user_data(i)["username"][1]
        req = requests.get("http://localhost/api/v1/user/username/" + name, headers=header)
        assert req.status_code == 200
