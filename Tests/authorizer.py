import requests
from config import auth_user

max_attempts = 10


def get_auth_token():
    attempt = 0
    user = {"username": (None, auth_user[0]), "password": (None, auth_user[1])}
    while attempt < max_attempts:
        req = requests.post("http://localhost/api/v1/user/login/", files=user)
        if req.status_code == 200:
            return {"Authorization": "Bearer " + req.json()["access"]}
        else:
            attempt += 1
    raise Exception("Max auth attempts exceeded")
