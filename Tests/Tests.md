# Unit tests

## Configuration
In order to configure unit tests, edit the file config.py.
The file is split into 3 categories: task, user and authentication parameters.
As each test uses one token created at it's beginning, it's not advised to enter very large numbers,
because each test should finish before token timeout.

### Task parameters
<code>task_count</code> - specifies the number of tasks that will be inserted into database during tests.
Half of the tasks will be updated, and the other half deleted.  
<code>users</code> - an array of users that will be assigned randomly to roughly half of the inserted tasks.
the first element would be assigned to updated tasks.
The list is not created on test user registration, as it would render task unit tests dependable on user tests.

### User parameters
<code>user_count</code> - specifies the number of test users, that would be registered in the database.

### Authentication parameters
<code>auth_user</code> - a tuple containing the username and password of a valid user.
This data is used to authenticate the user in tests when it is needed.
