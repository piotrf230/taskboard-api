# HTTP API Endpoints - User authorization

## <code>/api/v1/user/register/</code>
### POST
Creates a new user.

## <code>/api/v1/user/login/</code>
### POST
Returns refresh and access tokens based on username and password.

## <code>/api/v1/user/refresh-token/</code>
### POST
Returns refresh and access tokens based on already existing refresh token.

## <code>/api/v1/user/verify-token/</code>
### POST
Verifies the sent token.

## <code>/api/v1/user/all/</code>
### POST
Retrieves a list of all users (ids and usernames only)

## <code>/api/v1/user/username/*[username]*</code>
### POST
Retrieves user by username. (ids and usernames only)

# User registration body pattern
```json
{  
    "username": [username],  
    "password": [password],  
    "email": [email | optional]  
    "first_name": [first name | optional]  
    "last_name": [last name | optional]  
}
```