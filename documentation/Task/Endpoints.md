# HTTP API Endpoints - Task management
**All task requests must contain 'Authorization' header with authorization token ([more infomarion about user authorization](../User/Endpoints.md))**

## <code>/api/v1/tasks/</code>
### GET
Retrieves the full task list
### POST
Adds a new task to the database.
Please refer to the [task body pattern](#task-request-body-pattern).

## <code>/api/v1/task/id/*[task id]*</code>
### GET
Retrieves data of the task with specified ID.
### PUT
Updates the task with given data.
Please refer to the [task body pattern](#task-request-body-pattern).
### DELETE
Removes the task from the database.

## <code>/api/v1/task/user/*[user id]*</code>
### GET
Retrieves a list of tasks assigned to the user specified by ID.

## <code>/api/v1/task/unassigned/</code>
### GET
Retrieves a list of tasks not assigned to any user.

## <code>/api/v1/task/keyword/*[keyword]*</code>
### GET
Retrieves a list of tasks containing the keyword in name or description, ignores letter case.

## <code>/api/v1/task/state/*[state]*</code>
### GET
Retrieves a list of tasks in the defined state.

## <code>/api/v1/task/history/</code>
### GET
Retrieves a full history of tasks actions.

## <code>/api/v1/task/history/*[id]*</code>
### GET
Retrieves a history of task specified by ID.

#  Task request body pattern
```json
{  
    "name": [name],  
    "description": [description | optional - empty for default],  
    "status": [**"new"**|"in_progress"|"done" | optional - default "new"]  
    "user": [user id | optional]  
}
```