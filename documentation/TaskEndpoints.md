# HTTP API Endpoints - Task management
**All task requests must contain 'Authorization' header with authorization token ([more infomation about user authorization](../User/Endpoints.md))**

## <code>/api/v1/tasks/</code>
<details>
<summary>GET</summary>

### GET
Retrieves the full task list.

```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTUzNDc0LCJpYXQiOjE2ODI5NTMxNzQsImp0aSI6ImZmOWRhZGJiMDlmNTRhNzQ5YmFiNzhhMmI0YjRjMGU2IiwidXNlcl9pZCI6MX0.ZntS2n3_voGG7wSe7t58rxzoI5SZ_4Fk2n7qp0_FgCo" localhost/api/v1/task/
{
    "count":4,
    "next":null,
    "previous":null,
    "results":[
        {"id":5, "created":"2023-05-01T14:56:32.235767Z","updated":"2023-05-01T14:56:32.235741Z","name":"Add a task","description":"","user":4,"state":"in_progress"},
        {"id":4,"created":"2023-05-01T14:55:38.188281Z","updated":"2023-05-01T14:55:38.188255Z","name":"Make a task assigned to an user","description":"","user":4,"state":"new"},
        {"id":2,"created":"2023-05-01T14:37:28.270192Z","updated":"2023-05-01T14:37:28.270178Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"},
        {"id":1,"created":"2023-05-01T14:36:59.103920Z","updated":"2023-05-01T14:36:59.103903Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"}
    ]
}
```
</details>

<details>
<summary>POST</summary>

