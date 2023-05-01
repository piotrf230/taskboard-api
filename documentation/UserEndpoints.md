# HTTP API Endpoints - User authorization

## <code>/api/v1/user/register/</code>
<details>
<summary>POST</summary>

### POST
Creates a new user.

```console
$ curl -X POST -F 'username=example' -F 'password=PA55W0rd' localhost/api/v1/user/register/
{"message":"User example created with id 1!"}
```
</details>

## <code>/api/v1/user/login/</code>
<details>
<summary>POST</summary>

### POST
Returns refresh and access tokens based on username and password.

```console
$ curl -X POST -F 'username=example' -F 'password=PA55W0rd' localhost/api/v1/user/login/
{
"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzAyNjU1OSwiaWF0IjoxNjgyOTQwMTU5LCJqdGkiOiI5MjJkODdhMjc0ZTM0MGJkYjFkOWE2NjY4NzE0NzQzOCIsInVzZXJfaWQiOjF9.5lN-YvOzS3bdxXAAqMm_mGgpfzYTYXHSCwRj3Gr-ebQ",
"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTQwNDU5LCJpYXQiOjE2ODI5NDAxNTksImp0aSI6Ijg3MjVjNTcyOTA1MTQ3OTg4OWNkNTJiYmQwYjBmMzY3IiwidXNlcl9pZCI6MX0.yrDxKw-6lCDMAzw7fRMNF52ERzDk8ohbcAd16eBcdrI"
}
```
</details>
  
## <code>/api/v1/user/refresh-token/</code>
<details>
<summary>POST</summary>

### POST
Returns refresh and access tokens based on already existing refresh token.

```console
$ curl -X POST -F 'refresh=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzAyNjU1OSwiaWF0IjoxNjgyOTQwMTU5LCJqdGkiOiI5MjJkODdhMjc0ZTM0MGJkYjFkOWE2NjY4NzE0NzQzOCIsInVzZXJfaWQiOjF9.5lN-YvOzS3bdxXAAqMm_mGgpfzYTYXHSCwRj3Gr-ebQ' localhost/api/v1/user/refresh-token/
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTQwOTU0LCJpYXQiOjE2ODI5NDAxNTksImp0aSI6ImE3MTA0ZjhkOGM0YjRhNjRiZjRmODdmNDljNzNkNzA0IiwidXNlcl9pZCI6MX0.qGa3cBj1HBx4-oMX154SayKZvGZF676etaKczYK6jCA"}
```
</details>
  
## <code>/api/v1/user/verify-token/</code>
<details>
<summary>POST</summary>

### POST
Verifies the sent token.

```console
$ curl -X POST -F 'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzAyNjU1OSwiaWF0IjoxNjgyOTQwMTU5LCJqdGkiOiI5MjJkODdhMjc0ZTM0MGJkYjFkOWE2NjY4NzE0NzQzOCIsInVzZXJfaWQiOjF9.5lN-YvOzS3bdxXAAqMm_mGgpfzYTYXHSCwRj3Gr-ebQ' -w '%{http_code}' localhost/api/v1/user/verify-token/
{}200
```
</details>
  
## <code>/api/v1/user/all/</code>
<details>
<summary>GET</summary>

### GET
Retrieves a list of all users (ids and usernames only)

```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTQxOTY5LCJpYXQiOjE2ODI5NDE2NjksImp0aSI6IjU0MmUxOTYxZmM3NjRkYzhiYTY0NThlNTdhMzUwNGM5IiwidXNlcl9pZCI6MX0.YBVLwdcdAEEWEN3hjy7P6VKL2u-4q1BGno0JL0xb2QU" localhost/api/v1/user/all/
{"count":4,"next":null,"previous":null,"results":[{"id":1,"username":"example"},{"id":2,"username":"testuser"},{"id":3,"username":"otheruser"},{"id":4,"username":"placeholder"}]}
```
</details>

## <code>/api/v1/user/username/*[username]*</code>
<details>
<summary>GET</summary>

### GET
Retrieves user by username. (ids and usernames only)

```console
$ curl -X GET -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgyOTQyMzA0LCJpYXQiOjE2ODI5NDIwMDQsImp0aSI6IjJjNjRjYzdhMTM5ZjRlYjNiZGY1NjY5Y2U0MTYwNjQyIiwidXNlcl9pZCI6MX0.BqGcFSx72sdSGWry3T53ZS1ICGeTuiJyb8u5qUwH0h0" localhost/api/v1/user/username/testuser
{"count":1,"next":null,"previous":null,"results":[{"id":2,"username":"testuser"}]}
```
</details>

# User registration body pattern
```json
{
    "username": [username],
    "password": [password],
    "email": [email | optional],
    "first_name": [first name | optional],
    "last_name": [last name | optional],
}
```