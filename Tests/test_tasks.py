import random

from authorizer import get_auth_token
import requests
from config import task_count,users

states = ('new', 'in_progress', 'done')
ids = []


def create_random_tasks(count):
    tasks = []

    for i in range(count):
        r = random.randint(0, 3)
        u = random.randint(1 - len(users), len(users) - 1)
        task = {"name": (None, "task" + str(i))}
        if r < 3:
            task["state"] = (None, states[r])
        if u > 0:
            task["user"] = (None, users[u])
        tasks.append(task)

    return tasks


def test_add_tasks():
    auth = get_auth_token()
    for t in create_random_tasks(task_count):
        req = requests.post("http://localhost/api/v1/task/", headers=auth, files=t)
        assert req.status_code == 201
        ids.append(req.json()["id"])


def test_add_tasks_wrong():
    auth = get_auth_token()
    task_inv_state = {"name": "invalid task", "state": "invalid"}
    task_inv_user = {"name": "invalid task", "user": 30000}
    req = requests.post("http://localhost/api/v1/task/", headers=auth, files=task_inv_state)
    assert req.status_code == 400
    req = requests.post("http://localhost/api/v1/task/", headers=auth, files=task_inv_user)
    assert req.status_code == 400


def test_list_tasks():
    auth = get_auth_token()
    req = requests.get("http://localhost/api/v1/task/", headers=auth)
    assert req.status_code == 200


def test_get_id():
    auth = get_auth_token()
    for i in ids:
        req = requests.get("http://localhost/api/v1/task/id/" + str(i), headers=auth)
        assert req.status_code == 200


def test_get_id_wrong():
    auth = get_auth_token()
    req = requests.get("http://localhost/api/v1/task/id/30000", headers=auth)
    assert req.status_code == 404


def test_put_id():
    auth = get_auth_token()
    for i in ids[:len(ids) // 2]:
        task_upd = {
            "name": (None, "updated task"),
            "state": (None, "done"),
            "user": (None, users[0])
        }
        req = requests.put("http://localhost/api/v1/task/id/" + str(i), headers=auth, files=task_upd)
        assert req.status_code == 200


def test_delete_id():
    auth = get_auth_token()
    for i in ids[len(ids) // 2:]:
        req = requests.delete("http://localhost/api/v1/task/id/" + str(i), headers=auth)
        assert req.status_code == 204


def test_get_user():
    auth = get_auth_token()
    for i in users:
        req = requests.get("http://localhost/api/v1/task/user/" + str(i), headers=auth)
        assert req.status_code == 200


def test_get_unassigned():
    auth = get_auth_token()
    req = requests.get("http://localhost/api/v1/task/unassigned/", headers=auth)
    assert req.status_code == 200


def test_get_history():
    auth = get_auth_token()
    req = requests.get("http://localhost/api/v1/task/history/", headers=auth)
    assert req.status_code == 200


def test_get_history_id():
    auth = get_auth_token()
    for i in ids:
        req = requests.get("http://localhost/api/v1/task/history/" + str(i), headers=auth)
        assert req.status_code == 200