### POST
Adds a new task to the database.
Please refer to the [task body pattern](#task-request-body-pattern).  

```console
$ curl -X POST -F "name=add sample task" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTUzODEzLCJpYXQiOjE2ODI5NTM1MTMsImp0aSI6ImZkMGNhODAzMjk0NDQ1OTNhM2JiMGNiYWM2YjZmNDU2IiwidXNlcl9pZCI6MX0.RgPqmPvgvU87CLDouExi6Qx1VG8ki8scG90dDRQJUqs" localhost/api/v1/task/
{"id":6,"created":"2023-05-01T15:05:18.528204Z","updated":"2023-05-01T15:05:18.528189Z","name":"add sample task","description":"","user":null,"state":"new"}
```
</details>

</details>

## <code>/api/v1/task/id/*[task id]*</code>
<details>
<summary>GET</summary>

### GET
Retrieves data of the task with specified ID.
```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU0Mjc5LCJpYXQiOjE2ODI5NTM5NzksImp0aSI6ImY3ZGY5N2M5NWZmNjRhMDBiZWQxMGMxODdiZDg3NzllIiwidXNlcl9pZCI6MX0.k1C2tr7F-Lv1ahNFX5E2nfRDhb5wNTO5hAEQXW5qOx0" localhost/api/v1/task/id/6
{"id":6,"created":"2023-05-01T15:05:18.528204Z","updated":"2023-05-01T15:05:18.528189Z","name":"add sample task","description":"","user":null,"state":"new"}
```
</details>

<details>
<summary>PUT</summary>

### PUT
Updates the task with given data.
Please refer to the [task body pattern](#task-request-body-pattern).
```console
$ curl -X PUT -F "state=in_progress" -F "name=add sample task" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU0NDI1LCJpYXQiOjE2ODI5NTQxMjUsImp0aSI6ImZhZWRlYWNhZjQyOTQ3ZWJiZGNlNGY2MjhmMzU1MTMxIiwidXNlcl9pZCI6MX0.Lj-XOcFv_DGyOZA-4riPA4wY8xd7axAil6c2a5Nj95I" localhost/api/v1/task/id/6
{"id":6,"created":"2023-05-01T15:05:18.528204Z","updated":"2023-05-01T15:16:37.141777Z","name":"add sample task","description":"","user":null,"state":"in_progress"}
```
</details>

<details>
<summary>DELETE</summary>

### DELETE
Removes the task from the database.
```console
$ curl -X DELETE -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU0NDI1LCJpYXQiOjE2ODI5NTQxMjUsImp0aSI6ImZhZWRlYWNhZjQyOTQ3ZWJiZGNlNGY2MjhmMzU1MTMxIiwidXNlcl9pZCI6MX0.Lj-XOcFv_DGyOZA-4riPA4wY8xd7axAil6c2a5Nj95I" localhost/api/v1/task/id/6
```
</details>

## <code>/api/v1/task/user/*[user id]*</code>
<details>
<summary>GET</summary>

### GET
Retrieves a list of tasks assigned to the user specified by ID.

```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU0NjgzLCJpYXQiOjE2ODI5NTQzODMsImp0aSI6IjkyZDRiMDg1MWZiZDRjNzQ4NDgyMDNhNTY0ODZlYmIzIiwidXNlcl9pZCI6MX0.6gtsOAMS4D_IFfzg7-IGF108h9oW40XrWJUypE6N-Pk" localhost/api/v1/task/user/4
{
    "count":2,
    "next":null,
    "previous":null,
    "results":[
        {"id":5,"created":"2023-05-01T14:56:32.235767Z","updated":"2023-05-01T14:56:32.235741Z","name":"Add a task","description":"","user":4,"state":"in_progress"},
        {"id":4,"created":"2023-05-01T14:55:38.188281Z","updated":"2023-05-01T14:55:38.188255Z","name":"Make a task assigned to an user","description":"","user":4,"state":"new"}
    ]
}
```
</details>

## <code>/api/v1/task/unassigned/</code>
<details>
<summary>GET</summary>

### GET
Retrieves a list of tasks not assigned to any user.
```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU0NjgzLCJpYXQiOjE2ODI5NTQzODMsImp0aSI6IjkyZDRiMDg1MWZiZDRjNzQ4NDgyMDNhNTY0ODZlYmIzIiwidXNlcl9pZCI6MX0.6gtsOAMS4D_IFfzg7-IGF108h9oW40XrWJUypE6N-Pk" localhost/api/v1/task/unassigned/
{
    "count":2,
    "next":null,
    "previous":null,
    "results":[
        {"id":2,"created":"2023-05-01T14:37:28.270192Z","updated":"2023-05-01T14:37:28.270178Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"},
        {"id":1,"created":"2023-05-01T14:36:59.103920Z","updated":"2023-05-01T14:36:59.103903Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"}
    ]
}
```
</details>

## <code>/api/v1/task/keyword/*[keyword]*</code>
<details>
<summary>GET</summary>

### GET
Retrieves a list of tasks containing the keyword in name or description, ignores letter case.
```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU0OTI3LCJpYXQiOjE2ODI5NTQ2MjcsImp0aSI6ImZlNDQ4MTA4MDAzZDRkN2Q4YzYzMmNlYTY5YTkzMTAyIiwidXNlcl9pZCI6MX0.rlm0IfwuvYtraLyPDjEnkkkQbt7dSOVGaeSGxlyTDlo" localhost/api/v1/task/keyword/make
{
    "count":3,
    "next":null,
    "previous":null,
    "results":[
        {"id":4,"created":"2023-05-01T14:55:38.188281Z","updated":"2023-05-01T14:55:38.188255Z","name":"Make a task assigned to an user","description":"","user":4,"state":"new"},
        {"id":2,"created":"2023-05-01T14:37:28.270192Z","updated":"2023-05-01T14:37:28.270178Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"},
        {"id":1,"created":"2023-05-01T14:36:59.103920Z","updated":"2023-05-01T14:36:59.103903Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"}
    ]
}
```
</details>

## <code>/api/v1/task/state/*[state]*</code>
<details>
<summary>GET</summary>

### GET
Retrieves a list of tasks in the defined state.
```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU0OTI3LCJpYXQiOjE2ODI5NTQ2MjcsImp0aSI6ImZlNDQ4MTA4MDAzZDRkN2Q4YzYzMmNlYTY5YTkzMTAyIiwidXNlcl9pZCI6MX0.rlm0IfwuvYtraLyPDjEnkkkQbt7dSOVGaeSGxlyTDlo" localhost/api/v1/task/state/new
{
    "count":3,
    "next":null,
    "previous":null,
    "results":[
        {"id":4,"created":"2023-05-01T14:55:38.188281Z","updated":"2023-05-01T14:55:38.188255Z","name":"Make a task assigned to an user","description":"","user":4,"state":"new"},
        {"id":2,"created":"2023-05-01T14:37:28.270192Z","updated":"2023-05-01T14:37:28.270178Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"},
        {"id":1,"created":"2023-05-01T14:36:59.103920Z","updated":"2023-05-01T14:36:59.103903Z","name":"Make more tasks","description":"A few, about 3","user":null,"state":"new"}
    ]
}
```
</details>

## <code>/api/v1/task/history/</code>
<details>
<summary>GET</summary>

### GET
Retrieves a full history of tasks actions.
```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU2NTg3LCJpYXQiOjE2ODI5NTYyODcsImp0aSI6ImIyNzRmMmU3NTEwYzRhMTViNDYxNDNhY2NiZDM2MTkzIiwidXNlcl9pZCI6MX0.mRAlY0CrW00b2MzDvTdcaiIstBJoe2ck7QluZUxbxuE" localhost/api/v1/task/history/
{
    "count":8,
    "next":"http://localhost/api/v1/task/history/?page=2",
    "previous":null,
    "results":[
        {"created":"2023-05-01T15:17:18.898551Z","action":"deleted","task_id":6,"name":"add sample task","description":"","user":null,"state":"in_progress"},
        {"created":"2023-05-01T15:16:37.143653Z","action":"updated","task_id":6,"name":"add sample task","description":"","user":null,"state":"in_progress"},
        {"created":"2023-05-01T15:05:18.530273Z","action":"created","task_id":6,"name":"add sample task","description":"","user":null,"state":"new"},
        {"created":"2023-05-01T14:57:48.737404Z","action":"deleted","task_id":3,"name":"Edit more tasks","description":"A few, about 3","user":4,"state":"in_progress"},
        {"created":"2023-05-01T14:57:39.298603Z","action":"updated","task_id":3,"name":"Edit more tasks","description":"A few, about 3","user":4,"state":"in_progress"}
    ]
}
```
</details>

## <code>/api/v1/task/history/*[id]*</code>
<details>
<summary>GET</summary>

### GET
Retrieves a history of task specified by ID.
```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTU2NTg3LCJpYXQiOjE2ODI5NTYyODcsImp0aSI6ImIyNzRmMmU3NTEwYzRhMTViNDYxNDNhY2NiZDM2MTkzIiwidXNlcl9pZCI6MX0.mRAlY0CrW00b2MzDvTdcaiIstBJoe2ck7QluZUxbxuE" localhost/api/v1/task/history/6
{
    "count":3,
    "next":null,
    "previous":null,
    "results":[
        {"created":"2023-05-01T15:17:18.898551Z","action":"deleted","task_id":6,"name":"add sample task","description":"","user":null,"state":"in_progress"},
        {"created":"2023-05-01T15:16:37.143653Z","action":"updated","task_id":6,"name":"add sample task","description":"","user":null,"state":"in_progress"},
        {"created":"2023-05-01T15:05:18.530273Z","action":"created","task_id":6,"name":"add sample task","description":"","user":null,"state":"new"}
    ]
}
```
</details>

#  Task request body pattern
```json
{
    "name": [name],
    "description": [description | optional - empty for default],
    "status": [**"new"**|"in_progress"|"done" | optional - default "new"],
    "user": [user id | optional],
}
```