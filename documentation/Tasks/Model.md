# Task Model
Tasks are saved as database entities, containing the following information:
- id - unique, automatically assigned integer
- created - date, when the task was created
- updated - date, when the task was last updated
- name - a short char sequence
- description - a long optional char sequence
- status - indicates the status of the task (new, in_progress, done)
- user - indicates the user assigned to the task

Every creation, update, and delete operation on task creates a TaskHistory entity, which contains the following fields:

- id - unique, atomatically assigned integer
- created - date, idicates the operation date
- action - idicates the operation (create, update, delete)
- task - indicates the affected task's id number

- name (copy of affected task's field)
- description (copy of affected task's field)
- status (copy of affected task's field)
- user (copy of affected task's field)

fields are saved after the creation or update, and before the delete operation.