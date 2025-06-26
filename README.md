# Task management application backend
## Docker deployment using docker-compose
Application requires Docker and docker-compose in order to run.
In order to run the app in Docker, one should execute the following commands in project root directory:
```shell
docker-compose up -d  --build
docker-compose exec backend python manage.py collectstatic
docker-compose exec backend python manage.py migrate
```
The following command can be used to create administrator user:
```shell
docker-compose exec backend python manage.py createsuperuser
```
## Local installation
In order to install the application locally for testing and development, one should follow these steps.
Python 3.11 and Docker are required, working on python virtual environment is highly advised.

1. Install required python packages  
`pip install -r requirements-dev.txt`
2. Install the app in interactive mode  
`pip install -e .`
3. Run a database container  
`docker run --name db -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres12345 -e POSTGRES_DB=taskboard postgres:16.2-alpine`
4. Collect static files  
`./manage.py collectstatic`
5. Apply migrations to database  
`./manage.py migrate`
6. Optionally create a superuser  
`./manage.py createsuperuser`
7. Run the application  
`./manage.py runserver`

## Documentation
The application uses `drf-spectacular` for automatic documentation generation, which can be accessed after running the app at:

- `localhost/api/schema-tasks/`
- `localhost/api/schema-tasks/swagger-ui/`
- `localhost/api/schema-tasks/redoc/`
- `localhost/api/schema-users/`
- `localhost/api/schema-users/swagger-ui/`
- `localhost/api/schema-users/redoc/`
- `localhost/api/schema-token/`
- `localhost/api/schema-token/swagger-ui/`
- `localhost/api/schema-token/redoc/`

Or, if running locally, at localhost:8000 analogically.